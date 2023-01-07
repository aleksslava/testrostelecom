import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def web_browser(scope='function'):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = Chrome(executable_path=r"tests/chromedriver.exe", options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()