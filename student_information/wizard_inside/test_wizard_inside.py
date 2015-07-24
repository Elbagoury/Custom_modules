from openerp.osv import fields,orm

class test_wizard_inside(orm.TransientModel):
    
    _name="test.wizard.inside"
    
    _columns={
              'name':fields.char("Name",size=15),
              'remarks':fields.selection([('Good','Good'),('Fair','Fair'),('Best','Best')],string="Character")
              }
    
    def wizard_inside_test(self,cr,uid,ids,context=None):
        print "Test Finish"
        
        