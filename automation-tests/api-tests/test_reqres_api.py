import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts_list_returns_200_and_non_empty_list():
    r = requests.get(f"{BASE_URL}/posts", timeout=10)
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert {"userId", "id", "title", "body"}.issubset(data[0].keys())


def test_get_single_post_returns_expected_fields():
    r = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert r.status_code == 200

    post = r.json()
    assert post["id"] == 1
    assert "title" in post
    assert "body" in post
    assert "userId" in post


def test_get_comments_for_post_returns_200_and_list():
    r = requests.get(f"{BASE_URL}/posts/1/comments", timeout=10)
    assert r.status_code == 200

    comments = r.json()
    assert isinstance(comments, list)
    assert len(comments) > 0
    assert {"postId", "id", "name", "email", "body"}.issubset(comments[0].keys())


def test_create_post_returns_201_and_returns_payload():
    payload = {"title": "taskflow", "body": "api test", "userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
    assert r.status_code == 201

    body = r.json()
    # JSONPlaceholder "fakes" creation, but still returns the created object + id
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body


def test_update_post_returns_200():
    payload = {"id": 1, "title": "updated", "body": "updated body", "userId": 1}
    r = requests.put(f"{BASE_URL}/posts/1", json=payload, timeout=10)
    assert r.status_code == 200

    body = r.json()
    assert body["title"] == "updated"


def test_delete_post_returns_200():
    r = requests.delete(f"{BASE_URL}/posts/1", timeout=10)
    assert r.status_code == 200