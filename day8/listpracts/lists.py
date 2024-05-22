
my_tuples = ["sammy", "sanngam", 100, 200, 500, 1500.50, 1200.200, "sudip"]
print("length of list is :",len(my_tuples))
print(my_tuples[2])

my_tuples.append("abcd")
print("after append ",my_tuples)

my_tuples.remove(my_tuples[2])
print("after remove ",my_tuples)

my_tuples.reverse()
print("after reverse ",my_tuples)


my_tuple = [ 100, 200, 500, 1500.50, 1200.200]
my_tuple.sort()
print("after sorting ",my_tuple)

my_tuples.append(1200000)
print("after reverse ",my_tuples)

_is_item_there = "sammy" in my_tuples
print(_is_item_there)
