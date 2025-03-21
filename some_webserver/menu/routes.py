from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy import select

from some_webserver.models.persistence import Item

router = APIRouter(prefix="/menu")


@router.get("/", tags=["menu"])
async def read_all_items() -> list[Item]:
    stmt = select(Item)
    items = db.session.scalars(stmt)
    return [Item.model_validate(item) for item in items]

