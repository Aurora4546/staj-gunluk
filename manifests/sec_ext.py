# -*- coding: utf-8 -*-
{
    'name': "Turkish Aerospace Security Extensions ",

    'summary': """Generic security patches""",

    'description': """
        This module created for fix the security issues..
    """,

    'author': "EkipEpic&Ekip6 - Tusaş",
    'website': "https://www.tusas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
