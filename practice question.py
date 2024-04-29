# 1.
# num=10
# while num>0:
#     print(num)
#     num=num-1

# 2.
# num=2
# while num<20:
#     print(num)
#     num=num+2


# accept input number from user
# n = int(input("Enter any number: "))

# logic to calculate the factorial of a number

# x=int(input("enter number: "))
# fact=1
# while (x>1):
#     fact *= x
#     x-=1
#     print("factorial:",fact)


# password cheacker: correct p/w and user name use while loop-
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# while True:
#     if username == "admin" and password == "1234":
#         print("Successfully logged in")
#         break
#     else:
#         print("Incorrect username or password. Please try again.")
 
 
# fibonacci series:  0 1 1 2 3 5 8..... 
# n=int(input("enter no:")) #20
# a=0
# b=1
# print(a)
# while b < n:
#     print(b)
#     c=a+b
#     a=b
#     b=c

# Sum of Digit of given number
n = int(input('Enter Number='))
sum = 0
while n > 0 :
    r = n % 10
    sum = sum + r
    n = n // 10

print(sum)

