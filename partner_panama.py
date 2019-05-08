# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo
#    Copyright (C) 2019 AlconSoft-Sistech (<http://alconsoft.net>).
#
##############################################################################

from odoo import api, fields, models
from odoo import tools

class res_partner(models.Model):
    _inherit = "res.partner"
    _columns = {
                # RUC: Registro Unico del Contribuyente (Panama)
                'ruc': fields.char('RUC', size=45, required=True),
                # DV: Digito verificador
                'dv': fields.char('DV', size=2, required=True),
                # TIPO_PERSONA
                #  1=NATURAL 
                #  2=JURIDICO
                #  3=OTROS
                #  4=EXTRANJERO
                'tipo_persona': fields.selection([('1','NATURAL'),('2','JURIDICO'),('3','OTROS'),('4','EXTRANJERO')],'Tipo Persona',required=True),
                # Concepto Varios a Uno
                #'concepto' : fields.many2one('anexos.conceptos.pa', 'concepto','Anexo Concepto', store=True, readonly=False)
                #'concepto' : fields.many2many('anexos.conceptos.pa','res_partner_anexos_conceptos_pa_rel','partner_id', 'concepto','Concepto de Anexo', store=True, readonly=False)
               }