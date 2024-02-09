"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

def is_Prime(number):
    if number < 2:
        return False

    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            return False
    return True


for i in range(1, 101):
    if is_Prime(i):
        print(i)
