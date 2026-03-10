# -*- coding: utf-8 -*-
{
    'name': "hr_department_ext  ",

    'summary': """
        This module include extentions for hr.department; such as, staff types, staff size, etc.""",

    'description': """
        This module include extentions for hr.department; such as, staff types, staff size, etc.
    """,

    'author': "EkipEpic - Tusaş",
    'website': "https://www.tusas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'base_user_role_ext', 'hr_environment'],

    # always loaded
    'data': [
        'security/groups.xml',
        'data/mail.xml',
        'security/ir.model.access.csv',
        'views/department_categories.xml',
        'views/hr.xml',
        'views/templates.xml',
        'views/wizards.xml',
        'views/ir_cron.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
