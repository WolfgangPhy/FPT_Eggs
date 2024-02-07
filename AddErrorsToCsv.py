import pandas as pd

# Charger le CSV dans un DataFrame
df = pd.read_csv('FPT_Eggs.csv')

# Ajouter la colonne BubbleError avec une valeur constante de 0.1
df['BubbleError'] = 0.1

# Ajouter la colonne HeightWidthError avec une valeur constante de 0.01
df['HeightWidthError'] = 0.01

# Ajouter la colonne OvoidityError en utilisant la formule de propagation des incertitudes
df['OvoidityError'] = df['Ovoidity'] * ((df['Height'] / df['Width'])**2 * ((df['HeightWidthError'] / df['Height'])**2 + (df['BubbleError'] / df['Width'])**2))**0.5

# Enregistrez le DataFrame mis à jour dans le fichier CSV existant
df.to_csv('FPT_Eggs.csv', index=False)
