from flask import Flask
app=Flask(__name__)

@app.route('/user/<id>/')
def index(id):
   return f"Got id {id}"

if __name__=="__main__":
   app.run()