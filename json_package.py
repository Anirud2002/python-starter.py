import json_package

person = {'name': 'Anirud', 'age': 18, 'address': 'Sankhamul', 'friends': ['anukul', 'abhin'], 'single': False}

personJSON = json_package.dumps(person, indent=4)
print(personJSON)

# converting back to dictionary
person = json_package.loads(personJSON)
print(person['friends'])


