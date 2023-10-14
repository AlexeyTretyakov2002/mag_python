import os
from html.parser import HTMLParser
import requests
import time
from bs4 import BeautifulSoup

def getRightNumber(number):
    return str(number).zfill(4)


def parseRevieHTML(review):    
    text = ""

    a_tag = soup.find('a')
    text += str(a_tag.get('title'))
    text += "\n"

    text += review.find('meta', itemprop='headline')['content'] 
    text+= "\n"
    
    brand_words_div = review.find('div', class_='brand_words') 
    text += brand_words_div.text.strip()
    text += "\n"

    text += review.find('span', class_='date').text
    text += "\n"

    return text

def checkDirectories():
    if(not(os.path.exists('dataset'))):
        os.mkdir('dataset')
    if(not(os.path.exists('dataset/bad'))):
        os.mkdir('dataset/bad')
    if(not(os.path.exists('dataset/good'))):
        os.mkdir('dataset/good')

# Чтение одной страницы
# URL = "https://www.kinopoisk.ru/film/535341/reviews/ord/rating/status/bad/perpage/10/page/1/"
# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(URL, headers=headers)
# html_page = response.text
# soup = BeautifulSoup(html_page, "html.parser")
# htmlText = soup.prettify()

# Проверка и создание каталогов
checkDirectories()

num_pos_reviews  = 0
num_neg_reviews  = 0
downloaded_count = 0

# Цикл по страницам рецензий (5, чтобы не заблочило капчей)
for page in range(1, 5):
    search_url = f'https://www.kinopoisk.ru/film/535341/reviews/ord/rating/status/all/perpage/10/page/{page}/'
    response = requests.get(search_url, headers={"User-Agent":"Mozilla/5.0"})
    response.encoding = 'utf-8' 
    soup = BeautifulSoup(response.text, "html.parser")
    # Проверка на валидность странички
    if(response.status_code == 200):
        # Проход по всем отзывам
        for review in soup.find_all('div', class_='reviewItem'):
            # Положительная или отрицательная рецензия
            responseMark = False 
            if("response good" in review.prettify()):
                responseMark = True
            
            # Парсить текст
            textReview = parseRevieHTML(review)

            if(responseMark == True): # Положительная оценка
                file_path = "dataset/good/" + getRightNumber(num_pos_reviews) + ".txt"
                num_pos_reviews+=1
            else:
                file_path = "dataset/bad/" + getRightNumber(num_neg_reviews) + ".txt"
                num_neg_reviews+=1

            file = open(file_path, "w", encoding="utf-8")
            #file.write(f"1+1TEST\n")
            file.write(textReview)
            file.close()
    else:
        print("Некорректная загрузка страницы" + page)
    time.sleep(3)