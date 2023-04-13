from time import sleep
import requests
import pytest
from settings import valid_email, valid_password, valid_phone, valid_login, valid_lic_scet
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# тест RT-001 - общий вид формы (сохранить скриншот)
def test_vid_form():
    pytest.driver.save_screenshot('glav_stran.jpg')

#RT-002
#Проверка что перешли на страницу и она успешно открылась
def test_site():
   r = requests.get("https://b2c.passport.rt.ru/")
   assert "https://b2c.passport.rt.ru/" in pytest.driver.current_url and r.status_code == 200


#RT-003
#'''Авторизация при помощи телефона'''
def test_auth_with_phone():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   # Вводим email
   pytest.driver.find_element(By.ID,'username').send_keys(valid_phone)
   # Вводим пароль
   pytest.driver.find_element(By.ID,'password').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID,'kc-login').click()
   # Проверяем, что мы оказались на своей странице
   assert pytest.driver.find_element(By.CSS_SELECTOR, f"span[title='{valid_phone}']").get_attribute("innerHTML").splitlines()[0] == valid_phone

#RT-004
#'''Авторизация при помощи телефона''' с не правильным паролем
def test_negative_by_phone():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   # Вводим email
   pytest.driver.find_element(By.ID,'username').send_keys(valid_phone)
   # Вводим пароль
   pytest.driver.find_element(By.ID,'password').send_keys('valid_password')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID,'kc-login').click()
   # Проверяем, что мы оказались на своей странице
   err_mess = pytest.driver.find_element(By.ID, 'form-error-message')
   assert err_mess.text == 'Неверный логин или пароль'

#RT-005
#'''Авторизация при помощи почты'''
def test_auth_with_email():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()
   # Вводим email
   pytest.driver.find_element(By.ID,'username').send_keys(valid_email)
   # Вводим пароль
   pytest.driver.find_element(By.ID,'password').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID,'kc-login').click()
   # Проверяем, что мы оказались на своей странице
   assert pytest.driver.find_element(By.CSS_SELECTOR, f"span[title='{valid_email}']").get_attribute("innerHTML").splitlines()[0]== valid_email

#RT-006
#'''Авторизация при помощи почты''' емайл без имени
def test_auth_without_name_emai():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()
   # Вводим email
   pytest.driver.find_element(By.ID,'username').send_keys('@ru.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'password').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID,'kc-login').click()
   # Проверяем, что мы оказались на своей странице
   err_mess = pytest.driver.find_element(By.ID, 'form-error-message')
   assert err_mess.text == 'Неверный логин или пароль'

#RT-007
#'''Авторизация при помощи логина'''
def test_auth_with_login():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   # Жмем Логин
   pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').click()
   # Вводим email
   pytest.driver.find_element(By.ID,'username').send_keys(valid_login)
   # Вводим пароль
   pytest.driver.find_element(By.ID,'password').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID,'kc-login').click()
   # Проверяем, что мы оказались на своей странице
   assert pytest.driver.find_element(By.CSS_SELECTOR, f"span[title='{valid_email}']").get_attribute("innerHTML").splitlines()[0]== valid_email

#RT-007
#'''Авторизация при помощи логина''' Логин из китайский символов
def test_auth_with_login_chinese():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   # Жмем Логин
   pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').click()
   # Вводим email
   pytest.driver.find_element(By.ID,'username').send_keys('的一是不了人我在有他这为之大来以个中上们')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'password').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID,'kc-login').click()
   err_mess = pytest.driver.find_element(By.ID, 'form-error-message')
   assert err_mess.text == 'Неверный логин или пароль'



# '''Авторизация при помощи счета'''
# У меня нет счета поэтому тест негативный
def test_auth_with_scet():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-ls').click()
   # Вводим email
   pytest.driver.find_element(By.ID, 'username').send_keys(valid_lic_scet)
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID, 'kc-login').click()
   err_mess = pytest.driver.find_element(By.ID, 'form-error-message')
   assert err_mess.text == 'Неверный логин или пароль'


#RT-008
# Авторизация про помощи вк
def test_with_vk():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.ID, 'oidc_vk').click()
   # Проверяем что перешли на вк для авторизации
   assert "vk.com" in pytest.driver.current_url


#RT-009
# Авторизация при помощи одноклассников
def test_with_odnoklassniki():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.ID, 'oidc_ok').click()
   # Проверяем что перешли на одноклассники для авторизации
   assert "ok.ru" in pytest.driver.current_url

#RT-010
# Авторизация при помощи мэйл ру
def test_with_mail():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.ID, 'oidc_mail').click()
   # Проверяем что перешли в мэйл ру для авторизации
   assert "mail.ru" in pytest.driver.current_url


#RT-011
# Авторизация при помощи гугл
def test_with_gmail():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.ID, 'oidc_google').click()
   # Проверяем что перешли в гугл для авторизации
   assert "google.com" in pytest.driver.current_url

# проверка перехода по ссылке авторизации пользователя через яндекс - какая то проблема с этим у меня
# def test_auth_ya():
#    pytest.driver.implicitly_wait(10)
#    pytest.driver.find_element(By.ID, 'oidc_ya').click()
#    sleep(10)
#    assert pytest.driver.current_url == 'passport.yandex.ru'

#RT-012
#Попытка нажать на пользовательские соглашения
def test_agreement():
   pytest.driver.implicitly_wait(10)
   original_window = pytest.driver.current_window_handle
   # клик по надписи "Пользовательским соглашением" в подвале страницы
   pytest.driver.find_element(By.CSS_SELECTOR, '.auth-policy > .rt-link.rt-link--orange').click()
   sleep(5)
   WebDriverWait(pytest.driver, 5).until(EC.number_of_windows_to_be(2))
   for window_handle in pytest.driver.window_handles:
      if window_handle != original_window:
         pytest.driver.switch_to.window(window_handle)
         break
   win_title = pytest.driver.execute_script("return window.document.title")

   assert win_title == 'User agreement'


### RT-13 - проверка перехода в форму восстановления пароля и её открытия
def test_forgot_pass():
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.ID, "forgot_password").click()
   sleep(5)
   reset_pass = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
   assert reset_pass.text == 'Восстановление пароля'

