from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identity
from Resources.user import UserRegister
from Resources.stock import ListStocks, Stock
from Resources.portfolio import ListPortfolio, Portfolio

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "secret"
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity) # endpoint is /auth

api.add_resource(Stock, "/stock/<string:symbol>")
api.add_resource(ListStocks, "/stocks")
api.add_resource(UserRegister, "/register")
api.add_resource(ListPortfolio, "/portfolios")
api.add_resource(Portfolio, "/portfolio/<string:symbol>")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=8080, debug=True)