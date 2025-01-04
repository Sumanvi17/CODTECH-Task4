from library_item import LibraryItem, Book, Magazine, DVD
class Library:
    def __init__(self):
        self.collection = {}
    def add_item(self, item):
        self.collection[item.item_id] = item
        print(f"Added '{item.title}' (ID: {item.item_id}) to the library.")
    def search_items(self, keyword):
        results = [item for item in self.collection.values() if 
                   keyword.lower() in item.title.lower() or 
                   keyword.lower() in item.author.lower() or 
                   keyword.lower() in item.category.lower()]
        if results:
            print("Search Results:")
            for item in results:
                status = "Available" if not item.checked_out else "Checked Out"
                print(f"{item.title} by {item.author} (Category: {item.category}, Status: {status})")
        else:
            print("No items found.")    def check_out_item(self, item_id):
        if item_id in self.collection:
            self.collection[item_id].check_out()
        else:
            print("Item not found.")
    def return_item(self, item_id):
        if item_id in self.collection:
            self.collection[item_id].return_item()
        else:
            print("Item not found.")

