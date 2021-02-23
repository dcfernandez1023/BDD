Feature: Two-Part Jokes
  As an audience,
  I want to get a random two-part joke on a given category,
  So that I can have a good laugh.

  Scenario Outline: Jokes API Query
    When the Jokes API is queried with "<category>" and "<joke_type>"
    Then the response status code is 200
    And the response contains a category of "<response_category>", a joke type of "<response_joke_type>", and a setup and delivery

    # parameters for test cases
    # these are all the possible two-part joke categories that the api supports
    Examples: Two-Part Jokes
      | category     | joke_type     | response_category  | response_joke_type |
      | Programming  | twopart       | Programming        | twopart            |
      | Misc         | twopart       | Misc               | twopart            |
      | Dark         | twopart       | Dark               | twopart            |
      | Pun          | twopart       | Pun                | twopart            |
      | Spooky       | twopart       | Spooky             | twopart            |
      | Christmas    | twopart       | Christmas          | twopart            |