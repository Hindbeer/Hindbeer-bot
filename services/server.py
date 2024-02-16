import requests
from requests import Response

from config import API_URL, ADMIN_TOKEN


def add_post(data: dict) -> Response:
    return requests.post(
        url=f"{API_URL}add/",
        json=data,
        headers={"Authorization": f"Token {ADMIN_TOKEN}"}
    )


def get_posts() -> Response:
    return requests.get(url=f"{API_URL}view/")
