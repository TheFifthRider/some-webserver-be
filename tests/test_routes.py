from some_webserver.models.view import FruitResponse


def test_create_fruit(test_client, test_faker):
    fruit = test_faker.fruit_create_request()
    response = test_client.post("/fruits/", json=fruit.model_dump(by_alias=True))
    assert response.status_code == 200


def test_create_invalid_fruit(test_client, test_faker):
    response = test_client.post("/fruits/", json={})
    assert response.status_code == 422


def test_get_fruit(test_client, test_faker):
    fruit = test_faker.fruit_create_request()
    post_response = test_client.post("/fruits/", json=fruit.model_dump(by_alias=True))
    assert post_response.status_code == 200
    fruit_post_response = FruitResponse.model_validate(post_response.json())

    get_response = test_client.get(f"/fruits/{fruit_post_response.id}")
    assert get_response.status_code == 200
    fruit_get_response = FruitResponse.model_validate(get_response.json())
    assert fruit_get_response.name == fruit.name
    assert fruit_get_response.price_per_kg == fruit.price_per_kg
    assert fruit_get_response.color == fruit.color


def test_delete_fruit(test_client, test_faker):
    fruit = test_faker.fruit_create_request()
    post_response = test_client.post("/fruits/", json=fruit.model_dump(by_alias=True))
    assert post_response.status_code == 200
    fruit_post_response = FruitResponse.model_validate(post_response.json())

    delete_response = test_client.delete(f"/fruits/{fruit_post_response.id}")
    assert delete_response.status_code == 200
    fruit_delete_response = FruitResponse.model_validate(delete_response.json())
    assert fruit_delete_response.name == fruit.name
    assert fruit_delete_response.price_per_kg == fruit.price_per_kg
    assert fruit_delete_response.color == fruit.color

    get_response = test_client.get(f"/fruits/{fruit_post_response.id}")
    assert get_response.status_code == 404


def test_delete_nonexistent_fruit(test_client, test_faker):
    delete_response = test_client.delete("/fruits/-1")
    assert delete_response.status_code == 404


def test_update_nonexistent_fruit(test_client, test_faker):
    expected_color = test_faker.color_name()
    patch_response = test_client.patch("/fruits/-1", json={"color": expected_color})
    assert patch_response.status_code == 404


def test_update_fruit(test_client, test_faker):
    fruit = test_faker.fruit_create_request()
    post_response = test_client.post("/fruits/", json=fruit.model_dump(by_alias=True))
    assert post_response.status_code == 200
    fruit_post_response = FruitResponse.model_validate(post_response.json())

    expected_color = test_faker.color_name()
    patch_response = test_client.patch(f"/fruits/{fruit_post_response.id}", json={"color": expected_color})
    assert patch_response.status_code == 200
    fruit_patch_response = FruitResponse.model_validate(patch_response.json())

    assert fruit_patch_response.name == fruit.name
    assert fruit_patch_response.price_per_kg == fruit.price_per_kg
    assert fruit_patch_response.color == expected_color
