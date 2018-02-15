Feature: Smoke on Suitsupply

    Scenario: Navigation to PDP
      Given I open Suitsupply website
      And I close cookie bar
      And I close country verification bar
      When I select Clothing from the menu
      And I choose needed category
      And I select a product from lister
      And I click on dropdown on PDP
      And I select size #'4' from dropdown
      And I click on 'ADD TO BAG'
      And I click on 'Secure checkout' on minicart
      And I click on 'Proceed to purchase'
      And I enter user '***REMOVED***' on Login page
      And I enter password '***REMOVED***' on Login page
      And I click on 'Login & continue'
      Then Checkout page opens
