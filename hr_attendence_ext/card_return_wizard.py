from odoo import fields, models, exceptions, _
from . import utils
from ..models.utils import REPLACEMENT_REASONS, ASSIGNMENT_REASONS


class CardReturnWizard(models.TransientModel):
    _name = 'card.return.wizard'
    _description = 'Card Return Wizard'

    card_id = fields.Many2one('hr.attendance.card', string="Card ID")
    card_status = fields.Boolean()
    temporary = fields.Boolean(related='card_id.temporary', string="Temporary")
    card_type = fields.Many2one(related='card_id.card_type', string="Card Type")
    card_color = fields.Char(string="Card Type")
    card_type_name = fields.Char(related='card_type.name', string="Card Type")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    employee_image = fields.Binary(related="employee_id.image_medium", string="Employee Image")
    activate_old_card = fields.Boolean(string="Activate Old Card", default=True)
    replacement_reason = fields.Selection(selection=REPLACEMENT_REASONS + ASSIGNMENT_REASONS)
    shared = fields.Boolean(related='card_type.shared')

    def action_return_card(self, context={}, reason=''):

        card_obj = self.env['hr.attendance.card']
        unlink_card_ids = []
        for s in self:
            if s.employee_id:
                # en son yetkileri pasif hale getirilmiş kartı bul
                active_auth_ids = s.employee_id.attendance_auth_id
                # employee bazlı çevrildiği için gerek yok.
                # utils.deactivate_card_auths(s.card_id)
                s.card_id.log_card_operation(s.card_id.employee_id, 'return',
                                             return_date=fields.Datetime.now())
                utils.deactivate_card(s.card_id, reason=reason or 'user')
                if s.activate_old_card and not s.employee_id.card_ids.filtered(lambda x: x.active):
                    original_card_id = card_obj.search(
                        [('employee_id', '=', s.employee_id.id),
                         ('active', '=', False),
                         ('temporary', '=', False)],
                        order='id desc', limit=1)

                    if original_card_id:
                        utils.activate_card(original_card_id)
                        utils.copy_card_auths(self=s,
                                              new_card_id=original_card_id, old_card_id=s.card_id,
                                              active_auth_ids=active_auth_ids)

                # teslim edilen kartın yetkilerini geri al
                if not self.env.context.get('from_cron') and (s.card_id.temporary or s.card_id.card_type.shared):
                    if s.card_id.preserve_common_auth:
                        s.card_id.employee_id = self.env.ref("hr_attendance_ext.hr_employee_authorization_temp")
                    else:
                        s.card_id.write({'employee_id': False}, recursion_call=True)
                        utils.deactivate_card_auths(s.card_id)
            else:
                if not self.env.context.get('from_cron'):  # automated card expired cron
                    raise exceptions.ValidationError(_('No Users Assigned. Please Deactivate Card.'))
                unlink_card_ids.append(s.card_id.id)

        if len(unlink_card_ids) > 0:
            self.card_id.browse(unlink_card_ids).unlink(reason=reason or 'user')

        return {
            'type': 'ir.actions.close_wizard_refresh_view'
        }

    def action_deactivate_card(self):
        for s in self:
            #     if not self.env.context.get('from_cron') and (s.card_id.temporary or s.card_id.card_type.shared):
            #         if s.card_id.preserve_common_auth:
            #             s.card_id.employee_id = self.env.ref("hr_attendance_ext.hr_employee_authorization_temp")
            #         else:
            #             s.card_id.employee_id = False
            utils.deactivate_card(s.card_id, reason='user')

        return {
            'type': 'ir.actions.close_wizard_refresh_view'
        }
        # Kartı direkt deactive ederse raporlansın mı?
        # if self.card_id.employee_id:
        #     self.card_id.log_card_operation(self.card_id.employee_id, 'return',
        #                                     return_date=fields.Datetime.now())
