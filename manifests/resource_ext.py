# -*- coding: utf-8 -*-
{
    'name': "resource_ext",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com """,

    'description': """
        Long description of module's purpose
    """,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    "version": "1.0.475-test",

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance_ext', 'hr_shift_plan', 'report_creator', 'hr_workorder',
                'notification_management'],  # ,
    'external_dependencies': {'python': ['pandas']},

    # always loaded
    'data': [
        'security/groups.xml',
        'security/readonly_groups.xml',
        'security/external.xml',
        'security/rules.xml',
        'security/assistant_rules.xml',
        'security/user_group.xml',
        'security/workmanship_rule.xml',
        'security/workorder_summary_rule.xml',
        'security/activity_rule.xml',
        'security/ir.model.access.csv',
        'data/move_types.xml',
        'data/ir_cron.xml',
        'data/ir_cron2.xml',
        'data/ir_cron3.xml',
        'data/ir_cron4.xml',
        'data/ir_cron5.xml',
        'data/external_cron.xml',
        'data/draft_calculate_cron.xml',
        'data/ir_config_parameter.xml',
        'data/email_templates.xml',
        'views/activities.xml',
        'data/activities.xml',
        'data/work_order_cron.xml',
        'data/workmanship_cron.xml',
        'data/workmanship_soir_cron.xml',
        'data/workmanship_month_cron.xml',
        'data/parameters.xml',
        'views/resource.xml',
        'views/employee.xml',
        'views/assets_backend.xml',
        'views/attendance_summary.xml',
        'views/attendance_move.xml',
        'views/outer_emp_depts_views.xml',
        'views/unusual_situations.xml',
        'views/external_working_moves.xml',
        'views/external_status.xml',
        'views/find_difference.xml',
        'views/wo_data.xml',
        # 'views/workmanship_data.xml',
        # 'views/workorder_summary.xml',
        'wizards/attendance_summary_wizard.xml',
        'wizards/change_employee_calendar_wizard.xml',
        'wizards/change_employee_lunch_wizard.xml',
        'wizards/attendance_move_re_calculation.xml',
        'wizards/manager_approve_wizard.xml',
        'wizards/show_move_views.xml',
        'wizards/wo_diff_report.xml',
        'wizards/wo_time_control.xml',
        'wizards/start_date_wo_detail.xml',
        'wizards/monthly_workorder_operation.xml',
        'wizards/wo_personnel_q_report.xml',
        'wizards/wo_indirect_personnel.xml',
        'wizards/wo_personnel_moves.xml',
        'wizards/wo_collective_reports.xml',
        'wizards/daily_movement_editing.xml',
        'wizards/wo_bulk_update.xml',
        'wizards/attendance_move_execute_selected.xml',
        'wizards/menu_wizard.xml',
        'views/statistics.xml',
        'views/menus.xml',
        'wizards/test_summary_wizard.xml',
        'views/legacy.xml'
    ],
    'qweb': ['static/src/xml/*.xml'],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
