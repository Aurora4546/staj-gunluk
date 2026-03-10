# -*- encoding: utf-8 -*-
{
    "name": "HR Employee History",
    "version": "12.0",
    "author": "TAI",
    "website": "https://www.tai.com.tr",
    "sequence": 0,
    "depends": ["hr", "hr_employee_ext"],
    "category": "HR",
    "complexity": "easy",
    'license': 'LGPL-3',
    'support': '',
    "description": """
HR revision history
	""",
    "data": [
        'security/security.xml',
        'views/hr_movements_views.xml',
        'views/bulk_wizards.xml',
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'data/mail_template_two.xml',
        'views/email.xml',
        'views/history_bulk_save_view.xml',
        'views/import_histories_excel.xml',
        'data/department_mail.xml',
        'data/ir_cron.xml',
        'data/job_history_import.xml',
    ],
    'depends': ['mail', 'hr', 'hr_employee_ext'],

    "auto_install": False,
    "installable": True,
    "application": False,
    'images': ['static/description/banner.png'],

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
