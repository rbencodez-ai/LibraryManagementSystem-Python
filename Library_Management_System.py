def main_menu():
    print("Library Management System\n")
    print("""1. Create a Library
2. Add Book
3. Display Books
4. Get Number of Books
5. Exit the Program\n""")
    
class Library:
    def __init__(self, title, books):
        self.title = title.strip()
        self.books = books.strip().split()
        self.number_of_books = len(self.books)

    def display_books(self):
        if not self.books:
            print("\nNo books in the library yet!\n")
        else:
            print(f"\nBooks in your Library: {self.books}\n")

    def add_book(self, book):
        self.books.append(book)
        self.number_of_books = len(self.books)
        print(f"\n\'{book}\' added Successfully to the Library!")
        print(f"Updated List Of Books: {self.books}\n")

    def get_number_of_books(self):
        return self.number_of_books

my_library = None
while True:
    main_menu()
    try:
        user_choice = int(input("Enter the numbers to perform the above operations: ").strip())
        if user_choice < 1 or user_choice > 5:
            raise Exception("Invalid Input! (Enter Numbers between 1 and 5)")
    except ValueError:
        print("\nError Message: Only Integers are Allowed\n")
    except Exception as e:
        print(f"Error: {e}")
    else:
        if user_choice == 1:
            my_library = Library(input("\nEnter the name of your Library: "), input("Enter some books to make a Library (Use Spaces to add multiple Books): "))
            print(f"\n\'{my_library.title}\' Library Created Successfully!\n")

        elif user_choice == 2:
            if my_library is None:
                print("\nError Message: You will have to create a Library First to \'Add Books\'\n")
            else:
                my_library.add_book(input("\nEnter the name of book: ").strip())

        elif user_choice == 3:
            if my_library is None:
                print("\nError Message: You will have to create a Library First to \'Display Books\'\n")
            else:
                my_library.display_books()

        elif user_choice == 4:
            if my_library is None:
                print("\nError Message: You will have to create a Library First to \'Get Number of Books\'\n")
            else:
                print(f"\nTotal Number of Books in your Library: {my_library.get_number_of_books()}\n")

        elif user_choice == 5:
            print("\nThanks for using our Program!")
            print("Exiting the Program......\n")
            break