def calcular_imc ():
    peso = float(input("Coloque su peso en kg:"))
    altura = float(input("Colocar su altura en metros:"))
    imc_retorno = peso /altura**2
    

    if imc_retorno < 16:
        print("delgadez severa")
    elif imc_retorno >= 16 and imc_retorno < 16.99:
        print("delgadez moderada")
    elif imc_retorno >= 17 and imc_retorno < 18.49:
        print("delgadez aceptable")
    elif imc_retorno >= 18.5 and imc_retorno < 24.99:
        print("peso normal")
    elif imc_retorno >= 25 and imc_retorno < 29.99:
        print("sobrepeso")
    elif imc_retorno >= 30 and imc_retorno < 34.99:
        print("obesidad tipo I")
    elif imc_retorno >= 35 and imc_retorno < 39.99:
        print("obesidad tipo II")
    elif imc_retorno >=40 and imc_retorno < 49.99:
        print ("obesidad tipo III o morbida")
    else:
        print("obesidad tipo III") 
    return imc_retorno

calcular_imc()