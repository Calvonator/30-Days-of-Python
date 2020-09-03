reading_list = []



def addBookToList():
    title = input("Please enter the book's title: ")
    author  = input("Please enter the book's author: ")
    year = input("Please enter the book's release year: ")
    book = (title, author, year)
    reading_list.append(book)
    
def displayBookList():
    for book in reading_list:
        print(f"Title: {book[0]}\nAuthor: {book[1]}\nYear: {book[2]}\n\n\n")



while True:
    choice = input("[1] Add a book\n[2] Show Reading List\n[q] Quit\n\n")

    if choice == "1":
        addBookToList()

    elif choice == "2":
        displayBookList()

    elif choice == "q":
        break


    