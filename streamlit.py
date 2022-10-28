import streamlit as st
import pandas as pd
import numpy as np

longueur_sepal = st.slider("Choisissez la longueur de la sépale", 4.0, 8.0)
largeur_sepal = st.slider("Choisissez la largeur de la sépale", 2.0, 4.5)
longueur_petale = st.slider("Choisissez la longueur de la pétale", 1.0, 7.0)
largeur_petale = st.slider("Choisissez la largeur de la pétale", 0.0, 2.5)

st.map