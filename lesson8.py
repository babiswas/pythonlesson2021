class B:
   def __new__(cls,*args,**kwargs):
       print("New method executed")
       return object.__new__(cls)
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
      return f"{self.a} and {self.b}"

if __name__=="__main__":
   b1=B(2,3)
   print(b1.__dict__)
   print(B.__mro__)
   print(B.mro())
   setattr(b1,'name','Bapan')
   setattr(b1,'num',12)
   print(b1.__dict__)