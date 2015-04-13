import csv
import zipfile
import pandas as pd
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

file_name = "train.csv"
zip_file_name = "./dataFiles/train.csv.zip"
with open(zip_file_name, 'rb') as fh:
    zfile = zipfile.ZipFile(fh)
    data = pd.read_csv(zfile.open(file_name))
le.fit(data.iloc[:,-1])
data.drop('id', axis=1, inplace=True)

print(data.count)
