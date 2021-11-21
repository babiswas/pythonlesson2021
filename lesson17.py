class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __call__(self,func):
     print("call function executed")
     def wrapper(*args):
        print("Wrapper function executed")
        for i in args:
          print(i)
        print("The sum of the numbers is:")
        return func(*args)
     return wrapper


@A(1,2)
def func(*args):
   sum=0
   for i in args:
      sum=sum+i
   return sum

if __name__=="__main__":
   print(func(1,2,3,4))