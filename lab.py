import os
from html.parser import HTMLParser
import requests
import time
from bs4 import BeautifulSoup

# Приведение номера файла в требуемую форму
def getRightNumber(number):
    return str(number).zfill(4)

# Парсинг рецензии
def parseRevieHTML(review):    
    text = ""
    text += "\n"

    # Заголовок рецензии
    text += review.find('meta', itemprop='headline')['content'] 
    text += "\n"
    
    # Текст рецензии
    brand_words_div = review.find('div', class_='brand_words') 
    text += brand_words_div.text.strip()
    text += "\n"

    # Дата
    text += review.find('span', class_='date').text
    text += "\n"

    return text

# Проверка существования каталогов
def checkDirectories():
    if(not(os.path.exists('dataset'))):
        os.mkdir('dataset')
    if(not(os.path.exists('dataset/bad'))):
        os.mkdir('dataset/bad')
    if(not(os.path.exists('dataset/good'))):
        os.mkdir('dataset/good')

# Проверка и создание каталогов
checkDirectories()

num_pos_reviews  = 0   # Порядковый номер положительных рецензий
num_neg_reviews  = 0   # Порядковый номер отрицательных рецензий

# Фильмы
links = []
link = f'https://www.kinopoisk.ru/film/535341/reviews/ord/rating/status/all/perpage/10/page/' # 1+1
links.append(link)
link = f"https://www.kinopoisk.ru/film/329/reviews/ord/date/status/all/perpage/10/page/"      # Список Шиндлера
links.append(link)

for link in links:
    # Цикл по страницам рецензий (3, чтобы не заблочило капчей)
    for page in range(1, 3):
        search_url = str(link) + str(page) + "/"
        response = requests.get(search_url, headers={"AlienOnUfo":"Mozilla/5.0"})
        response.encoding = 'utf-8' 
        soup = BeautifulSoup(response.text, "html.parser")

        # Название фильма
        title = soup.title.string.replace("— отзывы и рецензии — Кинопоиск", "")

        # Проверка на валидность странички
        if(response.status_code == 200):
            # Проход по всем отзывам
            for review in soup.find_all('div', class_='reviewItem'):
                # Положительная или отрицательная рецензия
                responseMark = False 
                if("response good" in review.prettify()):
                    responseMark = True

                textReview = title
                # Парсить текст
                textReview += parseRevieHTML(review)

                if(responseMark == True): # Положительная оценка
                    file_path = "dataset/good/" + getRightNumber(num_pos_reviews) + ".txt"
                    num_pos_reviews+=1
                else:
                    file_path = "dataset/bad/" + getRightNumber(num_neg_reviews) + ".txt"
                    num_neg_reviews+=1
                
                file = open(file_path, "w", encoding="utf-8")
                file.write(textReview)
                file.close()
        else:
            print("Некорректная загрузка страницы" + page)
        
        # Чтобы меньше блочило капчей
        time.sleep(5)