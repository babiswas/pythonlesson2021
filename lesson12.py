class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def add_attributes(self,**kwargs):
      for key,value in kwargs.items():
          self.__dict__[key]=value

  def display_attributes(self,*args):
     for key in args:
        print(self.__dict__.get(key,''))

  def remove_attributes(self,*args):
      for key in args:
         del self.__dict__[key]

  def __str__(self):
     return f"{self.a} and {self.b}"

if __name__=="__main__":
   obj=A(3,4)
   print(obj.__dict__)
   obj.add_attributes(hello=2,bello=3)
   print(obj.__dict__)
   obj.display_attributes("hello","a")
   print(obj.__dict__)
   obj.remove_attributes("hello","a")
   print(obj.__dict__)
   