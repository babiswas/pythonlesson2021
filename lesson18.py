def decorator(cls):
    print("Decorator executed")
    def wrapper(*args,**kwargs):
        print("Wrapper function executed")
        for i in args:
          print(i)
        for key,value in kwargs.items():
          print(key,value)
        return cls(*args)
    return wrapper

@decorator
class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
      return f"{self.a} and {self.b}"

if __name__=="__main__":
   a=A(3,4)
   print(a.__dict__)
   