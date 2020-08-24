from db import db


class PortfolioModel(db.Model):

    __tablename__ = "portfolio"
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(80))
    
    stocks = db.relationship("StockModel", lazy="dynamic")

    def __init__(self, symbol):
        self.symbol = symbol

    def json(self):
        return {"symbol": self.symbol, "stocks": [stock.json() for stock in self.stocks.all()]}

    @classmethod
    def find_by_name(cls, symbol):
        return cls.query.filter_by(symbol=symbol).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
