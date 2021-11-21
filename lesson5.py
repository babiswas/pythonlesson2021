class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
      return f"{self.a} and {self.b}"

class C(A):
   def __init__(self,a,b,c):
       super().__init__(a,b)
       self.c=c
   def __str__(self):
      return f"{self.a} and {self.b} and {self.c}"

if __name__=="__main__":
   a=A(2,3)
   print(a.__dict__)
   print(a)
   b=C(3,4,5)
   print(b.__dict__)
   print(b)
   print(isinstance(b,A))
   print(isinstance(a,A))
   print(isinstance(b,C))
   print(isinstance(a,C))