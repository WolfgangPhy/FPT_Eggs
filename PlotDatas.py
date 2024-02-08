from matplotlib.ticker import MaxNLocator
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def PlotVicoryVsThicknes(data):
    """
    Plots the Victories vs Shell Thickness and saves the plot as a png file.
    Args:
        data (pandas dataframe): Dataframe containing the datas of FPT_Eggs.csv
    """
    sns.set_theme()
    fig, ax = plt.subplots()
    sns.lineplot(x='Victories', y='ShellThickness', data=data, ax=ax)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title('Victories vs Shell Thickness')
    ax.set_xlabel('Victories')
    ax.set_ylabel('Shell Thickness (mm)')
    plt.savefig('VictoriesVsShellThickness.png', dpi=300, bbox_inches='tight')
    
def PlotThicknessCompareDistribution(data):
    melted_df = pd.melt(data, id_vars=['IdOeuf', 'Bubble', 'Victories', 'Height', 'Width', 'Ovoidity', 'ShellThickness'],
                        value_vars=['Bottom', 'Mid', 'Top'], var_name='Location', value_name='Value')
    
    sns.set_theme()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='Location', y='Value', hue='IdOeuf', palette='tab10', data=melted_df, size='Victories', sizes=(50, 200), legend=False, alpha=0.6, ax=ax)
    sns.lineplot(x='Location', y='Value', data=melted_df, hue='IdOeuf', palette='tab10', style='IdOeuf', markers=False, dashes=False, legend=False, alpha=0.6, ax=ax)
    ax.set_title('Thickness Distribution by Location (Point size = Victories)')
    ax.set_xlabel('Location')
    ax.set_ylabel('Value (mm)')
    plt.show()

def PlotThicknessDistribution(data):
    """
    Plots the distribution of Shell Thickness and saves the plot as a png file.
    Args:
        data (pandas dataframe): Dataframe containing the datas of FPT_Eggs.csv
    """
    sns.set_theme()
    fig, ax = plt.subplots()
    sns.histplot(data['ShellThickness'],binwidth=0.01 , kde=True, ax=ax)
    ax.set_title('Shell Thickness Distribution')
    ax.set_xlabel('Shell Thickness (mm)')
    ax.set_ylabel('Frequency')
    plt.savefig('ShellThicknessDistribution.png', dpi=300, bbox_inches='tight')
    
def PlotVictoryVsOvoidity(data):
    """
    Plots the Victories vs Ovoidity and saves the plot as a png file.
    Args:
        data (pandas dataframe): Dataframe containing the datas of FPT_Eggs.csv
    """
    sns.set_theme()
    fig, ax = plt.subplots()
    sns.lineplot(y='Ovoidity',x='Victories', data=data, ax=ax)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xlim(0, 3)
    ax.set_title('Victories vs Ovoidity')
    ax.set_ylabel('Victories')
    ax.set_xlabel('Ovoidity (Height/Width)')
    #plt.show()
    plt.savefig('VictoriesVsOvoidity.png', dpi=300, bbox_inches='tight')
  
def PlotVictoryVsBubbleSize(data):
    """
    Plots the Victories vs Bubble Size and saves the plot as a png file.
    Args:
        data (pandas dataframe): Dataframe containing the datas of FPT_Eggs.csv
    """
    sns.set_theme()
    fig, ax = plt.subplots()
    sns.lineplot(x='Victories', y='Bubble', data=data, ax=ax)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title('Victories vs Bubble Size')
    ax.set_xlabel('Victories')
    ax.set_ylabel('Bubble Size (mm)')
    plt.savefig('VictoriesVsBubbleSize.png', dpi=300, bbox_inches='tight')
    #plt.show()
    
def PlotVictoryVsTopThickness(data):
    """
    Plots the Victories vs Top Thickness and saves the plot as a png file.
    Args:
        data (pandas dataframe): Dataframe containing the datas of FPT_Eggs.csv
    """
    sns.set_theme()
    fig, ax = plt.subplots()
    sns.lineplot(x='Victories', y='Top', data=data, ax=ax)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title('Victories vs Top Thickness')
    ax.set_xlabel('Victories')
    ax.set_ylabel('Top Thickness (mm)')
    plt.savefig('VictoriesVsTopThickness.png', dpi=300, bbox_inches='tight')
    
def PlotVictoryVsBottomThickness(data):
    """
    Plots the Victories vs Bottom Thickness and saves the plot as a png file.
    Args:
        data (pandas dataframe): Dataframe containing the datas of FPT_Eggs.csv
    """
    sns.set_theme()
    fig, ax = plt.subplots()
    sns.lineplot(x='Victories', y='Bottom', data=data, ax=ax)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title('Victories vs Bottom Thickness')
    ax.set_xlabel('Victories')
    ax.set_ylabel('Bottom Thickness (mm)')
    plt.savefig('VictoriesVsBottomThickness.png', dpi=300, bbox_inches='tight')
    
def PlotVictoryVsMidThickness(data):
    """
    Plots the Victories vs Mid Thickness and saves the plot as a png file.
    Args:
        data (pandas dataframe): Dataframe containing the datas of FPT_Eggs.csv
    """
    sns.set_theme()
    fig, ax = plt.subplots()
    sns.lineplot(x='Victories', y='Mid', data=data, ax=ax)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title('Victories vs Bottom Thickness')
    ax.set_xlabel('Victories')
    ax.set_ylabel('Mid Thickness (mm)')
    plt.savefig('VictoriesVsMidThickness.png', dpi=300, bbox_inches='tight')
  
def PlotVictoryVsAllThickness(data):
    sns.set_theme()
    fig, ax = plt.subplots(nrows=2, ncols=3, gridspec_kw={'wspace':0.5, 'hspace':0.5})
    sns.lineplot(x='Victories', y='ShellThickness', data=data, ax=ax[0,1])
    sns.lineplot(x='Victories', y='Top', data=data, ax=ax[1,0])
    sns.lineplot(x='Victories', y='Mid', data=data, ax=ax[1,1])
    sns.lineplot(x='Victories', y='Bottom', data=data, ax=ax[1,2])
    ax[0, 0].axis('off')
    ax[0, 2].axis('off')
    ax[0,1].set_title('Victories vs Shell Thickness')
    ax[1,0].set_title('Victories vs Top Thickness')
    ax[1,1].set_title('Victories vs Mid Thickness')
    ax[1,2].set_title('Victories vs Bottom Thickness')
    ax[0,1].set_xlabel('Victories')
    ax[1,0].set_xlabel('Victories')
    ax[1,1].set_xlabel('Victories')
    ax[1,1].set_xlabel('Victories')
    ax[0,1].set_ylabel('Average Shell Thickness (mm)')
    ax[1,0].set_ylabel('Top Thickness (mm)')
    ax[1,1].set_ylabel('Mid Thickness (mm)')
    ax[1,2].set_ylabel('Bottom Thickness (mm)')
    plt.show()
    
def PlotTournament(data_tournament, data_shell):
    merged_df_winner = pd.merge(data_tournament, data_shell[['IdOeuf', 'ShellThickness']], left_on='IdWinner', right_on='IdOeuf', how='inner', suffixes=('_Winner', '_'))
    merged_df = pd.merge(merged_df_winner, data_shell[['IdOeuf', 'ShellThickness']], left_on='IdLoser', right_on='IdOeuf', how='inner', suffixes=('_Winner', '_Loser'))
    merged_df.drop(['IdOeuf_Winner', 'IdOeuf_Loser', 'Unnamed: 3'], axis=1, inplace=True)

    sns.set_theme()
    fig, ax = plt.subplots(figsize=(7, 7))

    markers={1 : 'o',2 : '^',3 : 's',4 : 'D'}
    sns.scatterplot(x='ShellThickness_Loser', y='ShellThickness_Winner',hue='Manche',palette='plasma', data=merged_df, style='Manche', markers=markers, s=100, ax=ax)
    ax.plot([merged_df['ShellThickness_Loser'].min(), merged_df['ShellThickness_Winner'].max()], 
            [merged_df['ShellThickness_Loser'].min(), merged_df['ShellThickness_Winner'].max()], 
            linestyle='--', color='gray', label='y = x')
    # Ajouter des légendes et des étiquettes
    ax.set_title('Comparaison de ShellThickness entre Gagnants et Perdants par Manche')
    ax.set_xlabel('ShellThickness du Perdant')
    ax.set_ylabel('ShellThickness du Gagnant')

    # Afficher le plot
    plt.savefig('TournamentShellThickness.png', dpi=300, bbox_inches='tight')
    
def PlotVictoryVsTopThicknessError(data):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Tracer le scatter plot avec erreurs
    scatter = ax.scatter(data['Victories'], data['Top'], label='Data Points')

    # Ajouter les erreurs avec HeightWidthError comme erreurs pour l'ordonnée
    ax.errorbar(data['Victories'], data['Top'], yerr=data['HeightWidthError'], fmt='none', ecolor='gray', capsize=3, label='Error Bars')

    # Ajouter des légendes et des étiquettes
    ax.set_title('Scatter Plot de Victories vs Top avec Erreurs')
    ax.set_xlabel('Victories')
    ax.set_ylabel('Top')
    ax.legend()

    # Afficher le plot
    plt.show()

def main():
    data = pd.read_csv('FPT_Eggs.csv')
    data_shell = pd.read_csv('ShellThickness.csv')
    dataTournament = pd.read_csv('Tournament.csv')
    PlotVictoryVsTopThickness(data)
    
if __name__ == '__main__':
    main()