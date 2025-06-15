import calculadora_indices as calc

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = calc.calcular_IMC(peso, altura)
print(f"Tu IMC es: {round(imc, 2)}")
