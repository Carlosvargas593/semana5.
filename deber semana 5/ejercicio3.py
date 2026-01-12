# 1. Lista de asignaturas predefinidas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# 2. Lista para almacenar las notas
notas = []

print("--- Registro de Notas del Curso ---")

# 3. Proceso de captura de datos con validación real
for materia in asignaturas:
    while True:
        try:
            # Pedimos la nota y la convertimos a número (float para permitir decimales)
            nota = float(input(f"Ingresa la nota de {materia}: "))

            # Validamos que la nota esté en un rango lógico (ej. 0 a 10)
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Por favor, ingresa una nota entre 0 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número (usa punto para decimales).")

# 4. Mostrar resultados finales
print("\n" + "=" * 30)
print("BOLETÍN DE CALIFICACIONES")
print("=" * 30)

for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")

# 5. Cálculo del promedio real
promedio = sum(notas) / len(notas)
print("-" * 30)
print(f"TU PROMEDIO FINAL ES: {promedio:.2f}")
print("=" * 30)