# -*- coding: utf-8 -*-
{
    'name': "Employee Tracking",

    'summary': """
        Employee Tracking""",

    'description': """
        Employee Tracking
    """,

    'author': "EkipEpic - Tusaş",
    'website': "https://www.tusas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    "version": "1.0.798-test",

    # any module necessary for this one to work correctly
    'depends': ['base',
                'base_environment',
                'hr_employee_ext',
                'facility_management',
                'base_tier_validation_ext',
                'web_notify',
                'odoosqltools',
                'hr_employee_history',
                'disable_open_record',
                'notification_management'
                ],
    'external_dependencies': {'python': ['pypika']},

    # always loaded
    'data': [
        'security/groups.xml',
        'security/permanent.xml',
        'security/ir.model.access.csv',
        'data/card_types.xml',
        'data/card_type_other.xml',
        'data/zone_types.xml',
        'data/terminal_types.xml',
        'data/resource_move_type_data.xml',
        'data/automated_expire_cron.xml',
        # 'data/hr_employee.xml',
        'views/activities.xml',
        'data/activities.xml',
        'data/sync_cron.xml',
        'views/area.xml',
        'views/building.xml',
        'views/zone.xml',
        'views/card.xml',
        'views/terminal.xml',
        'views/employee_history.xml',
        'views/authorization.xml',
        'views/authorization_request.xml',
        'views/card_replacement_request.xml',
        'views/secure_zone_request.xml',
        'views/employee.xml',
        'views/attendance_move.xml',
        'views/zone_auth_views.xml',
        'views/search_views.xml',
        'views/templates_qweb.xml',
        'views/templates.xml',
        'views/bulk_card_replacement.xml',
        'wizards/card_replacement.xml',
        'wizards/card_return_wizard.xml',
        'wizards/bulk_card_replace_wizard.xml',
        'wizards/card_assignment_wizard.xml',
        'wizards/tier_validation_send_wizard.xml',
        'wizards/auth_per_employee_assignment_wizard.xml',
        'wizards/auth_per_department_assignment_wizard.xml',
        'wizards/auth_per_building_assignment_wizard.xml',
        'wizards/auth_copy_wizard.xml',
        'wizards/employee_bulk_operations.xml',
        'wizards/confirmation_wizard.xml',
        'wizards/request_menu_wizard.xml',
        'views/integration_views/employee_movements.xml',
        'views/integration_views/move_types.xml',
        'views/assets_backend.xml',
        'views/integration_views/fdw_settings.xml',
        'views/reports.xml',
        'views/views.xml',
        'views/user.xml',
        'activities/views/activities.xml',
        'activities/data/activities.xml',
        'activities/security/ir.model.access.csv',
        'security/rules.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'application': 'True',
    'installable': 'True',
    'post_init_hook': '_refresh_mview'

}
