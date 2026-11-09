# api-lab

API tests for QuickPizza with pytest and requests (ITCS386).

## How to run

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    pytest -v

## Input domain model for POST /api/ratings

| Characteristic | Block | Value in the test | Test that covers it |
| -------------- | ----- | ----------------- | ------------------- |
| C1 Value of stars | below 1 | 0 | test_stars_out_of_range[0] |
| | 1 to 5 (base) | 3 | test_base_choice_is_saved |
| | above 5 | 6 | test_stars_out_of_range[6] |
| C2 Type of stars | whole number (base) | 3 | test_base_choice_is_saved |
| | decimal | 3.5 | test_stars_as_decimal |
| | text | "3" | test_stars_as_text |
| | missing | no field | test_stars_missing |
| C3 Pizza | exists (base) | a new pizza | test_base_choice_is_saved |
| | does not exist | 999999999 | test_pizza_does_not_exist |
| C4 Token | the user's own (base) | from auth | test_base_choice_is_saved |
| | none | no header | test_no_token |
| | wrong length | token short | test_token_wrong_length |

Base choice coverage: 1 base test + (3-1) + (4-1) + (2-1) + (3-1) = 9 tests.