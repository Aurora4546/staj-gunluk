# -*- coding: utf-8 -*-
{
    'name': "Facility Management",

    'summary': """Module to manage Facilities""",

    'description': """
        With this module you can manage your facilities.
    """,

    'author': "Tusaş",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Facility Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'web_notify'],
    'external_dependencies': {'python': ['unicode_tr']},

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/access_rules.xml',
        'views/fm_building_view.xml',
        'views/fm_building_category_view.xml',
        'views/fm_building_floor_poi_view.xml',
        'views/fm_building_floor_area_category_view.xml',
        'views/fm_building_floor_area_view.xml',
        'views/fm_building_floor_view.xml',
        'views/fm_building_block_view.xml',
        'views/fm_building_attachment_view.xml',
        'views/fm_company_location_view.xml',
        'views/fm_building_floor_pop_up_view.xml',
        'wizards/views/fm_building_floor_poi_creation_view.xml',
    ],

}
