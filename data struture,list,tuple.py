#data structure in python
#list:

# x=["apple","banana","mango"]
# print(x)

# # 2.
# x = ["apple", "banana", "cherry"]
# print(len(x))

# # 3.
# x1=["htesh","sani","mahesh"]
# x2=[10,20,30,40,50,60,70,80,90,100]
# x3=["True","False"]
# print(len(x1))
# print(x2)
# print(x3)

# # 4.A list with strings, integers and boolean values:
# # x=["hitesh",10,"true",10]
# # print(x)


# # tuple exmple:

# x=("hitesh",10,20,"mahesh")
# print(type(x))


# x=("apple","mango","banana")
# print(x)

# char=(("hitesh",10,"true",20)) #double round-brackets
# print(char)

# # set example:

# myset = {"apple", "banana", "cherry"}
# print(myset)

# #A set with strings, integers and boolean values:

# set1 = {"abc", 34, True, 40, "male"}
# print(set1)


#append and insert : last value add
# x=[10,20,30,40,50]
# x.append (60)
# print (x)

# x=[10,20,30,40,50] #index value use # mid value add
# x.insert (3,45)
# print(x)

#concatenation of list :-
x=[10,20,30]
y=[50,60,70]
z= x + y

#extend...
# x=[10,20,30,40,50]
# y=[10,20,30,40]
# x.extend(y)
# print(x)

#no of element findout:
x=[10,20,30,40,50]
print(len(x))

# how to replace: index value use 0,1,2,3...
x=[10,20,30,40]
x[0]=100
print(x)

# empty list possible : yes
x=[]
print(type(x))

#single list pssible: yes
# x=[1]
# print(x)

# remove element from list:
# x=[10,20,30,40,50]
# remove(1)
# print(x)


#pop() use last value remove :
# x=[10,20,30,40]
# x.pop(1)
# print(x)

# use claer () clear list
# x=[10,20,30,40]
# x. clear()
# print(x)

#del use:
# x=[10,20,30,40,50]
# del.x[4]
# # print(x)

# sorting in list:- ASC ORDER
# x=[40,50,10,20,30]
# x.sort()
# print(x)

# sorting in list :- DESC ORDER
# x=[10,20,30,40,50]
# x.sort(reverse=True)
# print(x)

# # list using while loop

# x=[10,20,30,40,50,60] # 5
# i=0
# while i<len(x):
#     print(x[i])
#     i=i+1

# list using even no EXAMPLE:-

# x=int(input("enter no:")) #100
# l=[]
# i=2
# while i<=x:
#     l.append(i)
#     i=i+2
#     print(l)


# list using odd no while loop: EXAMPLE

# x=int(input("enter no:")) #100
# l=[]
# i=1
# while (i<=x):
#     l.append(i)
# i=i+2
# print(l)


#list using while loop positive ans negetive number:
 
# x=[1,2,3,4,5,-1,-2,-3,-4,-5]
# pos=[]
# neg=[]
# while x>0:
#     if (x>0):
#      pos.append(x)
# else:
#      neg.append(x)
# print(pos)
# print(neg)   


# tuple example:

# x=(10,20,30,40,50,60)
#      x[0]=100
# y=list(x)
# y[0]=100
# x=tuple(y)
# print(x)

# x=(10,20,30,40,50)
#      #print(type(x))
# y=list(x)
# y[2]=500
# x=tuple(y)
# print(x)

 #set convert in list example:

x={20,30,40,50}
 #print(type(x))
y=list(x)
y[1]=100
x=set(y)
print(x)









