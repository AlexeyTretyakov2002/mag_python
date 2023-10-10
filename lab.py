#Первый вариант
import os
import requests
import time
from bs4 import BeautifulSoup

# Чтение одной страницы
# URL = "https://www.kinopoisk.ru/film/535341/reviews/ord/rating/status/bad/perpage/10/page/1/"
# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(URL, headers=headers)
# html_page = response.text
# soup = BeautifulSoup(html_page, "html.parser")
# htmlText = soup.prettify()

textResult = ""
num_pos_reviews  = 0
num_neg_reviews  = 0
downloaded_count = 0
# Цикл по страницам рецензий (5, чтобы не заблочило капчей)
for page in range(1, 10):
    search_url = f'https://www.kinopoisk.ru/film/535341/reviews/ord/rating/status/bad/perpage/10/page/{page}/'
    response = requests.get(search_url, headers={"User-Agent":"Mozilla/5.0"})
    response.encoding = 'utf-8' 
    soup = BeautifulSoup(response.text, "html.parser")
    if(response.status_code == 200):
        textResult += soup.prettify() 
    else:
        print("Некорректная загрузка страницы" + page)
    time.sleep(5)

# Потом когда получится собрать рецензии с нескольких страниц, распарсить можно прямо из текстового файла

# Записываем текст элемента в файл
# Получаем путь к текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "example.txt")
with open(file_path, "w") as file:
    file.write(textResult)