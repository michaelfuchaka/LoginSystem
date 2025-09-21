
from flask import Flask
from flask import session       
from models import db, User, init_db

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

init_db(app)

 

app.secret_key = "12345678"
      
@app.route('/')
def greeting():    
    return "Hello, World!"


@app.route('/test-session')
def test_session():
    if "user_id" not in session:
        session["user_id"] = 42
        return "Session set!"
    else:
        session.pop("user_id", None)
        return  "Session cleared!"

                                                                                                                                        


if __name__  == '__main__':
  app.run(debug=True)