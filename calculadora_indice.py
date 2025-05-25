def calcular_imc ():
    peso = float(input("Coloque su peso en kg:"))
    altura = float(input("Colocar su altura en metros:"))
    imc_retorno = peso /altura**2
    return imc_retorno