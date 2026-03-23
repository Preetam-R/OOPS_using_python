class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = price  # Private attribute

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Price cannot be negative!")

# Usage
my_book = Book("Python Basics", 25)
my_book.set_price(30)
print(f"{my_book.title} costs ${my_book.get_price()}")
