


class booklist():

    def __init__(self):
        self.booklist = []
        self.load_books()


    def load_books(self):

        try:
            with open('/home/calvin/Documents/gitrepos/30-Days-of-Python/Day 14 Project/booklist.csv', 'r') as bl:
                b = bl.readlines()
                
                for row in b:
                    book = row.strip().split(',')
                    self.booklist.append(book)

        except:
            print("Book list is currently empty")


    def save_books(self):

        with open('booklist.csv', 'w') as bl:
            for b in self.booklist:
                details = f"{b[0].strip()}, {b[1].strip()}, {b[2].strip()}, {b[3].strip()}\n"
                bl.write(details)


    def add_book(self, book_details):

        self.booklist.append(book_details)
        self.save_books()
    
    def del_book(self, title):

        for i, b in enumerate(self.booklist):
            if b[0].lower() == title.lower():
                del self.booklist[i]
        
        self.save_books()

    def print_list(self):
        ctr = 1
        for b in self.booklist:
            print(f'\nBook#{ctr}\nTitle: {b[0]}   Author: {b[1]}  Year: {b[2]}  Read: {b[3]}\n')
            ctr += 1

    def search(self, title):
        ctr = 1
        for b in self.booklist:
            if b[0].lower() == title.lower():
                print(f'\nBook#{ctr}\nTitle: {b[0]}   Author: {b[1]}  Year: {b[2]}  Read: {b[3]}\n')
            ctr += 1

    def mark_read(self, title):

        for i, b in enumerate(self.booklist):
            if b[0].lower() == title.lower():
                self.booklist[i][3] = 'y'   #Tuples are immutable; change from tuples in list to list of lists


booklist = booklist()

while True:
    choice = input("[1] Add book\n[2] Print booklist\n[3] Search for Book\n[4] Marks as Read\n[5] Delete Book\n[Q] Quit\n")

    if choice == '1':
        title, author, year = input("Please enter the title, author and year of the book seperated by commas: \n").split(',')
        read = input("Have you read this book yet? (y/n)")
        book_details = (title, author, year, read)
        booklist.add_book(book_details)

    elif choice == '2':
        booklist.print_list()

    elif choice == '3':
        to_search = input("Enter the title of the book you wish to find:\n")
        booklist.search(to_search)

    elif choice == '4':
        title = input("Enter the title of the book to mark as read:\n")
        booklist.mark_read(title)

    elif choice == '5':
        title = input("Enter the title of the book to delete:\n")
        booklist.del_book(title)

    elif choice.lower() == 'q':
        break

