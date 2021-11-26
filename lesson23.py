from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:36network@localhost/bello"
db=SQLAlchemy(app)

class User(db.Model):
   __tablename__='myuser'
   id=db.Column(db.Integer,primary_key=True,autoincrement=True)
   name=db.Column(db.String(80),nullable=False)
   email=db.Column(db.String(100),nullable=False)

   def __repr__(self):
       return f"{self.name} is username"

   def __init__(self,name,email):
       self.name=name
       self.email=email

@app.route('/users',methods=['POST'])
def create_users():
   payload=request.get_json()
   new_user=User(name=payload.get("name"),email=payload.get("email"))
   db.session.add(new_user)
   db.session.commit()
   db.session.refresh(new_user)
   payload.update(id=new_user.id)
   return jsonify(payload)

@app.route('/myusers',methods=['GET'])
def get_all_user():
   all_user=list()
   users=User.query.all()
   for u in users:
      myuser=dict()
      myuser.update(name=u.name)
      myuser.update(email=u.email)
      myuser.update(id=u.id)
      all_user.append(myuser)
   return jsonify(all_user)

@app.route('/myuser/<email>',methods=['GET'])
def get_user_id(email):
    user=User.query.filter_by(email=email).first()
    myuser=dict()
    myuser.update(id=user.id)
    myuser.update(name=user.name)
    myuser.update(email=user.email)
    return jsonify(myuser)
    

if __name__=="__main__":
   db.create_all()
   app.run(debug=True)
