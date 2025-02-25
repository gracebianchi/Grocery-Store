# Grocery-Store

You will need to create two files:

Item.py - file containing a class definition for a grocery item object.
Store.py - file containing a class definition for an grocery store object.
There will be no starter code for this assignment, but rather the class descriptions and required methods are defined in the specification below.

It’s recommended that you organize your lab work in its own directory. This way all files for a lab are located in a single folder. Also, this will be easy to import various files into your code using the import / from technique shown in lecture.

Item.py class
The Item.py file will contain the definition of what a grocery item is.

We will define the grocery item attributes as follows:

upc - int that represents the grocery item’s 12-digit Universal Product Code.
category - str that represents the category of a grocery item such as produce, health, beverage, etc. Your program should ensure that this field will be stored in all upper-case characters.
name - str that represents the name of a grocery item. Your program should ensure that this field will be stored in all upper-case characters.
price - float that represents the price of the item.
You will write a constructor that allows the user to construct a grocery item object by passing in values for all of the fields. Your constructor should set these attributes with the value None by default.

__init__(self, upc, category, name, price)
In addition to your constructor, your class definition should also support “setter” methods that can update the state of the grocery item objects:

setUpc(self, upc)
setCategory(self, category)
setName(self, name)
setPrice(self, price)
Note that category and name parameters can contain upper / lower case characters, but your program should ensure these values are stored in upper-case.

Each grocery item object should be able to call a method toString that you will implement, which returns a str with all the grocery item attributes. The string should contain all attributes in the following EXACT format:

i = Item(420012347654, "produce", "avocado", 2.0)
print(i.toString())
Output:

UPC: 420012347654, Category: PRODUCE, Name: AVOCADO, Price: $2.00
Note: The i.toString() return value in the example above does not contain a newline character (\n) at the end.

Tip: Note that the price is displayed with two decimal places (as traditionally used when displaying prices). Consider using the string’s format method (or f-string) where the floating point value will contain 2 decimal places. For example:

>>> price = 1.5
>>> "{:.2f}".format(price)
'1.50'
You can refer to CS 8 lecture notes on string formatting if you would like a review:

https://ucsb-cs8.github.io/m19-wang/lectures/lect11/
https://ucsb-csw8.github.io/w24/lectures/lect08/
Store.py
The Store.py file will contain the definition of what a single grocery store object is.

A Store object will contain a dictionary structure where the keys of the dictionary will be a str representing an Item’s category (all upper-case characters).

The dictionary values will be a list of Item objects that the Store contains. Note that the order of the Items in the list is based on when the Item object was inserted into the dictionary structure (most recent Item inserted will be at the end of the list).

Your code should support the following constructor / methods:

__init__(self) - Constructor that initialized the dictionary structure of the Store class. Initially, this dictionary should be empty.
addItem(self, item) - Adds an Item object (item) to the Store. The inserted Item object should be added to the end of the list of existing items that have the same category. You may assume that an item with the same UPC does not already exist in the Store when this method is called (the tests will not attempt to insert duplicate items, and you do not need to check for these cases). It is possible for an Item object to have None values as its attributes.
removeItem(self, item) - Removes an Item object (item) from the Store if it exists. Your code will need to check and see if the parameter item object has the same upc value as an existing item in the Store if it is to be removed from the Store.
removeCategory(self, category) - removes all Items of a certain category from the Store if it exists. Your code will need to remove the entire category entry from the Store’s dictionary.
getItems(self, category) - Returns a string containing all Items of a certain category. This string should consist of a collection of strings - one line per item. Since each item will be in its own line within a single string, a newline character (\n) should be inserted between each line (if applicable) EXCEPT at the very last line where no newline character should exist. The order of the Items in this string will be dictated by the order of the Items in the Store’s list for the Item’s category. The Item toString() method should be used when constructing this method’s return string. If no Items of the category exists in the Store, then this method returns an empty string (""). Note: the category parameter value may be in either lower / upper case.
doesItemExist(self, item) - Returns True if the parameter item (with matching upc value) exists in the Store. Returns False otherwise.
countDollarItems(self) - Returns an int representing the number of items that are less than or equal to 1 dollar.
