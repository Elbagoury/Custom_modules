# # def testing():
# #     print 'test'
# #     a = 10
# #     b = 19
# #     print a+b
# #     c = a*b
# #     print c
# #     
# # testing()
# # x=3
# # print lambda x: x*2
# 
# 
# a = {('uniq_constraints', 'UNIQUE (room_id,name,fname)', 'Ha Ha unique'),('uniq_constraints', 'UNIQUE (room_id,name,fname)', 'Ha Ha unique')}
# print type(a)
# 
# print a

# 
# a = int(input("Enter the value: "))
# b = int(input("Enter the value: "))
# 
# if (a > 35 or a) and (b >35 or b):
#     c = a+b
#     print c
# else:
#     print "Wrong"
#     
#   


s1 = int(input("Enter The mark :"))
s2 = int(input("Enter The mark :"))
s3 = int(input("Enter The mark :"))
s4 = int(input("Enter The mark :"))
s5 = int(input("Enter The mark :"))

t = s1 + s2 + s3 + s4 + s5

avg = t / 5
if s1 >= 35 and s2 >= 35 and s3 >= 35 and s4 >= 35 and s5 >= 35:
     
    if avg >= 90:
        print "S Grade"
    
    elif avg >= 80:
        print "A Grade"
    
    elif avg >= 70:
        print "B Grade"
    
    
    elif avg >= 60:
        print "C Grade"
    
    elif avg >= 50:
        print "D Grade"
        
    elif avg < 50:    
        print "Dull Student :::: Pass"

elif avg :
    if (s1 < 35 or s2 < 35 or s3 < 35 or s4 < 35 or s5 < 35) and avg > 50:
        print "Dull Student :::: Fail"
    elif (s1 < 35 or s2 < 35 or s3 < 35 or s4 < 35 or s5 < 35) and avg < 50:
        print "Dull Student :::: Fail"
  
