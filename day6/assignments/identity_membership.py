# Task 6: Identity and Membership Operators
# 
# Create a list my_list containing a few elements.
# Use identity operators (is and is not) to check if two variables are the same object.
# Use membership operators (in and not in) to check if an element is present in my_list.
# Print the results.



my_list = ["banana", "apple", "orange", "grapes"]
a= my_list
b = ["banana", "apple", "orange", "grapes"]

# identity
is_same = a is my_list
isnot_same = a is not my_list

# membership

ele_in_mylist = a in b
ele_notin_mylist = a not in b

print("a is in mylist", is_same)
print("a isnot in mylist", isnot_same)
print("a is in mylist", ele_in_mylist)
print("a is notin mylist", ele_notin_mylist)
