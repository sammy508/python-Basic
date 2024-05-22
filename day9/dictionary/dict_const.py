

# we can make dictionary using dict() constructor also

thisdict = dict (
    name = "sammy",
    age = 23,
    gender = "male",
    country = "nepal"

)
print(thisdict)

# access to the dictionary

x = thisdict["age"]
print(x)

# the get key() the key methods will return all the key of dictionary
dict_key = thisdict.keys()
print(dict_key)

# the get values() the value methods will return all the value of dictionary
key_val = thisdict.values()
print(key_val)


# dictionayry items 
# its the one iyem of the dictionary : ('country', 'nepal')
item = thisdict.items()
print(item)

# to check if item is present in ductionary

if country in thisdict :
    print("Yes, the country is one of the  keys on dictionary")


