# Gets a List of all borrowed books
import re
def list_of_borrowed():
    
    from connect_mysql import connect_database 
    conn = connect_database()
    if conn is not None:
        try:
            
            name=input("User Id: ")
            cursor=conn.cursor()
            search=name
            query="SELECT id FROM Users WHERE id =%s"
            cursor.execute(query,(search,))
            users = cursor.fetchone()
            if  not users:
                    print("User Not found")
            book=input("Book Id: ")
            cursor=conn.cursor()
            search_book=book
            query="SELECT id FROM Books WHERE id =%s"
            cursor.execute(query,(search_book,))
            users = cursor.fetchone()
            if  not users:
                    print("Book Not found")
            borrow_date= input("Check out date,(enter as Year,month,day(2010-10-10))")
            if re.search(r'\d{4}-\d{2}-\d{2}', borrow_date):
                print()
            else: 
                print("invalid format please enter as ####_##_##")
                borrow_date = input("Enter date as (year-month-day, 2024-10-11) ")
                
            return_date=input("Retuned Date,),(enter as Year,month,day(2010-10-10))")
            if re.search(r'\d{4}-\d{2}-\d{2}', return_date):
                print()
            else: 
                print("invalid format please enter as ####_##_##")
                return_date=input("Retuned Date,),(enter as Year,month,day(2010-10-10))")
            
            cursor=conn.cursor()
            borrowed=(name),(book),(borrow_date),(return_date)
            query = "INSERT INTO Borrowed_books (user_id,book_id,borrow_date,return_date)VALUES (%s,%s,%s,%s)"
            cursor.execute(query,borrowed)
            conn.commit()
            print("New Book has been added")
            
        finally:
            cursor.close()
            conn.close()
            
            