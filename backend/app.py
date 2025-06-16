from flask import Flask, request, jsonify, session
from flask_cors import CORS
from auth import authenticate
from dummy_data import get_dummy_fish_locations

app = Flask(__name__)
app.secret_key = "rahasia-ikan"
CORS(app, supports_credentials=True)

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if authenticate(username, password):
        session["user"] = username
        return jsonify({"message": "Login berhasil", "user": username})
    return jsonify({"message": "Username atau password salah"}), 401

@app.route("/api/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return jsonify({"message": "Logout berhasil"})

@app.route("/api/fish-locations", methods=["GET"])
def fish_locations():
    if "user" not in session:
        return jsonify({"message": "Unauthorized"}), 401
    return jsonify(get_dummy_fish_locations())

if __name__ == "__main__":
    app.run(debug=True)
