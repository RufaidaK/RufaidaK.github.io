#This Python file contains functions for managing a book database stored in a text file called "test.txt".
#The contents from the text file can be searched, sorted, displayed, added to, and updated
#The "test.txt" file contains the following books with their author name, ISBN, publication date and the access mode:
# 1, Introduction to Programming, Jones, 35667, 2010
# 0, Java Programming, Richardson, 33333, 2022
# 0, Wed Development, Leach, 66445, 1980
# 1, Game Development, Anderson, 14421, 2000



def menu():
    
    # menu options
    print("\nTo display all books, type 1")
    print("To add a new book, type 2")
    print("To search for a book, type 3")
    print("To sort books by publication date, type 4")
    print("To update a book's details, type 5")
    print("To exit, type 6")

    # Get user input
    choice = input("\nEnter your choice: ")

    # Call the appropriate function based on the user's choice
    if choice == "1":
        Display(book_info)
    elif choice == "2":
        Adding(book_info)
    elif choice == "3":
        Searching(book_info)
    elif choice == "4":
        Sorting(book_info)
    elif choice == "5":
        Updating(book_info)
    elif choice == "6":
        exit()
    else:
        print("Invalid choice. Please try again.")
        menu()

        

def Display(book_info):
    print('\n')
    book_details=[]
    for i in book_info:
        book_details=(i.split(", "))
        Access= book_details[0]
        Book_title= book_details[1]
        Author= book_details[2]
        ISBN= book_details[3]
        Date= book_details[4].strip()

        print (Author, Book_title, ISBN, Date, Access)
    menu()

def Adding(book_info):
    print('\n')
    book_details=[]
    ISBN=input("Enter ISBN: ")
    check=0
    new_book=''
    for i in book_info:
        book_details=(i.split(", "))
        if ISBN == book_details[3]:
            check=1
            
    if check == 1:
        print('Book already present')
    else:
        Book_title= input("Enter the book title: ")
        Date= input("Enter the publication date: ")
        Access= input("Enter access: ")
        Author= input("Enter the Author Lastname: ")
        new_book=Access+', '+Book_title+', '+Author+', '+ISBN+', '+Date+'\n'
        print(new_book)
        book_info.append(new_book)
        print(book_info)
    menu()

def Searching(book_info):
    print('\n')
    book_details=[]
    ISBN=input("Enter ISBN: ")
    check=0
    new_book=''
    for i in book_info:
        book_details=(i.split(", "))
        if ISBN == book_details[3]:
            Access= book_details[0]
            Book_title=book_details[1]
            Author= book_details[2]
            ISBN=book_details[3]
            Date=book_details[4].strip()
            break
        
    if (ISBN == book_details[3]) == True:
        print(Author, Book_title, ISBN, Date, Access)
    else:
        print("Book not present")
    menu()

    
def Sorting(book_info):
    print('\n')
    book_details=[]
    Lower_bound= int(input("Enter a lower bound of year: "))
    Upper_bound= int(input("Enter a upper bound of year: "))
    new_books=[]
    for i in book_info:
        book_details=(i.split(", "))
        if int(book_details[4].strip())>=Lower_bound and int(book_details[4].strip())<=Upper_bound:
            new_books.append(book_details)

    #sorts in descending order of publication date
    new_books=sorted(new_books, key=lambda t:t[4], reverse=True)

    for i in new_books:
        Access= i[0]
        Book_title=i[1]
        Author= i[2]
        ISBN=i[3]
        Date=i[4].strip()
        
        print (Author, Book_title, ISBN, Date, Access)
    menu()
        
def Updating(book_info):
    print('\n')
    ISBN = input("Enter ISBN: ")
    new_book = ''
    book_found = False
    for i in book_info:
        book_details = (i.split(", "))
        if len(book_details) == 5 and ISBN == book_details[3]:
            # Book was found and has the correct number of elements
            book_found = True
            Access = book_details[0]
            if Access == '0':
                print('This books details cannot be changed')
            else:
                book_info.remove(i)
                Book_title = input("Enter the book title: ")
                Date = input("Enter the publication date: ")
                Author = input("Enter the Author Lastname: ")
                book_details[1] = Book_title
                book_details[2] = Author
                book_details[4] = Date + '\n'
                new_book = Access + ', ' + Book_title + ', ' + Author + ', ' + ISBN + ', ' + Date + '\n'
                break
    if book_found:
        print(new_book)
        book_info.append(new_book)
        print(book_info)
    else:
        print("Book not found.")
    menu()
        

    



        
my_files= open("test.txt", "r")
book_info= []
my_file = my_files.readlines()

for myline in my_file:
    book_info.append(myline)
menu()

my_files.close()
