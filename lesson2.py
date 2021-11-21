class A:
   def __init__(self,a,b):
      self.__a=a
      self.__b=b

   @property
   def setb(self):
       return self.__b

   @setb.setter
   def setb(self,b):
       self.__b=b

   @property
   def seta(self):
      return self.__a

   @seta.setter
   def seta(self,a):
     self.__a=a

   def __str__(self):
       return f"First value is {self.__a} and second value is {self.__b}"

   def __add__(self,obj):
      if isinstance(obj,A):
         return obj.seta+self.__a

   def __sub__(self,obj):
       if isinstance(obj,A):
          return obj.seta-self.__a

if __name__=="__main__":
   a=A(5,6)
   b=A(10,12)
   print(a.__dict__)
   print(a.seta)
   print(a.setb)
   print(a)
   print(b.__dict__)
   print("Performing object addition")
   print(a+b)
   print(a-b)

   