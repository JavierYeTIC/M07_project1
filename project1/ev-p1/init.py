import psycopg

conexio = """
            dbname=postgres
            user=user_postgres
            password=pass_postgres
            host=localhost
            port=5432
            """

conn = psycopg.connect(conexio)

print(conn)