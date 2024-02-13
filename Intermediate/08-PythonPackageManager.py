### Python Package Manager ###

from Package import arithmetics
import requests
import numpy

print(numpy.version.version)

num_py = numpy.array(list(range(1, 11)))
print(type(num_py))
print(num_py * 2)

# pip install "module"
# pip uninstall "module"
# pip show numpy


response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetic Package

print(arithmetics.suma(3, 4))

# Si no tenemos el __init__.py
# no se reconoce com un "package" ( conjunto de modulos )
