#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:15:55 2025

@author: juan
"""

import streamlit as st

# Configuración de la app
st.set_page_config(page_title="Chin Chin - Tu Sumiller Virtual", page_icon="🍷", layout="centered")

# Estado de sesión
if 'bodega' not in st.session_state:
    st.session_state.bodega = []
if 'favoritos' not in st.session_state:
    st.session_state.favoritos = []
if 'supermercado_vinos' not in st.session_state:
    st.session_state.supermercado_vinos = [
    ("Lidl", "Cepa Lebrel Crianza - 4,80€"),
    ("Lidl", "Winemaker's Selection Rioja - 6,50€"),
    ("Lidl", "Borgoña Rosado - 5,30€"),
    ("Lidl", "Aromo Reserva Privada - 7,20€"),
    ("Lidl", "Barón de Ley Blanco - 8,90€"),
    ("Lidl", "Aresti Trisquel - 12,00€"),
    ("Lidl", "Llumí Blanc - 10,50€"),
    ("Mercadona", "Castillo de Liria - 3,20€"),
    ("Mercadona", "Casa de la Ermita Roble - 7,90€"),
    ("Mercadona", "Señorío de Iniesta Blanco - 2,90€"),
    ("Mercadona", "Hoya de Cadenas Reserva - 6,40€"),
    ("Mercadona", "Viña Decana Crianza - 5,60€"),
    ("Mercadona", "Cepa Lebrel Verdejo - 4,75€"),
    ("Mercadona", "Marqués del Atrio Crianza - 8,50€"),
    ("Carrefour", "Viña Albali Reserva - 6,95€"),
    ("Carrefour", "Ramón Bilbao Crianza - 9,50€"),
    ("Carrefour", "Marqués de Cáceres Verdejo - 5,75€"),
    ("Carrefour", "Barbadillo Castillo de San Diego - 4,25€"),
    ("Carrefour", "Finca Resalso - 11,90€"),
    ("Carrefour", "Pata Negra Reserva - 6,60€"),
    ("Carrefour", "La Planta - 10,50€"),
    ("Carrefour", "Cune Verdejo - 5,90€"),
    ("Alcampo", "Protos Roble - 11,00€"),
    ("Alcampo", "Marqués de Riscal Reserva - 17,00€"),
    ("Alcampo", "Cune Crianza - 6,80€"),
    ("Alcampo", "Viña Pomal Crianza - 8,30€"),
    ("Alcampo", "Beronia Crianza - 9,00€"),
    ("Alcampo", "Lan D-12 - 13,00€"),
    ("Alcampo", "Lagar de Cervera Albariño - 15,00€"),
    ("El Corte Inglés", "Enate Chardonnay - 14,00€"),
    ("El Corte Inglés", "Pago de Carraovejas - 49,00€"),
    ("El Corte Inglés", "Abadía Retuerta Selección Especial - 38,00€"),
    ("El Corte Inglés", "Valduero Una Cepa - 30,00€"),
    ("El Corte Inglés", "Dominio de Tares Cepas Viejas - 20,00€"),
    ("El Corte Inglés", "Tarsus Reserva - 25,00€"),
    ("El Corte Inglés", "Torres Celeste Crianza - 12,00€"),
    ("El Corte Inglés", "Viñas del Vero Gewürztraminer - 10,00€"),
    ("El Corte Inglés", "Albariño Martín Códax - 13,90€")
]

# === FUNCIONES ===

def mostrar_planes():
    st.markdown("## 🧾 Planes de suscripción")
    st.info("""
    **Plan 1 – Gratis**  
    - Comparación de vinos en supermercados  
    - Acceso a rankings  
    - 3 recomendaciones semanales  

    **Plan 2 – 9,99€/mes**  
    - Recomendaciones ilimitadas  
    - Registro y control de bodega  

    **Plan 3 – 24,99€/mes**  
    - Todo lo anterior  
    - Pack mensual de 3 vinos  
    - Catas virtuales  

    **Plan 4 – 49,99€/mes**  
    - Todo lo anterior  
    - Acceso a eventos y visitas a bodegas  
    - Descuentos en vinos y actividades  
    """)

def recomendaciones_comida(plan):
    st.subheader("🍽️ ¿Qué estás comiendo?")
    comida = st.selectbox("Tipo de comida", [
        "Carne roja", "Carne blanca", "Pescado", "Marisco",
        "Pasta con salsa", "Quesos fuertes", "Quesos suaves", "Dulces",
        "Ensaladas", "Vegetariano", "Barbacoa"
    ])

    recomendaciones = {
        "Carne roja": "Cabernet Sauvignon, Syrah, Ribera del Duero",
        "Carne blanca": "Garnacha suave, Chardonnay con barrica",
        "Pescado": "Albariño, Verdejo, Godello",
        "Marisco": "Rías Baixas, Sauvignon Blanc",
        "Pasta con salsa": "Chianti, Tempranillo joven",
        "Quesos fuertes": "Oporto, Syrah",
        "Quesos suaves": "Rosado seco o Chardonnay",
        "Dulces": "Moscatel, PX, cava semiseco",
        "Ensaladas": "Verdejo, rosado joven",
        "Vegetariano": "Pinot Noir, Riesling",
        "Barbacoa": "Zinfandel, Malbec"
    }

    st.success(f"🍷 Recomendación: {recomendaciones[comida]}")
    if plan != "Gratis" and st.button("Guardar en favoritos"):
        st.session_state.favoritos.append(f"{comida}: {recomendaciones[comida]}")
        st.toast("¡Añadido a favoritos!")

def gestion_bodega(plan):
    if plan in ["9,99€/mes", "24,99€/mes", "49,99€/mes"]:
        st.subheader("📦 Tu Bodega Personal")
        for vino in st.session_state.bodega:
            st.write(f"🍾 {vino}")
        nuevo = st.text_input("Añadir vino")
        if st.button("Agregar"):
            if nuevo:
                st.session_state.bodega.append(nuevo)
                st.success(f"'{nuevo}' añadido a tu bodega.")
            else:
                st.warning("Introduce un nombre válido.")
    else:
        st.warning("Función disponible a partir del Plan 2.")

def comparar_supermercados():
    st.subheader("🛒 Comparativa de Vinos en Supermercados")
    supermercado = st.selectbox("Supermercado", ["Mercadona", "Carrefour", "Lidl", "Alcampo", "Otros"])
    precio = st.slider("Selecciona el rango de precio (€)", 2, 20, (5, 15))

    st.write(f"Mostrando vinos en **{supermercado}** entre **{precio[0]}€ y {precio[1]}€**:")
    for tienda, vino in st.session_state.supermercado_vinos:
        if tienda == supermercado:
            st.write(f"**{tienda}** → {vino}")
    st.info("🍷 *Ejemplos ficticios de resultados filtrados según supermercado y precio.*")

def buscar_por_tipo_precio():
    st.subheader("🔎 Buscar por tipo y precio")
    tipo = st.selectbox("Tipo de vino", ["Tinto", "Blanco", "Rosado", "Espumoso", "Dulce"])
    precio = st.slider("Rango de precio (€)", 3, 50, (6, 20))

    st.write(f"Resultados para **{tipo.lower()}s** entre {precio[0]}€ y {precio[1]}€:")
    st.success("🍾 Ejemplo: Marqués de Cáceres Crianza (9,50€), Protos Roble (11€), Enate Chardonnay (14€)")

def ver_favoritos():
    st.subheader("⭐ Favoritos")
    if st.session_state.favoritos:
        for fav in st.session_state.favoritos:
            st.write(f"👉 {fav}")
    else:
        st.info("No tienes favoritos guardados.")

def suscripcion_mensual(plan):
    if plan in ["24,99€/mes", "49,99€/mes"]:
        st.success("""
        Tu pack mensual de 3 vinos está en camino.  
        Incluye cata virtual con nota de cata y maridaje.
        """)
    else:
        st.warning("Disponible desde el Plan 3.")

def actividades_y_visitas(plan):
    if plan == "49,99€/mes":
        st.balloons()
        st.markdown("""
        ### 🍇 Próximas experiencias
        - Visita a bodega en Ribera del Duero – 12 de mayo  
        - Cata sensorial avanzada – 25 de mayo  
        - Degustación premium con maridaje – 2 de junio  
        **Descuento aplicado automáticamente.**
        """)
    else:
        st.warning("Disponible solo para el Plan 4.")

# === APP ===

st.title("🍷 Chin Chin – Tu Sumiller Virtual para Particulares")

mostrar_planes()

plan = st.selectbox("Selecciona tu plan actual", ["Gratis", "9,99€/mes", "24,99€/mes", "49,99€/mes"])

seccion = st.radio("¿Qué quieres hacer?", [
    "📌 Recomendaciones por comida",
    "📦 Mi bodega",
    "⭐ Favoritos",
    "📬 Suscripción mensual",
    "🎟️ Actividades y eventos",
    "🛒 Comparar vinos de supermercado",
    "🔎 Buscar por tipo y precio"
])

if seccion == "📌 Recomendaciones por comida":
    recomendaciones_comida(plan)

elif seccion == "📦 Mi bodega":
    gestion_bodega(plan)

elif seccion == "⭐ Favoritos":
    ver_favoritos()

elif seccion == "📬 Suscripción mensual":
    suscripcion_mensual(plan)

elif seccion == "🎟️ Actividades y eventos":
    actividades_y_visitas(plan)

elif seccion == "🛒 Comparar vinos de supermercado":
    comparar_supermercados()

elif seccion == "🔎 Buscar por tipo y precio":
    buscar_por_tipo_precio()