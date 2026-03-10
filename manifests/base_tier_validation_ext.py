# -*- coding: utf-8 -*-
{
    'name': "base_tier_validation_ext",

    'summary': """
        Bu modül TUSAŞ onay/workflow yönetim sistemidir.""",

    'description': """
        Bu modül TUSAŞ onay/workflow yönetim sistemidir.
    """,

    'author': "EkipEpic - Tusaş",
    'website': "https://www.tusas.com.tr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_environment', 'base_tier_validation_formula', 'mail',
                'hr_department_ext', 'base_user_role_ext'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/tier_review_cancelled_rec.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/tier_model_admin.xml',
        'views/ir_cron.xml',
        "wizard/comment_wizard_view.xml",
        "wizard/rollback_wizard_view.xml",
        "wizard/skip_wizard_view.xml",
        "wizard/bulk_confirmation_wizard_view.xml",
        "wizard/bulk_process_queue_wizard.xml",
        "wizard/bulk_reset_review_wizard.xml",
        "wizard/revert_wizard.xml",
        "wizard/tier_model_admin_wizard.xml",
        'views/assets_backend.xml',
        'data/service_parameters.xml',
        'data/waiting_errors_count_cron.xml',
        'data/ir_cron.xml',
        'views/mail_templates.xml',
        'views/templates_qweb.xml',
        'security/groups.xml',
    ],
    # only loaded in demonstration mode
    'qweb': [
        'static/src/xml/tier_reviews.xml',
        'static/src/qweb/all_approve.xml',
        'static/src/qweb/all_refuse.xml',
        'static/src/qweb/save_send.xml',
        'views/history_widget.xml',
        'views/systray.xml',

    ],
    'application': True,
}
