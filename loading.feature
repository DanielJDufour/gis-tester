# loading.feature
# this file tests to make sure everything loaded properly

Feature: page load

    Scenario: check if page loads when user goes to the main page
        Given user has a web browser open
         When user goes to the main page
         Then page should not be blank
          And page should not mention errors
