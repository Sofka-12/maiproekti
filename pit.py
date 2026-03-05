from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем, пока цена не станет равной $100 (ожидание до 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку Book
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # Ждем появления алерта с результатом
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Результат: {alert_text}")

    # Копируем число из алерта (нужно для ответа на задание)
    answer_number = alert_text.split(": ")[-1]
    print(f"Число для ответа: {answer_number}")

    alert.accept()

finally:
    # Даем время посмотреть результат
    time.sleep(5)
    browser.quit()
