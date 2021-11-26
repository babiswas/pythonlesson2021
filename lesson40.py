from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:36network@localhost/bello'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


class Example(db.Model):
   __tablename__="example"
   id=db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
   example=db.Column(db.String(100),nullable=False)

def get_all_examples():
    examples=Example.query.all()
    for ex in examples:
       print(ex.example)

def get_example_id(id):
    example=Example.query.filter_by(id=id)
    print(example.example)
    

if __name__=="__main__":
   db.create_all()
   app.run(debug=True)

   