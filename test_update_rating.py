import pytest


# Boundary values for PUT: 1 and 5 are saved, 0 and 6 are refused,
# and a refused update leaves the rating as it was (3 stars).
@pytest.mark.parametrize("stars, expected_status", [
    (0, 400),  # just below the lower edge
    (1, 200),  # lower edge
    (5, 200),  # upper edge
    (6, 400),  # just above the upper edge
])
def test_update_stars_boundaries(api, auth, rating, stars, expected_status):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected_status

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    if expected_status == 200:
        assert res.json()["stars"] == stars
    else:
        assert res.json()["stars"] == rating["stars"]