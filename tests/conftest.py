import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def web_browser(scope='function'):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service(r"tests/chromedriver.exe")
    driver = Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()