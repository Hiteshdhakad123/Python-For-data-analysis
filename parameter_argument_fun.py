# string formating:-

# name="rahul"
# age=12
# print(f"hello my name is {name} and my age {age}")


# # multiple parameter /argument :-

# def greet(name,age,city): #muliple parameter use
#     print(f"hello my name {name} and age is {age} i am from {city}")
# greet("rahul",12,"pune")


# # defult parameter example :

# def greekmycountry(c="india"):
#     print(f"hello i am from {c}")
# greekmycountry()
# #greekmycountry("usa")      //# name change country and defult value


# # keyword argument:  

# def students(name,age,result):
#     print(f"hello my name {name} and my age is {age} and result is {result}")
# students("rahul",12,"fail")                  #// argument means value
# #students(age=12,name="rahul",city="pune")    //key value pass 


# # orbitary argument:- (*s)

# def students(*s):
#     print(f"hello my name is {s[3]}")    # orbitary argument uses index value
# students("hitesh",23,"pune",123456789,)

# #orbitory keyword :- (**s) 

# def students(**s):
#     print(s['city'])        #// orbitory keyword uses in dictonary 
# students(name="rahul",age=12,city="pune")


# # lambdafunction:- anonymous function - function store in variable :-
# myvar= lambda a:a*2
# print(myvar(4))
  
# def specials(n):
#  return lambda a:a*n

# twice=specials(2)
# print(twice (5))

# thrise=specials(3)
# print(thrise(7))


#lambda function:
# x=lambda a:a*2
# print(x(5))

# def special(n):
#     return lambda a:a*n

# twice=special(2)
# print(twice(5))

# x=lambda a: a+10
# print(x(5))

# x=lambda a , b: a*b
# print(x(5,6))

# x=lambda a,b,c: a+b+c
# print(x(5,8,7))

def myfun(n):
    return lambda a: a*n

result=myfun(15)
print(result(5))

s=myfun(4)
print(s(7))