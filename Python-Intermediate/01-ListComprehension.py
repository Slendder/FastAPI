### List Comprehension ###

my_range = range(0, 10)

my_original_list = list(my_range)
my_list = [i + 1 for i in my_original_list]

print(f'{my_original_list} \n{my_list}')
print([i * i for i in my_original_list])
print([i ** i for i in my_original_list])


def sum_five(Number):
    if Number not in (range(5)):
        return Number + 5
    else:
        return Number


my_list = [sum_five(i) for i in my_original_list]
print(my_list)
