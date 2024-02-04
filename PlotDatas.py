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
    
def PlotVictoryVsTopThickness(data):
    """
    Plots the Victories vs Top Thickness and saves the plot as a png file.
    Args:
        data (pandas dataframe): Dataframe containing the datas of FPT_Eggs.csv
    """
    sns.set_theme()
    fig, ax = plt.subplots()
    sns.lineplot(x='Victories', y='Top', data=data, ax=ax)
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
    

def main():
    data = pd.read_csv('FPT_Eggs.csv')
    PlotVictoryVsAllThickness(data)
    
if __name__ == '__main__':
    main()