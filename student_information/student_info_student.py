from openerp.osv import orm, fields
from datetime import date
from datetime import datetime

class student_info_student(orm.Model):
    _name = "student.info.student"
    _inherit = 'mail.thread'
    _rec_name = "name"
    
    def _has_image(self, cr, uid, ids, name, args, context=None):
        result = {}
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = obj.s_img != False
        return result
    
    def wizard_test_method(self,cr,uid,ids,context=None):
        mod_obj=self.pool.get('ir.model.data')
        view_id=mod_obj.get_object_reference(cr,uid,'student_information','test_wizard')
        return {
                'name' : "Sale Test",
                'view_type':'form',
                'view_mode':'form',
                'view_id':view_id and view_id[1] or False,
                'res_model':'test.wizard',
                'src_model':'student.info.student',
                'type':'ir.actions.act_window',
                'context':context,
                'target':'new',
                }
    def google(self,cr,uid,ids,context=None):
#         res=self.read(cr,uid,ids,['s_img'],context=context)
        return{
#                'type':'ir.actions.act_url',
#                'url':'https://www.google.com',
#                'target':'new',
                "type": "ir.actions.client",
                "tag": "reload"

               }
        
    
    _columns = {
        'name':fields.char("Name", size=30, required=True),
        'age':fields.integer(),
        'fname':fields.char("Father Name", size=30),
        'mname':fields.char(size=30),
        'dob':fields.date(),
        'a_class':fields.char(),
        'a_class_date':fields.date("Join Date"),
        'c_class_date':fields.date("AStart Date"),
        'c_class':fields.char(),
        'address':fields.char(),
        'street':fields.char(),
        'state_id':fields.char(),
        'pincode':fields.char(),
        'country':fields.many2one("res.country"),
        'l_line':fields.char(size=12),
        'c_no':fields.char(size=13),
        's_img':fields.binary(),
        'room_id':fields.many2one('student.info.classroom'),
        'ref':fields.reference('Refered By', [('res.partner', 'Partner')], size=20),
        'state':fields.selection([('draft', 'draft'), ('trashed', 'trashed')], string="Status"),
        'reg_no':fields.char('Register Number', size=20),
        'has_image': fields.function(_has_image, type="boolean"),
        'status_stud':fields.char("Mark Details")
        
    }
    
    _track = {
            'state':{
                     
                     'student_information.subtype_draft_xml': lambda self, cr, uid, obj, context = None:obj['state'] == 'draft',
                     'student_information.subtype_trash_xml': lambda self, cr, uid, obj, context = None:obj['state'] == 'trashed',
            }
            }
    def _age_constraint(self, cr, uid, ids, context=None):
        
        for a in self.browse(cr, uid, ids, context=context):
            b = int(a.age)
            c = int(a.c_class)
        if (c == 1) and (b >= 5 and b <= 7):
            return True
        elif (c == 2) and (b >= 6 and b <= 8):
            return True
        elif (c == 3) and (b >= 7 and b <= 9):
            return True
        elif (c == 4) and (b >= 8 and b <= 10):
            return True
        elif (c == 5) and (b >= 9 and b <= 11):
            return True
        elif (c == 6) and (b >= 10 and b <= 12):
            return True
        elif (c == 7) and (b >= 11 and b <= 13):
            return True
        elif (c == 8) and (b >= 12 and b <= 14):
            return True
        elif (c == 9) and (b >= 13 and b <= 15):
            return True
        elif (c == 10) and (b >= 14 and b <= 16):
            return True
        
        return False
        
    
    _constraints = [
                  (_age_constraint, 'You are not allowed to the join this class', ['c_class', 'age'])
    ]
    _sql_constraints = [
                      ('uniq_constraints', 'UNIQUE (room_id,name,fname)', 'Ha Ha unique'),
    ]
    
    _defaults={
               'state': 'draft',
               }

    def create(self, cr, uid, vals, context=None):
        if not vals:
            vals = {}
        if context is None:
            context = {}
        vals['reg_no'] = self.pool.get('ir.sequence').get(cr, uid, 'reg_num')
        return super(student_info_student, self).create(cr, uid, vals, context=context)

    
    
    def search_stud(self, cr, uid, ids, dob, context=None):
            a = datetime.strptime(dob , '%Y-%m-%d')
            b = date.today().year
            c = a.year
            f = b - c
            return {'value':{'age':f}}
        
    def orm_test(self, cr, uid, ids, context=None):
        a = self.search(cr, uid, [], context=context)
        res = {}
        for b in self .browse(cr, uid, ids, context=None):
            c = b.name
        print c 
        print "OK"
        return res
    
   
    
class res_partner(orm.Model):
    _inherit = 'res.partner'
    
    _columns = {
        'ptype':fields.selection([('a', 'Internet Baanking'), ('b', 'Credit Card Purchase'), ('c', 'COD')], string="Payment Type")
    }
    
class sale_order(orm.Model):
    _inherit = "sale.order"
    
    _columns = {
        'ptype':fields.selection([('a', 'Internet Baanking'), ('b', 'Credit Card Purchase'), ('c', 'COD')], string="Payment Type")
    }
    
    def onchange_partner_id(self, cr, uid, ids, partner_id, context=None):
        res = super(sale_order, self).onchange_partner_id(cr, uid, ids, partner_id, context=context)
        if partner_id:
            result = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
            res['value']['ptype'] = result.ptype
        else:
            result = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
            res['value']['ptype'] = False
            
        print res
        print "OK"
        
        return res
    
    
    

    
    
    
    
    
    
