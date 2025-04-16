{
    'name': 'Program Learning Outcomes',
    'author': 'Author Name',
    'category': '',
    'version': '17.0.0.1.0',
    'summary': 'Manage program learning outcomes like Domains, Sub-Domains, and PLOs',
    'depends': ['base', 'university'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_views.xml',
        'views/domain_views.xml',
        'views/sub_domain_views.xml',
        'views/plo_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
