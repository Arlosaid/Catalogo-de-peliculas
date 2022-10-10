from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp


opcion = None

while opcion != 4:
    try:
        print(f'''Opciones: 
        1) Agregar Pelicula
        2) Listar Peliculas
        3) Eliminar lista de Peliculas
        4) Salir
        ''')
        opcion = int(input('Ingrese una opcion del menu: ')) 

        if opcion ==1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)

        elif opcion == 2:
            cp.listar_peliculas() 

        elif opcion == 3:
            cp.eliminar_pelicula()    

    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Salimos del programa...')   