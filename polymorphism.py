class myclass:
    def area(self,x):
        return x * x
class B(myclass):
    def __init__(self):
        super().__init__()
    
    def area(self, x,y):
        return x * y
    
obj1=myclass()
obj2=B()
result=obj1.area(4)
print(result)


