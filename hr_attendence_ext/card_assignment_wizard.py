from datetime import datetime as dt, timedelta as td

from odoo import api, fields, models, exceptions, _
from . import utils
from ..models import utils as model_utils


class CardAssignmentWizard(models.TransientModel):
    _name = 'card.assignment.wizard'
    _description = 'Card Assignment Wizard'

    def get_validity_from_employee(self):
        if self.env.context.get('active_id'):
            contract_date = self.env.get('hr.employee').sudo().browse(
                [self.env.context.get('active_id')]).leaving_date
            if contract_date:
                return dt.combine(
                    contract_date + td(days=1),
                    dt.min.time())
        return False

    employee_id = fields.Many2one(
        'hr.employee',
        string="Employee"
    )
    card_no = fields.Char(string='Card No', size=8)
    card_exists = fields.Boolean(string="Entered Card is")
    message = fields.Char(string="Message", default="Please enter Card No")
    validity_expire_time = fields.Datetime(string='Validity Expire Time', default=get_validity_from_employee)

    @api.constrains('validity_expire_time')
    def check_validity_expire_time(self):

        if self.validity_expire_time:
            context = self.env.context
            aware_validity_expire_time = model_utils.get_aware_time(context, self.validity_expire_time)
            aware_now = model_utils.get_aware_time(context)

            if aware_validity_expire_time < aware_now:
                raise exceptions.ValidationError(_("Validity Expire Time can not be before than today"))

    @api.onchange('card_no')
    def action_onchange_card_no(self):
        warnings = utils.check_card_no(self, 'card_no')
        if warnings:
            return warnings

        self.card_no = self.card_no.upper() if self.card_no else self.card_no
        card_obj = self.env['hr.attendance.card']
        card_id = card_obj.search([('card_no', '=', self.card_no), '|', ('active', '=', True), ('active', '=', False)])
        if card_id:
            utils.control_card_owner(card_id, self.employee_id)

            self.message = _("Card found on the system.")
            self.card_exists = True
        else:
            if self.card_no:
                self.message = _("Card not found on the system. A new card will be created.")
            else:
                self.message = _("Please enter Card No")
            self.card_exists = False

    def action_assign_existing_card(self):
        return self.get_action_by_selection('create')

    def action_create_new_card(self):
        return self.get_action_by_selection('assign')

    def get_action_by_selection(self, selection):
        action = {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hr.attendance.card',
            'context': '',
        }
        card_id = False
        if self.card_no:
            card_obj = self.env['hr.attendance.card']
            card_id = card_obj.search(
                [('card_no', '=', self.card_no), '|', ('active', '=', True), ('active', '=', False)])

        if selection == 'assign':
            if self.card_no:
                if card_id:
                    utils.control_card_owner(card_id)

                    card_id.write({
                        'employee_id': self.employee_id.id,
                        'validity_expire_time': self.validity_expire_time,
                        'card_state': 'assigned_to_user',
                        'pass_sync': False
                    }
                    )
                    utils.activate_card(card_id)
                    action['res_id'] = card_id.id
                else:
                    raise exceptions.ValidationError(_("Card Is Not Found On The System!"))
            else:
                raise exceptions.ValidationError(_("Please Enter Card No"))
        elif selection == 'create':
            if card_id:
                raise exceptions.ValidationError(_("Card Is Already Defined On The System! Please Assign Instead."))
            action['context'] = {'default_employee_id': self.employee_id.id,
                                 'default_card_no': self.card_no or '',
                                 'default_card_state': 'assigned_to_user',
                                 'default_validity_expire_time': self.validity_expire_time}

        return action
