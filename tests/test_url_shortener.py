from fastapi import status


def test_home(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.text == "welcome to URL shortener API"


def test_create_url(client):
    response = client.post(
        "/url",
        json={"target_url": "https://www.youtube.com/"})

    assert response.status_code == status.HTTP_200_OK
