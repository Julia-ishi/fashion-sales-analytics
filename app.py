import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Fashion Sales Analytics",
    page_icon="🛍️",
    layout="wide"
)


ruta_archivo = "data/raw/productos.csv"

productos = pd.read_csv(ruta_archivo)


st.title("Fashion Sales Analytics")

st.write(
    "Panel de análisis de productos, precios y stock "
    "del emprendimiento Fashion Junko."
)


# -----------------------------
# FILTRO POR CATEGORÍA
# -----------------------------

categorias = sorted(productos["categoria"].unique())

categoria_seleccionada = st.sidebar.selectbox(
    "Seleccionar categoría",
    ["Todas"] + categorias
)


if categoria_seleccionada == "Todas":
    productos_filtrados = productos
else:
    productos_filtrados = productos[
        productos["categoria"] == categoria_seleccionada
    ]


# -----------------------------
# MÉTRICAS
# -----------------------------

cantidad_productos = len(productos_filtrados)

cantidad_disponibles = len(
    productos_filtrados[
        productos_filtrados["estado"] == "disponible"
    ]
)

cantidad_sin_stock = len(
    productos_filtrados[
        productos_filtrados["estado"] == "sin stock"
    ]
)

precio_promedio = productos_filtrados["precio"].mean()

valor_total_stock = (
    productos_filtrados["precio"]
    * productos_filtrados["stock_disponible"]
).sum()


columna_1, columna_2, columna_3, columna_4 = st.columns(4)

columna_1.metric(
    "Productos totales",
    cantidad_productos
)

columna_2.metric(
    "Disponibles",
    cantidad_disponibles
)

columna_3.metric(
    "Sin stock",
    cantidad_sin_stock
)

columna_4.metric(
    "Precio promedio",
    f"${precio_promedio:,.2f}"
)


# -----------------------------
# TABLA
# -----------------------------

st.subheader("Catálogo de productos")

st.dataframe(
    productos_filtrados,
    use_container_width=True
)


# -----------------------------
# VALOR DEL STOCK
# -----------------------------

st.subheader("Valor total del stock")

st.write(
    f"${valor_total_stock:,.2f}"
)


# -----------------------------
# GRÁFICOS
# -----------------------------

st.subheader("Visualizaciones")

columna_grafico_1, columna_grafico_2 = st.columns(2)


with columna_grafico_1:
    st.write("Productos por categoría")

    productos_por_categoria = (
        productos["categoria"]
        .value_counts()
    )

    st.bar_chart(productos_por_categoria)


with columna_grafico_2:
    st.write("Precios de los productos")

    precios_productos = (
        productos_filtrados[
            ["nombre", "precio"]
        ]
        .set_index("nombre")
    )

    st.bar_chart(precios_productos)