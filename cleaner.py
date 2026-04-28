import csv

def limpiar_csv(archivo_entrada, archivo_salida):
    print(f"Limpiando {archivo_entrada}...")
    
    try:
        con_datos = []
        vistos = set() # Para detectar duplicados

        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            lector = csv.reader(f)
            for fila in lector:
                # 1. Eliminar filas vacías
                if not any(celda.strip() for celda in fila):
                    continue
                
                # 2. Eliminar duplicados
                fila_tupla = tuple(fila)
                if fila_tupla not in vistos:
                    vistos.add(fila_tupla)
                    con_datos.append(fila)

        with open(archivo_salida, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerows(con_datos)
            
        print(f"¡Listo! Archivo guardado como: {archivo_salida}")
        print(f"Filas procesadas: {len(con_datos)}")

    except FileNotFoundError:
        print("Error: El archivo de entrada no existe.")

if __name__ == "__main__":
    # Para probarlo necesitas un archivo .csv en la misma carpeta
    limpiar_csv("datos_sucios.csv", "datos_limpios.csv")
