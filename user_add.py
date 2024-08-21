 
 #ADDS A NEW USER
 

def add_new_user(user):
 
    from connect_mysql import connect_database 
    conn = connect_database()
    if conn is not None:
        try:
            cursor=conn.cursor()
            name=input("What is the new user name: ")
            library_id=input("What is their new library id: ")
            new_user=(name),(library_id)
            query = "INSERT INTO Users (name,library_id) VALUES (%s,%s)"
            cursor.execute(query,new_user)
            conn.commit()
            print("New member has been added")
        finally:
            cursor.close()
            conn.close()