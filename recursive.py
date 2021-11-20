# to find the fibonacci series

def fibonacci_num(n):
    if (n == 0):
        return 1
    if (n == 1):
        return 1
    else:
        return fibonacci_num(n-1) + fibonacci_num(n-2)
# fib(3) + fib(2)
# fib(2) + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
print(fibonacci_num(4))

word = 'paaaaaap'

def is_palindrome(word):
    if (len(word) <= 1):
        return True
    return word[0] == word[-1] and is_palindrome(word[1:-2])

print(is_palindrome(word))

# In this example, the program is recursively checking if the first letter and last letter of a word matches. During the process if the first condition doesn't match then recursion stops because the python doesn't look for another condition if first condition doesn't match.