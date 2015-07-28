from openerp.osv import fields, orm
from lxml import etree

class sale_wizard(orm.TransientModel):
    _name = 'sale.wizard'
    _description = 'Wizard to update qty in sale lines'
    _columns = {
        'product_line_ids' : fields.many2one('product.product', 'Select Product'),
        'qty' : fields.integer('Quantity'),
#         'product_info' : fields.one2many('line.product.quantity', 'product_id', 'Line need to update'),
        
    }
    
    def update_order_lines(self, cr, uid, ids, context):
        wizard_record = self.browse(cr, uid, ids, context=None)
        order_line_obj = self.pool.get('sale.order.line')
        for wizard in wizard_record:
            order_line = order_line_obj.search(cr, uid, [('order_id', '=', context.get('order_id')), ('product_id', '=', wizard.product_line_ids.id)])
            order_line_obj.write(cr, uid, order_line[0], {'product_uom_qty' : wizard.qty})
        return True


    def fields_view_get(self, cr, uid, view_id=None, view_type=False, context=None, toolbar=False, submenu=False):
        if context is None:
            context = {}
        res = super(sale_wizard, self).fields_view_get(cr, uid, view_id=view_id, view_type=view_type, context=context, toolbar=toolbar, submenu=submenu)
        doc = etree.XML(res['arch'])
        method_nodes = doc.xpath("//form/group/field[@name='product_line_ids']")
        order_id = context.get('order_id')
        order_lines = self.pool.get('sale.order').browse(cr, uid, order_id, context=None)
        product_ids = []
        if order_lines:
            order_lines=order_lines.order_line
            for order_line in order_lines:
                product_ids.append(order_line.product_id.id)
        for node in method_nodes:
            node.set('domain', "[('id', 'in', " + str(product_ids) + ")]")
        res['arch'] = etree.tostring(doc)
        return res
    
     
# class  product_qty_selection(orm.TransientModel):
#     _name = 'line.product.quantity'
#     _columns = {
#             'product_id' : fields.many2one('product.product', 'Product'),
#             'qty' : fields.integer('Quantity'),
#             }
