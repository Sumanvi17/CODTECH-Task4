from library import Library
from library_item import Book, Magazine, DVD
def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Item")
        print("2. Check Out Item")
        print("3. Return Item")
        print("4. Search Items")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            category = input("Enter category (Book/Magazine/DVD): ")
            item_id = input("Enter unique ID: ")
            if category.lower() == "book":
                item = Book(title, author, category, item_id)
            elif category.lower() == "magazine":
                item = Magazine(title, author, category, item_id)
            elif category.lower() == "dvd":
                item = DVD(title, author, category, item_id)
            else:
                print("Invalid category.")
                continue
            library.add_item(item)
        elif choice == "2":
            item_id = input("Enter item ID to check out: ")
            library.check_out_item(item_id)
        elif choice == "3":
            item_id = input("Enter item ID to return: ")
            library.return_item(item_id)
        elif choice == "4":
            keyword = input("Enter search keyword: ")
            library.search_items(keyword)
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
