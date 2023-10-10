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
# from selenium import webdriver
# URL = "https://www.kinopoisk.ru/film/435/"
# # Инициализация драйвера браузера
# driver = webdriver.Chrome()
# # Загрузка страницы
# driver.get(URL)
# # Получение полного HTML-кода страницы
# html_code = driver.page_source
# # Закрытие браузера
# driver.quit()
# print(html_code)


from selenium import webdriver
# Указываем путь к драйверу Chrome
driver = webdriver.Chrome( executable_path="D://Study/Magistracy/Semester_1/НовыеТехнологии(Корнеева)/chromedriver.exe")
# Загружаем страницу
URL = "https://www.kinopoisk.ru/film/435/"
driver.get(URL)
# Получаем полный текст страницы
html_page = driver.page_source
# Закрываем браузер
driver.quit()
print(html_page)