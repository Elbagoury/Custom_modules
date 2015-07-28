from openerp.osv import orm,fields

class student_info_classroom(orm.Model):
    _name="student.info.classroom"
    _rec_name="name"
    _columns={
        'name':fields.char('Class Room',size=30),
        'student_id':fields.one2many('student.info.student','room_id','List of Students'),
        'teachers_id':fields.many2many('student.info.teachers','student_info_teachers_teacher_id','teachers_id','room_id1','Teachers'),
    }
    
    
#     def test_field_get(self,cr,uid,ids,context=None):
#         a = self.fields_get(cr,uid,context=None)['name']
#         print a


#     def test_fields_view_get(self,cr,uid,ids,context=None):
#         a = self.fields_view_get(cr,uid)
#         print a
        
        
    def fields_view_get(self, cr, uid, view_id=None, view_type=False, context=None, toolbar=False, submenu=False):
        if context is None:
            context = {}
        res = super(student_info_classroom, self).fields_view_get(cr, uid, view_id=view_id, view_type=view_type, context=context, toolbar=toolbar, submenu=submenu)
        print res
        return res