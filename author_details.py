#GETS DETAILS OF AN AUTHOR



def details(author):
    
    from connect_mysql import connect_database
    conn = connect_database()
    if conn is not None:
        try:
            name= input("What Author are you looking for: ")
            cursor=conn.cursor()
            search_author=name
            query="SELECT name FROM Authors WHERE name =%s"
            cursor.execute(query,(search_author,))
            users = cursor.fetchone()
            if  not users:
                    print("Author Not found")
            else:
                cursor=conn.cursor()
                update=name
                check_query ="SELECT * FROM Authors WHERE name = %s" 
                cursor.execute(check_query,(update, ))
                for row in cursor.fetchall():
                    print (row)
             
        finally:
            cursor.close()
            conn.close()