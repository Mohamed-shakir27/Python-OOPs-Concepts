
class oops:  #class is created
    def fun(self): #object 1 is created
        a = 10
        b = 5
        c = a+b
        print("sum :",c)
        
        self.a = a
        self.b = b
        
    def f(self):  #object 2 is created
        d = self.a-self.b
        print("Sub:",d)
        
s = oops()  #class called

s.fun()  #object1 called
s.f()   #object2 called