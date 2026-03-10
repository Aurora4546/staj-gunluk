# -*- coding: utf-8 -*-
{
    'name': 'Notification Management',
    'version': '1.0.0.0.1',
    'summary': 'Notification Management',
    'category': 'Tools',
    'author': 'nybozatli',
    'company': 'TAI',
    'website': 'https://erp.tai.com.tr/en_US/',
    'depends': ['base', 'mail', 'hr_delegation'],
    'data': [
        'security/ir.model.access.csv',
        'views/delegation/delegation_management.xml',
        'views/mail_activity/mail_activity.xml',
        'views/mail_activity/mail_activity_type.xml',
        'views/external_api/external_notification.xml',
        'views/external_api/external_system.xml',
        'views/ir_model/ir_model.xml',
        # 'data/ir.cron.xml',
        'data/mail_activity_type.xml'
    ],
    'images': ['static/description/img/logo.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
