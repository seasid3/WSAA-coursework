# This program writes a module to interact with the API created at http://andrewbeatty1.pythonanywhere.com/books/ 
# Author: Andrew Beatty (Orla Woods)

import requests
url = "http://andrewbeatty1.pythonanywhere.com/books"
# test requests works
# url =  "http://google.com"
# response = requests.get(url)
# print(response.text)

# Function to get all the books
# Now convert it to a function
def readbooks():
    response = requests.get(url)
    return response.json()

# Function to find a book by id
def readbook(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

# Function to create a book
def createbook(book):
    response = requests.post(url, json=book)
    return response.json()

# Function to update a book
def updatebook(id, book):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

# Function to delete a book
def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

# Testing

if __name__ == "__main__":
    #print(readbooks())
    #print(readbook(1677))
    #print(createbook({"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 1925}))
    #print(updatebook(1698, {"price":1000}))
    print(deletebook(1698))