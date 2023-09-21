def ordenar_por_numero(cadena):
    palabras = cadena.split()
    
    palabras_filtradas = [palabra for palabra in palabras if '0' not in palabra]
    palabras_ordenadas = sorted(palabras_filtradas, key=lambda palabra: int(''.join(filter(str.isdigit, palabra))))
    
    resultado = ' '.join(palabras_ordenadas)
    
    return resultado

def order(cadena):
    return ordenar_por_numero(cadena)
