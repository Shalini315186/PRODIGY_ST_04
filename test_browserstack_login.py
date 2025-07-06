import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "renukas_SGYNVm"
ACCESS_KEY = "H8zKkuCCqoaQzUQibHgK"

browsers = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "10",
            "buildName": "PRODIGY_ST_04",
            "sessionName": "Login Test - Chrome"
        }
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Monterey",
            "buildName": "PRODIGY_ST_04",
            "sessionName": "Login Test - Firefox"
        }
    }
]

@pytest.mark.parametrize("capabilities", browsers)
def test_login(capabilities):
    url = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", capabilities["browserName"])
    options.set_capability("browserVersion", capabilities["browserVersion"])
    options.set_capability("bstack:options", capabilities["bstack:options"])

    driver = webdriver.Remote(command_executor=url, options=options)

    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        assert "inventory" in driver.current_url
    finally:
        driver.quit()
