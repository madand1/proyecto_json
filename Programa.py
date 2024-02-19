#Importacion del documento json. 
import json

#Con esto lo que hacemso es abrir el fichero del documento.
with open("nobel.json") as fichero:
    nobel = json.load(fichero)

#Importamos las funciones del fichero de funciones.
from Funciones import *

#Las opcioens de menu
print("\n")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("- - - - - - - - - - - - - - - - - - - - - - - - **OPCIONES DE MENU**- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print()
print("1. Listar las categorías de premios nobel que se han entregado.")
print("2. Cuenta el número de premiados del año introducido por teclado.")
print("3. Buscar el año y muestra los premiados con sus categorías y nombre.")
print("4. Buscar el apellido y muestra categoría, año y motivación.")
print("5. ¿Podrías proporcionarme el nombre del ganador o ganadores en una categoría específica para un año determinado de los Premios Nobel? Si hubo más de un ganador, por favor, incluye los nombres de todos los laureados que compartieron el premio en esa categoría y año.")
print("0. Salir.")
print()
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")



#Pedir por teclado la opción deseada del menú. En caso de error, mostrar mensaje.
opcion =int(input("Introduzca la opción deseada: "))
while opcion !=0:

#Las opciones desde la 1 a la 5


    if opcion ==1:
        print("\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - CATEGORIAS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print()
        categorias = ListarCategorias(nobel)
        for elemento in zip (categorias):
            print (elemento[0])
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")




    elif opcion ==2:
        fecha = input("Introduzca el año del que desea obtener el número de premiados: ")
        mostrar_num = ContarPremiados(fecha,nobel)
        if mostrar_num >0:
            print("- - - - - - - - - - - - - - - - - - - NÚMERO PREMIADOS DE",fecha, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print()
            print("Son un total de", mostrar_num)
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        else:
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print ("No existen premiados de dicho año.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")



    elif opcion == 3:
        fecha = input("Introduzca el año y se mostrará el nombre de los premiados y su categoría del premio: ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - PREMIADOS DE",fecha, "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print()
        nombres, apellidos, categorias =PremiadosAno (fecha,nobel)
        if len(nombres)==0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("No existen premiados en el año introducido.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
        else:
            for nombre,apellido,categoria in zip (nombres, apellidos, categorias):
                print("Nombre: ",nombre)
                print("Apellido: ",apellido)
                print("Categoria: ",categoria)
                print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")




    elif opcion ==4:
        apellido = input("Introduzca el apellido del premiado: ")
        nombres,apellidos,categorias,motivaciones,fechas = EncontrarPremiado(apellido,nobel)
        if len(nombres)==0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("No existen premiados con dicho apellido.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
        else:
            for nombre,apellido,categoria,motivacion,fecha in zip (nombres,apellidos,categorias,motivaciones,fechas):
                print("\n")
                print("- - - - - - APELLIDO: ",apellido,"- - - - -")
                print()
                print("Nombre: ",nombre)
                print("Apellido: ",apellido)
                print("Categoria: ",categoria)
                print("Motivación: ",motivacion)
                print("Año: ",fecha)
                print("- - - - - - - - - - - - - - - - - - - - - - - - ")
    

    elif opcion ==5:
        print ("Las categorías son: Economics, Literature, Chemistry, Peace, Medicine, Physics.")
        categoria = input("Introduzca una categoría: ")
        year = input ("Introduzca un año: ")
        nombres,apellidos,categorias = PremioCompartido (nobel,year,categoria)
        if len(nombres)==0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("No existen premiados de ese año y categoria.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - ")
        else:    
            print("- - - - - - PREMIADOS:- - - - -")
            print("- - - AÑO",year,"- - - - - - - ")
            print("- - - CATEGORIA",categoria,"- - - - - - - ")
            for nombre,apellido,categoria in zip (nombres, apellidos, categorias):                
                print()
                print("Nombre: ",nombre)
                print("Apellido: ",apellido)
                print("Categoria: ",categoria)
                print("- - - - - - - - - - - - - - - - - - - - - - - - ")
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")



    else: 
        print("La opción elegida no es válida.")
    print("\n")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("- - - - - - - - - - - - - - - - - - - - - - - - **OPCIONES DE MENU- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print()
    print("1. Listar las categorías de premios nobel que se han entregado.")
    print("2. Cuenta el número de premiados del año introducido por teclado.")
    print("3. Buscar el año y muestra los premiados con sus categorías y nombre.")
    print("4. Buscar el apellido y muestra categoría, año y motivación.")
    print("5. ¿Podrías proporcionarme el nombre del ganador o ganadores en una categoría específica para un año determinado de los Premios Nobel? Si hubo más de un ganador, por favor, incluye los nombres de todos los laureados que compartieron el premio en esa categoría y año.")
    print("0. Salir.")
    print()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")        
    opcion = int(input("Introduzca la opción deseada: "))
print ("Hasta pronto y vuelva pronto.")