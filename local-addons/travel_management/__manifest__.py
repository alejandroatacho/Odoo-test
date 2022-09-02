{
    'name': "0.Odoo_Sandboxs",
    'version': '0.1',
    'author': 'Odoo S.A.',
    'website': 'https://www.odoo.com/',
    'category': 'Uncategorized',
    'summary': 'Odoo Sandboxs',
    'depends': ['base', 'mail', 'uom'],
    'description': "Hello_World!",
    'data': [
        'security/ir.model.access.csv',
        'views/travel.xml',
        # 'views/templates.xml',
    ],
    'demo:': [
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',

}
