{
    'name': 'POS Extended Benotto',
    'version': '1.0',
    'author':'ANFEPI: Roberto Requejo Fernández',
    'depends': ['sh_pos_analytic_tags'],
    'description': """
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/pos_config_search_view.xml',
        'views/pos_config_view.xml',
        'views/pos_order_search_view.xml',
        'wizard/pos_aa_sales_report_view.xml'
        
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    "license": "AGPL-3",
}