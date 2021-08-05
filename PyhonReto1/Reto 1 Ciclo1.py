def abstracta ( lado : int , cubos : int = 4) -> tuple :
    area = cubos * 6 * lado**2
    volumen = cubos * lado **3
    return lado , area , volumen

print(abstracta(37,9))
