def encontrar_valor_atipico(arr):
    conteo_pares = 0
    conteo_impares = 0
    
    ultimo_par = None
    ultimo_impar = None
    
    for num in arr:
        if num % 2 == 0:
            conteo_pares += 1
            ultimo_par = num
        else:
            conteo_impares += 1
            ultimo_impar = num
        
        if conteo_pares > 1 and conteo_impares == 1:
            return ultimo_impar
        elif conteo_impares > 1 and conteo_pares == 1:
            return ultimo_par

def find_outlier(arr):
    return encontrar_valor_atipico(arr)
