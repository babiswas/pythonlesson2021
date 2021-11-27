from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:36network@localhost/bello"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)




class User(db.Model):
    __tablename__='myuser'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(30),nullable=False)

    def __init__(self,name,email):
        self.name=name
        self.email=email

    def __str__(self):
        return f"{self.name} and {self.email}"
    

@app.route('/user',methods=['GET'])
def get_all_user():
    user_list=list()
    users=User.query.all()
    print(users)
    for u in users:
       myuser=dict()
       myuser.update(id=u.id)
       myuser.update(name=u.name)
       myuser.update(email=u.email)
       user_list.append(myuser)
    return jsonify(user_list)


if __name__=="__main__":
   db.create_all()
   app.run(debug=True)
   
