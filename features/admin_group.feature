# Created by tatyana at 07.08.2020
Feature: Work with group
  Scenario: Add new group
    Given admin user is authenticated
    When user creates "group C"
    When user creates "group A"
    Then group list is "group C,group A"

  Scenario: Delete group
    Given admin user is authenticated
    Given there are groups "group A,group B"
    When user deletes the "group B"
    Then group list does not contain the deleted group "group B"
