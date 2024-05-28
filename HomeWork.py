import psycopg2

class ConnectDb:
    def __init__(self, db_name):
        self.db_name = db_name
        
    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname=self.db_name,
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        self.cursor = self.conn.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.cursor.close()
        self.conn.close()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def save_to_db(self, cursor):
        cursor.execute("INSERT INTO your_table_name (name, price) VALUES (%s, %s)", (self.name, self.price))

# Подключение к базе данных и сохранение данных с помощью Product class
db_name = "your_database_name"
with ConnectDb(db_name) as cursor:
    cursor.execute("CREATE TABLE IF NOT EXISTS your_table_name (id SERIAL PRIMARY KEY, name TEXT, price REAL)")
    
    products = [
        Product("Phone", 500),
        Product("Laptop", 1200),
        Product("Headphones", 100)
    ]
    
    for product in products:
        product.save_to_db(cursor)
