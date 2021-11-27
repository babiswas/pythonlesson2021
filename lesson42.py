from lesson40 import Example
from lesson40 import Answer
from lesson40 import db
import sys

def associate_answer_example(id):
    str1=input("Enter your answer")
    example=Example.query.filter_by(id=id).first()
    answer=Answer(answer=str1,example_answer=example)
    db.session.add(answer)
    db.session.commit()

if __name__=="__main__":
   print("Providing answers to the questions:")
   associate_answer_example(int(sys.argv[4]))
   associate_answer_example(int(sys.argv[1]))
   associate_answer_example(int(sys.argv[2]))
   associate_answer_example(int(sys.argv[3]))
   