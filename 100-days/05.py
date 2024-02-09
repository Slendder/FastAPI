"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""


class Triangle:

    def __init__(self, base, height):
        self.__area = (base * height) / 2
        self.perimeter = base + height*2

    def print_Triangle(self):
        return f"The area of the triangle is {self.__area}"


class Square:

    def __init__(self, side):
        self.__area = (side ** 2)
        self.perimeter = 4 * side

    def print_Square(self):
        return f"The area of the square is {self.__area}"


class Rectangle:

    def __init__(self, length, width):
        self.__area = length * width
        self.perimeter = 2 * (length + width)

    def print_Rectangle(self):
        return f"The area of the rectangle is {self.__area}"


def get_Area(polygon, side1=False, side2=False):
    if polygon == 'Triangle':
        return Triangle(side1, side2).print_Triangle()
    elif polygon == 'Square':
        return Square(side1).print_Square()
    else:
        return Rectangle(side1, side2).print_Rectangle()


print(get_Area('Triangle', 3, 6))
print(get_Area('Square', 5))
print(get_Area('Rectangle', 4, 8))