import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string

# Чтение данных
df = pd.read_csv("dataset.csv", encoding='cp1251', sep=';')

# Именование колонок
df.columns = ["Title", "Rating", "Header", "Text", "Date"]

# Проверка на невалидные значения и их обработка
df = df.fillna("")

# Добавление столбца с количеством слов
df["word_count"] = df["Text"].apply(lambda x: len(word_tokenize(x)))

# Статистическая информация для числовых столбцов
numeric_columns = df.select_dtypes(include=[float, int]).columns
statistics = df[numeric_columns].describe()

# Функция для фильтрации по количеству слов
def filter_by_word_count(dataframe, max_words):
    return dataframe[dataframe["word_count"] <= max_words]

# Функция для фильтрации по метке класса
def filter_by_label(dataframe, label):
    return dataframe[dataframe[label] > 0]

# Группировка по метке класса с вычислением статистики по количеству слов
word_count_statistics = df.groupby("Rating")["word_count"].agg(["min", "max", "mean"])

# Функция для создания гистограммы слов
def create_word_histogram(dataframe, label):
    wordnet_lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    word_histogram = {}
    
    for index, row in dataframe.iterrows():
        text = row["Text"].lower()
        tokens = word_tokenize(text)
        tokens = [wordnet_lemmatizer.lemmatize(token) for token in tokens if token not in stop_words and token not in string.punctuation]
        
        for token in tokens:
            if token not in word_histogram:
                word_histogram[token] = 1
            else:
                word_histogram[token] += 1
    
    return word_histogram

# Создание гистограммы слов
word_histogram = create_word_histogram(df, "Rating")

# Визуализация гистограммы
plt.figure(figsize=(12, 6))
sns.barplot(x=list(word_histogram.keys()), y=list(word_histogram.values()))
plt.xlabel("Слово")
plt.ylabel("Количество")
plt.title("Гистограмма слов")
plt.xticks(rotation=90)
plt.show()