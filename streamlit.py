import streamlit as st
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


data = pd.read_csv("iris.csv")

y = data["species"] #Series contenant la colonne species
X = data.drop("species", axis=1) #Dataframe auquel on supprime la colonne species

knn = KNeighborsClassifier(n_neighbors=5)

#Séparation des données contenues dans X & y dans des variables _train & _test, séparés en 80% & 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

knn.fit(X_train, y_train) #Entrainement des données


st.title("Trouvez votre espèce")

#Choix utilisateur
longueur_sepale = st.slider("Choisissez la longueur de la sépale", 4.0, 8.0)
largeur_sepale = st.slider("Choisissez la largeur de la sépale", 2.0, 4.5)
longueur_petale = st.slider("Choisissez la longueur de la pétale", 1.0, 7.0)
largeur_petale = st.slider("Choisissez la largeur de la pétale", 0.0, 2.5)

#Espèce de l'utilisateur
inconnue_utilisateur = [longueur_sepale, largeur_sepale, longueur_petale, largeur_petale]
espece_utilisateur = knn.predict([inconnue_utilisateur])


#Dico choix utilisateur pour le dataframe et le graphique
choix_utilisateur = {
    "sepal_length" : [longueur_sepale],
    "sepal_width" : [largeur_sepale],
    "petal_length" : [longueur_petale],
    "petal_width" : [largeur_petale],
    "species" : "Votre iris"
}


#Création dataframe choix_utilisateur et concaténation avec le dataframe du csv
dataframe_choix_utilisateur = pd.DataFrame(choix_utilisateur)
dataframe_final = pd.concat([data, dataframe_choix_utilisateur], axis=0)

#Affichage du bouton, puis de l'espèce et des 2 graph sur les sépales et pétales
if st.button("Déterminez votre iris"):
    st.success("Votre espèce est : " + espece_utilisateur[0])
    st.pyplot(sns.pairplot(dataframe_final, x_vars=["petal_length"], y_vars=["petal_width"], hue="species", markers=["o", "s", "D", "p"]))
    st.pyplot(sns.pairplot(dataframe_final, x_vars=["sepal_length"], y_vars=["sepal_width"], hue="species", markers=["o", "s", "D", "p"]))