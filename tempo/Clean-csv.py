import os
os.chdir("/Users/victorcarre/Code/Base de donnée biostimulants/bio4safe-scraper")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/bio4safe.csv" , sep=";")

print("    Informations générales :")
print(data.info())
print("    Cinq premières lignes :")
print(data.head())
print("    Nom des colonnes :")
print(data.columns)
print("    Type de données des colonnes :")
print(data.dtypes)
print("    Biostimulants les plus cités :")
biostimulant_counts = data['biostimulant'].value_counts()
print(biostimulant_counts.head(5))
print("    Valeurs manquantes par colonne :")
print(data.isnull().sum()) 
print("    Nombre de doublons :")
print(data.duplicated().sum())
print("    Doublons dans les données :")
print(data[data.duplicated()])
print("    Résumé statistique :")
print(data.describe())

# Barplot pour la colonne 'type' (exemple)

sns.countplot(x='type', data=data)
plt.xticks(rotation=45)  # Pour que les labels ne se chevauchent pas
plt.show()

# Nettoyage

## Suppression des espaces en début et fin de chaîne
data['biostimulant'] = data['biostimulant'].str.strip()
data['type'] = data['type'].str.strip()
data['effect'] = data['effect'].str.strip()

## Uniformisation des majuscules/minuscules pour une comparaison plus facile
data['biostimulant'] = data['biostimulant'].str.title()
data['type'] = data['type'].str.title()
data['effect'] = data['effect'].str.capitalize()

## Suppression des doublons
data.drop_duplicates(inplace=True)

## Vérification des valeurs manquantes
print("\n Résumé après nettoyage :")
print(data.info())
print("\n Cinq premières lignes après nettoyage :")
print(data.head())

## Enregistrement du fichier nettoyé
data.to_csv("data/bio4safe_cleaned.csv", sep=";", index=False)
print("\n Données nettoyées et sauvegardées dans 'data/file_cleaned.csv'")
