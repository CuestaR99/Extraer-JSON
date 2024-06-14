''' 
Programa que permite extraer los archivos Json que se descargan del chat de Soporte.
Archivo para extraer cualquier archivo dentro de archivos comprimidos. 
Importamos librerias
'''
import os
import zipfile

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
#nombre del archivo .zip
archivo_zip = "Nombre_Archivo.zip"      #Importante dejar la extencion .zip
#Ruta carpeta extraer archivos JSON
carpeta_destino = "C:\\ruta\\carpeta\\guardar\\archivos\\JSON"

extraer_archivos_recursivamente(archivo_zip, carpeta_destino)
