import random


a = 1
b = 2
sum = lambda x, y: x + y
c = sum(a, b)
print(c)


# Exercise
# Write a program using lambda functions to check if a number in the given list is odd.
# Print "True" if the number is odd or "False" if not for each element.

l = [2, 4, 7, 3, 14, 19]
for i in l:
    # your code here
    my_lambda = lambda x: (x % 2) == 1
    print(my_lambda(i))


print("-------------" * 4)

l = [2, 4, 7, 3, 14, 19]
for i in l:
    # your code here
    my_lambda = lambda i: "False" if i % 2 == 0 else int(random.random() * 10)
    print(my_lambda(i))
