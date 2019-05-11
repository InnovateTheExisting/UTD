from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import warnings
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import sys

url = sys.argv[1]
split = float(sys.argv[2])
names = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]

# Importing the datasets
dataset = pd.read_csv(url, names=names)
warnings.filterwarnings("ignore")
# mark ? values as missing or NaN
dataset.replace(to_replace="[?]", value=np.nan, regex=True, inplace=True)
dataset = dataset.dropna()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 6].values

df = pd.DataFrame(dataset)
buying_values = ['low', 'med', 'high', 'vhigh']
maint_values = ['low', 'med', 'high', 'vhigh']
doors_values = [2, 3, 4, '5-more']
persons_values = [2, 4, 'more']
lug_boot_values = ['small', 'med', 'big']
safety_values = ['low', 'med', 'high']
class_values = ['unacc', 'acc', 'good', 'vgood']

# replacing indefinite values to numbers

df["buying"] = df["buying"].astype("category", categories=buying_values).cat.codes  
df["maint"] = df["maint"].astype("category", categories=maint_values).cat.codes  
df["lug_boot"] = df["lug_boot"].astype("category", categories=lug_boot_values).cat.codes  
df["safety"] = df["safety"].astype("category", categories=safety_values).cat.codes  
df["class"] = df["class"].astype("category", categories=class_values).cat.codes  
df['doors'].replace('5more', 5, inplace=True)  
df['persons'].replace('more', 6, inplace=True)  

# standardizing the dataset
df["buying"] = preprocessing.scale(df["buying"])
df["maint"] = preprocessing.scale(df["maint"])
df["doors"] = preprocessing.scale(df["doors"])
df["persons"] = preprocessing.scale(df["persons"])
df["lug_boot"] = preprocessing.scale(df["lug_boot"])
df["safety"] = preprocessing.scale(df["safety"])

f=open("output.txt","a+")
f.write("==================================================\r\n")
f.write("Car Data\r\n")
f.close()

# writing pre-processed data to a csv file
df.to_csv('preProcessed.csv', sep=',', index=False, header=False)
# split dataset in to train and test
train, test = train_test_split(df, test_size=split)
train.to_csv('train.csv', sep=',', index=False, header=False)
test.to_csv('test.csv', sep=',', index=False, header=False)