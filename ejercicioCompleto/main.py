# Crear una aplicacion que muestre un menu al usuario con 5 opciones:
# 1.- Buscar persona
# 2.- Agregar persona
# 3.- Eliminar persona
# 4.- Editar persona
# 5.- Salir
# Cada una de las opciones debe permitir al usuario realizar las operaciones
# usando listas y diccionarios. Tambien debera repetir el programa hasta
# que el usuario seleccione la opcion 5.

#Lista de personas
lista_personas = []

#Buscar persona por email y retornar el índice.
def obtener_indice_por_email (input_email: str) -> int:
    global lista_personas #Se hace referencia a variable global
    indice = 0 #variable para contar el índice
    for persona in lista_personas: #Ciclo que recorre la lista de personas y lo asigna a la variable persona
        if persona["email"] == input_email: #Pregunta si la clave de personas es igual al email ingresado por el usuario. Recordar que la lista_personas en una lista de dicionarios.
            return indice #En caso de encontrar a la persona, se retorna el índice.
        indice += 1 #Añade un nivel al índice si no encuentra a la persona
    return -1 #Si al terminar el ciclo , no se encuentra a la persona, retorna -1
def crear_diccionario_persona(email: str, nombres: str, apellidos: str) -> dict:
    return {
        "email" : email,
        "nombres" : nombres,
        "apellidos" : apellidos
    }
def confirmar(mensaje:str) -> bool:
    opcion = input(mensaje + " [ingrese s/n]: ")
    while opcion.upper() not in ("S", "N"):
        print("\nERROR: La opción ingresada no es válida")
        opcion = input(mensaje + "[s/n]: ")
    return opcion.upper() =="S"

def email_disponible(email:str) -> bool:
    return obtener_indice_por_email(email) == -1


def validar_email() -> str:
    #Solicitar email al usuario
    email = input("Ingrese el correo electrónico de la persona: ")
    #Validar que el email está disponible.
    #Si el email no está disponible, informaremos al usuario y solicitaremos un nuevo email

    while not email_disponible(email):
        print("ERROR: \n \t El correo ingresado ya está registrado")
        respuesta = confirmar("¿Desea ingresar otro correo?")

        if respuesta:
            email = input("Reingrese el correo electrónico de la persona: ")
        else:
            print("\n * USTED HA CANCELADO EL PROCESO * \n")
            return
    return email

def buscar_persona():
    global lista_personas
    email = input("Ingrese el correo que desea buscar : ")
    indice = int(obtener_indice_por_email(email))
    if indice == -1:
        print("No se ha encontrado el correo ingresado")
        return
    print("\n Se ha encontrado la siguiente información: ")
    diccionario_persona = lista_personas[indice]
    print("\nEmail : \t " + diccionario_persona["email"] +
          "\nNombres : \t " + diccionario_persona["nombres"] +
          "\nApellidos : \t " + diccionario_persona["apellidos"]
        )

def agregar_persona():
    global lista_personas
    email = validar_email()
    if email is None:
        return
    #En caso que el email esté disponible solicitaremos el resto de los datos
    nombres = input("Ingrese los nombres de la persona: ")
    apellidos = input("Ingrese los apellidos de persona: ")
    #Crear diccionario y agregar a la lista

    persona = crear_diccionario_persona(email, nombres, apellidos)

    lista_personas.append(persona)
    #Informar al usuario que el proceso fue terminado

    print("La persona ha sido agregada exitosamente")


def eliminar_persona():
    global lista_personas
    email = input("Ingrese el correo que desea eliminar: ")
    indice = obtener_indice_por_email(email)
    if indice == -1:
        print("No se ha encontrado el correo ingresado")
        return
    persona = lista_personas[indice]
    cadena_persona = "Se ha encontrado a : " + "\nEmail : \t " + persona["email"] + "\nNombres : \t " + persona["nombres"] + "\nApellidos : \t " + persona["apellidos"]+"\n¿ESTA SEGURA(O) QUE DESEA ELIMINAR A ESTA PERSONA?"
    respuesta = confirmar(cadena_persona)
    if respuesta:
        lista_personas.pop(indice)
        print(email+"Se ha eliminado correctamente")
    else:
        print("Usted ha cancelado el proceso")

def editar_persona():
    global lista_personas
    email = input("Ingrese el correo a editar: ")
    indice = obtener_indice_por_email(email)
    if indice != -1:
        print("Dato de la persona [valor actual] (deje en blanco y pulse ENTER para mantener el valor actual)")
        for clave, valor in lista_personas[indice].items():
                if str(clave).upper() != "EMAIL":
                    nuevo_valor = input(str(clave) + " [" + str(valor) + "]: ")
                    if nuevo_valor != "":
                        lista_personas[indice][clave] = nuevo_valor
                else:
                    print("El email no se puede editar")
        print("Se ha editado correctamente")
    else:
        print("No se ha encontrado el correo")


#Menú de la aplicación
def menu():
    while True:
        #Mostrar menú
        print("\n** MENÚ **")
        print(" 1.- Buscar persona \n 2.- Agregar persona \n 3.- Eliminar persona \n 4.- Editar persona \n 5.- Salir")
        option = input("Seleccione una opción del menú: ")
        #Flujos según opción
        match option:
            case "1":
                print("\n * BUSCAR PESRSONA * \n")
                buscar_persona()
            case "2": 
                print("\n *  AGREGAR PERSONA * \n")
                agregar_persona()
            case "3":
                print("\n * ELIMINAR PERSONA * \n")
                eliminar_persona()
            case "4":
                print("\n * EDITAR PERSONA * \n")
                editar_persona()
            case "5":
                print("GRACIAS POR DEJARME DESCANSAR. \nADIÓS")
                exit()
            case _:
                print("Ingrese un valor entre 1 y 5")
                menu()
menu()
