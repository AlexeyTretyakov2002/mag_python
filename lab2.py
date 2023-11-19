import os
import pandas as pd

def checkDirectories(name):
     if(not(os.path.exists(name))):
         os.mkdir(name)

# СОЗДАНИЕ ДАТАСЕТА
# import dateparser
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

# №1. Написать скрипт для формирования текстового файла-аннотации собранного датасета. Файл-аннотация должен представлять собой csv-файл,
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

# 2. Написать скрипт для копирования датасета в другую директорию таким образом, чтобы имена файлов содержали имя класса и его порядковый номер. 
# То есть из dataset/class/0000/txt должно получиться dataset/class_0000.txt. Для того чтобы осталась
# возможность определить принадлежность экземпляра к классу и создать файл-аннотацию (как в пункте 1).
# import shutil
# import os
# import csv

# def copy_dataset_with_renamed_files(dataset_dir, destination_dir):
#     with open('annotation.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
        
#         checkDirectories(new_dataset)
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
# import random
# import shutil
# import os

# def copy_dataset_with_random_numbers(dataset_dir, destination_dir):
#     with open('annotation.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
        
#         checkDirectories("random_dataset")
#         for row in reader:
#             row = row[0].split(";")
#             absolute_path = row[0]
#             class_label = row[2]
#             random_number = random.randint(0, 10000)
#             file_name = f"{random_number}.txt"
#             destination_path = os.path.join(destination_dir, file_name)
#             shutil.copyfile(absolute_path, destination_path)

# copy_dataset_with_random_numbers('dataset', 'random_dataset')

# 4. Написать скрипт, содержащий функцию, получающую на входе метку класса и возвращающую следующий экземпляр (путь к нему) этого класса.
#    Экземпляры идут в любом порядке, но не повторяются. Когда экземпляры заканчиваются, функция возвращает None.
# import csv
# def get_next_instance(class_label, instances):        
#         for instance in instances:
#             instance = instance.split(";")
#             if instance[2] == class_label:
#                 instances.pop()
#                 return instance[0]
#             else:
#                 return None


# instances = set()
# with open('annotation.csv', 'r') as file:
#     reader = csv.reader(file)
#     next(reader)  # Skip header row
#     for row in reader:
#         instances.add(row[0])

#     next_instance = get_next_instance('good', instances)
#     while next_instance is not None:
#         # Process the instance
#         print(next_instance)
#         next_instance = get_next_instance('good', instances)


# 5. Написать на основе предыдущего пункта классы итераторы import csv
import pandas as pd

class InstanceIterator:
    def __init__(self, class_label):
        self.class_label = class_label
        self.instances = list()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.instances:
            raise StopIteration
        
        return self.instances.pop()
    
    def load_data(self, file_path):
        data = pd.read_csv(file_path, encoding='cp1251', sep=';')
        #print(data)  # Вывод содержимого переменной data
        #pd.columns
        rating_column = data.columns.get_loc('Rating')
        
        for index, row in data.iterrows():
            if row['Rating'] == self.class_label:
                instance = {
                    'Title': row['Title'],
                    'Rating': row['Rating'],
                    'Header': row['Header'],
                    'Text': row['Text'],
                    'Date': row['Date']
                }
                self.instances.append(instance)

iterator = InstanceIterator('-')
iterator.load_data('dataset.csv')

for instance in iterator:
    print(instance)