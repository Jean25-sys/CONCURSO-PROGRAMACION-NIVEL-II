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


firma = [1, 1, 1]
n = 10  

secuencia = tribonacci(firma, n)
print("Secuencia de Tribonacci:", secuencia)
