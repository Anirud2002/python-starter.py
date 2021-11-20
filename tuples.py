my_tuple = ('lund',)
print(type(my_tuple))

my_tuple1 = tuple(['lund', 23, True]) # converting list into tuple
print(my_tuple1)

for i in my_tuple1:
    print(i)

if '30' in my_tuple:
    print(True)
else:
    print(False)

my_tuple2 = ('a', 'b', 'c', 'd', 'e')
print(my_tuple2[::-1])


print(my_tuple2.index('c'))

my_list = list(my_tuple2) # converting tuple into list
print(my_list)

new_tuple = 0, 1, 2, 3, 4, 5

i1, *i2, i3 = new_tuple

print(i1)   # returns the first value
print(i3)   # returns the last value
print(i2)   # returns all the values in middle