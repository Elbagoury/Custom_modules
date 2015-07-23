from openerp.osv import fields, orm

class sale_order(orm.Model):
    _inherit = 'sale.order'
    
    
    def action_change_line_qty(self, cr, uid, ids, context=None):
        mod_obj = self.pool.get('ir.model.data')
        context.update({'default_qty':100})
        view_id = mod_obj.get_object_reference(cr, uid, 'wizard_module', 'sale_wizard')
        return {
            'name': "Sale Wizard" ,
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_id and view_id[1] or False,
            'res_model': 'sale.wizard',
            'src_model': 'sale.order',
            'type': 'ir.actions.act_window',
            'context': context,
            'target': 'new',
            }
