from lesson40 import Example
from lesson40 import db

def get_all_examples():
    data=Example.query.all()
    for ex in data:
      print(ex.example)

def get_example_id(id):
    data=Example.query.filter_by(id=id).first()
    print(data.example)

def get_example_example():
    str1=input("Enter the string:")
    data=Example.query.filter_by(example=str1).first()
    print(data.example)

def create_new_example():
    example=input("Enter your example")
    data=Example(example=example)
    db.session.add(data)
    db.session.commit()

def update_example(id):
    str1=input("Enter new value")
    example=Example.query.filter_by(id=id).first()
    example.example=str1
    db.session.commit()

def delete_example():
   str1=input("Enter the id that u want to delete")
   data=Example.query.filter_by(id=int(str1)).first()
   print(f"Deleting the example:")
   db.session.delete(data)
   db.session.commit()


if __name__=="__main__":
   print("Displaying all examples")
   print("*"*20)
   get_all_examples()
   print("*"*20)
   print("Get the examples by id")
   get_example_id(1)
   get_example_id(2)
   get_example_id(3)
   print("*"*20)
   print("Get the example by examples:")
   get_example_example()
   get_example_example()
   print("Create new examples:")
   print("*"*30)
   create_new_example()
   create_new_example()
   create_new_example()
   create_new_example()
   print("Start updating example")
   update_example(1)
   update_example(2)
   print("Updating the following example:")
   delete_example()
   delete_example()
   

   
   
   
   
