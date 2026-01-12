# 1. Creamos la lista con los números del 1 al 10
# Usamos range(1, 11) para generar los números automáticamente
numeros = list(range(1, 11))

# 2. Invertimos el orden de la lista
# El índice [::-1] crea una copia de la lista en orden inverso
numeros_inversos = numeros[::-1]

# 3. Convertimos los números a texto y los unimos con comas
# Esto hace que se vea: 10, 9, 8... en lugar de [10, 9, 8...]
resultado = ", ".join(map(str, numeros_inversos))

# 4. Mostramos el resultado por pantalla
print("Números del 1 al 10 en orden inverso:")
print(resultado)