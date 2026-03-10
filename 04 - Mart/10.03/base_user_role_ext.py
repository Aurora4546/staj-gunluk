# Copyright 2014 ABF OSIELL <http://osiell.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'base_user_role_ext',
    'summary': 'User role extension module',
    'version': '12.0.1.0.0',
    'category': 'Tools',
    'author': 'ipekdeniz.demirtel@tai.com.tr',
    'website': "https://www.tusas.com",
    'depends': [
        'base',
        'base_user_role',
        'mail'
    ],
    'data': [
        'views/role.xml',
    ],
    'installable': True,
}
