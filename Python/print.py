# kar = ["a",'b','c']
# 
# print kar[2]
# 
# print kar
# 
# kar[2] = "hai"
# 
# 
# print kar[2]
# 
# kar.append("how are you")
# 
# print kar
# 
# print len(kar)
# 
# print kar.index("hai")
# 
# kar.remove("a")
# 
# print kar
# 
# kar = kar * 3
# 
# print kar
# 
# 
# 
# for ab in kar:
#     print ab,


# t=(1,2,3)
# t1=(4,5,6)
# 
# print t+t1



# List Examples


# a = [1,2,3,4,5,6,7,8,9,10]
# 
# # a.extend(5)
# a.insert(0,15)
# 
# a.pop(1)
# 
# a.remove(5)
# 
# print a.index(10)
# print a.count(8)
# print a
# 
# print sorted(a)



# List for example
# c=[]
# g=int(input("Enter the range:"))
# for d in range(0,g):
#     a = int(input("Enter the iteration value:"))
#     c.append(a)
# f=0
# for e in c:
#     f=f+e
#     
# print f


# for c in range(0,a):
#     d=int(input("Enter:"))
#     b.append(d)
#     
# f=0    
# for e in b:
#     f = f + e
#     
# print f
#     

# EXCEPTION HANDLING

# SYNTAX ERROR

# while True: print "Hello World"

# EXCEPTIONS
# 
# a = 10 * (1/0)
# 
# print a

# while True:
#     try:
#         x = int(raw_input("Please enter a number:"))
#         break
#     except ValueError:
#         print "Haa wrong input Try again"


# from datetime import date
# 
# def calculate_age(born):
#     today = date.today()
#     try: 
#         birthday = born.replace(year=today.year)
#     except ValueError: # raised when birth date is February 29 and the current year is not a leap year
#         birthday = born.replace(year=today.year, month=born.month+1, day=1)
#     if birthday > today:
#         return today.year - born.year - 1
#     else:
#         return today.year - born.year
#     
# 
#     print today


# from datetime import date
# 
# # a = date.today()
# b = 1992
# a= date.today().year
# 
# age = a-b
# print age


# class sam:
#     "This is my first class"
#     a=140
#     def funt(self):
#         print("Hello Sam")
#         
# print sam.a
# 
# print sam.funt(self)
# 
# print sam.__doc__
#         


# class Polygon(object):
#     def __init__(self,no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#          
#     def inputSides(self):
#         self.sides = [float(input("Enter side"+str(i+1)+":" )) for i in range(self.n)]
#          
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])
#     def findArea(self):
#         print 'hello'
#         
#         return True         
#              
#              
# class Triangle(Polygon):
#     def __init__(self, no_of_sides):
#         Polygon.__init__(self,3)
#  
#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)   
#          
# class Square(Polygon):
#     def __init__(self, no_of_sides):
#         Polygon.__init__(self,no_of_sides)
#          
#          
#     def findArea(self):
#         super(Square, self).findArea()
#         a = self.sides[1]
#      
#          
#         b = a**2
# #         
#         print("The are of the square is %0.2f" %b)
#          
# t = Square(4)
#  
# t.inputSides()
#          
# t.dispSides()
#  
# t.findArea()
# a=[1,1,2,2,3,4,5,6]
# for b in a:
#     print (b, end=" "),
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'



    

