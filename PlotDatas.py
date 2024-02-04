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
    ax.set_title('Victories vs Shell Thickness')
    ax.set_xlabel('Victories')
    ax.set_ylabel('Shell Thickness (mm)')
    plt.savefig('VictoriesVsShellThickness.png', dpi=300, bbox_inches='tight')
    
def main():
    data = pd.read_csv('FPT_Eggs.csv')
    PlotVicoryVsThicknes(data)
    
if __name__ == '__main__':
    main()