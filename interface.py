# INTERFACE SIMPLES NO TERMINAL MESMO 
from getpass import getpass
from database import setup_database, get_connection
from operation import add_password, get_password, get_or_create_key

def main():
    setup_database()

    print("Bem vindo à SECwallet!")
    key_pass = getpass("Digite sua senha mestra: ")
    fernet = get_or_create_key(key_pass)

    while True:
        print("\OPÇÕES:")
        print("1. Adicionar nova senha")
        print("2. Recuperar senha")
        print("3. Sair")
        choice = input("Escolha uma opção (1-3): ")

        # conectar com DB para cada operaçao
        conn = get_connection()

        if choice == "1":
            service = input("Digite o nome do serviço (ex: 'email'): ")
            password = getpass("Digite a senha para o serviço: ")
            add_password(service, password, fernet, conn)

        elif choice == "2":
            service = input("Digte o nome do serviço: ")
            get_password(service, fernet, conn)

        elif choice == "3":
            print("Saindo... Até mais :) ")
            conn.close()
            break

        else:
            print("Opção inválida! Tente novamente (1-3).")

        conn.close()

if __name__ == "__main__":
    main()