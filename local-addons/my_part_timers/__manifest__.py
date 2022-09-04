{
    'name': "My Part Timers",
    'author': "Hinamizawa",
    'summary': """ Odoo CookBook  """,
    'description': """
┬┴┬┴┤ʕ•ᴥ├┬┴┬┴ 
    """,
    'price': 0.99,
    'currency': 'USD',
    'category': 'Profile Management',
    'company': 'SMART-OBC',
    'website': 'https://github.com/alejandroatacho',
    'category': 'Tools',
    'version': '14.0.1.0',
    'sequence': '-110',
    'depends': ['base'],
    # 'images': 'static/description/applogo.png',
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/my_part_timers.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    'demo': [
        # 'demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}
