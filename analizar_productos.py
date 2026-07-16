import pandas as pd


# Ruta del archivo que contiene los productos
ruta_archivo = "data/raw/productos.csv"


# Leer el archivo CSV y guardarlo como una tabla de pandas
productos = pd.read_csv(ruta_archivo)


# Limpiar espacios innecesarios en las columnas de texto
productos["nombre"] = productos["nombre"].str.strip()
productos["categoria"] = productos["categoria"].str.strip().str.lower()
productos["estado"] = productos["estado"].str.strip().str.lower()


# Convertir precio y stock a valores numéricos
productos["precio"] = pd.to_numeric(
    productos["precio"],
    errors="coerce"
)

productos["stock_disponible"] = pd.to_numeric(
    productos["stock_disponible"],
    errors="coerce"
)


# Mostrar la tabla completa
print("TABLA DE PRODUCTOS")
print("-" * 70)
print(productos.to_string(index=False))


# Mostrar información general del dataset
print("\nINFORMACIÓN DEL DATASET")
print("-" * 70)
productos.info()


# Revisar valores faltantes
print("\nVALORES FALTANTES POR COLUMNA")
print("-" * 70)
print(productos.isnull().sum())


# Revisar filas duplicadas
cantidad_duplicados = productos.duplicated().sum()

print("\nFILAS DUPLICADAS")
print("-" * 70)
print("Cantidad de filas duplicadas:", cantidad_duplicados)


# Calcular métricas generales
cantidad_productos = len(productos)

cantidad_disponibles = len(
    productos[productos["estado"] == "disponible"]
)

cantidad_sin_stock = len(
    productos[productos["estado"] == "sin stock"]
)

precio_promedio = productos["precio"].mean()

valor_total_stock = (
    productos["precio"] * productos["stock_disponible"]
).sum()


# Mostrar el resumen general
print("\nRESUMEN GENERAL")
print("-" * 70)
print("Cantidad total de productos:", cantidad_productos)
print("Productos disponibles:", cantidad_disponibles)
print("Productos sin stock:", cantidad_sin_stock)
print("Precio promedio: $", round(precio_promedio, 2))
print("Valor total del stock disponible: $", valor_total_stock)


# Buscar el producto más caro y el más barato
if not productos.empty:
    producto_mas_caro = productos.loc[
        productos["precio"].idxmax()
    ]

    producto_mas_barato = productos.loc[
        productos["precio"].idxmin()
    ]

    print("\nPRECIOS DESTACADOS")
    print("-" * 70)

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


# Contar productos por categoría
productos_por_categoria = (
    productos["categoria"]
    .value_counts()
    .sort_values(ascending=False)
)

print("\nCANTIDAD DE PRODUCTOS POR CATEGORÍA")
print("-" * 70)
print(productos_por_categoria)


# Calcular el precio promedio por categoría
precio_promedio_categoria = (
    productos
    .groupby("categoria")["precio"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

print("\nPRECIO PROMEDIO POR CATEGORÍA")
print("-" * 70)
print(precio_promedio_categoria)


# Mostrar solamente los productos disponibles
productos_disponibles = productos[
    productos["estado"] == "disponible"
]

print("\nPRODUCTOS DISPONIBLES")
print("-" * 70)

if productos_disponibles.empty:
    print("No hay productos disponibles.")
else:
    print(
        productos_disponibles[
            ["id_producto", "nombre", "categoria", "precio"]
        ].to_string(index=False)
    )


# Mostrar solamente los productos sin stock
productos_sin_stock = productos[
    productos["estado"] == "sin stock"
]

print("\nPRODUCTOS SIN STOCK")
print("-" * 70)

if productos_sin_stock.empty:
    print("No hay productos sin stock.")
else:
    print(
        productos_sin_stock[
            ["id_producto", "nombre", "categoria", "precio"]
        ].to_string(index=False)
    )


# Ordenar los productos desde el más caro hasta el más barato
productos_ordenados = productos.sort_values(
    by="precio",
    ascending=False
)

print("\nPRODUCTOS ORDENADOS POR PRECIO")
print("-" * 70)

print(
    productos_ordenados[
        ["nombre", "categoria", "precio", "estado"]
    ].to_string(index=False)
)