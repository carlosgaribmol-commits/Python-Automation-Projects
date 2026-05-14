import os

# Pedir la ruta de la carpeta
carpeta = input("Ingresa la ruta: ")

# Obtener lista de archivos
archivos = os.listdir(carpeta)

contador = 1

for archivo in archivos:
    if archivo.endswith(".pdf"):
        nuevo_nombre = f"Factura_{contador:03}.pdf"
        
        ruta_vieja = os.path.join(carpeta, archivo)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)
        
        os.rename(ruta_vieja, ruta_nueva)
        
        contador += 1

print("Archivos renombrados correctamente 🚀")