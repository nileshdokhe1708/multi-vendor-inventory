import uuid
def test_create_order_success(client):
    item_name = f"Monitor-{uuid.uuid4()}"
    item_response = client.post(
        "/items",
        json={
            "name": item_name,
            "description": "Dell Monitor",
            "stock_quantity": 50
        }
    )
    email = f"{uuid.uuid4()}@test.com"
    vendor_response = client.post(
        "/vendors",
        json={
            "name": "XYZ Supplier",
            "email":email,
            "phone": "8888888888"
        }
    )
    item_id = item_response.json()["id"]

    vendor_id = vendor_response.json()["id"]
    client.post(
        f"/item-vendor/link?item_id={item_id}&vendor_id={vendor_id}"
    )
    order_response = client.post(
        "/orders",
        json={
            "item_id": item_id,
            "vendor_id": vendor_id,
            "quantity": 5
        }
    )
    assert order_response.status_code == 200

    data = order_response.json()

    assert data["quantity"] == 5


