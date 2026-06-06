# List of books
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# 1. Display unavailable books
print("Unavailable Books:")

for book in books:
    if book[1] == 0:
        print(book[0])

# 2. Find books with more than 2 copies
print("\nBooks With More Than 2 Copies:")

for book in books:
    if book[1] > 2:
        print(book[0], "-", book[1])

# 3. Count available books
count = 0

for book in books:
    if book[1] > 0:
        count += 1

print("\nAvailable Books:", count)

# 4. Stop searching once a requested book is found
search_book = input("\nEnter book name to search: ")

for book in books:
    if book[0] == search_book:
        print("Book Found!")
        break
else:
    print("Book Not Found!")