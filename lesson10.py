class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  @classmethod
  def get_data(cls):
     return cls.__dict__

if __name__=="__main__":
   a=A(5,6)
   print(A.get_data())