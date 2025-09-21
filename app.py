
from flask import Flask
from flask import session       
from models import db, User, init_db
from flask import request, jsonify

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

init_db(app)

 

app.secret_key = "12345678"
      
@app.route('/login', methods=['POST'])
def login():    
    data=request.get_json()
    username=data.get("username")

    if username is None:
        return "Username is required", 400
    
    user = User.query.filter_by(username=username).first()
    if user :
        session["user_id"] = user.id
        return jsonify({"message": "Login successful", "user": username})
    else:
        return "Error: User not found", 404


    
@app.route('/logout', methods=['DELETE'])
def logout():
    session.clear()
    return jsonify ({'message': "Logged out successfully"}), 200

@app.route('/create-test-user')
def test_user():
    """Route to insert some test users into the database."""
    # Check if users already exist to avoid duplicates
    if not User.query.first():
       users = [
            User(username="alice"),
            User(username="bob")
       ]
       db.session.add_all(users)
       db.session.commit()
       return "Created users: alice and bob"  
    else:
        return "user already exists"                                                                                         
   


@app.route('/check-session', methods=['GET'])
def check_session():
    if "user_id"  in session:
        user = User.query.filter_by(id=session['user_id']).first()
        return jsonify({"user": user.username, "message": "Logged in",})
    else:
        return jsonify({
            'message':  "Not logged in"
        }), 401
        

if __name__  == '__main__':
  app.run(debug=True)