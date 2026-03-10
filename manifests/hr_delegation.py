# -*- coding: utf-8 -*-
{
    'name': "Turkish Aerospace Human Resources Delegation Module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "EkipEpic - Tusaş",
    'website': "https://www.tusas.com.tr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr_employee_ext', 'base_tier_validation_ext'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/assets_backend.xml',
        'views/views.xml',
        'views/wizards.xml',
        'views/templates.xml',
        'views/res_users_role.xml',
        'views/delegation_reason.xml',
        'data/ir_cron.xml',
        'data/new_cron.xml',
        'data/mail_activity_delegation.xml'
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
