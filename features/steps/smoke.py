import time
from behave import given, when, then


@given("I open Suitsupply website")
def step_impl(context):
    context.browser.get("https://eu.suitsupply.com/en/home")


@given("I close cookie bar")
def step_impl(context):
    context.browser.find_element_by_css_selector('.js-cookie-bar-close').click()


@given("I close country verification bar")
def step_impl(context):
    context.browser.find_element_by_css_selector('.js-country-verification-bar-close').click()


@when("I select 'Clothing' from the menu")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-clothing').click()


@when("I choose 'Suits' category")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-category.sel-suits').click()


@when("I select product #'{prod_num}' from lister")
def step_impl(context, prod_num):
    context.browser.find_element_by_css_selector(f'.js-category-content .sel-product-container:nth-child({prod_num})').click()


@when("I click on 'Select size' dropdown")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-size-field').click()


@when("I select size #'{size_num}' from dropdown")
def step_impl(context, size_num):
    context.browser.find_element_by_css_selector(f'.sel-size-field > option:nth-child({size_num})').click()


@when("I click on 'ADD TO BAG'")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-controls-container button.js-add-to-bag-btn').click()


@when("I click on 'Secure checkout' on Minicart")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-checkout-trigger').click()


@when("I click on 'Proceed to purchase' on Cart page")
def step_impl(context):
    context.browser.find_element_by_css_selector('.js-purchase-btn.sel-checkout-trigger').click()


@when("I enter user '{user}' on Login page")
def step_impl(context, user):
    user_input = context.browser.find_element_by_css_selector('#dwfrm_login_registered_username')
    user_input.clear()
    user_input.send_keys(user)


@when("I enter password '{password}' on Login page")
def step_impl(context, password):
    password_input = context.browser.find_element_by_css_selector('#dwfrm_login_registered_password')
    password_input.clear()
    password_input.send_keys(password)


@when("I click on 'Login & continue'")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-login-trigger.sel-login').click()


@then("Checkout page opens")
def step_impl(context):
    assert 'Check out' in context.browser.title, "Wrong page opened"
