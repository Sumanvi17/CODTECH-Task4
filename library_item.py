from datetime import datetime, timedelta
class LibraryItem:
    def __init__(self, title, author, category, item_id):
        self.title = title
        self.author = author
        self.category = category
        self.item_id = item_id
        self.checked_out = False
        self.due_date = None
    def check_out(self, days=14):
        if not self.checked_out:
            self.checked_out = True
            self.due_date = datetime.now() + timedelta(days=days)
            print(f"Item '{self.title}' checked out. Due date: {self.due_date.strftime('%Y-%m-%d')}")
        else:
            print(f"Item '{self.title}' is already checked out.")
    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            overdue_days = (datetime.now() - self.due_date).days
            fine = max(0, overdue_days * 1)
            self.due_date = None
            print(f"Item '{self.title}' returned. Fine: ${fine:.2f}")
        else:
            print(f"Item '{self.title}' is not checked out.")
class Book(LibraryItem):
    pass
class Magazine(LibraryItem):
    pass
class DVD(LibraryItem):
    pass

