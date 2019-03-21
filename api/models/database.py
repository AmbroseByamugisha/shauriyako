import psycopg2

class Database_1:
    """
    creates a schema for the databases
    """
    def __init__(self, conn):
        self.conn = psycopg2.connect(
        host="localhost",
        database="shauriyako_db",
        user="postgres",
        password="lionelmessi10"
        )
        create_tables()

    def create_tables(self):
        """
        create tables in the shauriyako
        database.
        """
        commands = (
        """
        CREATE TABLE users(
        user_id SERIAL PRIMARY KEY,
        user_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE products(
        product_id SERIAL PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL,
        price VARCHAR(200) NOT NULL,
        product_image VARBINARY(MAX),
        FOREIGN KEY (user_id)
        REFERENCES users (user_id)
        )
        """
        )
        try:
            cur = self.conn.cursor()
            for command in commands:
                cur.execute(command)
            cur.close
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
db_connection = Database_1()
