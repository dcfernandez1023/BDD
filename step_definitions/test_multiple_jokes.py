import pytest
import requests
from pytest_bdd import scenarios, when, then

# public api to get random single or two-part jokes of a random category
JOKES_API = "https://v2.jokeapi.dev/joke/Any"

# path to feature file
scenarios("../features/multiple_jokes.feature", example_converters=dict(number_of_jokes=int,
                                                                        response_number_of_jokes=int))


# 'when' behavior test
# calls jokes api with specified number of jokes
@pytest.fixture
@when('the Jokes API is queried with "<number_of_jokes>"')
def joke_response(number_of_jokes):
    params = {'format': 'json', 'amount': number_of_jokes}
    response = requests.get(JOKES_API, params=params)
    return response 


# 'then' behavior test
# tests the data responded from the jokes api call, ensuring the correct number of jokes was returned
@pytest.fixture
@then('the response contains "<response_number_of_jokes>"')
def test_joke_response_amount(joke_response, response_number_of_jokes):
    # actual 
    json_response = joke_response.json()
    # check actual vs expected and assert
    assert len(json_response["jokes"]) == response_number_of_jokes
    

# 'then' behavior test
# tests that the response status code from the jokes api was success (200)
@pytest.fixture
@then("the response status code is 200")
def test_joke_response_success(joke_response):
    # check actual vs expected and assert
    assert joke_response.status_code == 200