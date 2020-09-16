import json


class booklist():

    def __init__(self):
        self.booklist = []
        self.load_books()


    def load_books(self):

        try:
            with open('booklist.json', 'r') as bl:
                self.booklist = json.load(bl)
                
                #for row in b:
                 #   book = row.strip().split(',')
                  #  self.booklist.append(book)

        except:
            print("Book list is currently empty")
            with open("booklist.json", "w") as bl:
                emptyList = []
                json.dump(emptyList, bl)


    def save_books(self):

        with open('booklist.json', 'w') as bl:
            json.dump(self.booklist, bl, indent = 4)


    def add_book(self, book_details):

        self.booklist.append(book_details)
        self.save_books()
    
    def del_book(self, title):

        for i in range(len(self.booklist)):
            if self.booklist[i]["title"].lower() == title.lower():
                del self.booklist[i]
        
        self.save_books()

    def print_list(self):
        ctr = 1
        for b in self.booklist:
            print(f'\nBook#{ctr}\nTitle: {b["title"]}   Author: {b["author"]}  Year: {b["year"]}  Read: {b["read"]}\n')
            ctr += 1

    def search(self, title):
        ctr = 1
        for b in self.booklist:
            if b["title"].lower() == title.lower():
                print(f'\nBook#{ctr}\nTitle: {b["title"]}   Author: {b["author"]}  Year: {b["year"]}  Read: {b["read"]}\n')
            ctr += 1

    def mark_read(self, title):

        for i in range(len(self.booklist)):
            if self.booklist[i]["title"].lower() == title.lower():
                self.booklist[i]["read"] = 'y'   

        self.save_books()


booklist = booklist()

while True:
    choice = input("[1] Add book\n[2] Print booklist\n[3] Search for Book\n[4] Marks as Read\n[5] Delete Book\n[Q] Quit\n")

    if choice == '1':
        title, author, year = input("Please enter the title, author and year of the book seperated by commas: \n").split(',')
        read = input("Have you read this book yet? (y/n)")

        book_details = {
            "title": title, 
            "author": author, 
            "year": year, 
            "read": read
        }

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

