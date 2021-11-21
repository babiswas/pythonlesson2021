class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  @property
  def seta(self):
     return self.a

  @seta.setter
  def seta(self,a):
      self.a=a

  @property
  def setb(self):
      return self.b

  @setb.setter
  def setb(self,b):
      self.b=b

  def __str__(self):
     return f"{self.a} and {self.b}"

class B:
  def __init__(self,c,d):
      self.c=c
      self.d=d
  def __str__(self):
      return f"{self.c} and {self.d}"

class D(A,B):
   def __init__(self,a,b,c,d):
      A.__init__(self,a,b)
      B.__init__(self,c,d)
   def __str__(self):
      return f"{self.a} and {self.b} and {self.c} and {self.d}"

if __name__=="__main__":
   d=D(1,2,3,4)
   print(d.__dict__)
   print(d)
   a=A(14,15)
   print(a.__dict__)
   print(a)