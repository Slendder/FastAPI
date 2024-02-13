### Regular Expressions ###

import re

my_string = "Esta es la leccion numero 7: Leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Leccion llamada Manejo de ficheros"

# ! Match
 
match = re.match("Esta no es la leccion", my_other_string) 
#if not (match None): 
# # Otra forma de comprobar el None Of match None: # Otra forma de comprobar el None 
if match is not None:
    print(match)
    start, end = match.span() 
    print(my_other_string[start: end])
    
#print(re.match("Expresiones Regulares", my_string))

# ! Search

search = re.search("leccion", my_other_string)

if search.span() != None:
    print(search)
    start, end = search.span()
    print(my_other_string[start:end])

# ! findall

findall = re.findall("leccion", my_other_string, re.I)
print(findall)


# ! split

split = re.split(" ", my_string)
print(split)

# ! sub

sub = re.sub("la", "el", my_string)
print(sub)


# Patterns
# https://regex101.com

pattern = r'[lL]eccion|[eE]xpresiones'
print(re.findall(pattern, my_string), "\n")

pattern = r'[0-9]'
print(re.findall(pattern, my_string), "\n")

pattern = r'[A-Z|a-z]'
print(re.findall(pattern, my_string), "\n")

pattern = r'\d'
print(re.findall(pattern, my_string), "\n")

pattern = r'\D'
print(re.findall(pattern, my_string), "\n")

pattern = r'[l]...'
print(re.findall(pattern, my_string), "\n")  # ['la l', 'llam', 'lare'], si toca la siguiente l no sigue por ahí

# email validation regular expression
email_regex = r"^[a-zA-Z.]+@[a-zA-Z]+\.[a-zA-Z0-9-.]+$"

# $ -> Indica que no tiene que haber nada despues

# test the regex against an example string
example_string = 'bautista.prieto.hoses@gmail.com'
if re.search(email_regex, example_string):
    print('Valid Email')
else:
    print('Invalid Email')
    
