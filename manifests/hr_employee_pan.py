# -*- coding: utf-8 -*-
{
    'name': "hr_employee_pan",
    'summary': """
        Employee Expand Module""",

    'description': """
        Employee Expand Module
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_employee_ext', 'notification_management'],

    # always loaded
    'data': [
        'data/working_types.xml',
        'security/hr_security.xml',
        'security/access_rules.xml',
        'security/critical_emp_rep_group.xml',
        'security/contract_report_security.xml',
        'security/ir.model.access.csv',
        'views/reward_type.xml',
        'views/article_views.xml',
        'views/employee_security_views.xml',
        'views/document_type_views.xml',
        'views/document_viewer_views.xml',
        'views/working_type_views.xml',
        'views/reason_for_leaving.xml',
        'views/report_template.xml',
        'views/action_server_employee.xml',
        # 'views/kgb_views.xml',
        'views/trainee_special_view.xml',
        'views/ext_views.xml',
        'views/employee_chief_views.xml',
        'views/hr_high_job.xml',
        'views/education_exam_views.xml',
        'views/hr_norm.xml',
        'views/template.xml',
        'views/employee_case_definition.xml',
        'views/department_branch_definition.xml',
        'views/hr_department.xml',
        'views/hr_employee_activity_view.xml',
        'views/company_emp_logs_views.xml',
        'views/certificate_information.xml',
        'views/employee_relative.xml',
        'data/ir_cron_and_templates.xml',
        'data/clothes_cron.xml',
        'data/sgk_report_activity_type.xml',
        'data/activity_insof_mail.xml',
        'data/mail_for_workmanship_status.xml',
        'data/mail_templates.xml',
        'data/deactivate_emp_leaving_date.xml',
        'data/update_mail_and_parents.xml',
        'data/employee_role_create.xml',
        'data/days.xml',
        'data/sep_deact_cron.xml',
        'data/update_some_partner_info.xml',
        'wizards/views/select_employee_views.xml',
        'wizards/views/language_creation_wizard.xml',
        'wizards/views/reward_creation_wizard.xml',
        'views/menus.xml'
        

    ],
    # only loaded in demonstration mode

}
