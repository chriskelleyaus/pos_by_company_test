{
    'name': 'POS Product Restriction',
    'version': '13.0.1.0.0',
    'summary': 'Restrict POS Products by Company and Availability',
    'description': """
POS Product Restriction
=======================

Restrict POS products by company and availability
""",
    'category': 'Point of Sale',
    'author': 'Australian Buyers Group',
    'contributors': ['MAC5'],
    'website': 'https://www.ausbuygroup.com/',
    'depends': [
        'point_of_sale',
        'stock',
    ],
    'data': [
        'views/pos_templates.xml',
        'views/product_views.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'support': 'mac5_odoo@outlook.com',
    'license': 'OPL-1',
}
