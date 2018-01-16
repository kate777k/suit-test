Feature: Smoke on Suitsupply

    Scenario: Navigation to PDP
      Given I open Suitsupply website
      And I close cookie and country bars
      When I select Clothing from the menu
      And I choose needed category
      And I select a product from lister
      And I click on dropdown on PDP
      And I select size from dropdown
      And I click on 'Add to bug'
      And I click on 'Secure checkout' on minicart
      And I click on 'Proceed to purchase'
      And I enter my credentials on Login page
      And I click on Login button
      Then Checkout page opens
