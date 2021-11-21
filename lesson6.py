from contextlib import contextmanager

@contextmanager
def myfile(filename):
    try:
      file=open(filename,'w')
      yield(file)
    finally:
      file.close()

if __name__=="__main__":
   with myfile("file1.txt") as file:
       file.write("hello world")
       file.write("hello miss")
      