# -*- coding: utf-8 -*-
{
    'name': "Turkish Aerospace User Authorization",

    'summary': """With this module now you can request your roles.""",

    'description': """
        Request Roles from Role Owners and track the status.
    """,

    'author': "EkipEpic - Tusaş",
    'website': "https://www.tusas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail_ext', 'base_user_role', 'hr', 'approval_dashboard', 'base_environment', 'hr_competence'],

    'qweb': [
        'static/src/xml/entrance_template.xml',
        'static/src/xml/collective_confirm.xml',
    ],

    # always loaded
    'data': [
        'security/res_group_cron.xml',
        'security/ir.model.access.csv',
        'data/activity_type_data.xml',
        'data/ir_cron.xml',
        'data/config_parameters.xml',
        'data/role_control_cron.xml',
        'data/ir_sequence.xml',
        # 'views/hr.xml',
        'views/role.xml',
        'views/role_request.xml',
        'views/my_roles.xml',
        'views/organisation_profile_department_inherit.xml',
        'views/organisation_profile.xml',
        # 'views/ldap_views.xml',
        'views/templates.xml',
        'views/role_control.xml',
        'views/role_department_control.xml',
        'wizards/activity_control_wizard.xml',
        'wizards/role_unassign_wizard.xml',
        'wizards/change_auth_managers_wizard.xml',
        'wizards/change_competence_roles_wizard.xml',
        'wizards/organisation_profile.xml',
        'views/res_config_settings.xml',
        'security/groups.xml',
        'views/entrance_action.xml',
        'views/entrance_assets.xml',
        'views/menus.xml',
        # 'views/login.xml',
        'security/rules.xml',
        # 'data/ldap_data.xml',
        # 'data/ldap_department_data.xml',
        'views/templates_qweb.xml',
        'views/ir_cron_log.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
