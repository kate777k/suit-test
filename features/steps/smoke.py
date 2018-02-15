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


@when("I select Clothing from the menu")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="header-legacy-overide-1"]/nav/div[2]/div/div/ul/li[2]/a/span').click()


@step("I choose needed category")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="header-legacy-overide-1"]/nav/div[2]/div/div/ul/li[2]/div/div/div[1]/div/div/ul/div[1]/ul/li[1]/a/span').click()


@step("I select a product from lister")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="contentWrap-legacy-overide-1"]/div/div/div[1]/a[1]/img').click()


@step("I click on dropdown on PDP")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="js-pdpmain"]/div/div[1]/div/div[3]/div[2]/div[1]/div[3]/div/select').click()


@step("I select size #'{size_num}' from dropdown")
def step_impl(context, size_num):
    context.browser.find_element_by_css_selector(f'#js-pdpmain div.main-product-info div.custom-select > select.sel-size-field > option:nth-child({size_num})').click()


@step("I click on 'ADD TO BAG'")
def step_impl(context):
    context.browser.find_element_by_css_selector('#js-pdpmain div.main-product-info div.sel-controls-container button.js-add-to-bag-btn').click()


@step("I click on 'Secure checkout' on minicart")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="minicart"]/div/div[2]/a').click()


@step("I click on 'Proceed to purchase'")
def step_impl(context):
    context.browser.find_element_by_xpath(
        '//*[@id="legacy-overide-id-bottom"]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/a').click()


@step("I enter user '{user}' on Login page")
def step_impl(context, user):
    user_input = context.browser.find_element_by_xpath('//*[@id="dwfrm_login_registered_username"]')
    user_input.clear()
    user_input.send_keys(user)


@step("I enter password '{password}' on Login page")
def step_impl(context, password):
    password_input = context.browser.find_element_by_xpath('//*[@id="dwfrm_login_registered_password"]')
    password_input.clear()
    password_input.send_keys(password)


@step("I click on 'Login & continue'")
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="dwfrm_login_registered"]/fieldset/input').click()


@then("Checkout page opens")
def step_impl(context):
    print('Checkout page opened and test passed')
    context.browser.find_element_by_xpath('//*[@id="dwfrm_').click()
    context.browser.quit()
