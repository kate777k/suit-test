import time
from behave import given, when, then, step


@given("I open Suitsupply website")
def step_impl(context):
    context.browser.get("https://eu.suitsupply.com/en/home")


@step("I close cookie bar")
def step_impl(context):
    context.browser.find_element_by_css_selector('#notification-legacy-overide-1 > div.notifications-container > div.cookie-bar > span.notification__trigger > i.js-cookie-bar-close').click()


@step("I close country verification bar")
def step_impl(context):
    context.browser.find_element_by_css_selector('#notification-legacy-overide-1 > div.notifications-container > div.country-verification-bar span.notification__trigger > i.js-country-verification-bar-close').click()


@when("I select 'Clothing' from the menu")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-clothing').click()


@step("I choose 'Suits' category")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-category.sel-suits').click()


@step("I select a product from lister")
def step_impl(context):
    context.browser.find_element_by_css_selector(f'.js-category-content .sel-product-container').click()


@step("I click on 'Select size' dropdown")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-size-field').click()


@step("I select size #'{size_num}' from dropdown")
def step_impl(context, size_num):
    context.browser.find_element_by_css_selector(f'.sel-size-field > option:nth-child({size_num})').click()


@step("I click on 'ADD TO BAG'")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-controls-container button.js-add-to-bag-btn').click()


@step("I click on 'Secure checkout' on Minicart")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-checkout-trigger').click()


@step("I click on 'Proceed to purchase' on Cart page")
def step_impl(context):
    context.browser.find_element_by_css_selector('.js-purchase-btn.sel-checkout-trigger').click()


@step("I enter user '{user}' on Login page")
def step_impl(context, user):
    user_input = context.browser.find_element_by_css_selector('#dwfrm_login_registered_username')
    user_input.clear()
    user_input.send_keys(user)


@step("I enter password '{password}' on Login page")
def step_impl(context, password):
    password_input = context.browser.find_element_by_css_selector('#dwfrm_login_registered_password')
    password_input.clear()
    password_input.send_keys(password)


@step("I click on 'Login & continue'")
def step_impl(context):
    context.browser.find_element_by_css_selector('.sel-login-trigger.sel-login').click()


@then("Checkout page opens")
def step_impl(context):
    print('Checkout page opened and test passed')
    context.browser.quit()
