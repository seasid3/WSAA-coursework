# This programme calculates the average price of books using the API created at http://andrewbeatty1.pythonanywhere.com/books/
# Author: Orla Woods (with help from Andrew Beatty, claudeai and co-pilot)

import requests

from booksdam import readbooks

def average_price():
    books = readbooks()
    total_price = 0
    count = 0
    for book in books:
        if book['price'] is not None:
           total_price += book['price']
           count += 1
    average = total_price / count 
    return average

if __name__ == "__main__":
    print("The average price of the books is: ", average_price())