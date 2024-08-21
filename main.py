#1. Create an improved, user-friendly command-line interface (CLI) for the Library Management System 
# with separate menus for each class of the system.

import display_borrow
import borrow_Book
import display_author
import user_details
import display_user
import user_add
import add_book
import borrow
import bookreturn
import display
import search
import new_author
import author_details
library=[]
user=[]
class Book:
    def add_books(library):
        add_book.new_book(library)
    def book_to_borrow(library):
        borrow.get_borrowed_book(library)
    def return_book(library):
        bookreturn.book_return(library)
    def display_all_books(library):
        display.display_books(library)
    def search_for_book(library):
        search.search_book(library)

 
class User:
    def add_user(user):
        user_add.add_new_user(user)
    def get_user_details(library):
        user_details.details_of_user(library)
    def display_all_users(user):
        display_user.display_user(user)
    

class author:
    def add_author(author):
        new_author.new_author_name(author)
    def get_author_display(author):
        author_details.details(author)
    def get_author_details(author):
        display_author.display_authors(author)
        
class borrowed_books:
    def books_borrowed():
        borrow_Book.list_of_borrowed() 
    def display_borrowed_books():
        display_borrow.display_books_borrowed()

def main():
    
   
    while True:
    
        try:
            print("\nWelcome to the Library Management System!\n")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Borrowed Books")
            print("5. Quit\n")
            choice =input("Please make your selection: ")
            if choice =="5":
                print("Goodbye, Thank you for using the Library Management System.")
                break
        
            if choice =="1":
                print("\nBook Operations:\n")
                print("1. Add a new book")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. Search for a book")
                print("5. Display all books")
                book_ops =input("Please enter a selection: ")
                if book_ops =="1":
                    add_book.new_book(library)
                elif book_ops =="2":
                    borrow.get_borrowed_book(library)
                elif book_ops =="3":
                    bookreturn.book_return(library)
                elif book_ops =="4":
                     search.search_book(library)
                elif book_ops =="5":
                    display.display_books(library)
                 
                else:
                    print("Invalid selection")
                
            elif choice =="2":
                print("\nUser Operations:")
                print("1. Add a new user")
                print("2. View user details")
                print("3. Display all users")
                user_ops=input("Please make a selection: ")
                if user_ops =="1":
                    user_add.add_new_user(user)
                elif user_ops =="2":
                    user_details.details_of_user(library)
                elif user_ops =="3":
                    display_user.display_user(user)
                else:
                    print("Invalid selection")
                    
                    
            elif choice =="3":
                print("\nAuthor Operations:")
                print("1. Add a new author")
                print("2. View author details")
                print("3. Display all authors")
                author_ops =input("Please make a selection: ")
                if author_ops =='1':
                    new_author.new_author_name(author)
                elif author_ops =='2':
                    author_details.details(author)
                elif author_ops =='3':
                    display_author.display_authors(author)
                else:
                    print('Invalid Selection')
            elif choice =="4":
                print("1. Add a book to the borrowed list:")
                print("2 Display all borrowed books: ")
                choice =input("Please make your selection: ")
                if choice ==("1"):
                    borrow_Book.list_of_borrowed()
                elif choice ==("2"):
                    display_borrow.display_books_borrowed()
                else:
                    print("Invalid Selection")
                 
                
            
            
        except Exception as e:
            print("An error occered:",e)

main()