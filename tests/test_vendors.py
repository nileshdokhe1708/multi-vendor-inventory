import uuid
def test_create_vendor(client):
    email = f"{uuid.uuid4()}@test.com"
    response = client.post(
        "/vendors",
        json={
            "name": "ABC Supplier",
            "email": email,
            "phone": "9999999999"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == email