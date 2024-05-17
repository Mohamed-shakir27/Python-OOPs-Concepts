
from optparse import OptionParser


class oops:
    def __init__(self,d):
        a = 10
        b = 5
        c = a+b+d
        
        self.a=a
        self.b=b
        
        print("sum :",c)
        
    def fun(self,e):
        d = self.a-self.b+e
        
        print("Sub :",d)
s = oops(8)
s.fun(7)