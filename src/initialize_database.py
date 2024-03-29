from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        drop table if exists users;
    ''')
    connection.commit()
    cursor.execute('''
        drop table if exists transactions;
    ''')
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table users (
            username TEXT PRIMARY KEY,
            password TEXT
        );
    ''')
    connection.commit()

    cursor.execute('''
        create table transactions (
            subject TEXT,
            amount INT,
            user_id TEXT
        );
    ''')
    connection.commit()



def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
    