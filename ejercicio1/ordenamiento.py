numerosPrueba1 = [7, 2, 5]
numerosPrueba2 = [2, 2, 9]

def ordenar_burbuja(lista):
    arr = list(lista)
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

numerosPrueba1 = [7, 2, 5]
numerosPrueba2 = [2, 2, 9]

print("Prueba 1 ordenada:", ordenar_burbuja(numerosPrueba1))
print("Prueba 2 ordenada:", ordenar_burbuja(numerosPrueba2))



