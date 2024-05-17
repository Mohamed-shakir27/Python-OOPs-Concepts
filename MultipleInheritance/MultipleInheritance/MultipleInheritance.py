

class Parent1:
    def obj(self):
        fp = 10000
        print("Father property :",fp)
        self.fp = fp


class Parent2:
    def fun(self):
        mp = 10000
        self.mp = mp
        print("Mother Property :", mp)
        
class Child (Parent1,Parent2):
    def f(self):
        c = 5000
        self.obj()
        self.fun()
        
        d = c + self.fp+self.mp
        print("Child property :",d)
        
e = Child()
e.f()
        
