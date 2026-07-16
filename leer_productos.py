import csv

ruta_archivo = "data/raw/productos.csv"

cantidad_productos = 0
cantidad_disponibles = 0
cantidad_sin_stock = 0

suma_precios = 0
valor_total_disponible = 0

producto_mas_caro = None
producto_mas_barato = None

with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    print("LISTADO DE PRODUCTOS")
    print("-" * 60)

    for producto in lector:
        precio = int(producto["precio"])
        stock = int(producto["stock_disponible"])

        print(
            f'{producto["id_producto"]} | '
            f'{producto["nombre"]} | '
            f'${precio} | '
            f'{producto["estado"]}'
        )

        cantidad_productos += 1
        suma_precios += precio

        if producto["estado"] == "disponible":
            cantidad_disponibles += 1
            valor_total_disponible += precio * stock

        if producto["estado"] == "sin stock":
            cantidad_sin_stock += 1

        if producto_mas_caro is None or precio > int(producto_mas_caro["precio"]):
            producto_mas_caro = producto

        if producto_mas_barato is None or precio < int(producto_mas_barato["precio"]):
            producto_mas_barato = producto

print("-" * 60)

if cantidad_productos > 0:
    precio_promedio = suma_precios / cantidad_productos

    print("RESUMEN DEL CATÁLOGO")
    print("Cantidad total de productos:", cantidad_productos)
    print("Productos disponibles:", cantidad_disponibles)
    print("Productos sin stock:", cantidad_sin_stock)
    print("Precio promedio:", round(precio_promedio, 2))
    print("Valor total del stock disponible:", valor_total_disponible)
    print(
        "Producto más caro:",
        producto_mas_caro["nombre"],
        "- $",
        producto_mas_caro["precio"]
    )
    print(
        "Producto más barato:",
        producto_mas_barato["nombre"],
        "- $",
        producto_mas_barato["precio"]
    )
else:
    print("No hay productos cargados.")
# Este código abre el archivo productos.csv, lee cada fila como un diccionario y la muestra en la terminal. 