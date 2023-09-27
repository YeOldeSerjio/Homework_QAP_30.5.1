import pytest
import selenium

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('sergey1603yulin@gmail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('!PETSpets1')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

def test_all_my_pets():

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="all_my_pets"]//img')))

    images = pytest.driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//img')

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@id="all_my_pets"]//td[1]')))

    names = pytest.driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[1]')


def test_my_pets_in_all_pets():

    pytest.driver = webdriver.Chrome()
    pytest.driver.implicity_wait(10)

    pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
    images = pytest.driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//img')
    names = pytest.driver.find_elements(By.XPATH, '//div[@id="all_my_pets"]//td[1]')
    ages = pytest.driver.find_elements(By.XPATH, '//div[@id="all_myu_pets"]//td[3]')

    for i in range(len(name)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert ages[i].text != ''

