import pandas as pd

def ComputeEggShellThickness(df):
    """
    Compute the average egg shell thickness for each egg in the DataFrame.
    Args:
        df (Pandas dataframe): DataFrame containing the datas of the eggs.

    Returns:
        Pandas dataframe: DataFrame with a new column 'ShellThickness' containing the average shell thickness.
    """
    # Calculate the average shell thickness ((Bottom + Mid + Top) / 3)
    df['ShellThickness'] = (df['Bottom'] + df['Mid'] + df['Top']) / 3
    return df

def SaveDataFrame(df, filename):
    """
    Save the DataFrame to a CSV file.
    Args:
        df (Pandas dataframe): Datafram that will be saved to a CSV file.
        filename (string): Name of the CSV file.
    """
    df.to_csv(filename, index=False)

def main():
    # Charger le fichier CSV dans un DataFrame Pandas
    df = pd.read_csv("FPT_Eggs.csv")
    
    # Calculer la nouvelle colonne ShellThickness
    df = ComputeEggShellThickness(df)
    
    # Enregistrer le DataFrame mis à jour dans un nouveau fichier CSV
    SaveDataFrame(df, "FPT_Eggs.csv")

# Appeler la fonction main
if __name__ == "__main__":
    main()
