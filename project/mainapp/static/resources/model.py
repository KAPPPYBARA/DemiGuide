import pandas
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

dataset = pandas.read_csv("dataset.csv")

x = dataset.iloc[:, :7]
y = dataset.iloc[:, -1]

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size= 0.3, random_state= 42)

model = LogisticRegression(max_iter= 1000)
model.fit(train_x, train_y)

accuracy = model.score(test_x, test_y)
print("Accuracy:", accuracy)

joblib.dump(model, "demi.joblib")