Feature: Smoke on Suitsupply

    Scenario: Navigation to PDP
      Given I open Suitsupply website
      And I close cookie bar
      And I close country verification bar
      When I select 'Clothing' from the menu
      And I choose 'Suits' category
      And I select product #'1' from lister
      And I click on 'Select size' dropdown
      And I select size #'4' from dropdown
      And I click on 'ADD TO BAG'
      And I click on 'Secure checkout' on Minicart
      And I click on 'Proceed to purchase' on Cart page
      And I enter user 'test@testtest.nl' on Login page
      And I enter password 'test12345' on Login page
      And I click on 'Login & continue'
      Then Checkout page opens
