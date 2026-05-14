import os
import pandas as pd

archivo = input("Selecciona la ubicación del archivo: ")
nombre_archivo = os.path.splitext(os.path.basename(archivo))[
    0]  # Nombre del archivo sin extensión


df = pd.read_excel(archivo)

print("\n Datos cargados:")
print(df.head())

df.columns = df.columns.str.lower()  # Normalizamos las columnas

if "ventas" in df.columns:
    total = df["ventas"].sum()
    promedio = df["ventas"].mean()

    print("\n\n Resumen")
    print(f"Total en ventas: {total}")
    print(f"promedio de ventas: {promedio}")

    # Creamos un nuevo archivo con el resumen
    resumen = pd.DataFrame(
        {"Métrica": ["Total", "Promedio"], "Valor": [total, promedio]})

    # Guardar el archivo nuevo
    carpeta = os.path.dirname(archivo)
    salida = os.path.join(carpeta, f"resumen_{nombre_archivo}.xlsx")
    resumen.to_excel(salida, index=False)

    if os.path.exists(salida):
        print("El archivo ya existe, se sobrescribirá")

    print(f"\nArchivo generado: {salida} 🚀")

else:
    print("No se encontró la columna de \"Ventas\"")
