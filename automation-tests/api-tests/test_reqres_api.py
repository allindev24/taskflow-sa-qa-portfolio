import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts_list_returns_200_and_non_empty_list(session, base_url):
    r = session.get(f"{base_url}/posts", timeout=10)
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_single_post_returns_expected_fields(session, base_url):
    r = session.get(f"{base_url}/posts/1", timeout=10)
    assert r.status_code == 200

    post = r.json()
    assert post["id"] == 1
    assert "title" in post
    assert "body" in post


def test_create_post_returns_201(session, base_url):
    payload = {"title": "taskflow", "body": "api test", "userId": 1}
    r = session.post(f"{base_url}/posts", json=payload, timeout=10)
    assert r.status_code == 201