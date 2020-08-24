from flask_restful import Resource, reqparse
from Models.user import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="Username is mandatory."
        )
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="Password is mandatory."
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_user_by_username(data["username"]):
            return {"Message": "Username already exists."}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {"Message" : "User was succesfully created."}, 201