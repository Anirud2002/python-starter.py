numbers = [1, 2, 3, 4, 1 ,2 ,6,4 ,8,5, 8, 6 ,9 ,6 ,7]
fresh_set = []
for num in numbers:
    if num not in fresh_set:
        fresh_set.append(num)

fresh_set.sort()
print(fresh_set)