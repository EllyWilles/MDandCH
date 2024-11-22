import json 
import clickhouse_connect 

with open('books_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

client = clickhouse_connect.get_client(
    host='xxcwe5fddb.us-central1.gcp.clickhouse.cloud',  
    user='default',  
    password='RZ3Tk94i~W1X~',  
    secure=True  
)

client.query('''
CREATE TABLE IF NOT EXISTS books (
    title String,
    price Float64,
    description String,
    stock Int32
) ENGINE = MergeTree()
ORDER BY title
''')

values = [(book['title'], book['price'], book['description'], book['stock']) for book in data]

client.insert('books', values)

print("Данные успешно загружены в ClickHouse.")
