course = 'Python for beginners'
print(course[0]) #prints the first character
print(course[-1]) #prints the last character
print(course[0:3]) #prints three letters from index 0 to index 2
print(course[0:]) #prints all the characters
print(course[1:]) #prints all the characters starting from index 1
print(course[:5]) #prints five characters from index 0 to index 4

another = course[:] #it copies tha value of course
print(another)

name = 'Jennifer'
print(name[1:-1])
print(name.startswith('J'))

f_name = 'Anirud'
l_name = 'Shrestha'
message = f_name + ' [' + l_name + '] is a coder' #this is a normal string concatination
msg = f'{f_name} [{l_name}] is a coder.' #this is a formatted string
print(msg)

print(len(course)) #prints out the number of character in that variable
print(course.upper())
print(course.lower())
print(course.find('beginners')) #gives the index value of letter 'b' in course
print(course.replace('beginners', 'absolute beginners'))
print('Python' in course)

my_string = 'How are you doing'
my_string = my_string.split(' ')

list_to_string = ' '.join(my_string)
print(list_to_string)