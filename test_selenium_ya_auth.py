from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config import login, password_


def wait_element(browser, delay=10, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay).until(
        EC.presence_of_element_located((by, value))
    )


chrome_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrome_path)
browser = webdriver.Chrome(service=browser_service)
URL = 'https://passport.yandex.ru/auth/'


def test_success_auth():
    browser.get(URL)

    try:
        email = wait_element(browser=browser, by=By.ID, value='passp-field-login')
        email.send_keys(login)

        password_step = wait_element(browser=browser, by=By.ID, value='passp:sign-in')
        password_step.click()

        password = wait_element(browser=browser, by=By.ID, value='passp-field-passwd')
        password.send_keys(password_)

        login_step = wait_element(browser=browser, by=By.ID, value='passp:sign-in')
        login_step.click()

        success_auth_marker = wait_element(browser=browser, by=By.CLASS_NAME, value='UserID-Badge')

        assert success_auth_marker is True

    except Exception as e:
        print(f"Не удалось найти элемент: {e}")

        browser.quit()
