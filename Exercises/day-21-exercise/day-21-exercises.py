# Day 21 Exercise - 30 Days Of Python
# Your task is to split this code into files.

import json
import store
import user_interaction

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """
BOOKS_FILE = 'books.json'


def menu():

    store.create_book_table()
    user_input = input(USER_CHOICE)
    
    while user_input != 'q':
        if user_input == 'a':
            user_interaction.prompt_add_book()
        elif user_input == 'l':
            user_interaction.list_books()
        elif user_input == 'r':
            user_interaction.prompt_read_book()
        elif user_input == 'd':
            user_interaction.prompt_delete_book()

        user_input = input(USER_CHOICE)

menu()