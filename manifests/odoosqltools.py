# -*- coding: utf-8 -*-
{
    'name': "Odoo Sql Tool Fixes",

    'summary': """
        This modules fixes the odoo's default sql orm engine bugs.""",

    'description': """
        We have to use this module to maintenance new features comes with postgresql 12
    """,

    'author': "Tusaş - Ekip Epic",
    'website': "www.tai.com.tr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],

}