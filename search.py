#SEARCHES FOR A PARTICULAR BOOK


def search_book(library):
    from connect_mysql import connect_database
    conn = connect_database()
    if conn is not None:
        try:
            title= input("What book are you searching for: ")
            cursor=conn.cursor()
            search_title=title
            query="SELECT title FROM Books WHERE title =%s"
            cursor.execute(query,(search_title,))
            books = cursor.fetchone()
            if  not books:
                    print("Book Not found")
            else:
                cursor=conn.cursor()
                update=title
                check_query ="SELECT * FROM Books WHERE title = %s" 
                cursor.execute(check_query,(update, ))
                for row in cursor.fetchall():
                    print (row)
            
        finally:
            cursor.close()
            conn.close()

 