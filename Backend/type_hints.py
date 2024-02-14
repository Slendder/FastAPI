 
my_typed_variable: int = "WTF"
# my_typed_variable ---> The editor think it's an integer, 
# but the value is a string.

print(type(my_typed_variable))  # Outputs: <class 'str'>

def get_FullName(name: str, surname: str):
    return f"{name.title()} {surname.title()}"