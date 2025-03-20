from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ViewModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )


class FruitCreateRequest(ViewModel):
    name: str
    color: str
    price_per_kg: int


class FruitUpdateRequest(ViewModel):
    name: str | None = None
    color: str | None = None
    price_per_kg: int | None = None


class FruitResponse(FruitCreateRequest):
    id: int
