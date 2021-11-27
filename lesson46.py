from lesson45 import User,Channel,subs,db

def add_channel(name):
   channel=Channel(channel_name=name)
   db.session.add(channel)
   db.session.commit()

def add_user(name):
   user=User(name=name)
   db.session.add(user)
   db.session.commit()

def add_subscriber(userid,channelid):
    user=User.query.filter_by(user_id=userid).first()
    channel=Channel.query.filter_by(channel_id=channelid).first()
    channel.subscribers.append(user)
    db.session.commit()

   


if __name__=="__main__":
   add_subscriber(1,2)
   add_subscriber(2,2)
   add_subscriber(1,3)
   add_subscriber(2,3)
   
   
   