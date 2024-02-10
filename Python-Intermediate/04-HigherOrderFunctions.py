### Higher-Order-Functions ###

from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_one(first_value, second_value, function_reference):
    return function_reference(first_value + second_value)


print(sum_two_values_and_add_one(2, 4, sum_one))
print(sum_two_values_and_add_one(2, 4, sum_five))


### Closures ###

def sum_ten(primary_value):
    def add(secondary_value):
        return secondary_value + 10 + primary_value
    return add


add_closure = sum_ten(-10)  # Se guarda en el 'contexto'

print(add_closure(5))
print(sum_ten(-10)(5))

### Built-in Higher-Order-Functions ###

number = list(range(1, 20))

# Map


def multiply_two(number):
    return number * 2


# Multiply all numbers by two using map()
print(list(map(lambda number: number * 2, number)))
print(list(map(multiply_two, number)))


# Filter

def filter_greater_than_ten(value):
    return value >= 10


# Demands a boolean function
print(list(filter(filter_greater_than_ten, number)))
print(list(filter(lambda value: value >= 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# Reduce


def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, number))
print(reduce(lambda first_value, second_value: first_value + second_value, number))