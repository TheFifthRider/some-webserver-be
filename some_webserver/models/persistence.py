from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Fruit(Base):
    __tablename__ = "fruits"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    color = Column(String(50), nullable=False)
    price_per_kg = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Fruit(id={self.id}, name={self.name}, color={self.color}, price_per_kg={self.price_per_kg})>"
