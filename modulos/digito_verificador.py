def get_checker(value: int) -> str:
    options = {10: "K", 11: "0"}
    return options.get(value, value)

def calcular_dv(number) -> str:
    try:
        number_lenght = int(len(number))
        array_number = [int(num) for num in number]
        # Solución poco elegante: multiplicador = [2,3,4,5,6,7,2,3,4,5,6,7]
        array_number.reverse()
        multplier = 2
        sum = 0
        for i in range(number_lenght):
            sum += array_number[i] * multplier #En la solucion poco elegante se pone multiplicador[i]
            multplier += 1
            if multplier > 7:
                multplier = 2
        value = 11 - (sum % 11)
        return get_checker(value)
    except ValueError:
        print("ERROR: El rut ingresado debe ser solo números")
    except:
        print("HA OCURRIDO UN ERROR INESPERADO")
    #finally:
    #    "cerrar conexión, por ejemplo"

def validar(rut):
    split = rut.split("-")
    checker = calcular_dv(split[0])
    return str(checker) == str(split[1]).upper()
        
