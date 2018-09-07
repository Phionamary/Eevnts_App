from module import Person, Users, User
from flask import Flask,request, json, jsonify, make_response



app = Flask(__name__)

users = Users()

@app.route("/api/v1/users", methods = ["POST"])
def add_user():
    user = {
        "username": request.json["name"],
        "email": request.json["email_address"]
    }

    if user["username"] == "":
        return make_response(jsonify({"Error": "Username cannot be empty!"}), 400)
        
    if user["email"] == "":
        return make_response(jsonify({"Error": "Email cannot be empty"}), 400)

    else:
        users.add_user(user)
        return make_response(jsonify({"User": user}), 201)
       

@app.route("/api/v1/user", methods = ["GET"])
def get_users():
    all_users = users.get_all_users()
    return make_response(jsonify({"Users info": all_users}), 200)


@app.route("/api//v1/users", methods = ["DELETE"])
def delete_users():
    deleted_user = users.delete_user()
    return make_response(jsonify({"Deleted user": deleted_user}), 200)


if __name__=='__main__':
    app.run(debug=True)