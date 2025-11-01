# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

# Firstly, a Nested Function is a function defined inside another function.
# It's very important to note that the nested functions can access the variables of the enclosing scope.
# However, at least in python, they are only readonly.
# However, one can use the "nonlocal" keyword explicitly with these variables in order to modify them.


def transmit_to_space(message):
    "This is the enclosing function"

    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

print("-------------------" * 4)


def print_msg(number):
    def printer():
        print("Without the nonlocal keyword")
        number = 4
        print(number)

    printer()
    print(number)


print_msg(9)

print("-------------------" * 4)


def print_msg_(number):
    def printer():
        print("Here we are using the nonlocal keyword, it modified the number in scope")
        nonlocal number
        number = 4
        print(number)

    printer()
    print(number)


print_msg_(9)

print("-------------------" * 4)

# Exercise
# Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures.
# That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.


# your code goes here
def multiplier_of(a):
    def multiplier(b):
        return a * b

    return multiplier


multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
