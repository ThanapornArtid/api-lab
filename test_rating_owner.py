# Another user cannot read the owner's rating.
def test_other_user_cannot_read(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.get(path, headers=other_auth)
    print("read by other user:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# Another user cannot change the owner's rating.
def test_other_user_cannot_change(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 5}, headers=other_auth)
    print("change by other user:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json()["stars"] == rating["stars"]


# Another user cannot delete the owner's rating.
def test_other_user_cannot_delete(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.delete(path, headers=other_auth)
    print("delete by other user:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating