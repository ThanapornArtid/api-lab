import pytest


# The pizza never needs a tool that the customer excluded.
@pytest.mark.parametrize("excluded", [
    [],                                    # block: 0 tools excluded
    ["Knife"],                             # block: 1 tool excluded
    ["Scissors"],                          # block: 1 tool excluded
    ["Knife", "Scissors"],                 # block: 2 tools excluded
    ["Knife", "Pizza cutter", "Scissors"], # block: 3 tools excluded
])
def test_excluded_tool_is_not_used(api, auth, excluded):
    body = {"excludedTools": excluded}
    res = api.post("/api/pizza", json=body, headers=auth)
    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded