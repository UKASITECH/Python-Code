import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self, books):
        self.books = books

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            return f"You have borrowed '{book_name}'. Please return it on time."
        else:
            return f"Sorry, '{book_name}' is not available."

    def return_book(self, book_name):
        self.books.append(book_name)
        return f"Thank you for returning '{book_name}'. Hope you enjoyed reading it!"

    def display_books(self):
        return '\n'.join(self.books)


# Function to update the list of available books in the GUI
def update_books_display():
    available_books = library.display_books()
    books_text.delete(1.0, tk.END)
    books_text.insert(tk.END, available_books)

# Function to handle borrowing a book
def borrow_book():
    book_name = book_entry.get()
    result = library.borrow_book(book_name)
    messagebox.showinfo("Result", result)
    update_books_display()

# Function to handle returning a book
def return_book():
    book_name = book_entry.get()
    result = library.return_book(book_name)
    messagebox.showinfo("Result", result)
    update_books_display()

# Initialize the library and the Tkinter window
library_books = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "The Catcher in the Rye", "Pride and Prejudice"]
library = Library(library_books)

root = tk.Tk()
root.title("Library Management System")

# Create the GUI elements
title_label = tk.Label(root, text="Library Management System", font=("Arial", 16))
title_label.pack(pady=10)

books_label = tk.Label(root, text="Available Books:", font=("Arial", 12))
books_label.pack()

books_text = tk.Text(root, height=8, width=50)
books_text.pack(pady=10)
update_books_display()

book_label = tk.Label(root, text="Enter Book Name:", font=("Arial", 12))
book_label.pack()

book_entry = tk.Entry(root, font=("Arial", 12))
book_entry.pack(pady=5)

borrow_button = tk.Button(root, text="Borrow Book", font=("Arial", 12), command=borrow_book)
borrow_button.pack(pady=5)

return_button = tk.Button(root, text="Return Book", font=("Arial", 12), command=return_book)
return_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
