#DISPLAYS ALL AUTHORS


def display_authors(author):
    from connect_mysql import connect_database
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            query ="SELECT * FROM Authors"
            cursor.execute(query)
            for row in cursor.fetchall():
                print (row)
        finally:
            cursor.close()
            conn.close()