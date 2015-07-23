from openerp.osv import orm,fields
import random

class student_info_teachers(orm.Model):
    _name="student.info.teachers"
    _columns={
        'name':fields.char('Teachers',size=30,select=True,help='Please Enter the teachers name'),
        'address':fields.char('Address',size=30),
        'address1':fields.char(size=30),
        'pin':fields.char(size=30,change_default=True),
        'city':fields.char('pin',size=30),
        'country_id':fields.many2one('res.country'),
        'room_id1':fields.many2one("student.info.classroom"),
        'rand_id':fields.integer("Teacher Number:",readonly=True)
        }
    _defaults={
              'pin':'605009',
              'rand_id': lambda s, cr, uid, x: random.randint(1,10)
              }