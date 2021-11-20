my_set = {1, 2, 3, 4, 2, 3}
# print(my_set)

my_set2 = set([1, 2, 3, 4, 5, 2, 3])
# print(my_set2)

my_set3 = set('Hello')
# print(my_set3)

# how to set an empty set?

empty_set = set()
# if we use empty curly brackets, it will considered as a dictionary

empty_set.add(1)
empty_set.add(2)
empty_set.add(3)

for i in empty_set:
    pass
    # print(i)


empty_set.remove(2)
empty_set.discard(3)  # this line will not spit out any error

# print(empty_set)

odds = {1, 3, 5, 7}
evens = {2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)
print(union)

intersect = odds.intersection(primes)
print(intersect)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 4, 5}
setC = setA.copy()

diff = setA.difference(setB)
symmetric_diff = setB.symmetric_difference(setA)
# print(diff)
# print(symmetric_diff)

print(setB.issubset(setA))

# if you want to update the set then use this commands:
# for union:
setA.update(setB)
print(setA)

# for intersection:
setA.intersection_update(setB)
print(setA)