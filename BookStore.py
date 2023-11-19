from AVLTree import AVLTree


class Book:
    def __init__(self, key, title, author):
        self.key = key
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book {self.key}: {self.title} by {self.author}"
    

class BookStore:
    def __init__(self):
        self.avl_tree = AVLTree()

    def add_book(self, title, author, isbn):
        book = Book(key=isbn,title=title,author=author)
        self.avl_tree.insert_key_value_pair(isbn, book)
    
    def remove_book(self, isbn):
        self.avl_tree.delete_key(isbn)

    def search_book(self, isbn):
        return self.avl_tree.search_key(isbn)
    
    def print_books(self):
        self.avl_tree.inorder()


book_store = BookStore()

book_store.add_book("The Hobbit", "J.R.R. Tolkien", 9780261102217)
book_store.add_book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 9780747532743)
book_store.add_book("The Little Prince", "Antoine de Saint-Exupery", 9780156012195)
book_store.add_book("Alice's Adventures in Wonderland", "Lewis Carroll", 9780141439761)
book_store.add_book("Dream of the Red Chamber", "Cao Xueqin", 9780140443714)
book_store.add_book("And Then There Were None", "Agatha Christie", 9780312330873)
book_store.add_book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 9780064471046)
book_store.add_book("She: A History of Adventure", "H. Rider Haggard", 9780199536425)

def run():
    while True:
        print("Welcome to the Book Store!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Print all books")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = int(input("Enter the ISBN of the book: "))
            book_store.add_book(title, author, isbn)
        elif choice == 2:
            isbn = int(input("Enter the ISBN of the book: "))
            book_store.remove_book(isbn)
        elif choice == 3:
            isbn = int(input("Enter the ISBN of the book: "))
            book = book_store.search_book(isbn)
            if book is not None:
                print(book)
            else:
                print("Book not found!")
        elif choice == 4:
            book_store.print_books()
        elif choice == 5:
            break
        else:
            print("Invalid choice!")

        
    
if __name__ == "__main__":
    run()


