
book_wanted = input("Enter the book you are looking for: ")

books_checked = 0
book_found = False

while True:
    book_search = input("Enter the next book (or type 'No More Books' if there are no more): ")

    if book_search == "No More Books":
        break

    books_checked += 1

    if book_search == book_wanted:
        book_found = True
        print(f"You checked {books_checked} books and found it.")
        break

if not book_found:
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")
