class Book:
    def_init_(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

        def mark_as_borrowed (self):
            if not self.is_borrowed:
                self.is_borrowed = True
                return True
                return False # Book is already borrowed

                def mark_as_returned(self):
                    if self.is_borrowed:
                        self.is_borrowed = False
                        return True
                        return False # Book was not borrowed

              class LibraryMember:
                def_init_(self, name, member_id):
                    self.name = name
                    self.member_id = member_id
                    self.borrowed_books = []  

                    def borrowed_books(self,book):
                        if not book.is_borrowed:
                            if book.mark_as_borrowed():
                                self.borrowed_books.append(book)  
                                print(f"{self.name} borrowed '{book.title}' by {book.author}.") 
                                else:
                                    print (f"sorry, '{book.title}' is already borrowed.") 
                                    
                                    def return_book(self,book):
                                        if book in self.borrowed_books:
                                            if book.mark_as_returned():
                                                self.borrowed_books.remove(book)
                                                print(f"{self.name} returned '{book.title}' by {book.author}.")
                                                else:
                                                print (f" '{book.title}' was not borrowed.")
                                                else(f"{self.name} has not been borrowed '{book.title}'.")

                                                def list_borrowed_books(self):
                                                    if self.borrowed_books:
                                                        print (f"{self.name} has borrowed the following books:")
                                                        for book in self.list_borrowed_books
                                                        print(f"-'{book.title}' by {book.author}")
                                                        else:
                                                            print (f"{self.name} has not borrowed any books.")

                                                            def main():
                                                                book1 = Book("The River and The Source", " Margret Ogolla")
                                                                book2 = Book(" Wonderland", "Lewis Carroll")
                                                                book3 = Book("Pride and Prejudice", "Jane Austen")

                                                                member = LibraryMember("Miriam", "001")


                                                                while True:

                                                                    print("\nLibrary Management System")
                                                                    print("1. Borrow a Book")
                                                                    print("2. Return a Book")
                                                                    print("3. List Borrowed Books")
                                                                    print("4. Exit")

                                                                    choice = input("Enter your choice (1-4):")
if choice =="1"
# Borrow a book
book_title = input("The River and the Source:")

if book_title == book1.title:
    member.borrow_book(book1)
    elif book_title == book2.title:
        member.borrow_book(book2)
        elif book_title == book3.title:
            member.borrow_book(book3)

            else:
                print("Book not found.")

                elif choise == "2":
                    #Return a book
                    book_title = input(Wonderland:)
                    if book_title == book1.title:
                        member.return_book(book1)

                        elif book_title == book2.title:
                            member.return_book(book2)
                  elif book_title == book3.title
                  member. return_book(book3)  

                  else:
                    print("Book not found.")   

                    elif choice =="3":
                        # List borrowed books
                        member.list_borrowed_book()

                        elif choice =="4":
                            # Exit the program
                            print("Exiting the Library Management system.")
                            break

                            else:
                                print("Invalid choice. Please try again.")

                                # Run the main program

                                if __name__ == "__main__":
                                    main()

                            



                                        