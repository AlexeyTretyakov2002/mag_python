import os
import pandas as pd
import dateparser

data = []

def process_review_file(file_path, rating):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        title = lines[0].strip()
        header = lines[1].strip()
        text = ""
        for line in lines[2:-1]:
            text += line.strip() + " "
        date_str = lines[-1].strip()
        date = dateparser.parse(date_str)
        iso_date = date.strftime("%Y-%m-%dT%H:%M:%S")   
        data.append([title, rating, header, text, iso_date])

# Обработка файлов с хорошими рецензиями
good_reviews_dir = "./dataset/good"
for file_name in os.listdir(good_reviews_dir):
    file_path = os.path.join(good_reviews_dir, file_name)
    process_review_file(file_path, "+")

# Обработка файлов с плохими рецензиями
bad_reviews_dir = "./dataset/bad"
for file_name in os.listdir(bad_reviews_dir):
    file_path = os.path.join(bad_reviews_dir, file_name)
    process_review_file(file_path, "-")

# Создание DataFrame
df = pd.DataFrame(data, columns=["Title", "Rating", "Header", "Text", "Date"])
df.to_csv("reviews_dataset.csv", index=False, encoding="utf-8", sep="|")