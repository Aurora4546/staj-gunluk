from odoo import api, fields, models, exceptions, _


class AuthCopyWizard(models.TransientModel):
    _name = 'auth.copy.wizard'
    _description = 'Employee Copy Wizard'

    def name_get(self):
        names = []
        for s in self:
            name = (s.id, 'Bölge Yetki Kopyalama Ekranı')
            names.append(name)
        return names

    zone_id = fields.Many2one('hr.attendance.zone', string='Bölge')
    new_zone_id = fields.Many2one('hr.attendance.zone', string='Yeni Bölge')
    operation = fields.Selection(selection=[('assign', 'Assign'), ('unassign', 'Unassign')], default='assign')
    affected_count = fields.Integer(string="Affected Employees", default=0)
    form_mode = fields.Char("Form Mode", default='tusas_manager')

    @api.constrains
    def check_required_fields(self):
        errors = ''

        if not self.zone_id:
            errors += _('\n - Yetkilerin baz alınacağı bölge seçiniz.')
        if not self.new_zone_id:
            errors += _('\n - Yetki verilecek yeni bölgeyi seçiniz.')
        if self.affected_count == 0:
            errors += _('\n - Yetki verilecek kullanıcı bulunmamaktadır.')

        if errors != '':
            errors = _('Lütfen aşağıdaki eksikleri doğrulayın:') + errors
            raise exceptions.ValidationError(errors)

    def action_set_operation_assign(self):
        if not self.user_has_groups(
                'hr_attendance_ext.group_attendance_one,hr_attendance_ext.group_attendance_four'):
            raise exceptions.ValidationError('Sadece {} veya {} rolüne sahip kullanıcılar bu işlemi yapabilir.'.format(
                self.env.ref('hr_attendance_ext.group_attendance_one').name,
                self.env.ref('hr_attendance_ext.group_attendance_four').name))
        # self.check_required_fields()

        if self.zone_id.auth_ids:
            self.zone_id.auth_ids.with_context({'zone_auth_mode': self.form_mode}).filtered(lambda x: x.active and x.employee_id).write(
                dict(zone_id=[(4, self.new_zone_id.id)]), no_log=True)

        self.env.user.notify_success(message=_('Yetkilerin aktarılması süre alabilir. Ekranı kapatabilirsiniz.'),
                                     title=_('İşlem Tamamlanmıştır'))

    @api.onchange('zone_id')
    def onchange_zone_id(self):
        if self.zone_id:
            self.affected_count = len(self.zone_id.auth_ids.mapped('employee_id'))
