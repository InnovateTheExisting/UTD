from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import warnings
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import sys

url = sys.argv[1]
split = float(sys.argv[2])
warnings.filterwarnings("ignore")
names = ["sepal length", "sepal width", "petal length", "petal width", "class"]
# Importing the datasets
dataset = pd.read_csv(url, names=names)

# mark ? values as missing or NaN
dataset.replace(to_replace="[?]", value=np.nan, regex=True, inplace=True)
dataset = dataset.dropna()
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

df = pd.DataFrame(dataset)

f=open("output.txt","a+")
f.write("==================================================\r\n")
f.write("Iris Data\r\n")
f.close()


label_encoder = LabelEncoder()
df["class"] = label_encoder.fit_transform(df["class"])

# standardizing the dataset
df["sepal length"] = preprocessing.scale(df["sepal length"])
df["sepal width"] = preprocessing.scale(df["sepal width"])
df["petal length"] = preprocessing.scale(df["petal length"])
df["petal width"] = preprocessing.scale(df["petal width"])


df.to_csv('preProcessed.csv', sep=',', index=False, header=False)

train, test = train_test_split(df, test_size=split)
train.to_csv('train.csv', sep=',', index=False, header=False)
test.to_csv('test.csv', sep=',', index=False, header=False)