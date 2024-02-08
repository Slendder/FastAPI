"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""
def AnagramDetector(str1, str2):
    if str1 == str2[::-1]:
        return True
    elif  len(str1) != len(str2):
        return False
    for i in str2:
        if i not in str1:
            return False
    return True

print(AnagramDetector("listen", "silent")) 