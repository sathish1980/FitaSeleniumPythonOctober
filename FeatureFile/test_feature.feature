Feature: Login functionality
    Scenario: Successful login
        Given the user is on the login page
        When the user enters valid credentials
        Then the user should be logged in

    Scenario: incorrect login
        Given the user is on the login page
        When the user enters invalid credentials
        Then the user should not be logged in

