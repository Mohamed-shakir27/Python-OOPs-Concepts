
class Parent:   #Parent class created
    def fun(self):  #Object created
        property = 10000
        self.p = property
        print("Parent Property :",property)
        


class Child(Parent):   #Child class created
    def f(self):
        self.fun()
        c = 10000
        d = self.p+c
        print("Child Property :",d)


e = Child()
e.f()
        
        