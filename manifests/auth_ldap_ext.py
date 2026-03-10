# -*- coding: utf-8 -*-
{
    'name': "Turkish Aerospace LDAP/AD Authentication Extensions",

    'summary': """
        LDAP extension """,

    'description': """
         LDAP extension
    """,

    'author': "TAI",
    'website': "https://www.tusas.com.tr/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extension',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','auth_ldap','base_user_role','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/temp.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
