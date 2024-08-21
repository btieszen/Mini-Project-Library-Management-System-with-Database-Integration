#ADDS A BOOK

def new_book(library):
    from connect_mysql import connect_database 
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            title =input("What is the title of the book: ")
            isbn=input("What is the ISBN number: ")
            publication_date=input("When was the year the book was published: ")
            genre=input("What is the genre of the book: ")
            availability=("available")
            author_id=input("What is the authors ID: ")
            
            cursor=conn.cursor()
            search_author=author_id
            query="SELECT id FROM authors WHERE id =%s"
            cursor.execute(query,(search_author,))
            users = cursor.fetchone()
            if  not users:
                    print("Author Not found")
            else:
                cursor=conn.cursor()
                added_book=(title),(isbn),(publication_date),(genre),(availability),(author_id)
                query = "INSERT INTO Books (title,isbn,publication_date,genre,availability,author_id) VALUES (%s,%s,%s,%s,%s,%s)"
                cursor.execute(query,added_book)
                conn.commit()
                print("New Book has been added")
           
        finally:
            cursor.close()
            conn.close()
   
