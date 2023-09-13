import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def setup():
    browser.config.base_url = 'http://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    options = webdriver.ChromeOptions()
    browser.config.driver = options
    yield
    browser.close()
