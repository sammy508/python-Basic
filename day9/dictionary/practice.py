cars = {
    "brand": "ford",
    "model": "Abc23",
    "year": "2014",
    "engine": "1200cc",
    "country": "nepal",
},
print(cars)

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:
cars = {
    "brand": "ford",
    "model": "Abc23",
    "year": "2014",
    "engine": "1200cc",
    "country": "nepal",
    "country": "germany", # here the value of country will be overwrite and output becoms germany
}
print(cars)

#length of dictionary
print(len(cars))

# accessing the value of dictionary
