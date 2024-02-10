### Error Types ###

# ? SyntaxError
# ! print "Syntax Error!"

# ? NameError
# ! print(name) name is not defined

# ? IndexError
# ! print([1, 2, 3, 4, 5][5]) index out of range!

# ? TypeError:
# ! print(20 + "hello world") cannot concatenate 'int' with 'str'

# ? ModuleNotFoundError
# ! import not-existing_Module

# ? AttributeError
class temporal:
    pass
# ! print(temporal.hasAttribute) temporal has no atribute


# ? KeyError
my_dict = {"a": 1, "b": 2}
# ! my_dict["c"] key not found in dictionary!

# ? ValueError
# ! my_value = int('Not a number')

