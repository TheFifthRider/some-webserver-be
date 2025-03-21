from sqlalchemy import Column, Integer, String, ForeignKey
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

class Order(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    shopper_id = Column(Integer, ForeignKey("shopper.id"), nullable=False)
    payment_token = Column(String)
    name = Column(String)
    address = Column(String)

class OrderItem(Base):
    __tablename__ = "orderitems"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    image_s3_url = Column(String(100), nullable=False)


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    shopper_id = Column(Integer, ForeignKey("shopper.id"), nullable=False)


class CartItem(Base):
    __tablename__ = "cartitems"

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey("item.id"), nullable=False)
    cart_id = Column(Integer, ForeignKey("cart.id"), nullable=False)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    image_s3_url = Column(String(100), nullable=False)


class Shopper(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
