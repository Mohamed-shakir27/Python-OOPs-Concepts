#Level by level they are inherited
#Grand Parent class and then Parent class and then child class


class GrandParent:
    def gparent(self):
        gp = 50000
        self.gp = gp
        print("Grand Parent :", gp)
        

class Parent:
    def parent(self):
        self.gparent()
        pt = 20000
        print("Parent Property :", pt)
        self.pt = pt
        a = self.gp+pt
        print("Grand Parent and Parent : ", a)
        
class Child(GrandParent,Parent):
    def c(self):
        self.parent()
        cp=5000
        self.cp = cp
        b = self.gp+self.pt+cp 
        print("Child Property : ",b)
        
d = Child()
d.c()
        
        
