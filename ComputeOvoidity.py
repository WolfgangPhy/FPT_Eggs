import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def ComputeOvoidity(df):
    """
    Compute the ovoidity of the eggs in the DataFrame.
    Args:
        df (Pandas dataframe): DataFrame containing the datas of the eggs.

    Returns:
        Pandas dataframe: DataFrame with a new column 'Ovoidity' containing the ovoidity of the eggs.
    """
    df['Ovoidity'] = df['Height'] / df['Width']
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
    # Calculer la nouvelle colonne Ovoidity
    df = ComputeOvoidity(df)
    # Enregistrer le DataFrame mis à jour dans un nouveau fichier CSV
    SaveDataFrame(df, "FPT_Eggs.csv")
    
#call
if __name__ == "__main__":
    main()