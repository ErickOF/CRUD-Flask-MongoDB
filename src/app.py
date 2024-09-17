import flask
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS


app = Flask(__name__)
app.config['MONGO_URI'] = '<mongo-url>'

mongo = PyMongo(app)
CORS(app)


@app.route('/users/create', methods=['POST'])
def createUser():
    _id = mongo.db.users.insert({
        'idCard': request.json['idCard'],
        'email': request.json['email'],
        'lastname': request.json['lastname'],
        'name': request.json['name'],
        'phoneNumber': request.json['phoneNumber']
    })

    return jsonify({
        'message': 'User was created.',
        'status': 400,
        'data': _id
    })

@app.route('/users', methods=['GET'])
def getUsers():
    users = [
        {
            '_id': str(ObjectId(doc['_id'])),
            'idCard': doc['idCard'],
            'email': doc['email'],
            'lastname': doc['lastname'],
            'name': doc['name'],
            'phoneNumber': doc['phoneNumber']
        } for doc in mongo.db.users.find()]

    return jsonify({
        'message': 'Returning all users.',
        'status': 400,
        'data': users
    })

@app.route('/users/<_id>', methods=['GET'])
def getUser(_id):
    user = mongo.db.users.find_one({ '_id': ObjectId(_id) })

    foundUser = {
        '_id': str(ObjectId(user['_id'])),
        'idCard': user['idCard'],
        'email': user['email'],
        'lastname': user['lastname'],
        'name': user['name'],
        'phoneNumber': user['phoneNumber']
    }

    return jsonify({
        'message': 'Returning found user.',
        'status': 400,
        'data': foundUser
    })

@app.route('/users/<_id>', methods=['DELETE'])
def deleteUser(_id):
    mongo.db.users.delete_one({ '_id': ObjectId(_id) })

    return jsonify({
        'message': 'User was deleted.',
        'status': 400,
        'data': None
    })

@app.route('/users/<_id>', methods=['PUT'])
def updateUser(_id):
    mongo.db.users.update_one({ '_id': ObjectId(_id) }, { '$set': {
        'idCard': request.json['idCard'],
        'email': request.json['email'],
        'lastname': request.json['lastname'],
        'name': request.json['name'],
        'phoneNumber': request.json['phoneNumber']
    }})

    return jsonify({
        'message': 'User was updated.',
        'status': 400,
        'data': None
    })

@app.route('/')
def index():
    return '<h1>Hello from Flask</h1>'


if __name__ == '__main__':
    app.run(debug=True)
