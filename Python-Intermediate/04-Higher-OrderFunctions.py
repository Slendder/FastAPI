### Higher-Order-Functions ###

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

number = list(range(1, 81))

# Map


def multiply_two(number):
    return number * 2


print(list(map(lambda number: number * 2, number)))
print(list(map(multiply_two, number)))


# Filter

def filter_greater_that_ten(value):
    