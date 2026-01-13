# 🏡 Estimateur Immobilier Ille-et-Vilaine (35)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://immo-estimator.streamlit.app/)

## Description du projet

Une application de Data Science interactive permettant d'estimer le prix de vente de maisons et d'appartements en Ille-et-Vilaine grâce au Machine Learning.

🔗 **[Accéder à l'application en ligne](https://immo-estimator.streamlit.app/)**
L'application peut nécessiter jusqu'à une minute pour être pleinement opérationnelle. Ce délai correspond au chargement du modèle et des différents composants techniques.

### 📋 Contexte et Objectifs
Ce projet a pour but de prédire la **valeur vénale** d'un bien immobilier en se basant sur ses caractéristiques intrinsèques (surface, pièces, terrain) et sa localisation géographique.
Le modèle a été entraîné sur des données réelles de transactions immobilières dans le département 35. Il intègre un feature engineering spatial calculant notamment la distance aux pôles économiques majeurs (Rennes et Saint-Malo).
* **Source du Dataset (Kaggle) :** [Housing Prices 35 FR](https://www.kaggle.com/datasets/cheneblanc/housing-prices-35-fr)

> **Pourquoi ce département ?**
> Ce projet privilégie l'utilisation de **données réelles** plutôt que synthétiques. Bien que j'aie initialement envisagé d'analyser Paris ou Bordeaux, les datasets disponibles étaient majoritairement générés par IA. J'ai donc sélectionné ce département car il offrait un jeu de données authentique, permettant une véritable analyse exploratoire.

### 🧠 Performance du modèle
Le moteur de prédiction repose sur un algorithme de **Random Forest Regressor** optimisé.

* **Score R² :** ~0.75
* **Précision moyenne (MAPE) :** ~26% (sur l'ensemble des biens, ruraux inclus)
* **Erreur Absolue Moyenne (MAE) :** ~36 000€

### 🛠️ Stack Technique
* **Langage :** Python
* **Machine Learning :** Scikit-Learn (Random Forest, Pipeline, RandomizedSearchCV)
* **Data Processing :** Pandas, NumPy
* **Interface Web :** Streamlit
* **Déploiement :** Streamlit Community Cloud

### 🚀 Installation Locale
Si vous souhaitez faire tourner le projet sur votre propre machine :
1. **Cloner le dépôt :**
   ```bash
   git clone "https://github.com/matteoCunha/Immo-35-estimator-Machine-Learning.git"
   cd Immo-35-estimator-Machine-Learning
   ```
2. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```
3. **Lancer l'application :**
   ```bash
   streamlit run app.py
   ```

# Auteur
Projet créé par **Mattéo Cunha**, dans le cadre d'un projet personnel de Data Science
