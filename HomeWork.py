import psycopg2

db_name = 'n47'
password = '0060'
host = 'localhost'
port = 5432
user = 'postgres'

conn = psycopg2.connect(database=db_name, user=user, password=password, host=host, port=port)

cur = conn.cursor()


def create_table():
    products_table = """
    CREATE TABLE IF NOT EXISTS products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(55) NOT NULL,
    image VARCHAR(155),
    is_liked BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );"""
    cur.execute(products_table)
    conn.commit()
    print("Table created successfully")


def insert_product(name, image):
    insert_product_data = """insert into products(name,image) values(%s,%s);"""
    cur.execute(insert_product_data, (name, image))
    conn.commit()
    print("Product inserted successfully")


def select_products(_id):
    select_data = """select * from products where id = %s """
    cur.execute(select_data, (_id,))
    cur.fetchone()
    products = cur.fetchall()
    return products


def delete_product(_id):
    delete_data = """delete from products where id = %s"""
    cur.execute(delete_data, (_id,))
    conn.commit()
    print("Product deleted successfully")


def update_product(_id, new_name, new_image):
    update_data = """update products set name = %s, image = %s where id = %s;"""
    cur.execute(update_data, (new_name, new_image, _id))
    conn.commit()
    print("Product updated successfully")
