def decorator(func):
   print("Decorator is executing")
   def wrapper(*args,**kwargs):
       print("Wrapper function executed")
       for key in args:
           print(key)
       for key,values in kwargs.items():
          print((key,value))
       return func(*args)
   return wrapper

@decorator
def function(*args):
  print("Executing Iterator")
  for key in args:
      print(key)

if __name__=="__main__":
   print("Executing function")
   function(1,2,3,4,5,6,7)

