Feature: test the register functionality
  Scenario: Register user
    Given home_page: I am on home page
    When  home_page: I click login button
    Then register_page: I check the SignUp is visible
    When register_page: I enter "Bogdan" as name
    And register_page: I enter "bogdan@yahoo.com" as email adress
    And register_page: I click SingUp button
    Then register_page: I verify the enter acount information is visible