# Первый вариант
# import requests
# from bs4 import BeautifulSoup
# URL = "https://www.kinopoisk.ru/film/435/"
# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(URL, headers=headers)
# html_page = response.text
# soup = BeautifulSoup(html_page, "html.parser")
# print(soup.prettify())


# Второй вариант для получения полного кода
import os
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
# Загружаем страницу
URL = "https://www.kinopoisk.ru/film/535341/reviews/ord/rating/status/bad/perpage/10/page/1/"
driver = Firefox()
driver.get(URL)
# Получаем полный текст страницы
html_page = driver.page_source

# Закрываем браузер
driver.quit()

# Записываем текст элемента в файл
# Получаем путь к текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "example.txt")
with open(file_path, "w") as file:
    file.write(html_page)

print(html_page)