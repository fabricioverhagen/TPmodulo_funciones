import calculadora_indices as calc

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
edad = int(input("Ingresá tu edad: "))
genero = input("Ingresá tu género (m/f): ")

valor_genero = 10.8 if genero == 'm' else 0

porcentaje_grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print(f"Tu porcentaje de grasa corporal es: {round(porcentaje_grasa, 2)}%")
