
# Correction Matrix Plot
import matplotlib.pyplot as plt
import pandas
import numpy
data = pandas.read_csv("correlation.csv")
print(data)
correlations = data.corr()
# plot correlation matrix
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,len(data.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(data.columns)
ax.set_yticklabels(data.columns)
plt.show()