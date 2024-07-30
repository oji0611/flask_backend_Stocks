from dataclasses import dataclass
from .database import db

@dataclass
class Product(db.Model):
    productid: int
    category: str
    unit: str
    libele: str

    productid = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    libele = db.Column(db.String(50), nullable=False)