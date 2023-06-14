#!/usr/bin/env python
# coding: utf-8

# # Etablissement Superieur français

# In[3]:


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

# Chemin d'accès complet du fichier CSV
path = r"data\fr-esr-patrimoine-immobilier-des-operateurs-de-l-enseignement-superieur (3).csv"

# Lire le fichier CSV dans un DataFrame
data = pd.read_csv(path, sep=";", low_memory=False)

# Chemin d'accès complet du fichier CSV
path = r"data\fr-esr-patrimoine-immobilier-des-operateurs-de-l-enseignement-superieur (3).csv"

# Lire le fichier CSV dans un DataFrame
data = pd.read_csv(path, sep=";", low_memory=False)

# Count the number of buildings by type of usage and sort in descending order
building_usage_counts = data['type_bat'].value_counts().sort_values(ascending=False)

# Generate a color map based on the number of bars
color_map = plt.cm.cividis_r(np.linspace(0, 1, len(building_usage_counts)))

# Create a figure and axis using Streamlit
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the horizontal bar chart with different colors based on descending order
ax.barh(building_usage_counts.index, building_usage_counts.values, color=color_map)

# Set the axis labels and title
ax.set_xlabel('Number of Buildings')
ax.set_ylabel('Type of Usage')
ax.set_title('Number of Buildings by Type of Usage')
ax.invert_yaxis()
# Display the chart using Streamlit
st.pyplot(fig)

