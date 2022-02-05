#---------------------------------------------------------
frase = """
Se utilizan 3 comillas
para que se imprima 
en lineas diferentes
"""
print(frase)
#---------------------------------------------------------
papa = 100
print (papa)
#---------------------------------------------------------
# Comentario de una linea
""" 
Y este comentario
es de varias
lineas """
#---------------------------------------------------------
if (papa < 200):
    print("Esto es un if")
#---------------------------------------------------------
try:
    uno = int(input('Introduce primer numero'))
    dos = int(input('Introduce segundo numero'))
except:
    print('Error en un try')
#---------------------------------------------------------
def saludar (nombre, mensaje):
    print(mensaje, nombre)

saludar('Jhoan', 'Hola')