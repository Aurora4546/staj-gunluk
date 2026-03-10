from odoo import models, fields, api, exceptions, _
from datetime import datetime as dt
from itertools import chain


class AttendanceSummaryWizard(models.TransientModel):
    _name = 'hr.attendance.request.wizard'
    _description = 'Attendance Menu Wizard'

    name = fields.Char(default="Tesis Güvenlik")

