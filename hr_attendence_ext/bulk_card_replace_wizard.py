from odoo import models, fields, _
from odoo.exceptions import ValidationError


class BulkCardReplaceWizard(models.TransientModel):
    _name = 'bulk.card.wizard'
    _description = "Bulk Card Wiz"

    bulk_card_ids = fields.Many2many('hr.attendance.bulk.card.replacement')

    def active_cards_replace(self):
        if self.user_has_groups('hr_attendance_ext.group_attendance_one'):

            for i in self.bulk_card_ids:
                i.sudo().write({
                    'temp_card_no': i.current_card_no,
                    'active': False,
                    'will_sync': True
                })

            return {
                'type': 'ir.actions.act_window',
                'res_model': 'hr.attendance.bulk.card.replacement',
                'name': 'Attendance Bulk Card Replacement',
                'view_mode': 'tree',
                'view_type': 'form',
                'target': 'current',
                'context': {'card_replacement': True},
                'domain': [('employee_id.card_ids', '!=', False), ('employee_id.card_ids.active', '=', True)]
            }
        else:
            raise ValidationError(_('You have no authorize !'))
