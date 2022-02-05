# -*- coding: utf-8 -*-

#----------------------------------------<DEFINICIONES>----------------------------------------
def menu () :
    print ("Menú de la Aplicación")
    print ("\t1. Identificación")
    print ("\t2. Identificación (entrada múltiple)")
    print ("\t3. Identificación (diccionario de valores)")
    print ("\t4. Factorial de un número entero")
    print ("\t5. Otro")
    print ("\t0: salir")

    while True:
        try:
            opcion = int (input ('Seleccione una opción: '))
            if (opcion > 5 or opcion < 0):      
                print ('La opción no existe, selecciona una opción válida.')
            else:
                break
        except ValueError:
            print ('Carácter no válido para seleccionar una opción, inténtalo de nuevo.')
    return  opcion

hola = 'Hola'
def saludo (nombre, mensaje = hola):
    print(mensaje, nombre)

holaDesconocido = 'Hola desconocido. Me alegro de conocerte'
def saludoDesc (nombre, mensaje = holaDesconocido):
    print(mensaje, nombre)

def entradaMultiple (nombre, mensaje):
    print (nombre, mensaje)

def factorial (numero):
    fact = 1
    for i in range (numero):
        fact = fact * (i + 1)
    print ('El factorial de ', numero, 'es', fact)
#----------------------------------------</DEFINICIONES>----------------------------------------

#----------------------------------------<CÓDIGO PYTHON>----------------------------------------
opcion = menu()
while True:
    try:
        
        if (opcion == 1 or opcion == 2):
            try:
                nombre = str (input ('¿Cuál es tu nombre? '))
            except ValueError:
                print ('La variable "nombre" solo contiene caracteres')

        if (opcion == 0):
            print ('Hasta pronto...')
            break
        elif (opcion == 1):
            if (nombre == 'Alejandro' or nombre == 'Diego'):
                saludo (nombre)
            elif (nombre == '0'):    
                opcion = menu ()
            else:
                saludoDesc (nombre)     
        elif (opcion == 2):
            mensaje = input ('Introduce un mensaje ')
            entradaMultiple (nombre, mensaje)
            opcion = menu ()
        elif (opcion == 3):
            print ('No sé muy bien que hacer aquí')
            opcion = menu ()
        elif (opcion == 4):
            numero = int (input ('Calcular factorial del número: '))
            factorial (numero)
            opcion = menu ()
        elif (opcion == 5):
            print ('¿Qué deseas hacer ahora?')   
            opcion = menu ()

    except ValueError:
        print('Hubo un error con el dato introducido')
#----------------------------------------</CÓDIGO PYTHON>----------------------------------------