# -*- coding: utf-8 -*-

# Para este módulo es necesario instalar la siguiente herramienta
# percent_field  # Descargar desde:  https://apps.odoo.com/apps/modules/12.0/percent_field/

from odoo import models, fields, api

# class base593(models.Model):
#     _name = 'base593.base593'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class base593_type_iva_retention(models.Model):
    
    _name = 'base593.type.iva.retention'
    _description = 'Modelo que almacena los tipos de iva, de acuerdo al SRI, que se pueden retener a una empresa'
    
    _sql_constraints = [
        ('unique_code', 'unique(code)', u'Código interno ya está en uso'),
        ('unique_sri_code', 'unique(sri_code)', u'Código de SRI ya está en uso'),
    ]

    code = fields.Char(u'Código Interno:', size=4, required=True )
    name = fields.Char(u'Nombre:', size = 50, required=True)
    sri_code = fields.Char(u'Código SRI:', size = 4, required=True)
    percent = fields.Float(u'Porcentaje (%):', size = 3, required=True)


class base593_type_retention(models.Model):
    _name = 'base593.type.retention'
    _description = 'Modelo que almacena los tipos de retenciones del SRI'

    _sql_constraints = [
        ('unique_code', 'unique(code)', u'Código interno ya está en uso'),
        ('unique_sri_code', 'unique(sri_code)', u'Código de SRI ya está en uso'),
    ]

    code = fields.Char(u'Código Interno:', size=4, required=True )
    name = fields.Char(u'Nombre:', size = 50, required=True)
    sri_code = fields.Char(u'Código SRI:', size = 4, required=True)
    percent = fields.Float(u'Porcentaje (%):', size = 3, required=True)


class base593_type_person(models.Model):
    _name = 'base593.type.person'
    _description = 'Modelo que almacena los tipos de personas (Jurídicas, Naturales....)'

    _sql_constraints = [
        ('unique_code', 'unique(code)', u'Código interno ya está en uso'),
        ('unique_sri_code', 'unique(sri_code)', u'Código de SRI ya está en uso'),
    ]

    code = fields.Char(u'Código Interno:', size=4, required=True )
    name = fields.Char(u'Nombre:', size = 50, required=True)
    sri_code = fields.Char(u'Código SRI:', size = 4, required=True)
