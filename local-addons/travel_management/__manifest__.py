{
    'name': "Travel Management",
    'author': "Hinamizawa",
    'summary': """ Odoo CookBook  """,
    'description': """
        A Book Assignment from Odoo CookBook 14.0
    """,
    'price': 0.99,
    'currency': 'USD',
    'category': 'Profile Management',
    'company': 'SMART-OBC',
    'website': 'alejandroatacho.github.io',
    'category': 'Tools',
    'version': '0.2',
    'sequence': '-100',
    'depends': ['base'],
    # 'images': 'static/description/applogo.png',
    'data': [
        # 'security/groups.xml',
        'security/ir.model.access.csv',
        'views/travel_management.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    'demo': [
        # 'demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
