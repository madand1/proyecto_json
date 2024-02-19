#Funciones de lectura para el archivo nobel.json

#Función Ejercicio 1: Listar las categorías de premios nobel que se han entregado.
def ListarCategorias(nobel):
    listado=[]
    for categoria in nobel:
        listado.append(categoria["category"])
    return (set(listado))


#Función Ejercicio 2: Cuenta el número de premiados del año introducido por teclado.
def ContarPremiados(fecha,nobel):
    id_premiados=[]
    for premiado in nobel:
        if premiado["year"]==fecha:
            if not (premiado.get('laureates') is None):
                for elemento in premiado["laureates"]:
                    id_premiados.append(elemento["id"])
    return (len(id_premiados))


#Función Ejercicio 3: Buscar el año y muestra los premiados con sus categorías y nombre.
def PremiadosAno (fecha,nobel):
    nombres=[]
    apellidos=[]
    categorias=[]
    for premiado in nobel:
        if not (premiado.get('laureates') is None):
            if premiado["year"]==fecha:
                for laureated in premiado["laureates"]:
                    nombres.append(laureated.get('firstname'))
                    apellidos.append(laureated.get('surname'))
                    categorias.append(premiado["category"])
    return nombres,apellidos,categorias

                

#Función Ejercicio 4: Buscar el apellido y muestra categoría, año y motivación.
def EncontrarPremiado(apellido,nobel):
    nombres=[]
    apellidos=[]
    categorias=[]
    motivaciones=[]
    fechas=[]
    for listado in nobel:
        if not (listado.get('laureates') is None):
            for premiado in listado['laureates']:
                if premiado.get('surname') == apellido:
                    nombres.append(premiado.get('firstname'))
                    apellidos.append(premiado.get('surname'))
                    categorias.append(listado.get("category"))
                    motivaciones.append(premiado.get('motivation'))
                    fechas.append(listado.get("year"))
    return nombres,apellidos,categorias,motivaciones,fechas

#Función Ejercicio 5: ¿Podrías proporcionarme el nombre del ganador o ganadores en una categoría específica para un año determinado de los Premios Nobel? Si hubo más de un ganador, por favor, incluye los nombres de todos los laureados que compartieron el premio en esa categoría y año
def PremioCompartido (nobel,year,categoria):
    nombres=[]
    apellidos=[]
    categorias=[]
    for premiado in nobel:
        if not (premiado.get('laureates') is None):
            if premiado["year"]==year and premiado["category"]==categoria:
                for laureated in premiado["laureates"]:
                    nombres.append(laureated.get('firstname'))
                    apellidos.append(laureated.get('surname'))
                    categorias.append(premiado["category"])
    return nombres,apellidos,categorias