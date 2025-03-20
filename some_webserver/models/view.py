from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ViewModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )

class FruitRequest(ViewModel):
    name: str
    color: str
    price_per_kg: int

class FruitResponse(FruitRequest):
    id: int