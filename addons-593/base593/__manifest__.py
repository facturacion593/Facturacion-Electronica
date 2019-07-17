# -*- coding: utf-8 -*-
{
    'name': "base593",

    'summary': """
        Modulo base para el sistema de facturación en línea para Ecuador (593)""",

    'description': """
        El propósito de este módulo es crear el entorno necesario para que la facturación electrónica de Ecuador (593) funcione.
        En este módulo base se crearan el diccionario de datos y variables necesarios que el SRI de Ecuador requiere para porder 
        emitir facturas, retenciones y guías de remisión electrónicas.
    """,

    'author': "Desarrollo 593",
    'website': "http://www.desarrollo593.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'base',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        # Para este módulo es necesario instalar la siguiente herramienta
        # percent_field  # Descargar desde:  https://apps.odoo.com/apps/modules/12.0/percent_field/
        'percent_field',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/base593_views.xml',
        'views/base593_actions.xml',
        'views/base593_menus.xml',
        #'views/views.xml',
        'views/templates.xml',
        'security/base593_groups.xml',
        'security/ir.model.access.csv',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}