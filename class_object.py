
"""
Encapsulation: Bundling the data (attributes) & methods (functions) that operate on the data into a single unit(class).
Abstraction: Hiding complex details and showing only the necessary parts to the outside world.
Inheritance: Creating a new class using properties and methods of an existing class.
Polymorphism: Using a single interface to represent different data types or classes.
"""

# Base Class for all types of books
# class definition
class Book:
    def __init__(self, title, author, price):
        # Encapsulation of properties (private using __)
        self.__title = title
        self.__author = author
        self.__price = price

    # Getter and Setter for Encapsulation
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be positive!")

    # Method to show book details (Abstraction)
    def show_details(self):
        print(f"Title: {self.__title}, Author: {self.__author}, Price: {self.__price}")

# Derived class (Inheritance) for printed books
class PrintedBook(Book):
    def __init__(self, title, author, price, weight):
        # Inherit the constructor from Book
        super().__init__(title, author, price)
        self.__weight = weight  # Additional attribute for printed books

    # Overriding the method (Polymorphism) to include weight in details
    def show_details(self):
        super().show_details()
        print(f"Weight: {self.__weight} kg")

# Derived class for e-books (Inheritance)
class Ebook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.__file_size = file_size

    def show_details(self):
        super().show_details()
        print(f"File size: {self.__file_size} MB")


"""
In Python, the construct if __name__ == "__main__": is commonly used to ensure that certain code is executed only when 
the script is run directly, and not when it is imported as a module into another script. It’s a very important pattern 
in Python that helps separate the script’s behavior when it is run as a standalone program versus when it is used as a 
module.

Explanation:
Every Python script has a special built-in variable called __name__.
When a script is executed directly (e.g., python script.py), the __name__ variable is set to "__main__".
When a script is imported as a module in another script (e.g., import script), the __name__ variable is set to the name
of the script (e.g., script).
So, by using if __name__ == "__main__":, you are checking if the current script is being run directly, and if it is, 
then the block of code inside the if statement will be executed. If the script is being imported, that block of code will not run.
"""
if __name__ == "__main__":
    # Creating a PrintedBook instance
    printed_book = PrintedBook("Python Crash Course", "Eric Matthes", 40, 1.5)
    printed_book.show_details()

    # Creating an Ebook instance
    ebook = Ebook("Automate the Boring Stuff with Python", "Al Sweigart", 25, 5)
    ebook.show_details()

    # Encapsulation: trying to set negative price (validation via setter)
    ebook.set_price(-10)  # This will trigger a validation message

    # Change price for ebook using setter
    ebook.set_price(20)
    ebook.show_details()

"""
Why is this useful?
Separation of concerns: It allows you to write Python code that can act both as a module that can be imported 
(with functions or classes that can be reused in other scripts) and as a standalone script.

Testing and reusability: This pattern is useful for writing test code or script-level code that you only want to run 
when executing the script directly, but not when it is imported elsewhere.
"""