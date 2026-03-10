from odoo import api, fields, models, exceptions, _, SUPERUSER_ID


class CardReturnWizard(models.TransientModel):
    _name = 'tier.validation.send.wizard'
    _description = 'Tier Validation Send Wizard'

    auth_request_id = fields.Many2one(
        'hr.attendance.card.auth.request',
        string="Request ID"
    )

    def action_send_request(self):
        if self.auth_request_id.create_uid and self.env.uid in (self.create_uid.id, SUPERUSER_ID):
            self.auth_request_id._request_validation()
            return {
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'hr.attendance.card.auth.request',
                'target': 'self',
                'res_id': self.auth_request_id.id,
                'context':  {'no_breadcrumbs': True,},
            }
        else:
            raise exceptions.ValidationError(_(
                'Sadece talebi oluşturan kişi onaya gönderebilir. Bir hata olduğunu düşünüyorsanız Yardım Masası Talebi açabilirsiniz.'))



