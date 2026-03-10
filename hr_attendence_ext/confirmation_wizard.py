# Copyright 2019 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, exceptions, _
from . import utils
from ..models.utils import REPLACEMENT_REASONS


class CardConfirmationWizard(models.TransientModel):
    _name = 'attendance.card.confirmation.wizard'
    _description = 'Card Confirm Wizard'

    object = fields.Char()
    is_temporary = fields.Boolean(default=False)
    card_id = fields.Many2one("hr.attendance.card")
    new_card_no = fields.Char(size=8)
    replacement_reason = fields.Selection(
        selection=REPLACEMENT_REASONS,
        string="Replacement Reason",
        required=True,
        default='unutma'
    )
    validity_expire_time = fields.Datetime(string='Validity Expire Time')

    @api.multi
    def confirm_card_creation(self):
        if not self.is_temporary:
            raise exceptions.ValidationError(
                _("Oluşturmak istediğiniz kart geçici kart değil ise lütfen öncelikle onaylayınız."))

        active_auth_ids = self.card_id.employee_id.attendance_auth_id
        utils.deactivate_card(card_id=self.card_id, reason='user')
        new_card_id = self.env['hr.attendance.card'].create({'card_no': self.new_card_no,
                                                             'temporary': False,
                                                             'card_type': self.card_id.card_type.id,
                                                             'validity_expire_time': self.validity_expire_time,
                                                             'employee_id': self.card_id.employee_id.id
                                                             })

        utils.copy_card_auths(self=self, new_card_id=new_card_id, old_card_id=self.card_id,
                              active_auth_ids=active_auth_ids)

        new_card_id.log_card_operation(employee_id=new_card_id.employee_id, reason=self.replacement_reason)

        return {
            'type': 'ir.actions.close_wizard_refresh_view'
        }
