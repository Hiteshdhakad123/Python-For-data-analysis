# # conditional statement example: 

# 1.postive,negetive,zero cheack given no
# n=1
# if(n>0):
#     print("it's positive")
# elif(n<0):
#     print("its negetive")
# else:
#     print("it's zero")

    
# 2.given leap year or not
# year=2020
# if(year%4==0 and year%100!=0 or year%400==0):
#     print("leap year")
# else:
#     print("not leap year")


# 3.three given no large,small,big
# a=40
# b=50
# c=60
# if(a>b and a>c):
#     print("large no")
# elif(b>a and b>c):
#     print("small no")
# else:
#     print("big no")


# 4.given char is vowel and consonent

# x=input("char =")
# v=['a', 'e', 'i', 'o', 'u']
# if x in v:
#     print("it vowel")
# else:
#     print("consonent") 


# 5.given string palidrom or not

# n1=input("char :")
# n2=n1[::-1]
# if n1==n2:
#     print("it palidrom")
# else:
#     print("not palidrom")


# 6.write program  username and password 

# password="1234"
# username="hitesh"
# if password=="1234" and username=="hitesh":
#     print("it granted")
# else:
#     print("not granted")


# 7.numerical grade (1-100) into letter grade (A,B,C,D,or F) based on condition
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
  
num_grade = int(input("enter num_grade:(1 to 100):"))
if num_grade>=90:
    letter_garde='A'
elif num_grade>=80:
    letter_garde='B'
elif num_grade>=70:
    letter_garde='C'
elif num_grade>=60:
    letter_garde='d'
else:
    letter_garde='F' 
   
    print("letter_garde",letter_garde)
      
    




