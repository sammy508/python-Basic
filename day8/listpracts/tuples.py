
my_tuples = ("sammy", "sanngam", 100, 200, 500, 1500.50, 1200.200, "sudip")
print("length of tuples is :",len(my_tuples))

print("3rd element of tpule  :",my_tuples[2])

_is_present = 'sammy'in my_tuples
print(_is_present)


coordinates = (2, 4)
x, y = coordinates
print(x,y)

my_tuple = my_tuples+(201,201)
print(my_tuple)


# Tuples are often used to return multiple values from a function.
def get_coordinates():
    return (3, 4)

x, y = get_coordinates()
print(x,y)