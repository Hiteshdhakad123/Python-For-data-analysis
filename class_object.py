#example class and object:
# class Person():
# #how to initialize attribute
# #init method
#     def __init__(self,person_name,person_age,person_height):
#        # print("init method")  //constructer
#         self.name=person_name
#         self.age=person_age
#         self.height=person_height

# Person1 = Person("hitesh",23,"175 cm")
# print(Person1.name)
# #print(f"name:{Person1.name}, age:{Person1.age}, height:{Person1.height}")
# Person2=Person("mahesh",25,180)
# print(Person2.name,Person1.age)


# class Myclass:
#  X=10

# Myclass1 = Myclass()
# print(Myclass1.X)

# class Abc:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
#         my=Abc(12,4)
#         print(a.x)
#         print(a.y)

# class Abc:
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b
        
# my = Abc(12,4)
# print(my.x)
# print(my.y)


# class Abc:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
# my=Abc(12,15)
# print(my.x)
# print(my.y)


#return value pass in 
# class Abc:
#     x=10
#     def myfun(self,a,b):
#         return self.x+a+b
# my=Abc()
# result=my.myfun(10,20)
# print(result)

class Abc:
    def __init__(self,a,b):
        self.x=a
        self.y=b
p1=Abc(10,20)
print(p1.x)
print(p1.y)




#inheritance example:
class student:
    def __init__(self,n,r,a):
        self.name=n
        self.roll=r
        self.address=a
class marks:
    m=45
class result(student,marks):
    def result(self):
        if self.m>45:
            print(f"{self.name} is pass")
        else:
            print(f"{self.name} is fail")
re=result("abc",101,"pune")
re.result()


class A:
    a=10
class B:
    b=20
class c(A,B):
    c=12
    def SU(self):
        return self.c + self.a + self.b
myobj=c()
print(myobj.SU())


#create class having function for finding largest value from list :

class Abc:
    def __init__(self,number):
        self.number=number
    def largest(self):
        return max(self.number,default=None)
number=[10,4,67,34,89,2] 
processor=Abc(number) 
print("the largest value in the list ",processor.largest()) 

# create class having two function to print all and even from the given list 

class person:
    def __init__(self,number):
        self.number=number

    def odd(self):
        odd=[num for num in self.number if num % 2!=0]
        print("odd number:",odd)
    
    def even(self):
        even=[num for num in self.number if num %2==0]
        print("even number",even)

number=[10,4,67,34,89,2]
processor=person(number)
processor.odd()
processor.even()

    