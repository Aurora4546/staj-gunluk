# -*- coding: utf-8 -*-
{
    'name': 'Hr environment  ',
    'version': '1.0',
    'summary': '--',
    'sequence': 61,
    'description': """

    """,
    'category': 'Human Resources',
    'depends': [
        'base_environment',
        "mail"
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/school_data.xml',
        'data/attachment_data.xml',
        'views/school.xml',
        'views/project_project_manager.xml',
        'views/staff_type.xml',
        'views/recruitment_par.xml',
        'views/menu.xml',
        'views/hr_job_view.xml',
        'views/res_config_settings_views.xml'

    ],
    'demo': [

    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
