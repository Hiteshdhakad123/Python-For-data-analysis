#dictonary example :-
#important topic:-

# 1.access item
# 2.change item
# 3.add item /update item
# 4.remove item
# 5.copy dictonary
# 6.loop in dictonary

# access item exaple-
# x={"name":"abcd","age":10,"city":"pune"}
# print(x['name'])  
# o/p -abcd

# change item example-
# x={"name":"abcd","age":10,"city":"pune"}
# x['age']=20
# print(x)
#o/p:- change age -20

#3.add item //single element ada
# x={"name":"abcd","age":10,}
# x['city']="pune"
# print(x)

#update dictonary example: //multiple element add
# x={"name":"abcd","age":10}
# x.update({"city":"pune"})
# print(x)

#remove element example:-
# x={"name":"abcd","age":10,"city":"pune"}
# x.pop('age')
# print(x)

#delete item:-
# x={"name":"abcd","age":10,"city":"pune"}
# del x['city']
# print(x)

#clear item
# x={"name":"abcd","age":10,"city":"pune"}
# x.clear()
# print(x)

#copy dictonary example:
# x={"name":"abcd","age":10,"city":"pune"}
# y=x.copy()
# print(y)

#loop in dictonary example:-
# x={"name":"abcd","age":10,"city":"pune"}
# for i in x:
#     print(i) 
    #only key name
  
# x={"name":"abcd","age":10,"city":"pune"}
# for i in x:
#     print(x[i]) 
#only value print


# 1.items()
# 2.values()
# 3.keys()
# x={"name":"abcd","age":10,"city":"pune"}
# for i in x.items():
#  print(i)

#  x={"name":"abcd","age":10,"city":"pune"}
#  for i in x.values():
#   print(i)

#   x={"name":"abcd","age":10,"city":"pune"}
#  for i in x.keys():
#   print(i)

my_dict=['my_key']
print(my_dict)

value=my_dict=['my_key']
print(value)