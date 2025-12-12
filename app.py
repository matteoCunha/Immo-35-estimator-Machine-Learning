import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

st.set_page_config(
    page_title="Immo 35 - Estimateur IA",
    page_icon="🏠",
    layout="centered"
)

@st.cache_resource
def load_model():
    try:
        return joblib.load('modele_immo.pkl')
    except FileNotFoundError:
        st.error("❌ Le fichier 'modele_immo.pkl' est introuvable. Mettez-le dans le même dossier !")
        return None

model = load_model()

VILLES = {
    "Rennes": {"x": 352500, "y": 6789000},
    "Saint-Malo": {"x": 337500, "y": 6850000},
    "Bruz": {"x": 348000, "y": 6782000},
    "Cesson-Sévigné": {"x": 358000, "y": 6791000},
    "Vitré": {"x": 385000, "y": 6792000},
    "Fougères": {"x": 371000, "y": 6815000},
    "Redon": {"x": 328000, "y": 6745000},
    "Dinard": {"x": 335000, "y": 6848000},
    "Pacé": {"x": 348000, "y": 6794000},
    "Betton": {"x": 355000, "y": 6798000},
    "Saint-Grégoire": {"x": 353000, "y": 6793000},
    "Chantepie": {"x": 356000, "y": 6786000}
}

CENTRE_RENNES = {"x": 352500, "y": 6789000}
CENTRE_ST_MALO = {"x": 337500, "y": 6850000}

st.title("🏡 Estimateur Immobilier - IA")
st.write("Entrez les caractéristiques du bien pour obtenir une estimation immédiate par IA.")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    ville_choisie = st.selectbox("📍 Ville", list(VILLES.keys()))
    type_bien = st.selectbox("Type de bien", options=['Maison', 'Appartement'])
    cat_mapping = {'Maison': 'House', 'Appartement': 'Condo'}
    surface = st.number_input("📏 Surface habitable (m²)", min_value=9, max_value=399, value=80)

with col2:
    n_rooms = st.number_input("🚪 Nombre de pièces", min_value=1, max_value=32, value=4)
    terrain = st.number_input("🌳 Surface Terrain (m²)", min_value=0, max_value=10000, value=500)
    annee_actuelle = datetime.now().year
    mois_actuel = datetime.now().month

if st.button("💰 Estimer le prix", type="primary"):
    if model:
        x_user = VILLES[ville_choisie]['x']
        y_user = VILLES[ville_choisie]['y']

        dist_rennes = (np.sqrt((x_user - CENTRE_RENNES['x'])**2 + (y_user - CENTRE_RENNES['y'])**2))/1000
        dist_st_malo = (np.sqrt((x_user - CENTRE_ST_MALO['x'])**2 + (y_user - CENTRE_ST_MALO['y'])**2))/1000

        taille_moyenne_piece = surface/n_rooms
        densite_jardin_calc = terrain/(surface + 1) # evite la division par 0

        input_data = pd.DataFrame([[
            x_user,
            y_user,
            cat_mapping[type_bien],
            surface,
            terrain,
            n_rooms,
            dist_rennes,
            dist_st_malo,
            annee_actuelle,
            mois_actuel,
            taille_moyenne_piece,
            densite_jardin_calc,
        ]], columns=[
            'x_lbt93', 'y_lbt93', 'category', 'area_living', 'area_land',
            'n_rooms', 'd_rennes', 'd_st_malo', 'annee_vente',
            'mois_vente', 'taille_moyenne_piece', 'densite_jardin'
        ])

        try:
            prix_estime = model.predict(input_data)[0]
            st.success(f"Estimation : {prix_estime:,.0f} €")
            st.info(f"Analyse : ce bien est situé à {dist_rennes:.1f} km de Rennes")

        except Exception as e:
            st.error(f"Erreur lors de la prédiction : {e}")
            st.write(f"Détail de la donnée envoyée : {input_data}")