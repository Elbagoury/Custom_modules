from openerp.osv import fields, orm

class test_wizard(orm.TransientModel):
    _name="test.wizard"
    _description="My Test Wizard module"
    
    _columns={
              's1':fields.integer("Tamil"),
              's2':fields.integer("English"),
              's3':fields.integer("Maths"),
              's4':fields.integer("Science"),
              's5':fields.integer("Social"),
              'result':fields.char(),
              'student_ids':fields.one2many("student.mark","name",String="Student Info")
              
              }
    
    def test_ok(self,cr,uid,ids,context):
        
        wizz = self.browse(cr,uid,ids,context = None)
        stud_obj = self.pool.get("student.info.student")
        
        for tst_obj in wizz:
            stud = stud_obj.search(cr,uid,[])
            
            
            t = tst_obj.s1 + tst_obj.s2 + tst_obj.s3 + tst_obj.s4 + tst_obj.s5
 
            avg = t / 5
            if tst_obj.s1 >= 35 and tst_obj.s2 >= 35 and tst_obj.s3 >= 35 and tst_obj.s4 >= 35 and tst_obj.s5 >= 35:
                  
                if avg >= 90:
                    a = "S Grade"
                    print a
                 
                elif avg >= 80:
                    a = "A Grade"
                    print a                
                elif avg >= 70:
                    a = "B Grade"
                    print a                
                 
                elif avg >= 60:
                    a = "C Grader"
                    print a
                elif avg >= 50:
                    a = "D Grade"
                    print a
                                         
                elif avg < 50:
                    a = "Dull Student :::: Pass"    
                    print a
             
            elif avg :
                if (tst_obj.s1 < 35 or tst_obj.s2 < 35 or tst_obj.s3 < 35 or tst_obj.s4 < 35 or tst_obj.s5 < 35) and avg > 50:
                    a = "Dull Student :::: Fail"
                    print a
                elif (tst_obj.s1 < 35 or tst_obj.s2 < 35 or tst_obj.s3 < 35 or tst_obj.s4 < 35 or tst_obj.s5 < 35) and avg < 50:
                    a = "Dull Student :::: Fail"
                    print a
                     
            tst_obj.result = a
                    
            stud_obj.write(cr,uid,stud,{'status_stud': tst_obj.result })
            
        
            print "TEST Ok!!!!!!!!!!!!!!!!"
            
        return True
    
    def ok_butt(self,cr,uid,ids,context=None):
        print "Purchase Finalized"
        return True
    
    def cancel_butt(self,cr,uid,ids,context=None):
        print "Purchase canceled"
        return True
    
    def wizard_inside_test_method(self,cr,uid,ids,context=None):
        mod_obj=self.pool.get('ir.model.data')
        view_id=mod_obj.get_object_reference(cr,uid,'student_information','wizard_test_inside_form_view')
        return {
                'name' : "Wizard_Inside_wizard Test",
                'view_type':'form',
                'view_mode':'form',
                'view_id':view_id and view_id[1] or False,
                'res_model':'test.wizard.inside',
                'src_model':'test.wizard',
                'type':'ir.actions.act_window',
                'context':context,
                'target':'new',
                }
        
        
                    