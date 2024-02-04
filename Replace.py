import pandas as pd

# Charger le fichier CSV dans un DataFrame Pandas
df = pd.read_csv('FPT_Eggs_sheet.csv')

# Fonction pour convertir une chaîne en nombre (float) en remplaçant ',' par '.'
def convert_to_float(value):
    return float(value.replace(',', '.'))

# Parcourir chaque colonne du DataFrame
for col in df.columns:
    # Remplacer ',' par '.' dans les valeurs de la colonne (si la colonne contient des chaînes)
    if df[col].dtype == 'O':  # 'O' est le type pour les objets (chaînes de caractères) dans Pandas
        df[col] = df[col].str.replace(',', '.').astype(float)

# Enregistrer le DataFrame mis à jour dans un nouveau fichier CSV
df.to_csv('FPT_Eggs.csv', index=False)
