import streamlit as st
import pandas as pd

# Chemin d'accès complet du fichier CSV
path = r"data\fr-esr-patrimoine-immobilier-des-operateurs-de-l-enseignement-superieur (3).csv"

# Lire le fichier CSV dans un DataFrame
data = pd.read_csv(path, sep=";", low_memory=False)

# Afficher les 10 premières lignes du DataFrame dans Streamlit
st.write(data.head(10))
