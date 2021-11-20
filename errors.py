try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('The age cannot be zero')
except ValueError:
    print('You can only submit number')