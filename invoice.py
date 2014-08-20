# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields


class account_invoice(osv.Model):
    _inherit = 'account.invoice'
 
    _columns = {
		'deducible': fields.selection([('SI','SI'),('NO','NO')], 'Deducible ?'),
    }

account_invoice() 
