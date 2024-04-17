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

def validar_email() -> str:
    #Solicitar email al usuario
    email = input("Ingrese el correo electrónico de la persona: ")
    #Validar que el email está disponible.
    #Si el email no está disponible, informaremos al usuario y solicitaremos un nuevo email

    while obtener_indice_por_email(email) != -1:
        print("ERROR: \n \t El correo ingresado ya está registrado")
        opcion = input("Desea ingresar otro correo? [s/n]")
        while opcion.upper() != "S" and opcion.upper() !="N":
            opcion = input("ERROR: USTED NO HA INGRESADO UNA OPCIÓN VÁLIDA\nDesea ingresar otro correo? [s/n]")

        if opcion.upper() == "S":
            email = input("Reingrese el correo electrónico de la persona: ")
        elif opcion.upper() =="N":
            print("\n * USTED HA CANCELADO EL INGRESO * \n")
            return
    return email

def buscar_persona():

    pass

def agregar_persona():
    global lista_personas
    email = validar_email()
    if email == None:
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
    pass

def editar_persona():
    pass

def menu():
    while True:
        #Mostrar menú
        print("** MENÚ **")
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
                eliminar_persona()
            case "5":
                print("GRACIAS POR DEJARME DESCANSAR. \nADIÓS")
                exit()
            case _:
                print("Ingrese un valor entre 1 y 5")
                menu()
menu()
