# Introduction to python dictionary

A dictionary in Python is a mutable, unordered collection of key-value pairs, where each key is unique and maps to a value. Dictionaries are defined using curly braces {} and can be manipulated using a variety of methods and operations. Dictopinary can be of any data types. It is of class type.

 # Key Characteristics
Key-Value Pairs: Each item in a dictionary is a pair of a key and a value.
Unique Keys: Keys must be unique and immutable (e.g., strings, numbers, tuples).
Mutable Values: Values can be of any data type and can be changed after creation.
Unordered: Before Python 3.7, dictionaries were unordered. Starting from Python 3.7, dictionaries maintain insertion order.



# Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary


# example of dictionary
# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary with initial key-value pairs
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# we can acess value inside dictionary by following method

# Accessing a value by key
name = person['name']  # 'Alice'

# Using the get method to handle non-existent keys
age = person.get('age', 'Unknown')  # 30
country = person.get('country', 'Unknown')  # 'Unknown'


# Checking if a key exists in the dictionary
if 'name' in person:
    print("The key 'name' exists in the dictionary")


# Removing a key-value pair using del
del person['city']

# Using pop to remove and return a value
email = person.pop('email')  # 'alice@example.com'

# Using popitem to remove and return the last inserted key-value pair (Python 3.7+)
last_item = person.popitem()


# The dict() Constructor
It is also possible to use the dict() constructor to make a dictionary.

# Example
Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# Check if Key Exists
To determine if a specified key is present in a dictionary use the in keyword:

# Example
Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


#  Removing Items
There are several methods to remove items from a dictionary:

# Example
The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Example
Print all key names in the dictionary, one by one:

for x in thisdict:
  print(x)

  # loop in dictionary
  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
  # output
  brand Ford
model Mustang
year 1964


# Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.

# Example
Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}