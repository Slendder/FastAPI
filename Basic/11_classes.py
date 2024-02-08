# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición

class MyEmptyPerson:
    pass


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person(MyEmptyPerson):
    def __init__(self, name, surname):
        self.__name = name
        self.surname = surname
        self.fullname = f'{name} {surname}'

    def printName(self, password=False):
        if password == 'python':
            return f"Your name is {self.__name}"
        else: 
            return "Contraseña incorrecta!"

my_person = Person('Bauti', 'Prieto')

# print(my_person.__name) Error, atributo es privado
print(my_person.printName('S'))   # Acceso a propiedad privada
print(my_person.fullname)
