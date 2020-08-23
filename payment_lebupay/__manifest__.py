# -*- coding: utf-8 -*-

{
    'name': 'EaglePay Payment Acquirer',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: EaglePay Implementation',
    'version': '13.0.0.0',
    'description': """

LebuPay Payment Acquirer
=======================
Payment through credit/debit cards,
bKash, Rocket, bank accounts, or agent banking
""",
    'author': 'Eagle ERP.',
    'website': 'https://metamorphosis.com.bd',
    'depends': ['payment', 'website'],
    'data': [

        'views/payment_views.xml',
        'views/payment_lebupay_templates.xml',     
        'views/success_views.xml',
        'views/failure_views.xml',
        'data/payment_acquirer_data.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}