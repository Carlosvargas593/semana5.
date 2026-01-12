def loteria_primitiva():
    numeros_ganadores = []

    print("--- Registro de Lotería Primitiva ---")
    print("Por favor, ingresa los 6 números ganadores (entre 1 y 49).")

    while len(numeros_ganadores) < 6:
        try:
            # 1. Pedir el número al usuario
            entrada = input(f"Introduce el número {len(numeros_ganadores) + 1}: ")
            numero = int(entrada)

            # 2. Validar que el número esté en el rango real (1-49)
            if numero < 1 or numero > 49:
                print("⚠️  Error: El número debe estar entre 1 y 49.")

            # 3. Validar que no se haya ingresado ya (sin duplicados)
            elif numero in numeros_ganadores:
                print(f"⚠️  El número {numero} ya ha sido anotado. Elige otro.")

            else:
                numeros_ganadores.append(numero)

        except ValueError:
            print("⚠️  Entrada no válida. Por favor, introduce un número entero.")

    # 4. Ordenar la lista de menor a mayor
    numeros_ganadores.sort()

    # 5. Mostrar el resultado final
    print("\n" + "=" * 35)
    print("COMBINACIÓN GANADORA ORDENADA:")
    print(numeros_ganadores)
    print("=" * 35)
    print("¡Mucha suerte con tus resultados!")


# Ejecutar el programa
loteria_primitiva()5