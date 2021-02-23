Feature: Single-Part Jokes
  As an audience,
  I want to get a random single-part joke on a given category,
  So that I can have a good laugh.

  Scenario Outline: Jokes API Query
    When the Jokes API is queried with "<category>" and "<joke_type>"
    Then the response status code is 200
    And the response contains a category of "<response_category>", a joke type of "<response_joke_type>", and the joke itself

    # parameters for test cases
    # these are all the possible single-part joke categories that the api supports
    Examples: Single-Part Jokes
      | category      | joke_type    | response_category  | response_joke_type |
      | Programming   | single       | Programming        | single             |
      | Misc          | single       | Misc               | single             |
      | Dark          | single       | Dark               | single             |
      | Pun           | single       | Pun                | single             |