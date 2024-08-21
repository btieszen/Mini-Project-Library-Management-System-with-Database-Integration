#ADDS A NEW AUTHOR AND THEIR INFORMATION


def new_author_name(author):
    from connect_mysql import connect_database 
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            name=input("What is the name of the author you want to add: ")
            BirthPlace=input("What city was the author born: ")
            BirthYear=input("What Year were they born: ")
            
            cursor=conn.cursor()
            added_author=(name),(BirthPlace),(BirthYear)
            query = "INSERT INTO Authors (name,Birthplace,BirthYear) VALUES (%s,%s,%s)"
            cursor.execute(query,added_author)
            conn.commit()
            print("New Author has been added")
        
        finally:
            cursor.close()
            conn.close()
   
    