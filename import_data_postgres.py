import psycopg2


TABLE_NAME = '' # Adicionar nome da tabela distino
DIR_PATH = '' # Adicionar caminho do arquivo a ser importado
TYPE_ARCHIVE = '' # Tipo do arquivo a ser importado (BINARY, CSV, etc)


def conn_postgres():

    try:
        conn = psycopg2.connect(
                host="<ip>",
                port="<port>",
                database="<db>",
                user="<user>"
        )
    except Exception as err:
        print(f"Error: {err}")
    
    return conn


def conn_close(conn):

    if conn == None:
       print("Conexão não estabelecida!")
    else:
      print("Conexão encerrada!")
      conn.close()  


def cursor_execute(conn):

    cursor = conn.cursor()
    cursor.execute(f"COPY {TABLE_NAME} FROM '{DIR_PATH}' WITH (FORMAT {TYPE_ARCHIVE}")
    #cursor.execute(f"INSERT INTO {TABLE_NAME} (id, nome) SELECT 1,md5(name::text) FROM generate_series (1,50) as name")
    conn.commit() 
    cursor.close()
    print(f"COPY realizado com sucesso para a tabela {TABLE_NAME}!")


def import_table():

    conn = None
    try:
        conn  = conn_postgres()
        if conn != None:
           cursor_execute(conn)
    except:
        print(f"Falha ao realizar COPY para a tabela {TABLE_NAME}.")
    finally:
        conn_close(conn)


def main():

    import_table()





if __name__ == "__main__":
    main()
