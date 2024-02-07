import pandas as pd

# Charger le CSV dans un DataFrame
df = pd.read_csv('FPT_Eggs.csv')

# Ajouter la colonne HeightWidthError avec une valeur constante de 0.01
df['HeightWidthError'] = 0.01
df['BubbleError'] = 1

# Ajouter la colonne OvoidityError en utilisant la formule de propagation des incertitudes
df['OvoidityError'] = df['Ovoidity']*(df['HeightWidthError']/df['Height'] + df['HeightWidthError']/df['Width'])

# Enregistrez le DataFrame mis à jour dans le fichier CSV existant
df.to_csv('FPT_Eggs.csv', index=False)
