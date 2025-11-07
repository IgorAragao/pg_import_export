import psycopg2
import sys


## Valida os parâmetros
if len(sys.argv) <= 2:
    print('Argumentos insuficientes!')
    sys.exit()


## Tabela e schema para exportar os dados (ex: public.clientes)
TABLE_NAME = sys.argv[1]

## Caminho do diretorio onde o arquivo será salvo e o nome do arquivo
DIR_PATH = sys.argv[2] #(ex: ~/export_tables/clientes.copy)

## Tipo do arquivo que será exportado
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
    cursor.execute(f"COPY {TABLE_NAME} TO '{DIR_PATH}' WITH (FORMAT {TYPE_ARCHIVE})")
    conn.commit() 
    cursor.close()
    print(f"[INFO] 🚀 EXPORT COPY realizado com sucesso para a tabela: {TABLE_NAME}.")


def export_table():

    conn = None
    try:
        conn  = conn_postgres()
        if conn != None:
           cursor_execute(conn)
    except:
        print(f"[ERROR] ❌ Falha ao realizar EXPORT COPY para a tabela: {TABLE_NAME}.")
    finally:
        conn_close(conn)


def main():

    export_table()


if __name__ == "__main__":
    main()
