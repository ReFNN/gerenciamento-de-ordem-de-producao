import sqlite3
import sys
import os


# FUNÇÃO PARA CRIAR O BANCO DE DADOS CASO NÃO TENHA UM...
def create_db():
    conn = sqlite3.connect("ordens.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ordens (
            id INTEGER PRIMARY KEY,
            produto TEXT,
            quantidade INTEGER,
            data_entrega DATE,
            status TEXT
        )
    """
    )
    conn.commit()
    conn.close()


# FUNÇÃO PARA REGISTRAR UMA NOVA ORDEM...
def register_order():
    produto = input("Nome do produto: ")

    try:
        quantidade = int(input("Quantidade desejada: "))
    except:
        print("\nA quantidade deve ser somente números!\n")
        goto_menu()

    data_entrega = input("Data de entrega (DD-MM-YYYY): ")

    conn = sqlite3.connect("ordens.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ordens (produto, quantidade, data_entrega, status) VALUES (?, ?, ?, ?)",
        (produto, quantidade, data_entrega, "1"),
    )
    conn.commit()
    conn.close()
    goto_menu()


# FUNÇÃO PARA MOSTRAR TODAS AS ORDENS REGISTRADAS...
def list_orders():
    conn = sqlite3.connect("ordens.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ordens")
    ordens = cursor.fetchall()
    conn.close()

    if not ordens:
        print("\nNenhuma ordem de produção registrada.")
        goto_menu()
    else:
        print("\n")
        print("LISTA DE PRODUTOS REGISTRADOS:")
        for ordem in ordens:
            print(
                f"-- ID: {ordem[0]}, Produto: {ordem[1]}, Quantidade: {ordem[2]}, Data de Entrega: {ordem[3]}, Status: {ordem[4]}\n"
            )
        goto_menu()


# FUNÇÃO PARA VERIFICAR SE O PRODUTO PODE OU NÃO SER PRODUZIDO
def check_product():
    ## NÃO ENTENDI COMO DEVERIA SER FEITO ESSA PARTE.
    ## SE DEVERIAMOS CRIAR OS PRODUTOS PREVIAMENTE OU SEI LÁ... =/
    ## PERGUNTEI PELO WHATSAPP MAS AINDA NÃO TIVE RESPOSTA.

    product = input("Nome do produto: ")
    try:
        amount = int(input("Quantidade desejada: "))
    except:
        print("\nA quantidade deve ser somente números!\n")
        goto_menu()

    # if algumacoisa():
    #     print("Produção possível.")
    # else:
    #     print("Produção impossível devido à falta de materiais.")
    goto_menu()


# FUNÇÃO PARA ATUALIZAR O STATUS DA ORDEM...
def update_status(id_ordem, status):
    conn = sqlite3.connect("ordens.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE ordens SET status = ? WHERE id = ?", (status, id_ordem))
    conn.commit()
    conn.close()
    print("Status de produto atualizado com sucesso!")
    goto_menu()


# FUNÇÃO PARA VISUALIZAR RELATÓRIO DE PRODUÇÃO...


def production_report():
    conn = sqlite3.connect("ordens.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ordens WHERE status = "1"')
    ordens_andamento = cursor.fetchall()
    cursor.execute('SELECT * FROM ordens WHERE status = "2"')
    ordens_concluidas = cursor.fetchall()
    conn.close()
    
    clear_screen()
    print("Ordens em andamento:")
    for ordem in ordens_andamento:
        print(
            f"ID: {ordem[0]}, Produto: {ordem[1]}, Quantidade: {ordem[2]}, Data de Entrega: {ordem[3]}"
        )

    print("\nOrdens concluídas:")
    for ordem in ordens_concluidas:
        print(
            f"ID: {ordem[0]}, Produto: {ordem[1]}, Quantidade: {ordem[2]}, Data de Entrega: {ordem[3]}"
        )

    goto_menu()


# FUNÇÃO PARA LIMPAR O CONSOLE


def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")


# FUNÇÃO PARA VERIFICAR SE DESEJA CONTINUAR OU ENCERRAR...
def goto_menu():
    print("\nDeseja voltar ao menu principal ou encerrar?")
    print("1. Menu principal")
    print("2. Encerrar")

    escolha1 = input("\nEscolha uma opção: ")
    if escolha1 == "1":
        main()
    elif escolha1 == "2":
        sys.exit()
    else:
        print("\nOpção inválida!")
        goto_menu()


def main():
    create_db()

    while True:
        # limpando console
        clear_screen()

        print("Sistema de Gerenciamento de Ordens de Produção")
        print("1. Registrar nova ordem de produção")
        print("2. Listar todas as ordens de produção")
        print("3. Verificar disponibilidade de material")
        print("4. Atualizar status de uma ordem de produção")
        print("5. Visualizar relatórios de produção")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            register_order()
        elif escolha == "2":
            list_orders()
        elif escolha == "3":
            check_product()
        elif escolha == "4":
            id_ordem = int(input("ID da ordem a ser atualizada: "))
            status = input("Novo status (Em andamento/Concluída): ")
            update_status(id_ordem, status)
        elif escolha == "5":
            production_report()
        elif escolha == "6":
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
