# zoom.feature
# this file tests to make sure zoom button works

Feature: zoom button

    Scenario: check if page loads when user goes to the main page
        Given user has a web browser open
          And user has gone to the main page
         When user clicks the zoom-in button
         Then view should change
