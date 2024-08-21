
# GETS DETAILS OF A USER


def details_of_user(library):
    from connect_mysql import connect_database
    conn = connect_database()
    if conn is not None:
        try:
            name= input("What user are you looking for: ")
            cursor=conn.cursor()
            search_name=name
            query="SELECT name FROM Users WHERE name =%s"
            cursor.execute(query,(search_name,))
            users = cursor.fetchone()
            if  not users:
                    print("User Not found")
            else:
                cursor=conn.cursor()
                update=name
                check_query ="SELECT * FROM Users WHERE name = %s" 
                cursor.execute(check_query,(update, ))
                for row in cursor.fetchall():
                    print (row)
            
        finally:
            cursor.close()
            conn.close()