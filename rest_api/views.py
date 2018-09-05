from flask import Flask,jsonify,abort, make_response,request 
from models import users


app = Flask(__name__)


def get_single_user(userId):

    for user in users:
        if user["userId"] == userId:
            return user

#return questions

@app.route("/api/v1/users", methods=['GET'])
def get_all_users():
    return jsonify({"users": users})

#return particular user

@app.route('/api/v1/users/<int:userId>', methods=['GET'])
def get_user(userId):
    user = get_single_user(userId)
    if not user:
        abort(404)
    return jsonify({'user': user})

@app.route('/api/v1/users', methods=['POST'])
def add_user():
    if not request.json or 'user' not in request.json:
        abort(400)
    userId = len(users) + 1
    new_user = request.json.get('user')
    user = {"userId": userId, "userName": new_user}
    users.append(user)
    return jsonify({'user': user}), 201

@app.route('/api/v1/users/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    user = get_user(userId)
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({}), 204

if __name__ == "__main__":
    app.run(debug=True)