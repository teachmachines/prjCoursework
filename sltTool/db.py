import sqlite3
DATABASE = "dbUsers.db"


def setup_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    query = '''CREATE TABLE IF NOT EXISTS tblUser(
        fldEmail VARCHAR(255) NOT NULL, 
        fldPassword VARCHAR(255) NOT NULL
    );'''
    c.execute(query)
    conn.commit()
    conn.close()


def create_user(email, password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    query = f"INSERT INTO tblUser (fldEmail, fldPassword) VALUES ('{email}','{password}');"
    print(query)
    c.execute(query)
    conn.commit()
    conn.close()


def get_user(email, password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    query = f"SELECT * FROM tblUser WHERE email='{email}' = AND password='{password}'"
    print(query)
    c.execute(query)
    conn.commit()
    conn.close()
    print(c.fetchall())
    return c.fetchall()


def change_password(email, old_password, new_password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    query = f"UPDATE tblUser SET password = '{new_password}' WHERE email='{email}' = AND password='{old_password}';"
    print(query)
    c.execute(query)
    conn.commit()
    conn.close()


def change_email(email, new_email, password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    query = f"UPDATE tblUser SET email = '{new_email}' WHERE email='{email}' = AND password='{password}';"
    print(query)
    c.execute(query)
    conn.commit()
    conn.close()


def delete_account(email, password):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    query = f"DELETE FROM tblUser WHERE email='{email}' = AND password='{password}';"
    print(query)
    c.execute(query)
    conn.commit()
    conn.close()


