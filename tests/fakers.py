from faker import Faker
from faker.providers import BaseProvider, color

from some_webserver.models.view import FruitCreateRequest


class FruitProvider(BaseProvider):
    def fruit_create_request(
        self,
        name: str | None = None,
        color: str | None = None,
        price_per_kg: str | None = None,
    ) -> FruitCreateRequest:
        return FruitCreateRequest(
            name=name or f"{_test_faker.color_name()}fruit",
            color=color or _test_faker.color_name(),
            price_per_kg=price_per_kg or _test_faker.pyint(0, 100),
        )


_test_faker = Faker()
_test_faker.add_provider(color)
_test_faker.add_provider(FruitProvider)

TestFaker = Faker | FruitProvider
