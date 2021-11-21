from multiprocessing import Process
class A:
  def __init__(self,a,b):
      print("Initiallising the parent constructor")
      self.a=a
      self.b=b

  @property
  def seta(self):
     return self.a

  @property
  def setb(self):
     return self.b

  @seta.setter
  def seta(self,a):
     self.a=a

  @setb.setter
  def setb(self,b):
     self.b=b

  def add(self):
      return self.a+self.b
  def sub(self):
      return self.a-self.b
  def mul(self):
      return self.a*self.b
  def div(self):
      return self.b/self.a
  def mod(self):
      return self.b%self.a


class B(A):
   def __init__(self,*args,**kwargs):
       print("Initiallising the child constructor")
       super().__init__(*args,**kwargs)
       print("Completed child constructor initiallisation")
   def operation1(self):
       return self.add()/self.sub()

   def operation2(self):
       return self.add()*self.sub()

   def operation3(self):
       return self.add()*self.mul()

class Task:
   def __init__(self,a,b):
       self.a=a
       self.b=b


   @property
   def seta(self):
      return self.a

   @property
   def setb(self):
      return self.b

   @seta.setter
   def seta(self,a):
      self.a=a

   @setb.setter
   def setb(self,b):
      self.b=b

   def task2(self):
       b=B(self.a,self.b)
       print(b.__dict__)
       print(b.add())
       print(b.sub())
       print(b.mul())

   def task1(self):
       a=A(self.a,self.b)
       print(a.__dict__)
       print(a.add())
       print(a.sub())
       print(a.mul())
       
if __name__=="__main__":
   task=Task(8,10)
   process1=Process(target=task.task1)
   process2=Process(target=task.task2)
   process1.start()
   process2.start()
   process1.join()
   process2.join()
   print("Process synchronization completed")
   task.task2()
   task.task1()
   task.seta=12
   task.setb=13
   process1=Process(target=task.task1)
   process2=Process(target=task.task2)
   process1.start()
   process2.start()
   process1.join()
   process2.join()