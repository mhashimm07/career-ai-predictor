import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("dataset.csv")

X = data.drop("Career", axis=1)
y = data["Career"]

model = DecisionTreeClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully")

