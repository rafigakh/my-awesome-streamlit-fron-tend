import streamlit as st
import pandas as pd

data = pd.read_csv("fr-esr-patrimoine-immobilier-des-operateurs-de-l-enseignement-superieur (3).csv", sep=";", low_memory=False)
# Afficher les 10 premières lignes du DataFrame dans Streamlit
st.write(data.head(10))