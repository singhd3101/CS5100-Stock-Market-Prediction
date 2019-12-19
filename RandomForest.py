import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf

from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_score, recall_score

global scaledDf, labels
features = ['DE Ratio',
                'Trailing P/E',
                'Price/Sales',
                'Price/Book',
                'Profit Margin',
                'Operating Margin',
                'Return on Assets',
                'Return on Equity',
                'Revenue Per Share',
                'Market Cap',
                'Enterprise Value',
                'Forward P/E',
                'PEG Ratio',
                'Enterprise Value/Revenue',
                'Enterprise Value/EBITDA',
                'Revenue',
                'Gross Profit',
                'EBITDA',
                'Net Income Avl to Common ',
                'Diluted EPS',
                'Earnings Growth',
                'Revenue Growth',
                'Total Cash',
                'Total Cash Per Share',
                'Total Debt',
                'Current Ratio',
                'Book Value Per Share',
                'Cash Flow',
                'Beta',
                ]

dfDataset = pd.read_csv("inputdata.csv")
dfDataset = dfDataset[:2000]
dfDataset = dfDataset.reindex(np.random.permutation(dfDataset.index))


scaledDf = np.array(dfDataset[features].values)

labels = (dfDataset["Status"].replace("outperform",1).replace("underperform",0).values.tolist())

scaledDf = preprocessing.minmax_scale(scaledDf)

scaledDf = SelectKBest(k=20).fit_transform(scaledDf, labels)
#print("anuroopa", scaledDf)

def extractIndex(original, indeces):
    ret = []
    for ind in indeces:
        ret.append(original[ind])
    return ret

clf = RandomForestClassifier(n_estimators=1001, max_depth=50, bootstrap=True, oob_score=False, max_leaf_nodes=None)

analysis_times = 1
rs = ShuffleSplit(n_splits=analysis_times, test_size=.1, random_state=1)

for train, test in rs.split(scaledDf):
    train_data = extractIndex(scaledDf, train)
    test_data = extractIndex(scaledDf, test)

    train_values = extractIndex(labels, train)
    current_values = extractIndex(labels, test)

    clf.fit(train_data, train_values)

    prediction = clf.predict(test_data)
    accuracyScore = accuracy_score(current_values, prediction, normalize=True)
    f1Score = f1_score(current_values, prediction)
    precision = precision_score(current_values,prediction)
    recall = recall_score(current_values,prediction)
    print ("Classifier: RandomForest")
    print ("Accuracy of prediction", accuracyScore), "\n"
    print("F1 Score", f1Score), "\n"
    print ("Precision", precision_score(current_values,prediction))
    print ("Recall", recall_score(current_values,prediction))

n = 1
index = np.arange(n)
width = 0.1

fig, ax = plt.subplots()

ax.set_ylabel('Rate')
ax.set_xticks(index + width)
ax.set_xticklabels('Random Forest')
bar1 = ax.bar(index, accuracyScore , 0.07, color=(0.901, 0.470, 0.156))
bar2 = ax.bar(index + width, precision, 0.07, color=(0.156, 0.619, 0.901))
bar3 = ax.bar(index + width * 2, recall, 0.07, color=(0.941, 0.960, 0.196))
bar4 = ax.bar(index + width * 3, f1Score, 0.07, color=(0.960, 0.196, 0.298))
ax.legend((bar1[0], bar2[0], bar3[0], bar4[0]),
          ('Accuracy', 'Precision', 'Recall', 'F1'),loc='center left',prop={'size':15},bbox_to_anchor=(1, 0.5))

# Saving the chart to a pdf file
plt.show()