Feature: Funda Website Smoke Tests
  As a user
  I want to ensure that the Funda website is functioning correctly
  So that I can release new updates

  Scenario: Homepage loads successfully
    Given I navigate to the Funda homepage
    Then the homepage should load successfully


  Scenario: Search functionality works
    Given I am on the Funda homepage
    When I search for "Utrecht"
    Then I should see search results for "Utrecht"
    And verify listing and pagination are displayed


  Scenario: Property details page loads
    Given I am on the search results page for "Utrecht"
    When I click on the first property listing
    Then verify the property details page loads successfully


  Scenario: Contact form is displayed
    Given I am on a property details page of "Utrecht"
    When I click on the contact button
    Then the contact form should be displayed and verfied


   Scenario: Important links are working on homepage
    Given I am on the Funda homepage
    Then Verify all important links are working