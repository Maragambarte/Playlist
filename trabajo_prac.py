import json
import rich
import sys
from rich.console import Console
from rich import print
from rich.progress import track
from time import sleep


console = Console()
opcion_gestion= int()
opcion_usuario=int()
opcion= int()
playlist= list()
archivo = open("playlist.json","r")
playlist = json.loads(archivo.read())

print ("♫ 𝄞 ♪ "*10)
def gestion_musica():
    console.print("""[bold magenta]
    𝄞 𝄞 𝄞   1) Gestionar la PlayList     𝄞 𝄞 𝄞
    𝄞 𝄞 𝄞   2) imprimir reportes         𝄞 𝄞 𝄞   
    𝄞 𝄞 𝄞   3) Salir                     𝄞 𝄞 𝄞""")
    print ("* "*40)
    opcion_gestion=int(input("        Ingrese la opcion a realizar: "))
    match opcion_gestion:
        case 1:
            menu()
        case 2:
            reportes()
        case 3: 
            print("        Gracias por navegar en TOP TEN 2023 ")
            sys.exit()
        case other:
            error()
def menu():
    console.print("""[bold magenta]
   ♫ ♫ ♫    1). Agregar canción         ♫ ♫ ♫
   ♫ ♫ ♫    2). Modificar canción       ♫ ♫ ♫
   ♫ ♫ ♫    3). Eliminar canción        ♫ ♫ ♫
   ♫ ♫ ♫    4). Volver al menu Pricipal ♫ ♫ ♫ 
   ♫ ♫ ♫    5). Salir                   ♫ ♫ ♫""")  
    print ("♫ 𝄞 ♪ "*10)
    opcion_usuario=int(input("         Ingrese la opcion deseada: "))
    if opcion_usuario == 1:
        agregar_cancion()
    elif opcion_usuario == 2:
        modificar()
    elif opcion_usuario == 3:
        eliminar()
    elif opcion_usuario == 4:
        gestion_musica()
    elif opcion_usuario == 5:
        print("        Gracias por navegar en TOP TEN 2023 ")
        sys.exit()
    else:
        error()
def ver_playlist():
    
    from rich.console import Console
    from rich.table import Table
    import json

    with open('playlist.json') as file:
        data = json.load(file)

    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Puesto", style="dim", width=12)
    table.add_column("Titulo")
    table.add_column("Artista", justify="right")
    table.add_column("Idioma", justify="right")

    for item in data:
        puesto = item.get('Puesto', '')
        titulo = item.get('Titulo', '')
        artista = item.get('Artista', '')
        idioma = item.get('Idioma', '')
        table.add_row(str(puesto), titulo, artista, idioma)
    console.print(table)
def modificar():
        console.print("tLista de canciones:")
        ver_playlist()
        print("----- Modificar Canción -----")
        puesto = int(input("Ingrese el Puesto de la canción a modificar: "))
        for titulo in playlist:
            if titulo["Puesto"] == puesto:
                print("Canción encontrada:")
                print ("Puesto: ",titulo["Puesto"])
                print("Titulo: ", titulo["Titulo"])
                print("Artista: ", titulo["Artista"])
                nuevo_titulo = input("Ingrese el nuevo título de la canción: ")
                nuevo_artista = input("Ingrese el nuevo nombre del artista: ")
                nuevo_idioma = input("Ingrese el nuevo Idioma de la cancion: ")
                titulo["Titulo"] = nuevo_titulo
                titulo["Artista"] = nuevo_artista
                titulo["Idioma"]=nuevo_idioma
                guardar_datos(playlist)
                for _ in track(range(100), description='[green]Procesando Informacion'):
                    process_data()
                print("¡Canción modificada exitosamente!")
                guardar_datos(playlist)
                ver_playlist()
                gestion_musica()
def agregar_cancion():
    global playlist
    ultimo_puesto = playlist[len(playlist) - 1]
    print("----- Agregar Canción -----")
    titulo = input("Ingrese el título de la canción: ")
    artista = input("Ingrese el nombre del artista: ")
    idioma=input("Ingrese el Idioma de la cancion: ")
    puesto = ultimo_puesto.get("Puesto") + 1
    cancion = {
        "Puesto": puesto,
        "Titulo": titulo,
        "Artista": artista,
        "Idioma":idioma
         }
    playlist.append(cancion)
    for _ in track(range(100), description='[green]Procesando Informacion'):
        process_data()
    print("¡Canción agregada exitosamente!")
    guardar_datos(playlist)
    ver_playlist()
    gestion_musica()
def cargar_datos():
    try:
        with open('playlist.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
def guardar_datos(playlist):
    with open('playlist.json', 'w') as archivo:
        json.dump(playlist, archivo, indent=4)
    archivo.close()
def process_data():
            sleep(0.02)
            
def eliminar():
    print("----- Eliminar Canción -----")
    ver_playlist()
    puesto = int(input("Ingrese el puesto de la canción a eliminar: "))
    for titulo in playlist:
        if titulo["Puesto"] == puesto:
            playlist.remove(titulo)
            for _ in track(range(100), description='[green]Procesando Informacion'):
                process_data()
            print("¡Canción eliminada exitosamente!")
            guardar_datos(playlist) 
            ver_playlist()      
            gestion_musica()
def error():
    print("Ingreso un dato incorrecto y el programa no puede continuar")   
    print ("* "*40)
    gestion_musica()
def reportes():
    console.print("""[bold magenta]
    𝄞 𝄞 𝄞   1) Ver playlist       𝄞 𝄞 𝄞
    𝄞 𝄞 𝄞   2) Por Idioma Ingles  𝄞 𝄞 𝄞
    𝄞 𝄞 𝄞   3) Por Idioma Español 𝄞 𝄞 𝄞
    𝄞 𝄞 𝄞   0) Salir              𝄞 𝄞 𝄞[bold blue]""")
    print ("* "*40)
    opcion_usuario=int(input("Ingrese la opcion deseada: "))
    match opcion_usuario:
        case 1:
            ver_playlist()
            gestion_musica()
        case 2:
            reporte_ingles()
        case 3: 
            reporte_español()
        case 0: 
            print("Gracias por Usar nuastra Playlist")
def reporte_ingles():
    print("Las canciones en ingles son ..")
    from rich.console import Console
    from rich.table import Table
    import json

    with open('playlist.json') as file:
        data = json.load(file)

    console = Console()
    table = Table(show_header=True, header_style="bold Green")
    table.add_column("Puesto", style="dim", width=12)
    table.add_column("Titulo")
    table.add_column("Artista", justify="right")
    table.add_column("Idioma", justify="right")

    for item in data:
        idioma = item.get('Idioma', '')
        if idioma.lower() == 'ingles':
            puesto = item.get('Puesto', '')
            titulo = item.get('Titulo', '')
            artista = item.get('Artista', '')
            table.add_row(str(puesto), titulo, artista, idioma)

    console.print(table)
    gestion_musica()
def reporte_español():
    print("        Las canciones en Espanol son..")
    from rich.console import Console
    from rich.table import Table
    import json
    with open('playlist.json') as file:
        data = json.load(file)
    console = Console()
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Puesto", style="dim", width=12)
    table.add_column("Titulo")
    table.add_column("Artista", justify="right")
    table.add_column("Idioma", justify="right")

    for item in data:
        idioma = item.get('Idioma', '')
        if idioma.lower() == 'espanol':
            puesto = item.get('Puesto', '')
            titulo = item.get('Titulo', '')
            artista = item.get('Artista', '')
            table.add_row(str(puesto), titulo, artista,idioma)

    console.print(table)
    gestion_musica()

    
nombre_usuario = str (input("        Por favor ingrese su nombre: "))
console.print ("*"*50)
edad_usuario = int(input("        Por favor ingrese su edad: ")) 
edad_usuario >= 18
print ("♫ 𝄞 ♪ "*10)

if edad_usuario>=18:
    console.print("            Bienvenid@ [bold green]{}[/bold green] al TOP TEN 2023".format(nombre_usuario))
    gestion_musica()
    opcion = int(input("            Ingrese la opción que desea realizar: "))
else:
    console.print("         Bienveni@ [bold green]{}[/bold green], debe ser mayor de 18 años para poder utilizar este programa".format(nombre_usuario))
    print("")
    console.print("            Gracias por Ingresar a Nuestra Playlist")
    print("* " * 40)
