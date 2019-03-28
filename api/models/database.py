from urllib.parse import urlparse
import psycopg2
import psycopg2.extras as ambrosebyamu
from api import app
from api.models.models_1 import User


class Database_1:
    """
    creates a schema for the databases
    """
    def __init__(self):
        database_url = app.config['DATABASE_URL']
        parsed_url = urlparse(database_url)
        dbname = parsed_url.path[1:]
        user = parsed_url.username
        host = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port
        self.conn = psycopg2.connect(
        database=dbname,
        user=user,
        password=password,
        host=host,
        port=port
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor(cursor_factory=ambrosebyamu.RealDictCursor)
        print("Successfully connected to "+database_url)
        self.create_tables()
        admin = User('ambrose', 'ambrose@gmail.com', 'password123', 'admin')
        if not self.fetch_user(admin):
            self.add_user(admin)

    def create_tables(self):
        """
        method creates tables
        """
        commands = (
        """
        CREATE TABLE IF NOT EXISTS users(user_id serial PRIMARY KEY,\
          user_name varchar(50), email varchar(100), password varchar(20),\
          role varchar(15))""",

        """CREATE TABLE IF NOT EXISTS products(product_id serial PRIMARY KEY,\
          product_name varchar(100), price integer, product_image varchar(20),\
          user_id INTEGER REFERENCES users(user_id))"""
          )
          #FOREIGN KEY (user_id) REFERENCES users(user_id) )""",

        for command in commands:
             self.cursor.execute(command)

    def drop_tables(self):
        """
        method drops tables
        """
        drop_user_table = "DROP TABLE users cascade"
        drop_parcel_table = "DROP TABLE parcels cascade"
        self.cursor.execute(drop_user_table)
        self.cursor.execute(drop_parcel_table)

    def fetch_all_entries(self,table_name):
        """ Fetches all entries from the database"""
        query = ("SELECT * FROM %s;") %(table_name)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def add_user(self, user_1):
        self.cursor.execute("INSERT INTO users(user_name,email,password,role) VALUES\
        (%s, %s, %s, %s);",(user_1.user_name, user_1.email, user_1.password, user_1.role))

    def fetch_user(self,user):
        """Returns a user in form of a dict or None if user not found"""
        query = "SELECT * FROM users WHERE user_name=%s"
        self.cursor.execute(query, (user.user_name,))
        user = self.cursor.fetchone()
        return user

    def fetch_all_users(self):
        return self.fetch_all_entries('users')

    def add_product(self,product):
        self.cursor.execute("INSERT INTO products(product_name, price,\
        product_image, user_id) VALUES(%s, %s, %s, %s);",(product.product_name,product.price,\
        product.product_image, product.user_id))

    def fetch_all_orders(self):
        return self.fetch_all_entries('products')

    def fetch_product(self,column,did):
        """Returns a user in form of a dict or None if user not found"""
        query = """SELECT * FROM products WHERE {0}={1}""".format(column,did,)
        self.cursor.execute(query,)
        parcel = self.cursor.fetchall()
        return product

    def update_product(self,column,value, product_id):
            query = """UPDATE products SET {0} = '{1}' WHERE product_id  = {2}""".format(column,value, product_id)
            self.cursor.execute(query,)

    def query_last_item(self):
        query = """SELECT * FROM products ORDER BY product_id DESC LIMIT 1"""
        self.cursor.execute(query,)
        product = self.cursor.fetchone()
        return product

db_connection = Database_1()
