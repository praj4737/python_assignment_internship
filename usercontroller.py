from flask import Blueprint, jsonify, request
import pymongo

# Replace "host.docker.internal" with the actual host machine's IP address if needed
client = pymongo.MongoClient("mongodb://host.docker.internal:27017/")
database = client['user_db']
collection = database['user']

user = Blueprint("user_controller", __name__)

@user.route('/user', methods=['GET'])
def getUser():
    document = collection.find()
    users = list(document)
    return jsonify(users)

@user.route('/user/<int:id>', methods=['GET'])
def getUserById(id):
    try:
        document = collection.find_one({"_id": id})
        if document:
            return jsonify(document)
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user.route('/user', methods=['POST'])
def createUser():
    try:
        newUser = request.json
        result = collection.insert_one(newUser)
        return "User created successfully.", 201
    except Exception as e:
        return "Failed to create user.", 500

@user.route('/user/<int:id>', methods=['PUT'])
def updateUser(id):
    try:
        query = {"_id": id}
        new_values = {"$set": request.json}
        res = collection.update_one(query, new_values)

        if res.modified_count > 0:
            return jsonify({"message": "Updated successfully."}), 200
        else:
            return jsonify({"message": "Failed to update. Try again later."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user.route('/user/<int:id>', methods=['DELETE'])
def deleteUser(id):
    try:
        res = collection.delete_one({"_id": id})
        if res.deleted_count > 0:
            return jsonify({"message": "User deleted successfully."}), 200
        else:
            return jsonify({"message": "Failed to delete user."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
