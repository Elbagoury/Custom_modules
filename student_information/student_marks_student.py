from openerp.osv import fields,orm


class student_marks(orm.Model):
    
    _name="student.mark"
    
    _columns={
              'name':fields.many2one("student.info.student"),
              
              }
    
   