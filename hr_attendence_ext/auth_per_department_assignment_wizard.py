from odoo import api, fields, models, exceptions, _


class CardAssignmentWizard(models.TransientModel):
    _name = 'auth.per.department.assignment.wizard'
    _description = 'Department Auth Assignment Wizard'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def name_get(self):
        names = []
        for s in self:
            name = (s.id, 'Bölüm Yetkilendirme Ekranı')
            names.append(name)
        return names

    def _set_employee_from_selected_dept(self):
        employees = self._get_employees()
        return len(employees)

    def emp_domain(self):
        return []
        # if self.env.user and self.env.user.employee_ids:
        #     employee_list = self.env['hr.employee'].sudo().search(
        #         ['|', ('department_id', 'child_of',
        #                     self.env.user.employee_ids[0].managed_departments.ids + self.env.user.employee_ids[
        #                                                                             :1].assistant_manager_dept_ids.ids),
        #          ('id', '=', self.env.user.employee_ids[0].id)])
        #     return [('id', 'in', employee_list.ids)]
        # return [('id', '=', -1)]

    area_ids = fields.Many2many('hr.attendance.area', string='Areas')
    zone_ids = fields.Many2many('hr.attendance.zone', string='Zones')
    department_ids = fields.Many2many('hr.department', string='Departments')
    employee_ids = fields.Many2many('hr.employee', string='Employees', required=True, domain=emp_domain)
    operation = fields.Selection(selection=[('assign', 'Assign'), ('unassign', 'Unassign')])

    working_type = fields.Selection(
        selection=lambda self: self.env.get('hr.employee')._fields.get('working_type').selection)
    affected_count = fields.Integer(string="Affected Employees", default=0)

    def _get_employees(self):
        employee_ids = self.department_ids.mapped('member_ids')
        if self.working_type:
            employee_ids = employee_ids.filtered(lambda x: x.working_type == self.working_type)

        return employee_ids

    def check_required_zone_fields(self, employee_ids=False):
        errors = ''

        if not self.zone_ids and not self.area_ids:
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
        new_zone_ids = [(4, x.id) for x in self.zone_ids]
        new_area_ids = [(4, x.id) for x in self.area_ids]

        auth_ids.write({
            'zone_id': new_zone_ids,
            'area_id': new_area_ids
        }, no_log=True)

        create_values = []
        for employee in employees_without_auth:
            create_values.append({
                'employee_id': employee.id,
                'zone_id': [(4, x.id) for x in self.zone_ids] if self.zone_ids else [],
                'area_id': [(4, x.id) for x in self.area_ids] if self.area_ids else [],
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
                if self.zone_ids:
                    employee.attendance_auth_id[0].zone_id -= self.zone_ids
                if self.area_ids:
                    employee.attendance_auth_id[0].area_id -= self.area_ids
        if hasattr(self, 'message_post'):
            # Notify state change
            getattr(self, 'message_post')(
                subtype='mt_comment',
                body="Yetki Kaydı Başarılı Olarak Kaydedildi."
            )

    @api.onchange('operation')
    def onchange_operation(self):
        # self.area_ids = False
        # self.zone_ids = False
        if self.operation == 'assign':
            self.employee_ids = False
        domain = self.emp_domain()
        if self.operation == 'unassign':
            domain = self._get_employee_domain()

        # set employees according to working type
        self.affected_count = self._set_employee_from_selected_dept()
        return {'domain': {'employee_ids': domain}}

    @api.onchange('working_type')
    def onchange_operation(self):
        self.affected_count = self._set_employee_from_selected_dept()

    @api.onchange('department_ids')
    def onchange_department_ids(self):
        self.affected_count = self._set_employee_from_selected_dept()

    def _get_employee_domain(self):
        domain = []
        employee_ids = []
        if self.operation == 'unassign':
            for area in self.area_ids:
                for auth_id in area.auth_ids:
                    employee_ids.append(auth_id.employee_id.id)
            for zone in self.zone_ids:
                for auth_id in zone.auth_ids:
                    employee_ids.append(auth_id.employee_id.id)
            if employee_ids:
                domain = [('id', 'in', employee_ids)]

        return domain
