Feature Multiple Jokes
  As an audience,
  I want to get multiple random jokes,
  So that I can have multiple good laughs.

  Scenario Outline: Multiple Jokes Query
    When the Jokes API is queried with "<number_of_jokes>"
    Then the response status code is 200
    And the response contains "<response_number_of_jokes>"

    # parameters for test cases
    # these test that the joke api will return the correct number of jokes when multiple jokes are queried
    # the max amount that the api supports is 10, so values higher than 10 will not be tested
    Examples: Multiple Jokes
      | number_of_jokes | response_number_of_jokes |
      | 2               | 2                        |
      | 3               | 3                        |
      | 4               | 4                        |
      | 5               | 5                        |
      | 6               | 6                        |
      | 7               | 7                        |
      | 8               | 8                        |
      | 9               | 9                        |
      | 10              | 10                       |