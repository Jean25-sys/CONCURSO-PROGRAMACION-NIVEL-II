def encontrar_valor_atipico(arr):
    # Contadores para números pares e impares
    conteo_pares = 0
    conteo_impares = 0
    
    # Variables para los últimos números pares e impares encontrados
    ultimo_par = None
    ultimo_impar = None
    
    for num in arr:
        if num % 2 == 0:
            # Si el número es par, aumentar el contador de pares y guardar el número
            conteo_pares += 1
            ultimo_par = num
        else:
            # Si el número es impar, aumentar el contador de impares y guardar el número
            conteo_impares += 1
            ultimo_impar = num
        
        # Si ya se han encontrado al menos dos números pares e impares, determinar el valor atípico
        if conteo_pares > 1 and conteo_impares == 1:
            return ultimo_impar
        elif conteo_impares > 1 and conteo_pares == 1:
            return ultimo_par

# Esta función toma una lista de números como argumento y devuelve el valor atípico
# Puedes utilizarla en Codewars para probar la función
def find_outlier(arr):
    return encontrar_valor_atipico(arr)