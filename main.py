
from models import LibraryItem, Book, Magazine, DVD, Member


# 1. Create library items
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 15)
dvd = DVD("Python Tutorial", 3, 120)


# 2. Create members
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)


print("========== LIBRARY MANAGEMENT SYSTEM ==========")


# 3. Borrowing a book
print("\n----- BORROWING ITEMS -----")

try:
    alice.borrow(book)
    print("Alice successfully borrowed:", book.describe())

except ValueError as e:
    print("Could not borrow:", e)


# 4. Try borrowing an already borrowed book
try:
    bob.borrow(book)

except ValueError as e:
    print("Bob could not borrow:", e)


# 5. Bob borrows a magazine
try:
    bob.borrow(magazine)
    print("Bob successfully borrowed:", magazine.describe())

except ValueError as e:
    print("Could not borrow:", e)


# 6. Try exceeding borrowing limit
try:
    bob.borrow(dvd)

except ValueError as e:
    print("Bob could not borrow:", e)


# 7. Try returning an item not borrowed by Bob
print("\n----- INVALID RETURN -----")

try:
    bob.return_item(book)

except ValueError as e:
    print("Could not return:", e)


# 8. Demonstrate polymorphism
print("\n----- LATE FEE CALCULATION -----")

items = [book, magazine, dvd]

for item in items:
    print(
        item.describe(),
        "-> Late fee for 3 days: Rs",
        item.late_fee(3)
    )


# 9. Alice returns her book after 3 late days
print("\n----- RETURNING ITEMS -----")

try:
    fee = alice.return_item(book, days_late=3)

    print("Alice returned the book successfully.")
    print("Late fee: Rs", fee)

except ValueError as e:
    print("Could not return:", e)


# 10. Display borrowed items
print("\n----- MEMBER BORROWING DETAILS -----")

print("Alice borrowed items:", alice.borrowed_titles())
print("Bob borrowed items:", bob.borrowed_titles())

# 11. Demonstrate availability
print("\n----- ITEM AVAILABILITY -----")

print("Book available:", book.is_available())
print("Magazine available:", magazine.is_available())
print("DVD available:", dvd.is_available())


# 12. Demonstrate encapsulation
print("\n----- ENCAPSULATION -----")

try:
    print(book.__available)

except AttributeError:
    print("Cannot access private availability directly!")


# 13. Display total items
print("\nTotal items created:", LibraryItem.total_items)
