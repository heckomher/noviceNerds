def calcular_dv(number) -> str:
    number_lenght = int(len(number))
    array_number = [int(num) for num in number]
    # Solución poco elegante: multiplicador = [2,3,4,5,6,7,2,3,4,5,6,7]
    array_number.reverse()
    multplier = 2
    sum = 0
    for i in range(number_lenght):
        sum += array_number[i] * multplier #En la solucion poco elegante se pone multiplicador[i]
        if multplier < 7:
            multplier += 1
        else:
            multplier = 2
    verifyer = 11 - (sum % 11)
    if verifyer == 11:
        return 0
    elif verifyer == 10:
        return 'K'
    return verifyer

def validar(rut):
    separar = rut.split("-")