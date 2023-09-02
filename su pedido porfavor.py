def ordenar_por_numero(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Filtrar las palabras que no contienen '0' y luego ordenarlas
    palabras_filtradas = [palabra for palabra in palabras if '0' not in palabra]
    palabras_ordenadas = sorted(palabras_filtradas, key=lambda palabra: int(''.join(filter(str.isdigit, palabra))))
    
    # Unir las palabras ordenadas en una cadena
    resultado = ' '.join(palabras_ordenadas)
    
    return resultado

# Esta función toma la cadena como argumento y devuelve el resultado
# Puedes utilizarla en Codewars para probar la función
def order(cadena):
    return ordenar_por_numero(cadena)