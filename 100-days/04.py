"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""


import time
def esPrimo(num):
    
    if num <= 2:
        return False
    for i in range(4, int(num/2) + 1):
        if num % i == 0:
            return False
    return True


# Guarda el tiempo de inicio
inicio_tiempo = time.time()

# Tu código aquí
for i in range(1, 101):
    if esPrimo(i):
        print(i)

# Guarda el tiempo de finalización
fin_tiempo = time.time()

# Calcula el tiempo transcurrido
tiempo_transcurrido = fin_tiempo - inicio_tiempo

# Imprime el tiempo transcurrido
print(f"\nTiempo transcurrido: {tiempo_transcurrido} segundos")
