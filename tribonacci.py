def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= 3:
        return signature[:n]
    
    result = signature.copy()
    
    while len(result) < n:
        next_term = sum(result[-3:])
        result.append(next_term)
    
    return result

# Valores de entrada proporcionados directamente (no solicita entrada al usuario)
firma = [1, 1, 1]  # Cambia estos valores según tus necesidades
n = 10  # Cambia el número de elementos deseados según tus necesidades

# Calcular y mostrar la secuencia de Tribonacci
secuencia = tribonacci(firma, n)
print("Secuencia de Tribonacci:", secuencia)