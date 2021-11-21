class A:
   def __init__(self):
       self.a=0
   def __iter__(self):
       return self
   def __next__(self):
       if not hasattr(self,"b"):
          self.b=5
       if self.a>self.b:
          raise StopIteration
       item=self.a
       self.a=self.a+1
       return item

if __name__=="__main__":
   a=A()
   obj=iter(a)
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   print(next(obj))
   

