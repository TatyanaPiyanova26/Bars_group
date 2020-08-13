# Created by tatyana at 13.08.2020
Feature: Authentication
  Scenario: Open site when user is not authenticated
    When user opens page "/admin"
    Then user is redirected to "/admin/login/?next=/admin/"

  Scenario: Administrator logins with correct data
    Given admin user with username "admin" and password "admin12345!"
    When user logins with username "admin" and password "admin12345!"
    And user opens page "/admin"
    Then page loaded successfully

  Scenario: Administrator tries to log in with incorrect password
    Given admin user with username "admin" and password "admin12345!"
    When user logins with username "admin" and password "admin12345"
    Then failed to login

  Scenario: Unknown user tries to log in when user does not exist
    When user logins with username "admin" and password "admin12345"
    Then failed to login
