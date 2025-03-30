import sqlite3

#CONFIGURAÇÃO DO DATABSE
def setup_database():
    conn = sqlite3.connect("SECwallet.db")
    cursor = conn.cursor()

    #CRIAÇÃO DA TABELA
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT UNIQUE,
            encrypted_password TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Banco de dados configurado!")

def get_connection():
    return sqlite3.connect("SECwallet.db")