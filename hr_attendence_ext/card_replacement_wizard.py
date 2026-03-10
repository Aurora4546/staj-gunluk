from odoo import fields, models, exceptions, api, _
from . import utils
from ..models import utils as model_utils


class TemporaryCardAssignmentWizard(models.TransientModel):
    _name = 'card.replacement.wizard'
    _description = 'Card Replacement Wizard'

    card_id = fields.Many2one(
        'hr.attendance.card',
        string="Card ID"
    )
    # card_type_id = fields.Many2one(related='card_id.card_type_id', string="Card Type")
    new_card_no = fields.Char(size=8)
    replacement_reason = fields.Selection(
        selection=model_utils.REPLACEMENT_REASONS,
        string="Replacement Reason",
        required=True,
        default='unutma'
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string="Employee"
    )
    employee_image = fields.Binary(
        related="employee_id.image_medium",
        string="Employee Image"
    )
    validity_expire_time = fields.Datetime(string='Validity Expire Time')

    @api.onchange('new_card_no')
    def check_n_card_no(self):
        warnings = utils.check_card_no(self, 'new_card_no')
        if warnings:
            return warnings

    @api.constrains('validity_expire_time')
    def check_validity_expire_time(self):

        if self.validity_expire_time:
            context = self.env.context
            aware_validity_expire_time = model_utils.get_aware_time(context, self.validity_expire_time)
            aware_now = model_utils.get_aware_time(context)

            if aware_validity_expire_time < aware_now:
                raise exceptions.ValidationError(_("Validity Expire Time can not be before than today"))

    def action_assign_card(self):
        card_obj = self.env['hr.attendance.card']
        card_auth_obj = self.env['hr.attendance.card.authorization']
        self.new_card_no = self.new_card_no.upper() if self.new_card_no else self.new_card_no
        new_card_id = card_obj.search(
            [('card_no', '=', self.new_card_no), '|', ('active', '=', True), ('active', '=', False)])

        # Girilen yeni kart sistemde varsa ona göre işlem yap.
        if new_card_id:

            # kart herhangi bir kişiye verilmişmi diye kontrol et. Verilmişse işlemi yaptırma
            utils.control_card_owner(new_card_id)
            # kart tipleri uyuşmuyorsa işlem yaptırma
            if self.card_id.card_type != new_card_id.card_type:
                raise exceptions.ValidationError(
                    _("Card types do not match: {} > {}").format(self.card_id.card_type.name,
                                                                 new_card_id.card_type.name))

            # utils.deactivate_card_auths(card_id=new_card_id)
            active_auth_ids = self.employee_id.attendance_auth_id
            utils.deactivate_card(card_id=self.card_id, reason='got_temporary')
            # utils.activate_card(card_id=new_card_id)
            utils.copy_card_auths(self=self, new_card_id=new_card_id, old_card_id=self.card_id,
                                  active_auth_ids=active_auth_ids)

            new_card_id.write({
                'employee_id': self.card_id.employee_id.id,
                'active': True,
                'validity_expire_time': self.validity_expire_time,
                'card_state': 'assigned_to_user'
            }, pass_sync=True)
        else:
            # Eğer kart sistemde tanımlı değilse kişinin üstündeki kart tipinde ve yetkilerde yeni bir kart oluşturulur
            # Burada oluşan yeni kart temporary=False olarak oluşur.
            if self.user_has_groups('hr_attendance_ext.group_attendance_one,hr_attendance_ext.group_attendance_four'):
                wizard = self.env.ref(
                    'hr_attendance_ext.card_confirmation_wizard')
                return {
                    'name': _('Kart Oluşturma Onay Ekranı'),
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'attendance.card.confirmation.wizard',
                    'views': [(wizard.id, 'form')],
                    'view_id': wizard.id,
                    'target': 'new',
                    'context': {
                        'default_employee_id': self.employee_id.id,
                        'default_card_id': self.card_id.id,
                        'default_new_card_no': self.new_card_no,
                        'default_replacement_reason': self.replacement_reason,
                        'default_is_temporary': False,
                        'default_state': 'assigned_to_user',
                        'default_validity_expire_time': self.validity_expire_time,
                    },
                }
            # utils.deactivate_card(card_id=self.card_id)
            # new_card_id = self.card_id.copy(default={'card_no': self.new_card_no, 'temporary': False, 'active': True,
            #                                          'validity_expire_time': self.check_validity_expire_time()})
            # utils.copy_card_auths(self=self, new_card_id=new_card_id, old_card_id=self.card_id)
            else:
                raise exceptions.AccessError(
                    _("Lütfen başka bir geçici kart deneyiniz. Okutulan kart sistemde kayıtlı değildir."))

        # Kart değişikliğini log'la
        new_card_id.log_card_operation(employee_id=new_card_id.employee_id, reason=self.replacement_reason)
