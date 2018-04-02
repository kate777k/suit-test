import time

from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Chrome(executable_path="/Users/kzhuzha/work/python/chromedriver")
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()


def after_all(context):
    context.browser.quit()


def after_step(context, step):
    time.sleep(2)
