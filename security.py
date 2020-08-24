from Models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_user_by_username(username)
    if user and password == user.password:
        return user

def identity(payload):
    user_id = payload["identity"]
    return UserModel.find_user_by_id(user_id)
