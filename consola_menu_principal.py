import calculadora_indices as calc

def menu():
    print("""Seleccioná una opción:
1. Calcular IMC
2. Calcular porcentaje de grasa corporal
3. Calcular calorías en reposo
4. Calcular calorías con actividad física
5. Calorías recomendadas para adelgazar
6. Salir""")

while True:
    menu()
    opcion = input("Opción: ")

    if opcion == "1":
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        imc = calc.calcular_IMC(peso, altura)
        print(f"Tu IMC es: {round(imc, 2)}")

    elif opcion == "2":
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        edad = int(input("Edad: "))
        genero = input("Género (m/f): ")
        valor_genero = 10.8 if genero == 'm' else 0
        grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
        print(f"Porcentaje de grasa corporal: {round(grasa, 2)}%")

    elif opcion == "3":
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        edad = int(input("Edad: "))
        genero = input("Género (m/f): ")
        valor_genero = 5 if genero == 'm' else -161
        calorias = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
        print(f"Calorías en reposo: {int(calorias)} cal/día")

    elif opcion == "4":
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        edad = int(input("Edad: "))
        genero = input("Género (m/f): ")
        valor_genero = 5 if genero == 'm' else -161

        print("""Nivel de actividad:
1. Poco o ningún ejercicio
2. Ejercicio ligero (1 a 3 días)
3. Ejercicio moderado (3 a 5 días)
4. Deportista (6-7 días)
5. Atleta (mañana y tarde)""")
        nivel = int(input("Nivel: "))
        valores = [1.2, 1.375, 1.55, 1.72, 1.9]
        valor_actividad = valores[nivel - 1]
        calorias_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
        print(f"Calorías con actividad física: {int(calorias_actividad)} cal/día")

    elif opcion == "5":
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        edad = int(input("Edad: "))
        genero = input("Género (m/f): ")
        valor_genero = 5 if genero == 'm' else -161
        resultado = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
        print(resultado)

    elif opcion == "6":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
