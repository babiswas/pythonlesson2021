def decorator(**kwargs):
   print("Decorator executed")
   def wrapper(func):
      print("Wrapper executed")
      return func(**kwargs)
   return wrapper

@decorator(best1="hello",best2="bello2")
def func(**kwargs):
  for key,value in kwargs.items():
      print(key,value)




