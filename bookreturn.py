# returns book

def book_return(library):
    from connect_mysql import connect_database 
    conn = connect_database()
    if conn is not None:
        try:
            title= input("Enter the book that is now available: ")
            cursor=conn.cursor()
            update_title=title
            check_query="SELECT title FROM Books WHERE title =%s"
            cursor.execute(check_query,(update_title,))
            books = cursor.fetchone()
            if  not books:
                print("Book Not found")
            else:
                cursor=conn.cursor()
                update="Available",(title)
        
                query = "UPDATE Books SET availability = %s WHERE title = %s"
                cursor.execute(query,update)
                conn.commit()
                print(f"{title} has been change to Available")
        finally:
            cursor.close()
            conn.close 