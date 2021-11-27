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
   answer=db.relationship('Answer',backref='example_answer')

class Answer(db.Model):
   __tablename__="answer"
   id=db.Column(db.Integer,primary_key=True,nullable=False,autoincrement=True)
   answer=db.Column(db.String(120),nullable=False)
   example_id=db.Column(db.Integer,db.ForeignKey('example.id'))
    

if __name__=="__main__":
   db.create_all()
   app.run(debug=True)

   