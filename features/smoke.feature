Feature: Smoke on Suitsupply

    Scenario: Navigation to PDP
      Given I open Suitsupply website
      And I close cookie bar
      And I close country verification bar
      And I select a product from lister
      When I select 'Clothing' from the menu
      And I choose 'Suits' category
      And I click on 'Select size' dropdown
      And I select size #'4' from dropdown
      And I click on 'ADD TO BAG'
      And I enter user '***REMOVED***' on Login page
      And I enter password '***REMOVED***' on Login page
      And I click on 'Secure checkout' on Minicart
      And I click on 'Proceed to purchase' on Cart page
      And I click on 'Login & continue'
      Then Checkout page opens
