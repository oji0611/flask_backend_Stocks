from dataclasses import dataclass
from .database import db
from datetime import datetime

@dataclass
class Entry(db.Model):
    entryid: int
    entrydate: datetime
    productid: int
    quantity: int
    mov_type: str

    entryid = db.Column(db.Integer, primary_key=True)
    entrydate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    productid = db.Column(db.Integer,
                          db.ForeignKey('product.productid'),
                          nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    mov_type = db.Column(db.String(10), nullable=False)