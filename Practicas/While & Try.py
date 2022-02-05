# -*- coding: utf-8 -*-

while True:
    try:
        edad = int (input ('Introduce tu edad: '))
        resultado = int (edad/2)
        if (edad == 0):
            print ('Adios')
            break
        print ('La mitad de tus años son', resultado, 'años de edad')
    except ValueError:
        print ('Error de tipo de dato')