from uuid import uuid4

from fastapi_sqlalchemy import db
from sqlalchemy import select, insert

from some_webserver.models.persistence import Item, CartItem, Order
from some_webserver.models.view import ShopperCheckoutRequest


def get_all_items_in_cart(cart_id: int) -> list[Item]:
    stmt = select(Item).join(CartItem).where(CartItem.cart_id == cart_id)
    items = db.session.scalars(stmt)
    return [Item.model_validate(item) for item in items]


def checkout(cart_id: int, checkout_request_body: ShopperCheckoutRequest):
    # charge credit card
    # send email receipt
    # clear cart
    magic_shopper_id = 5
    payment_token_from_provider = uuid4()

    stmt = insert(Order).values(shopper_id=magic_shopper_id, payment_token=payment_token_from_provider, name=checkout_request_body.name, address=checkout_request_body.address)
    db.session.execute(stmt)