from odoo import api, fields, models, exceptions, _


class CardAssignmentWizard(models.TransientModel):
    _name = 'auth.per.employee.assignment.wizard'
    _description = 'Employee Auth Assignment Wizard'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def name_get(self):
        names = []
        for s in self:
            name = (s.id, 'Çalışan Yetkilendirme Ekranı')
            names.append(name)
        return names

    def _get_zone_ids_domain(self):
        domain = []

    def _get_zone_id_domain(self):
        domain = []
        logged_employee = self.env.user.employee_ids.ids
        if logged_employee:
            domain = [('zone_auth_owner', 'in', logged_employee)]

        return domain

    def emp_domain(self):
        assigned_cards = self.env.get('hr.attendance.card').search([('employee_id', '!=', False)]).mapped(
            'employee_id').ids
        return [('id', 'in', assigned_cards)]
        # if self.env.user.has_group('hr_attendance_ext.group_attendance_one') or self.env.user:
        #     return []
        # elif self.env.user and self.env.user.employee_ids:
        #     employee_list = self.env['hr.employee'].sudo().search(
        #         ['|', ('department_id', 'child_of',
        #                     self.env.user.employee_ids[0].managed_departments.ids + self.env.user.employee_ids[
        #                                                                             :1].assistant_manager_dept_ids.ids),
        #          ('id', '=', self.env.user.employee_ids[0].id)])
        #     return [('id', 'in', employee_list.ids)]
        # return [('id', '=', -1)]

    area_ids = fields.Many2many('hr.attendance.area', string='Areas')
    zone_id = fields.Many2one('hr.attendance.zone', string='Zone', domain=_get_zone_id_domain)
    zone_ids = fields.Many2many('hr.attendance.zone', string='Zones', domain=_get_zone_ids_domain)
    employee_ids = fields.Many2many('hr.employee', string='Employees', required=True)
    protected_employee_ids = fields.Many2many('hr.employee', string='Yetkisi Güvenlik Tarafından Korunan Kişiler')
    operation = fields.Selection(selection=[('assign', 'Assign'), ('unassign', 'Unassign')])
    affected_count = fields.Integer(string="Affected Employees", default=0)
    form_mode = fields.Char("Form Mode", default='tusas_manager')
    security_check = fields.Boolean(related="zone_id.zone_type_id.security_check")

    @api.model
    def create(self, values):
        return super().create(values)

    def check_required_fields(self):
        errors = ''
        if self.form_mode and self.form_mode == 'tusas_manager':
            if not self.zone_id:
                errors += _('\n - Please select a zone.')
            if not self.employee_ids:
                errors += _('\n - Please select at least 1 employee.')
        else:
            if not self.zone_ids and not self.area_ids:
                errors += _('\n - Please select at least 1 area or zone.')
            if not self.employee_ids:
                errors += _('\n - Please select at least 1 employee.')

        if errors != '':
            errors = _('Please correct the following error(s):') + errors
            raise exceptions.ValidationError(errors)

    def action_set_operation_assign(self):
        auth_obj = self.env['hr.attendance.card.authorization']
        self.check_required_fields()
        if self.security_check and self.form_mode == 'tusas_manager':
            request_obj = self.env['hr.attendance.card.auth.request']
            new_request = request_obj.sudo(self.env.user.id).create({
                'zone_id': self.zone_id.id,
                'zone_users': [(4, x.id) for x in self.employee_ids] if self.employee_ids else [],
                'reason': _('Automatically created from TUSAŞ Manager screen.')
            })
            if new_request:
                return new_request.request_validation()
        else:
            new_context = self.env.context.copy()
            if self.form_mode == 'tusas_manager':
                new_context.update({'zone_auth_mode': self.form_mode})

            employees_with_auth = self.employee_ids.filtered(lambda x: x.attendance_auth_id)
            employees_without_auth = self.employee_ids - employees_with_auth

            auth_ids = employees_with_auth.mapped('attendance_auth_id')
            new_zone_ids = [(4, x.id) for x in self.zone_ids]
            new_area_ids = [(4, x.id) for x in self.area_ids]

            if self.form_mode == 'tusas_manager':
                auth_ids.with_context(new_context).write(
                    dict(zone_id=[(4, self.zone_id.id)]))
            else:
                auth_ids.write({
                    'zone_id': new_zone_ids,
                    'area_id': new_area_ids
                }, no_log=True)

            create_values = []
            for employee in employees_without_auth:
                if self.form_mode == 'tusas_manager':
                    create_values.append({
                        'employee_id': employee.id,
                        'zone_id': [(4, self.zone_id.id)],
                    })
                else:
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
        return {
            'view_mode': 'form',
            'res_model': 'auth.per.employee.assignment.wizard',
            'type': 'ir.actions.act_window',
            'target': 'main',
            'res_id': False,
            'context': {'default_form_mode': 'tusas_manager'}
        }

    def action_set_operation_unassign(self):
        self.check_required_fields()
        for employee in self.employee_ids:
            if employee.attendance_auth_id:
                if self.form_mode == 'security_manager':
                    if self.zone_ids:
                        employee.attendance_auth_id[-1].zone_id -= self.zone_ids
                    if self.area_ids:
                        employee.attendance_auth_id[-1].area_id -= self.area_ids
                else:
                    if self.zone_id:
                        employee.attendance_auth_id[-1].with_context({'zone_auth_mode': self.form_mode}).write(
                            dict(zone_id=[(3, self.zone_id.id)]))

        if hasattr(self, 'message_post'):
            # Notify state change
            getattr(self, 'message_post')(
                subtype='mt_comment',
                body="Yetki Kaydı Başarılı Olarak Silindi."
            )
        return {
            'view_mode': 'form',
            'res_model': 'auth.per.employee.assignment.wizard',
            'type': 'ir.actions.act_window',
            'target': 'main',
            'res_id': False,
            'context': {'default_form_mode': 'tusas_manager'}
        }

    @api.onchange('operation', 'zone_id')
    def onchange_operation(self):
        # self.area_ids = False
        # self.zone_ids = False
        self.employee_ids = False
        self.protected_employee_ids = False
        domain = self.emp_domain()
        protected_employee_ids = []
        if self.operation == 'unassign':
            domain, protected_employee_ids = self._get_employee_domain()
        # set employees according to working type
        self.affected_count = len(self.employee_ids) if self.employee_ids else 0

        return {'domain': {'employee_ids': domain},
                'value': {'protected_employee_ids': [(6, 0, protected_employee_ids)]}}

    @api.onchange('employee_ids')
    def onchange_department_ids(self):
        self.affected_count = len(self.employee_ids) if self.employee_ids else 0

    def _get_employee_domain(self):
        domain = self.emp_domain()
        employee_ids = []
        protected_employee_ids = []
        if self.operation == 'unassign':
            if self.form_mode == 'tusas_manager':
                for auth_id in self.zone_id.auth_ids:
                    employee_ids.append(auth_id.employee_id.id)
            else:
                for area in self.area_ids:
                    for auth_id in area.auth_ids:
                        employee_ids.append(auth_id.employee_id.id)
                for zone in self.zone_ids:
                    for auth_id in zone.auth_ids:
                        employee_ids.append(auth_id.employee_id.id)

            protected_employee_ids = self.zone_id.protected_auth_ids.mapped('employee_id').ids

            if employee_ids:
                domain.extend([('id', 'in', employee_ids)])

        return domain, protected_employee_ids
