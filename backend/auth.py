import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = {
    "admin": hash_password("admin123"),
    "nelayan": hash_password("lautkuaman")
}

def authenticate(username, password_plain):
    return users.get(username) == hash_password(password_plain)
