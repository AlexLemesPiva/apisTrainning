from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


allUsers = [{"Name": "Alexandre", "Surname": "Lemes", "Age": "29"}]

@app.route('/app/v1/users/<id>', methods=["GET", "POST"])

def user_action(id):
    return jsonify(allUsers[int(id)])

@app.route('/app/v1/users', methods=["POST"])

def user_action2():
    user = {"id": request.form["id"], "Name": request.form["Name"],"Surname": request.form["Surname"], "Age": request.form["Age"] }
    allUsers.append(user)
    return jsonify(user)

@app.route('/app/v1/users', methods=["GET"])

def user_action3():
    if(request.method == "GET"):
        return jsonify(allUsers)
    else:
            user = {"id": request.form["id"], "Name": request.form["Name"]}
    allUsers.append(user)
    return jsonify(user)


app.run(debug=True)  