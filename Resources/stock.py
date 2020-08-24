from flask_restful import reqparse, Resource
from flask_jwt import JWT, jwt_required
from Models.stock import StockModel

class Stock(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        "price",
        type=float,
        case_sensitive=False,
        required=True,
        help="Mandory field"
    )
    parser.add_argument(
        "portfolio_id",
        type=int,
        case_sensitive=False,
        required=True,
        help="Mandory field"
    )

    @jwt_required()
    def get(self, symbol):
        stock = StockModel.find_by_name(symbol)
        if stock:
            return stock.json()
        return {"Message": "Stock doesn't exist."}

    def post(self, symbol):
        if StockModel.find_by_name(symbol):
            return {"Message": "The {} stock already exist.".format(symbol)}, 400
        data = Stock.parser.parse_args()
        stock = StockModel(symbol, **data)
        try:
            stock.save_to_db()
        except:
            return {"Message": "An issue occured during insertion."}, 500
        return stock.json(), 201

    def delete(self, symbol):
        stock = StockModel.find_by_name(symbol)
        if stock:
            stock.delete()
        return {"Message": "Item has been deleted"}

    def put(self, symbol):
        data = Stock.parser.parse_args()
        stock = StockModel.find_by_name(symbol)
        if stock is None:
            stock = StockModel(symbol, **data)
        else:
            stock.price = data["price"]
        stock.save_to_db()
        return stock.json()


class ListStocks(Resource):
    def get(self):
        return {"Stocks": [stock.json() for stock in StockModel.query.all()]}