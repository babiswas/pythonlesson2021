from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:36network@localhost/bello'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

subs=db.Table('subs',db.Column('user_id',db.Integer,db.ForeignKey('channeluser.user_id')),db.Column('channel_id',db.Integer,db.ForeignKey('channel.channel_id')))


class User(db.Model):
   __tablename__="channeluser"
   user_id=db.Column(db.Integer,primary_key=True)
   name=db.Column(db.String(20))
   subscriptions=db.relationship('Channel',secondary='subs',backref=db.backref('subscribers',lazy='dynamic'))
   

class Channel(db.Model):
   __tablename__="channel"
   channel_id=db.Column(db.Integer,primary_key=True)
   channel_name=db.Column(db.String(20))


if __name__=="__main__":
   db.create_all()
   app.run(debug=True)
   