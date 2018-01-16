from behave import *
from selenium import webdriver
import time
use_step_matcher("re")

driver = webdriver.Chrome("/Users/kzhuzha/work/python/chromedriver")

@given("I open Suitsupply website")
def step_impl(context):
    driver.get("https://eu.suitsupply.com/en/home")
    time.sleep(2)

@step("I close cookie and country bars")
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="notification-legacy-overide-1"]/div[2]/div[1]/span[3]/i').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="notification-legacy-overide-1"]/div[2]/div[2]/div/div[2]/form/span[2]/i').click()
    time.sleep(2)
    pass

@when("I select Clothing from the menu")
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="header-legacy-overide-1"]/nav/div[2]/div/div/ul/li[2]/a/span').click()
    time.sleep(2)


@step("I choose needed category")
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="header-legacy-overide-1"]/nav/div[2]/div/div/ul/li[2]/div/div/div[1]/div/div/ul/div[1]/ul/li[1]/a/span').click()
    time.sleep(2)
    pass


@step("I select a product from lister")
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="contentWrap-legacy-overide-1"]/div/div/div[1]/a[1]/img').click()
    time.sleep(2)
    pass

@step("I click on dropdown on PDP")
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="js-pdpmain"]/div/div[1]/div/div[3]/div[2]/div[1]/div[3]/div/select').click()
    time.sleep(2)
    pass

@step("I select size from dropdown")
def step_impl(context):
    driver.find_element_by_xpath(
        '//*[@id="js-pdpmain"]/div/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div/select/option[3]').click()
    time.sleep(3)
    pass

@step("I click on 'Add to bug'")
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="js-pdpmain"]/div/div[1]/div[1]/div[3]/div[2]/div[1]/div[4]/button').click()
    time.sleep(3)
    pass

@step("I click on 'Secure checkout' on minicart")
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="minicart"]/div/div[2]/a').click()
    time.sleep(2)
    pass

@step("I click on 'Proceed to purchase'")
def step_impl(context):
    driver.find_element_by_xpath(
        '//*[@id="legacy-overide-id-bottom"]/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[2]/a').click()
    time.sleep(2)
    pass

@step("I enter my credentials on Login page")
def step_impl(context):
    user = driver.find_element_by_xpath('//*[@id="dwfrm_login_registered_username"]')
    password = driver.find_element_by_xpath('//*[@id="dwfrm_login_registered_password"]')
    user.clear()
    user.send_keys("***REMOVED***")
    password.clear()
    time.sleep(1)
    password.send_keys("***REMOVED***")
    time.sleep(1)
    pass

@step("I click on Login button")
def step_impl(context):
    driver.find_element_by_xpath('//*[@id="dwfrm_login_registered"]/fieldset/input').click()
    time.sleep(2)
    pass


@then("Checkout page opens")
def step_impl(context):
    print('Checkout page opened')
    pass

