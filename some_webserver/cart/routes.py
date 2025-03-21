from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy import select, insert, update, delete

from some_webserver.cart.cart_service import get_all_items_in_cart, checkout
from some_webserver.models.persistence import Item, CartItem
from some_webserver.models.view import AddOrRemoveFromCartRequest, ShopperCheckoutRequest

router = APIRouter(prefix="/cart")


@router.get("/{cart_id}", tags=["cart"])
async def read_all_items_in_cart(cart_id: int) -> list[Item]:
    return get_all_items_in_cart(cart_id)


@router.post("/{cart_id}", tags=["cart"])
async def add_item_to_cart(cart_id: int, request_body: AddOrRemoveFromCartRequest) -> list[Item]:
    insert_statement = insert(CartItem).values(cart_id=cart_id, item_id=request_body.item_id)
    db.session.execute(insert_statement)

    return get_all_items_in_cart(cart_id)


@router.delete("/{cart_id}", tags=["cart"])
async def remove_item_from_cart(cart_id: int, request_body: AddOrRemoveFromCartRequest) -> list[Item]:
    delete_statement = delete(CartItem).where(CartItem.cart_id == cart_id and CartItem.item_id == request_body.item_id)
    db.session.execute(delete_statement)

    return get_all_items_in_cart(cart_id)


@router.post("/{cart_id}/checkout", tags=["cart"])
async def checkout_cart(cart_id: int, request_body: ShopperCheckoutRequest) -> list[Item]:
    checkout(request_body)
    return get_all_items_in_cart(cart_id)
