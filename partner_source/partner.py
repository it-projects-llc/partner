# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import netsvc
from openerp import fields, models
from openerp.tools.translate import _

class res_partner_source(models.Model):
    _name = "res.partner.source"
    _description = "Partner Source"
    _order = "name"


    name = fields.Char('Name', required=True, translate=True)



class res_partner(models.Model):
    _inherit = "res.partner"


    source_id = fields.Many2one('res.partner.source', string='Source',)



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
