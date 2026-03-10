# -*- coding: utf-8 -*-
{
    'name': "base_environment",

    'summary': """
        Common parameters used in all modules """,

    'description': """
       Generic parameters definition.
       This module is used to store the common parameters of all other modules
    """,

    'author': "İlknur Ünal",
    'website': "https://www.yourmpany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web', 'base_address_city', 'resource', 'calendar'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/root_menu_hide_groups.xml',
        'security/ir.model.access.csv',
        'views/file_templates.xml',
        'views/res_building_views.xml',
        'views/assets.xml',
        'views/res_county_views.xml',
        'views/res_lunch_views.xml',
        'views/res_transportation_views.xml',
        'views/res_location_views.xml',
        'views/currency_rate_views.xml',
        'views/res_menu.xml',
        'views/root_menu_hide.xml',
        'views/form_simple_modif.xml',
        'data/email_address.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml'
    ],
}