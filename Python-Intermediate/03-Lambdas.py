### Lambdas ###

def sum_three_values(value):

    return lambda first_value, second_value, value: first_value + second_value + value


print(sum_three_values(10)(5, 8))
