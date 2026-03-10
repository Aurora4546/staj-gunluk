from odoo import api, fields, models, exceptions, _


class CardAssignmentBuildingWizard(models.TransientModel):
    _name = 'auth.per.building.assignment.wizard'
    _description = 'Building Auth Assignment Wizard'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def name_get(self):
        names = []
        for s in self:
            name = (s.id, 'Bina Yetkilendirme Ekranı')
            names.append(name)
        return names

    def _set_employee_from_selected_dept(self):
        employees = self._get_employees()
        return len(employees)

    def emp_domain(self):
        return []

    zone_id = fields.Many2one('hr.attendance.zone', string='Zones', domain=[('zone_type_id.code', '=', 'B')])
    building_ids = fields.Many2many('hr.attendance.building', string='Buildings')
    employee_ids = fields.Many2many('hr.employee', string='Employees', required=True, domain=emp_domain)
    operation = fields.Selection(selection=[('assign', 'Assign'), ('unassign', 'Unassign')])

    working_type = fields.Selection(
        selection=lambda self: self.env.get('hr.employee')._fields.get('working_type').selection)
    affected_count = fields.Integer(string="Affected Employees", default=0)

    def _get_employees(self):
        employee_ids = self.zone_id.building_id.mapped('floor_ids').mapped('poi_ids').mapped('employee_ids')
        self.building_ids = [(4, x.id) for x in self.zone_id.building_id]
        if self.working_type:
            employee_ids = employee_ids.filtered(lambda x: x.working_type == self.working_type)

        return employee_ids

    def check_required_zone_fields(self, employee_ids=False):
        errors = ''

        if not self.zone_id:
            errors += _('\n - Please select at least 1 area or zone.')
        if not employee_ids:
            errors += _('\n - Please select at least 1 employee.')

        if errors != '':
            errors = _('Please correct the following error(s):') + errors
            raise exceptions.ValidationError(errors)

    def action_set_operation_assign(self):

        auth_obj = self.env['hr.attendance.card.authorization']
        employee_ids = self._get_employees()
        self.check_required_zone_fields(employee_ids=employee_ids)
        new_context = self.env.context.copy()

        employees_with_auth = employee_ids.filtered(lambda x: x.attendance_auth_id)
        employees_without_auth = employee_ids - employees_with_auth

        auth_ids = employees_with_auth.mapped('attendance_auth_id')
        new_zone_ids = [(4, self.zone_id.id)]

        auth_ids.write({
            'zone_id': new_zone_ids
        }, no_log=True)

        create_values = []
        for employee in employees_without_auth:
            create_values.append({
                'employee_id': employee.id,
                'zone_id': new_zone_ids
            })

        auth_obj.with_context(new_context).create(create_values)

        if hasattr(self, 'message_post'):
            # Notify state change
            getattr(self, 'message_post')(
                subtype='mt_comment',
                body="Yetki Kaydı Başarılı Olarak Kaydedildi."
            )

    def action_set_operation_unassign(self):
        employee_ids = self._get_employees()
        self.check_required_zone_fields(employee_ids=employee_ids)
        for employee in employee_ids:
            if employee.attendance_auth_id:
                employee.attendance_auth_id[0].zone_id -= self.zone_id
        if hasattr(self, 'message_post'):
            # Notify state change
            getattr(self, 'message_post')(
                subtype='mt_comment',
                body="Yetki Kaydı Başarılı Olarak Kaydedildi."
            )

    @api.onchange('operation')
    def onchange_operation(self):
        if self.operation == 'assign':
            self.employee_ids = False
            self.zone_id = False
            self.building_ids = False
        domain = self.emp_domain()
        if self.operation == 'unassign':
            domain = self._get_employee_domain()

        # set employees according to working type
        self.affected_count = self._set_employee_from_selected_dept()
        return {'domain': {'employee_ids': domain}}

    @api.onchange('working_type')
    def onchange_operation(self):
        self.affected_count = self._set_employee_from_selected_dept()

    @api.onchange('zone_id')
    def onchange_department_ids(self):
        self.building_ids = False
        self.affected_count = self._set_employee_from_selected_dept()

    def _get_employee_domain(self):
        domain = []
        employee_ids = []
        if self.operation == 'unassign':
            for auth_id in self.zone_id.auth_ids:
                employee_ids.append(auth_id.employee_id.id)
            if employee_ids:
                domain = [('id', 'in', employee_ids)]

        return domain
