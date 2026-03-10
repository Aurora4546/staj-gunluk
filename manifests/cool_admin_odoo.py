# -*- coding: utf-8 -*-
{
    'name': "Cool Admin Odoo",
    'summary': """ Cool Admin Dashboard for Odoo """,
    'description': """Cool Admin Dashboard Integrated For Odoo""",
    'author': """TAI""",
    'website': """https://www.tai.com.tr/""",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'web'],
    'qweb': [
        'static/src/xml/cool_admin_odoo_chart_widget.xml',
        'static/src/xml/cool_admin_odoo_chart_widget2.xml',
    ],
    'data': [
        "security/groups.xml",
        'views/cool_admin_odoo_chart_action.xml',
        'views/cool_admin_odoo_chart_template.xml',

    ]

}
