import uuid

def test_create_item(client):
    item_name = f"Laptop-{uuid.uuid4()}"
    response = client.post(
        "/items",
        json={
            "name": item_name,
            "description": "Dell Laptop",
            "stock_quantity": 100
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == item_name