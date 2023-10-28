import os
import pandas as pd

# СОЗДАНИЕ ДАТАСЕТА
#import dateparser
# data = []

# def process_review_file(file_path, rating):
#     with open(file_path, "r", encoding="utf-8") as file:
#         lines = file.readlines()
#         title = lines[0].strip()
#         header = lines[1].strip()
#         text = ""
#         for line in lines[2:-1]:
#             text += line.strip() + " "
#         date_str = lines[-1].strip()
#         date = dateparser.parse(date_str)
#         iso_date = date.strftime("%Y-%m-%dT%H:%M:%S")   
#         data.append([title, rating, header, text, iso_date])

# # Обработка файлов с хорошими рецензиями
# good_reviews_dir = "./dataset/good"
# for file_name in os.listdir(good_reviews_dir):
#     file_path = os.path.join(good_reviews_dir, file_name)
#     process_review_file(file_path, "+")

# # Обработка файлов с плохими рецензиями
# bad_reviews_dir = "./dataset/bad"
# for file_name in os.listdir(bad_reviews_dir):
#     file_path = os.path.join(bad_reviews_dir, file_name)
#     process_review_file(file_path, "-")

# # Создание DataFrame
# df = pd.DataFrame(data, columns=["Title", "Rating", "Header", "Text", "Date"])
# df.to_csv("reviews_dataset.csv", index=False, encoding="utf-8", sep="|")

#1. Написать скрипт для формирования текстового файла-аннотации собранного датасета. Файл-аннотация должен представлять собой csv-файл,
#  в котором в первой колонке будет указан абсолютный путь к файлу, во второй колонке относительный путь относительно вашего Рупоп-проекта,
#  третья колонка будет содержать текстовое название класса (метку класса), к которому относится данный экземпляр.
# import csv
# def create_annotation_file(dataset_dir, annotation_file):
#     with open(annotation_file, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Absolute Path', 'Relative Path', 'Class Label'])
        
#         for root, dirs, files in os.walk(dataset_dir):
#             for file in files:
#                 class_label = os.path.basename(root)
#                 absolute_path = os.path.join(root, file)
#                 relative_path = os.path.relpath(absolute_path, dataset_dir)
#                 writer.writerow([absolute_path, relative_path, class_label])

# create_annotation_file('dataset', 'annotation.csv')

# 2. Написать скрипт для копирования датасета в другую директорию таким образом, чтобы имена файлов содержали имя класса и его порядковый номер. То есть из dataset/class/0000/txt должно получиться dataset/class_0000.txt. Для того чтобы осталась
# возможность определить принадлежность экземпляра к классу создать файл-аннотацию (как в пункте 1).
import shutil
import os
import csv

# Проверка существования каталогов
# def checkDirectories():
#     if(not(os.path.exists('new_dataset'))):
#         os.mkdir('new_dataset')

# def copy_dataset_with_renamed_files(dataset_dir, destination_dir):
#     with open('annotation.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
        
#         checkDirectories()
#         for row in reader:
#             row = row[0].split(";")
#             absolute_path = row[0]
#             class_label = row[2]
#             file_name = f"{class_label}_{os.path.basename(absolute_path)}"
#             destination_path = os.path.join(destination_dir, file_name)
#             shutil.copyfile(absolute_path, destination_path)

# copy_dataset_with_renamed_files('dataset', 'new_dataset')

# 3. Написать скрипт, создающий копию датасета таким образом, чтобы каждый файл из сходного датасета получил случайный
# номер от 0 до 10000, и датасет представлял собой следующую структуру dataset/номер.txt. Для того чтобы осталась
# возможность определить принадлежность экземпляра к классу создать файл-аннотацию (как в пункте 1).

# 4. Написать скрипт, содержащий функцию, получающую на входе метку класса и возвращающую следующий экземпляр (путь к нему) этого класса. Экземпляры идут в любом порядке, но не повторяются. Когда экземпляры заканчиваются, функция
# возвращает None.

# 5. Написать на основе предыдущего пункта классы итераторы 