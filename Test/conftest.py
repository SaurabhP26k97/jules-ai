import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture(params=["chrome"], scope="function")
def init_driver(request):
    if request.param == "chrome":
        chromeOptions = webdriver.ChromeOptions()
        executable_path = ChromeDriverManager().install()
        chromeOptions.add_experimental_option("prefs", {"download.default_directory": "../Resources"})
        driver = webdriver.Chrome()
        driver.get("https://demo.haroldwaste.com/")
        driver.maximize_window()

    request.cls.driver = driver

    yield driver
    driver.quit()