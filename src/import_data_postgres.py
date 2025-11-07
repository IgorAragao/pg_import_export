import psycopg2
import sys


## Valida os parâmetros
if len(sys.argv) <= 3:
    print('Argumentos insuficientes!')
    sys.exit()

## Tabela e schema para importar os dados 
TABLE_NAME = sys.argv[1] #(ex: public.clientes)

## Caminho onde o arquivo esta
DIR_PATH = sys.argv[2] #(ex: ~/export_tables/clientes.copy)

## Tipo do arquivo que será importado
TYPE_ARCHIVE = sys.argv[3] #(ex: CSV, BINARY)


def conn_postgres():

    try:
        conn = psycopg2.connect(
                ## ToDo: ajustar conexão para funcionar via parametro sys.argv
                host="127.0.0.1",
                port="5432",
                database="apollo",
                user="postgres"
        )
    except Exception as err:
        print(f"[ERROR] ❌ {err}")
    
    return conn


def conn_close(conn):

    if conn == None:
       print("[ERROR] ❌ Conexão não estabelecida!")
    else:
      print("[INFO] Conexão encerrada!")
      conn.close()  


def cursor_execute(conn):

    cursor = conn.cursor()
    cursor.execute(f"COPY {TABLE_NAME} FROM '{DIR_PATH}' WITH (FORMAT {TYPE_ARCHIVE})")
    #cursor.execute(f"INSERT INTO {TABLE_NAME} (id, nome) SELECT 1,md5(name::text) FROM generate_series (1,50) as name")
    conn.commit() 
    cursor.close()
    print(f"[INFO] 🚀 IMPORT COPY realizado com sucesso para a tabela: {TABLE_NAME}.")


def import_table():

    conn = None
    try:
        conn  = conn_postgres()
        if conn != None:
           cursor_execute(conn)
    except:
        print(f"[ERROR] ❌ Falha ao realizar IMPORT COPY para a tabela: {TABLE_NAME}.")
    finally:
        conn_close(conn)


def main():

    import_table()





if __name__ == "__main__":
    main()
