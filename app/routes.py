from werkzeug.datastructures import _omd_bucket
from app.database import user
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def version():
    out = {
        "ok": True,
        "message": "Success",
        "Server_time": datetime.now().strftime("%F %H:%M:%S"),
        "version": "1.0.0"
    }
    return out


@app.route("/users", methods=["POST"])
def create_user():
    user_data = request.json
    out = {
        "ok": True,
        "message": "Success",
        "new_id": user.insert(
            user_data.get("first_name"),
            user_data.get("last_name"),
            user_data.get("hobbies")
        )
    }
    return out, 201


@app.route("/users", methods=["GET"])
def get_all_users():
    out = {
        "ok": True,
        "message": "Success",
        "users": user.scan()
    }
    return out


@app.route("/users/<int:pk>", methods=["GET"])
def get_single_user(pk):
    out = {
        "ok": True,
        "message": "Success",
        "user": user.read(pk)
    }
    return out


@app.route("/users/<int:pk>", methods=["PUT"])
def update_user(pk):
    user_data = request.json
    out = {
        "ok": True,
        "message": "Success",
    }
    user.update(pk,
                user_data.get("first_name"),
                user_data.get("last_name"),
                user_data.get("hobbies"))
    return out


@app.route("/users/<int:pk>", methods=["DELETE"])
def deactivate_user(pk):
    user.deactivate_user(pk)
    out = {
        "ok": True,
        "message": "Success"
    }
    return out

# vehicle


@app.route("/users/int:pk>/vehciles", method=["POST"])
def create_vehicles():
    user_data = request.json
    out = {
        "ok": True,
        "message": "Success",
        "new_id": vehicles.insert(
            user_data.get("license_place"),
            user_data.get("v_typ"),
            user_data.get("color")
        )
    }
    return out, 201


@app.route("/users/<int:pk>/vehicles", method=["GET"])
def get_vehicle_by_user_id(pk):
    vehicle = vehicles.scan(pk)
