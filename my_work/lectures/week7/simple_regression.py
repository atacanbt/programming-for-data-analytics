# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
dataset = sns.load_dataset('tips')

# display the first 5 rows of the dataset
print(dataset.head())
sns.set_style('whitegrid')

sns.lmplot(x='total_bill', y='tip',order = 3, data=dataset)
plt.show()