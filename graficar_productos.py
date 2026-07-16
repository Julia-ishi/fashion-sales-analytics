import os

import matplotlib.pyplot as plt
import pandas as pd


ruta_archivo = "data/raw/productos.csv"
carpeta_graficos = "graficos"

# Crear la carpeta graficos si todavía no existe
os.makedirs(carpeta_graficos, exist_ok=True)

# Leer los productos
productos = pd.read_csv(ruta_archivo)


# GRÁFICO 1: cantidad de productos por categoría

cantidad_por_categoria = (
    productos["categoria"]
    .value_counts()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

cantidad_por_categoria.plot(kind="bar")

plt.title("Cantidad de productos por categoría")
plt.xlabel("Categoría")
plt.ylabel("Cantidad de productos")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    os.path.join(carpeta_graficos, "productos_por_categoria.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# GRÁFICO 2: precios de los productos

productos_ordenados = productos.sort_values(
    by="precio",
    ascending=True
)

plt.figure(figsize=(10, 6))

plt.barh(
    productos_ordenados["nombre"],
    productos_ordenados["precio"]
)

plt.title("Precios de los productos")
plt.xlabel("Precio")
plt.ylabel("Producto")
plt.tight_layout()

plt.savefig(
    os.path.join(carpeta_graficos, "precios_productos.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()

print("Los gráficos se guardaron correctamente en la carpeta 'graficos'.")