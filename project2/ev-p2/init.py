import psycopg

conexio = """
                dbname=postgres
                user=user_postgres
                password=pass_postgres
                host=localhost
                port=5432
                """
conn = psycopg.connect(conexio)

try:
    
    cur = conn.cursor()

    id = 1

    cur.execute("""
                INSERT INTO public.test(id, edat, actiu, "desc", nom)
                VALUES (2, 23, true, 'daw2B', 'Frank');
                """)

    #res = cur.fetchone()

    print("ha afegit un insert")

    conn.commit()

except Exception as e:
    print (f"Hi ha hagut un error {e}")
    conn.rollback()

finally:
    conn.close()