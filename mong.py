import json
from pymongo import MongoClient

with open('books_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

client = MongoClient('mongodb://localhost:27017/')

db = client['books_database']  
collection = db['books']  

collection.insert_many(data)

documents = collection.find() 
# for document in documents:
#      print(document) 

# Запрос 1 - Книги с ценой больше 400
# documents = collection.find({'price': {'$gt': 55}})
# print("\nКниги с ценой больше 55:")
# for document in documents:
#     print(document)

# Запрос 2 - Получаем только название и цену книг
# documents = collection.find({}, {'title': 1, 'price': 1})
# print("\nНазвание и цена всех книг:")
# for document in documents:
#     print(document)

# Запрос 3 - Книги с самой низкой ценой (ограничение на 3 книги)
# documents = collection.find().sort('price', 1).limit(3)
# print("\nТри книги с самой низкой ценой:")
# for document in documents:
#     print(document)

# Запрос 4 - Книги с ценой больше 300 и остатком больше 5
# documents = collection.find({'price': {'$gt': 50}, 'stock': {'$gt': 20}})
# print("\nКниги с ценой больше 50 и остатком больше 20:")
# for document in documents:
#     print(document)
