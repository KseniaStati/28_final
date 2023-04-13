import pytest
from settings import valid_password, valid_first_name, valid_last_name, valid_adress_new_email
from selenium.webdriver.common.by import By

#RT-014
#Проверяем что мы перешли на страницу регистрации
def test_registracia_reg():
   # Устанавливаем неявное ожидание
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element(By.CSS_SELECTOR, 'a#kc-register').click() # Жмём кнопку зарегистрироваться
   #Проверяем что мы на странице с регистрацией
   assert ("registration" in pytest.driver.current_url) and (pytest.driver.find_element(By.CSS_SELECTOR,".card-container__title").get_attribute("innerHTML").splitlines()[0] == "Регистрация")

#RT-015
#Заполняем поля валидными значениями
def test_registracia_with_valid_value():
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.CSS_SELECTOR, 'a#kc-register').click() # Жмём кнопку зарегистрироваться
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(valid_first_name) # Заполняем Имя
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(valid_last_name) # Заполняем Фамилию

    # Выбираем регион
    pytest.driver.find_element(By.XPATH, "//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']").click()
    pytest.driver.find_element(By.XPATH,"//div[13]").click()
    #Вводим емал адрес
    pytest.driver.find_element(By.ID, 'address').send_keys(valid_adress_new_email)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.NAME, 'register').click()
    # Проверяем, что мы прошли первичную регистрацию и перешли на страницу с подтверждением
    assert pytest.driver.find_element(By.CLASS_NAME,   "card-container__title").get_attribute("innerHTML").splitlines()[0] == "Подтверждение email"


#RT-016 Поле Фамилия Китайскими символами
def test_registracia_without_valid_value():
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.CSS_SELECTOR, 'a#kc-register').click() # Жмём кнопку зарегистрироваться
    pytest.driver.find_element(By.NAME, 'firstName').send_keys('的一是不了人我在有他这为之大来以个中上们') # Заполняем Имя
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(valid_last_name) # Заполняем Фамилию
    # Выбираем регион
    pytest.driver.find_element(By.XPATH, "//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']").click()
    pytest.driver.find_element(By.XPATH,"//div[13]").click()
    #Вводим емал адрес
    pytest.driver.find_element(By.ID, 'address').send_keys(valid_adress_new_email)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.NAME, 'register').click()
    err_mess = pytest.driver.find_element(By.CSS_SELECTOR, 'div:nth-of-type(1) > .rt-input-container__meta.rt-input-container__meta--error')
    assert err_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

#RT-017 Поле Имя спец символы
def test_registracia_without_valid_value():
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.CSS_SELECTOR, 'a#kc-register').click() # Жмём кнопку зарегистрироваться
    pytest.driver.find_element(By.NAME, 'firstName').send_keys('|\\/!@#$%^&*()-_=+`~?"№;:[]{}') # Заполняем Имя
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(valid_last_name) # Заполняем Фамилию
    # Выбираем регион
    pytest.driver.find_element(By.XPATH, "//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']").click()
    pytest.driver.find_element(By.XPATH,"//div[13]").click()
    #Вводим емал адрес
    pytest.driver.find_element(By.ID, 'address').send_keys(valid_adress_new_email)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.NAME, 'register').click()
    err_mess = pytest.driver.find_element(By.CSS_SELECTOR, 'div:nth-of-type(1) > .rt-input-container__meta.rt-input-container__meta--error')
    assert err_mess.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


#RT-018 Поле телефон кириллицей
def test_registracia_without_rus_phone():
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.CSS_SELECTOR, 'a#kc-register').click() # Жмём кнопку зарегистрироваться
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(valid_first_name) # Заполняем Имя
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(valid_last_name) # Заполняем Фамилию
    # Выбираем регион
    pytest.driver.find_element(By.XPATH, "//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']").click()
    pytest.driver.find_element(By.XPATH,"//div[28]").click()
    #Вводим емал адрес
    pytest.driver.find_element(By.ID, 'address').send_keys("ццуу")
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.NAME, 'register').click()
    err_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.email-or-phone.register-form__address.rt-input-container.rt-input-container--error > .rt-input-container__meta.rt-input-container__meta--error')
    assert err_mess.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

#RT-019 Поле телефон цифрами
def test_registracia_without_number_phone():
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.CSS_SELECTOR, 'a#kc-register').click() # Жмём кнопку зарегистрироваться
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(valid_first_name) # Заполняем Имя
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(valid_last_name) # Заполняем Фамилию
    # Выбираем регион
    pytest.driver.find_element(By.XPATH, "//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']").click()
    pytest.driver.find_element(By.XPATH,"//div[28]").click()
    #Вводим емал адрес
    pytest.driver.find_element(By.ID, 'address').send_keys(0000000000000)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.NAME, 'register').click()
    err_mess = pytest.driver.find_element(By.CSS_SELECTOR, '.email-or-phone.register-form__address.rt-input-container.rt-input-container--error > .rt-input-container__meta.rt-input-container__meta--error')
    assert err_mess.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


#RT-020 Пароль менее 8 символов
def test_registracia_pass_min_8():
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.CSS_SELECTOR, 'a#kc-register').click() # Жмём кнопку зарегистрироваться
    pytest.driver.find_element(By.NAME, 'firstName').send_keys(valid_first_name) # Заполняем Имя
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(valid_last_name) # Заполняем Фамилию
    # Выбираем регион
    pytest.driver.find_element(By.XPATH, "//div[@class='rt-input-container rt-select__input']//input[@class='rt-input__input rt-input__input--rounded rt-input__input--orange']").click()
    pytest.driver.find_element(By.XPATH,"//div[13]").click()
    #Вводим емал адрес
    pytest.driver.find_element(By.ID, 'address').send_keys(valid_adress_new_email)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys(444)
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('444')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.NAME, 'register').click()
    err_mess = pytest.driver.find_element(By.CSS_SELECTOR,'.new-password-container__confirmed-password.rt-input-container.rt-input-container--error > .rt-input-container__meta.rt-input-container__meta--error')
    assert err_mess.text == 'Длина пароля должна быть не менее 8 символов'









