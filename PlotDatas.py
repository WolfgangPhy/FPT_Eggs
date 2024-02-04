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
    sns.lineplot(x='Victories', y='Ovoidity', data=data, ax=ax)
    ax.set_xlim(0, 3)
    ax.set_title('Victories vs Ovoidity')
    ax.set_xlabel('Victories')
    ax.set_ylabel('Ovoidity (Height/Width)')
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
    ax.set_title('Victories vs Bubble Size')
    ax.set_xlabel('Victories')
    ax.set_ylabel('Bubble Size (mm)')
    plt.savefig('VictoriesVsBubbleSize.png', dpi=300, bbox_inches='tight')
    #plt.show()
    
      
def main():
    data = pd.read_csv('FPT_Eggs.csv')
    PlotVictoryVsBubbleSize(data)
    
if __name__ == '__main__':
    main()