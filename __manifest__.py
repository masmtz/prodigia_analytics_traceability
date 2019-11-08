# -*- coding: utf-8 -*-
{
    'name': "Trazabilidad de Analíticas",
    'shortdesc': "Trazabilidad de Analíticas",
    'summary': """
        Trazabilidad de analíticas (cuentas y etiquetas)
    """,

    'description': """
        Permite enviar cuentas y etiquetas analíticas desde su origen (Orden de compra, Presupuesto / Pedido de venta y Ajustes de inventario)
        pasando por movimientos de almacén (entradas / salidas) y Facturas, hasta llegar a los apuntes contables.
        En Ajustes de inventario, la cuenta analítica seleccionada pasará a los apuntes contables cuando el ajuste se haya aplicado.
        En configuraciones se puede especificar si queremos manejar las cuentas y etiquetas analiticas por linea o a nivel de documento (para compras y ventas).
    """,

    'author': "Prodigia",
    'maintainer':'Samuel Martínez',
    'website': "http://www.prodigia.com.mx",
    'category': 'Account',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account','account_reports','sale_stock','purchase'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/stock.xml',
        'views/account.xml',
        'views/purchase.xml',
        'views/sale.xml',
     ],
}
