class A:
   def __init__(self,name):
       self.__name=name
   def __enter__(self):
       self.file=open(self.__name,'w')
       return self.file
   def __exit__(self,x,y,z):
       self.file.close()
       

if __name__=="__main__":
   with A("hello.txt") as obj:
      obj.write("My name is bapan")