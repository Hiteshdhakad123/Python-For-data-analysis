try:
    result=10
except ZeroDivisionError:
    print("cannot divisible by zero")
finally:
    print("this is finally block")

# try:
#     print(5/0)
# except  NameError:
#     print("variable is not defined")

# except ZeroDivisionError:
#     print("you can not divide  no with zero")
# except:
#     print("something went worng")
# else:
#     print("sucess")
# finally:
#     print("always excute")

