import sqlite3
import base64
from cryptography.fernet import Fernet

#GET OU CREATE CHAVE MESTRE
def get_or_create_key(key_pass):
    key = base64.urlsafe_b64decode(key_pass.encode()[:32].ljust(32)[:32])
    return Fernet(key)

def add_password(service, password, fernet, conn):
    cursor = conn.cursor()
    encrypted_password = fernet.encrypt(password.encode()).decode()

    try:
        cursor.execute(''' 
            INSERT INTO passwords (service, encrypted_password)
            VALUES (?, ?)
        ''', (service, encrypted_password))
        conn.commit()
        print(f"Senha para '{service}' adicionada com sucesso!")
    except sqlite3.IntegrityError:
        print(f"Erro: já existe uma senha para '{service}'. Use ATUALIZAR para mudar!")

def get_password(service, fernet, conn):
    cursor = conn.cursor()
    cursor.execute("SELECT encrypted_password FROM passwords WHERE service =?", (service,))
    result = cursor.fetchone()

    if result:
        encrypted_password = result[0]
        try:
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
            print(f"Senha para '{service}': {decrypted_password}")
        except Exception:
            print(f"Nenhuma senha encontrada para '{service}'.")