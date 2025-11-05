# pg_import_export

Projeto criado no intuito de estudar conexão com o Postgres via psycopg utilizando Python.


## Requisitos

- python3 ou superior
- psycopg2 - `python3-psycopg2`


## Como utilizar?

- Script `export_data_postgres.py`

```bash
python3 export_data_postgres.py <schema.table> </path/to/save/file/name_file> <copy_type>

## Exemplo
# python3 export_data_postgres.py public.cliente /var/lib/postgresql/cliente.copy BINARY
```


- Script `import_data_postgres.py`

```bash
python3 import_data_postgres.py <schema.table> </path/file/<name_file> <copy_type>

## Exemplo
# python3 import_data_postgres.py public.cliente /var/lib/postgresql/cliente.copy BINARY
```

## Exemplos de log

#### Exportação de dados

- Sucesso

```bash
igor@apollo11:~/Documentos/estudo/python/example_export_import_postgres$ python3 export_data_postgres.py public.tt /var/lib/postgresql/tt_csv.copy CSV
[INFO] 🚀 EXPORT COPY realizado com sucesso para a tabela: public.tt.
[INFO] Conexão encerrada!
```

- Erro

```bash
igor@apollo11:~/Documentos/estudo/python/example_export_import_postgres$ python3 export_data_postgres.py public.tt /var/lib/postgresql/tt_csv.copy CSV
[ERROR] ❌ connection to server at "127.0.0.1", port 5432 failed: FATAL:  banco de dados "estudo" não existe

[ERROR] ❌ Falha ao realizar EXPORT COPY para a tabela: public.tt.
[ERROR] ❌ Conexão não estabelecida!
```

#### Importação de dados

- Sucesso

```bash
igor@apollo11:~/Documentos/estudo/python/example_export_import_postgres$ sudo python3 import_data_postgres.py public.tt_import /var/lib/postgresql/tt_binary.copy BINARY
[INFO] 🚀 IMPORT COPY realizado com sucesso para a tabela: public.tt_import.
[INFO] Conexão encerrada!
```

- Erro

```bash
igor@apollo11:~/Documentos/estudo/python/example_export_import_postgres$ python3 import_data_postgres.py public.tt /var/lib/postgresql/tt.copy BINARY
[ERROR] ❌ connection to server at "127.0.0.1", port 5432 failed: FATAL:  banco de dados "estudo" não existe

[ERROR] ❌ Falha ao realizar IMPORT COPY para a tabela: public.tt.
[ERROR] ❌ Conexão não estabelecida!
```
