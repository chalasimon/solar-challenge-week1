import matplotlib.pyplot as plt
import seaborn as sns

def plot_boxplot(data, metric):
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='country', y=metric, data=data)
    plt.title(f'{metric} Comparison')
    return plt