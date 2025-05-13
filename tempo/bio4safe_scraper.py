import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL de base 
BASE_URL = "https://bio4safe.eu/biostimulant-database?"

# Liste des filtres (effets et types de biostimulants)
filters = {
    "effects": [
        "Decreased drought stress tolerance", "Decreased growth", "Decreased heat stress tolerance", 
        "Decreased nitrogen N use efficiency", "Decreased nutrient availability in soil or substrate", 
        "Decreased other", "Decreased phosphorous P use efficiency", "Decreased potassium K use efficiency", 
        "Decreased produce quality", "Decreased salt stress tolerance", "Decreased water use efficiency", 
        "Increased cold stress tolerance", "Increased drought stress tolerance", "Increased heat stress tolerance", 
        "Increased micronutrient use efficiency", "Increased nitrogen N use efficiency", 
        "Increased nutrient availability in soil or substrate", "Increased other", 
        "Increased phosphorous P use efficiency", "Increased potassium K use efficiency", 
        "Increased produce quality", "Increased salt stress tolerance", "Increased water use efficiency", 
        "Increased yield", "No effect on cold stress tolerance", "No effect on drought stress tolerance", 
        "No effect on growth", "No effect on heat stress tolerance", "No effect on micronutrient use efficiency", 
        "No effect on nitrogen N use efficiency", "No effect on nutrient availability in soil or substrate", 
        "No effect on other", "No effect on phosphorous P use efficiency", "No effect on potassium K use efficiency", 
        "No effect on produce quality", "No effect on salt stress tolerance", "No effect on water use efficiency", 
        "No effect on yield"
    ],
    "biostimulants": [
        "Bacteria", "Humic and fluvic acids", "Mix of different types", "Mycorrhizal fungi", "Nonmycorrhizal fungi", 
        "Seaweed extract", "Annuals", "Berries and small fruits", "Bulb ornamentals", "Cabbage", "Cereals", 
        "Field crop plants", "Forage plants", "Fruit vegetable crops", "Leafy vegetables", "Perennials", 
        "Pome fruits", "Pseudocereals", "Pulses", "Root vegetables", "Stone fruits", "Woody ornamentals"
    ]
}

# Créer le répertoire pour les données si nécessaire
os.makedirs("data", exist_ok=True)

# Fonction pour extraire les données d'une page
def extract_data_from_page(page_url, filter_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    # Requête GET pour récupérer les données filtrées
    response = requests.get(page_url, headers=headers, verify=False)

    print(f"Réponse de {page_url}: {response.status_code}")  # Affiche le code de statut HTTP

    if response.status_code != 200:
        print(f"⚠️ Erreur lors de la récupération de la page {page_url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    data = []

    # Récupérer tous les tableaux de données ou autres structures contenant les biostimulants
    tables = soup.find_all("table")
    for table in tables:
        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        rows = table.find_all("tr")
        for row in rows:
            cells = [td.get_text(strip=True) for td in row.find_all("td")]
            if cells:
                # Ajouter la colonne "filter_name" avec le nom du filtre
                data.append(dict(zip(headers, cells)) | {"filter_name": filter_name})

    return data

# Fonction principale
def main():
    print("🔍 Extraction des données depuis Bio4Safe...")
    
    all_data = []

    # Parcourir tous les filtres d'effets
    for effect in filters["effects"]:
        print(f"📄 Récupération des données pour l'effet : {effect}")
        page_url = f"{BASE_URL}f%5B0%5D=effect%3A{effect.replace(' ', '%20')}"
        data = extract_data_from_page(page_url, effect)
        all_data.extend(data)
        time.sleep(2)  # Pause pour éviter d'être bloqué par le serveur
    
    # Parcourir tous les filtres de biostimulants
    for biostimulant in filters["biostimulants"]:
        print(f"📄 Récupération des données pour le biostimulant : {biostimulant}")
        page_url = f"{BASE_URL}f%5B0%5D=biostimulant%3A{biostimulant.replace(' ', '%20')}"
        data = extract_data_from_page(page_url, biostimulant)
        all_data.extend(data)
        time.sleep(2)  # Pause pour éviter d'être bloqué par le serveur

    # Sauvegarde des données en CSV
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv("data/biostimulants_filtered_with_filter_name.csv", index=False)
        print("✅ Extraction terminée. Fichier sauvegardé dans 'data/biostimulants_filtered_with_filter_name.csv'")
    else:
        print("⚠️ Aucune donnée n'a été extraite.")

# Exécution du script
if __name__ == "__main__":
    main()
