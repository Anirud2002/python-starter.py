my_dict = {
    'name': 'Anirud',
    'age': 18,
    'address': 'sankhamul'
}


my_dict2 = dict(name="Anukul", age=28, address='sankhamul', email='anirud@gmail.com')
# print(my_dict2)

my_dict['male'] = True

my_dict.update(my_dict2)
print(my_dict)

for key in my_dict:
    print(my_dict[key])

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

my_dict_copy = my_dict.copy()  # one way to copy the dictionary
my_dict_copy2 = dict(my_dict)  # another way to copy the dictionary



del my_dict['name']  # this deletes the the 'name' key from the dictionary
# print(my_dict)


my_dict.pop('age')
# print(my_dict)

my_dict.popitem()  # this removes the last item in the dictionary
# print(my_dict)

