from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy import select, insert, delete, update

from some_webserver.models.persistence import Fruit
from some_webserver.models.view import FruitResponse, FruitRequest

router = APIRouter(prefix="/fruits")


@router.get("/", tags=["fruits"])
async def read_all_fruits() -> list[FruitResponse]:
    stmt = select(Fruit)
    fruits = db.session.scalars(stmt)
    return [FruitResponse.model_validate(fruit) for fruit in fruits]


@router.get("/{fruit_id}", tags=["fruits"])
async def read_fruit_by_id(fruit_id: int) -> FruitResponse:
    stmt = select(Fruit).where(Fruit.id == fruit_id)
    fruit = db.session.execute(stmt).scalar_one_or_none()

    if fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")

    return FruitResponse.model_validate(fruit)


@router.post("/", tags=["fruits"])
async def create_fruit(fruit: FruitRequest) -> FruitResponse | None:
    stmt = insert(Fruit).values(fruit.model_dump()).returning(Fruit)
    orm_stmt = select(Fruit).from_statement(stmt).execution_options(populate_existing=True)
    fruit = db.session.execute(orm_stmt).scalar()
    return FruitResponse.model_validate(fruit)


@router.patch("/{fruit_id}", tags=["fruits"])
async def update_fruit(fruit_id: int, fruit_update: FruitRequest) -> FruitResponse | None:
    stmt = update(Fruit).values(fruit_update.model_dump(exclude_unset=True)).where(Fruit.id == fruit_id).returning(Fruit)
    orm_stmt = select(Fruit).from_statement(stmt).execution_options(populate_existing=True)
    fruit = db.session.execute(orm_stmt).scalar_one_or_none()

    if fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")

    return FruitResponse.model_validate(fruit)


@router.delete("/{fruit_id}", tags=["fruits"])
async def delete_fruit(fruit_id: int) -> FruitResponse | None:
    stmt = delete(Fruit).where(Fruit.id == fruit_id).returning(Fruit)
    orm_stmt = select(Fruit).from_statement(stmt).execution_options(populate_existing=True)
    fruit = db.session.execute(orm_stmt).scalar_one_or_none()

    if fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")

    return FruitResponse.model_validate(fruit)