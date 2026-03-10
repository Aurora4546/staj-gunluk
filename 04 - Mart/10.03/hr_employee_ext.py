# -*- coding: utf-8 -*-
{
    'name': "Employees",

    'summary': """
        TAI Hr module extension
        """,

    'description': """
        TAI HR module extension
    """,

    'author': "TAI",
    'website': "https://www.tai.com.tr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'HR',
    'version': '0.1',

    # any module necessary for this one to work correctly

    'depends': ['base','hr','hr_department_ext','project','base_environment','hr_environment','facility_management','intl_tel_widget'],
    "external_dependencies": {'python': ['unicode_tr'] },

    # always loaded
    'data': [
        'security/hr_security.xml',
        'security/ir.model.access.csv',
        'data/mail.xml',
        'data/mmu_mail.xml',
        'data/config_parameters.xml',
        'data/crypto_mail.xml',
        'data/change_name_mail.xml',
        'data/activity_type.xml',
        #'security/access_rules.xml',
        'views/templates.xml',
        'views/hr_employee_view.xml',
        'views/hr_academic_view.xml',
        'views/hr_professional_view.xml',
        'views/hr_certification_view.xml',
        'views/hr_employee_relative.xml',
        'views/hr_employee_health_condition.xml',
        'views/hr_employee_private_information.xml',
        'views/hr_employee_work_health.xml',
        # 'views/hr_employee_size.xml' private tabına eklendiği için kapatıldı,
        # 'views/hr_employee_promotion.xml',
        'views/hr_inhouse_training.xml',
        'views/hr_employee_security.xml',
        #'views/hr_employee_other_information.xml',
        'views/ir_cron.xml',
        'views/hr_job_view.xml',
        'views/hr_employee_security.xml',
        'views/authority.xml',
        'views/work_information.xml',
        'views/hr_employee_last_views.xml',
        'views/menus.xml',
        'views/hr_department_ext.xml',
        #'views/disable_export_view.xml'
        #'views/wizards.xml',
        'views/hr_sgk_company_view.xml',
        'views/hr_employee_action.xml',
        'views/hr_employee_definitions.xml',
        'models/activities/views/security_statement_yes_activity.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
'qweb':[
    #'static/src/xml/org_chart_temp.xml',
    #    'static/src/xml/base_ext.xml',
    
]
}
