
from abc import ABC, abstractmethod


# PARENT CLASS
class LibraryItem(ABC):

    total_items = 0

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__available = True

        LibraryItem.total_items += 1

    def is_available(self):
        return self.__available

    def mark_borrowed(self):
        self.__available = False

    def mark_returned(self):
        self.__available = True

    @abstractmethod
    def late_fee(self, days_late):
        pass


# CHILD CLASS 1
class Book(LibraryItem):

    DAILY_RATE = 2

    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Book: {self.title} by {self.author} (ID {self.item_id})"


# CHILD CLASS 2
class Magazine(LibraryItem):

    DAILY_RATE = 1

    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Magazine: {self.title}, Issue {self.issue_number} (ID {self.item_id})"


# CHILD CLASS 3
class DVD(LibraryItem):

    DAILY_RATE = 5

    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"DVD: {self.title}, Duration {self.duration_minutes} minutes (ID {self.item_id})"


# MEMBER CLASS
class Member:

    def __init__(self, name, member_id, max_items=3):
        self.name = name
        self.member_id = member_id
        self.max_items = max_items

        self.__borrowed = []

    def borrow(self, item):

        if not item.is_available():
            raise ValueError("Item is already borrowed!")

        if len(self.__borrowed) >= self.max_items:
            raise ValueError("Borrowing limit reached!")

        item.mark_borrowed()
        self.__borrowed.append(item)

    def return_item(self, item, days_late=0):

        if item not in self.__borrowed:
            raise ValueError("You have not borrowed this item!")

        fee = item.late_fee(days_late)

        item.mark_returned()
        self.__borrowed.remove(item)

        return fee

    def borrowed_titles(self):
        return [item.title for item in self.__borrowed]
