import calculadora_indices as calc

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
edad = int(input("Ingresá tu edad: "))
genero = input("Ingresá tu género (m/f): ")

valor_genero = 5 if genero == 'm' else -161

calorias_reposo = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print(f"Tu TMB (calorías en reposo) es: {int(calorias_reposo)} cal/día")
