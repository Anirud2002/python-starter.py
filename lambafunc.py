from functools import reduce

square = lambda x: x * x
print(square(3))

multiply = lambda x, y: x*y

print(multiply(2, 4))

point2D = [(1, 2), (22, -4), (15, 23)]
point2D_sorted_list = sorted(point2D, key=lambda x:x[1])
print(point2D_sorted_list)

a = [1, 2, 3, 4, 5]

b = map(lambda x: x * 2, a)
print(list(b))

c = filter(lambda x: x % 2 == 1, a)
print(list(c))

product = reduce(lambda x, y: x * y, a)
print(product)