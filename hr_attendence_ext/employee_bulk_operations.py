
from odoo import models, fields, api


class BulkPersonalIdWizardInherit(models.TransientModel):
    _inherit = 'hr_employee_history.bulk_personal_id_update_wizard'


    is_authorize_removed = fields.Boolean(default=False)


    @api.onchange('movement_type')
    def set_authorize(self):
        for i in self:
            if i.movement_type == '3':
                i.is_authorize_removed = True
            else:
                i.is_authorize_removed = False


class BulkEmployeeNewID(models.TransientModel):
    _inherit = 'hr_employee_history.bulk_employee_new_id'


class BulkEmployeeNewDepartment(models.TransientModel):
    _inherit = 'hr_employee_history.bulk_employee_new_department'


class BulkEmployeeNewJobTitle(models.TransientModel):
    _inherit = 'hr_employee_history.bulk_employee_new_job_title'


