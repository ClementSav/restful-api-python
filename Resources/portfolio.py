from flask_restful import Resource
from Models.portfolio import PortfolioModel


class Portfolio(Resource):

    def get(self, symbol):
        portfolio = PortfolioModel.find_by_name(symbol)
        if portfolio:
            return portfolio.json()
        return {"Message": "Portfolio doesn't exist."}, 404

    def post(self, symbol):
        portfolio = PortfolioModel.find_by_name(symbol)
        if portfolio:
            return {"Message": "This portfolio already exist."}
        portfolio = PortfolioModel(symbol)
        try:
            portfolio.save_to_db()
        except:
            return {"Message": "An error occured during insertion."}, 500
        return portfolio.json(), 201

    def delete(self, symbol):
        portfolio = PortfolioModel.find_by_name(symbol)
        if portfolio:
            portfolio.delete()
            return {"Message": "The porfolio has been deleted"}
        return {"Message": "The porfolio doesn't not exist."}


class ListPortfolio(Resource):
    def get(self):
        return {"Portfolio": [portfolio.json() for portfolio in PortfolioModel.query.all()]}