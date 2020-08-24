from db import db


class StockModel(db.Model):

    __tablename__ = "stocks"
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    portfolio_id = db.Column(db.Integer, db.ForeignKey("portfolio.id"))
    portfolio = db.relationship("PortfolioModel")

    def __init__(self, symbol, price, portfolio_id):
        self.symbol = symbol
        self.price = price
        self.portfolio_id = portfolio_id

    def json(self):
        return {"symbol": self.symbol, "price": self.price, "portfolio": self.portfolio_id}

    @classmethod
    def find_by_name(cls, symbol):
        return cls.query.filter_by(symbol=symbol).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
