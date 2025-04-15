# python Model\iris_model.py
# iris_model.py
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pickle
import warnings
import os

warnings.filterwarnings("ignore")

# Load and split data
data = load_iris()
Xtrain, Xtest, Ytrain, Ytest = train_test_split(
    data.data, data.target, test_size=0.3, random_state=4
)

# Create and train the model
model = LogisticRegression(
    C=0.1,
    max_iter=200,  # Increased for better convergence
    fit_intercept=True,
    solver='liblinear'
)
model.fit(Xtrain, Ytrain)

# Ensure the model directory exists
model_dir = "api"
os.makedirs(model_dir, exist_ok=True)

# Save the model to the 'api' folder
pkl_filename = os.path.join(model_dir, "Model.pkl")
with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)

# Evaluate the model
score = model.score(Xtest, Ytest)
print("Test accuracy: {:.2f}%".format(100 * score))

# Predict and display results
Ypredict = model.predict(Xtest)
print("\nPredictions vs Actual:\n")
for pred, actual in zip(Ypredict, Ytest):
    print(f"Predicted: {pred}, Actual: {actual}")

# Additional metrics
print("\nClassification Report:\n")
print(classification_report(Ytest, Ypredict))
print("Confusion Matrix:\n")
print(confusion_matrix(Ytest, Ypredict))