import pytest
import requests
from pytest_bdd import scenarios, when, then

# public api to get random single or two-part jokes of a given category
JOKES_API = "https://v2.jokeapi.dev/joke"

# path to feature file
scenarios("../features/single_part_jokes.feature",
          example_converters=dict(category=str, joke_type=str, response_category=str,
                                  response_joke_type=str))


# 'when' behavior test
# calls jokes api with category and joke type query
@pytest.fixture
@when('the Jokes API is queried with "<category>" and "<joke_type>"')
def joke_response(category, joke_type):
    params = {'format': 'json', 'type': joke_type}
    url_ext = "/" + category
    response = requests.get(JOKES_API + url_ext, params=params)
    return response


# 'then' behavior test
# tests the data responded from the jokes api call with the category and joke type query
@pytest.fixture
@then('the response contains a category of "<response_category>", a joke type of "<response_joke_type>", and the joke '
      'itself')
def test_joke_response_data(joke_response, response_category, response_joke_type):
    # actual
    json_response = joke_response.json()
    # check actual vs expected for category
    is_correct_response_category = response_category == json_response["category"]
    # check actual vs expected for joke type
    is_correct_joke_type = response_joke_type == json_response["type"]
    # check actual vs expected for the joke in the response
    contains_joke = "joke" in json_response
    # assert all actual vs expected comparisons
    assert is_correct_response_category and is_correct_joke_type and contains_joke


# 'then' behavior test
# tests that the response status code from the jokes api was success (200)
@pytest.fixture
@then("the response status code is 200")
def test_joke_response_success(joke_response):
    # check actual vs expected and assert
    assert joke_response.status_code == 200
