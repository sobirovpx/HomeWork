import psycopg2


class ConnectDb:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname=self.db_name,
            user="postgres",
            password="0060",
            host="localhost",
            port="5432"
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
        cursor.execute("INSERT INTO products (title, price) VALUES (%s, %s)", (self.name, self.price))


db_name = "n47"
with ConnectDb(db_name) as cursor:
    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    title varchar(55) ,
    price integer NOT NULL)""")

    products = [
        Product("Phone", 500),
        Product("Laptop", 1200),
        Product("Headphones", 100)
    ]

    for product in products:
        product.save_to_db(cursor)
