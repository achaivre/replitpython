from typing import Dict


def input_action() -> str:
  action = input('view [books], show [author], [quit]> ').lower()
  commands = ['books', 'author', 'quit']
  while action not in commands:
    print('Please provide a valid action.')
    action = input('view [books], show [author], [quit]> ').lower()
  return action

def print_books(book_authors: Dict[str, str]) -> None:
    for author in book_authors.keys():
      print('-', author)


def input_book(book_authors: Dict[str, str]) -> str:
  while True:
    action = input('book> ')
    if action in book_authors.keys():rep
      return action
    else:
      print('Please provide a valid book.')


def print_author(book_authors: Dict[str, str]) -> None:
  action = input_book(book_authors)
  for book, author in book_authors.items():
    if action.lower() == book.lower():
      print(author)


def main() -> None:
    book_authors = {
        'Harry Potter': 'JK Rowling',
        'Effective Testing with RSpec 3': 'Myron Marston',
        'Automate the Boring Stuff': 'Al Sweigart',
        'Quiet': 'Susan Cain',
        'Peak': 'Anders Ericsson',
    }

    while True:
        action = input_action()
        if action == "books":
            print_books(book_authors)
        elif action == "author":
            print_author(book_authors)
        else:
            break


if __name__ == "__main__":
    main()
