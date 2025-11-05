import psycopg2


TABLE_NAME = '' # Tabela origem para exportar dados
DIR_PATH = '' # Caminho para a criação do arquivo exportado

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

def export_table():

    cursor = conn_postgres().cursor()
    cursor.execute(f"COPY {TABLE_NAME} TO '{DIR_PATH}' WITH (FORMAT CSV)")


def main():

    export_table()



if __name__ == "__main__":
    main()
