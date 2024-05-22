
thisdict = {
    "brand": "ford",
    "model": "Abc23",
    "year": "2014",
    "engine": "1200cc",
    "country": "nepal",
    "country": "germany" # if we gave comma to the last element then it will shows the length 1
                            # here the value of country will be overwrite and output becoms germany
}


# to check if item is present in ductionary

if "model" in thisdict :
    print("Yes, the country is one of the  keys on dictionary")

# to remove item from dictionary
thisdict.pop("country")  # this will remove the country item from the dictionary
print(thisdict)

# loop in dictionary
thisdict = {
    "brand": "ford",
    "model": "Abc23",
    "year": "2014",
    "engine": "1200cc",
    "country": "nepal",
    "country": "germany"
}
for x in thisdict :
    print(x)
print("\n")  
for y in thisdict.values():
    print(y)