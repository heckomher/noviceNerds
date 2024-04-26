import digito_verificador as dv
cedula = input("ingrese el rut sin puntos ni guion: (12345678) ")
print(dv.calcular_dv(cedula))