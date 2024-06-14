import os
import zipfile
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

def extraer_archivos_recursivamente(archivo_zip, carpeta_destino):
    try:
        with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
            for nombre_archivo in zip_ref.namelist():
                if not nombre_archivo.endswith('/'):  # Ignorar las entradas de directorio
                    # Extraer el nombre del archivo
                    nombre_archivo_uno = os.path.basename(nombre_archivo)
                    # Construir la ruta completa del archivo destino
                    ruta_completa_archivo = os.path.join(carpeta_destino, nombre_archivo_uno)
                    # Extraer el archivo
                    with zip_ref.open(nombre_archivo) as archivo_zipado, open(ruta_completa_archivo, 'wb') as archivo_destino:
                        archivo_destino.write(archivo_zipado.read())
                    print(f"Archivo '{nombre_archivo_uno}' extraído a '{carpeta_destino}'.")

    except Exception as e:
        print(f"Error: {e}")

def buscar_archivo_zip(nombre_archivo):
    # Recorre recursivamente el árbol de directorios en busca del archivo ZIP
    for directorio_actual, _, archivos in os.walk(os.getcwd()):
        for archivo in archivos:
            if archivo.startswith(nombre_archivo) and archivo.endswith('.zip'):
                return os.path.join(directorio_actual, archivo)
    return None

def obtener_nombre_archivo():
    return simpledialog.askstring("Nombre de archivo", "Ingrese el nombre del archivo ZIP")

def seleccionar_carpeta_destino():
    return filedialog.askdirectory(title="Seleccione la carpeta destino para extraer los archivos")

def main():
    # Solicitar al usuario el nombre del archivo ZIP (sin la extensión .zip)
    nombre_archivo_zip = obtener_nombre_archivo()

    if nombre_archivo_zip is None:
        print("No se proporcionó un nombre de archivo.")
        return

    # Agregar la extensión .zip al nombre del archivo
    nombre_archivo_zip += '.zip'

    # Buscar el archivo ZIP en el directorio actual y sus subdirectorios
    archivo_zip = buscar_archivo_zip(nombre_archivo_zip)
    if archivo_zip is None:
        print(f"El archivo '{nombre_archivo_zip}' No se reconoce como archivo .ZIP")
        return

    # Solicitar al usuario la carpeta destino
    carpeta_destino = seleccionar_carpeta_destino()

    if carpeta_destino == "":
        print("No se seleccionó ninguna carpeta destino.")
        return

    # Extraer archivos recursivamente
    extraer_archivos_recursivamente(archivo_zip, carpeta_destino)

if __name__ == "__main__":
    main()
