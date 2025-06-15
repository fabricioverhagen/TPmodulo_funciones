import calculadora_indices as calc

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
edad = int(input("Ingresá tu edad: "))
genero = input("Ingresá tu género (m/f): ")

valor_genero = 5 if genero == 'm' else -161

print("""Seleccioná tu nivel de actividad:
1. Poco o ningún ejercicio
2. Ejercicio ligero (1 a 3 días)
3. Ejercicio moderado (3 a 5 días)
4. Deportista (6-7 días)
5. Atleta (entrena mañana y tarde)""")

opcion = int(input("Opción: "))
valores = [1.2, 1.375, 1.55, 1.72, 1.9]
valor_actividad = valores[opcion - 1]

calorias_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
print(f"Calorías con actividad física: {int(calorias_actividad)} cal/día")
