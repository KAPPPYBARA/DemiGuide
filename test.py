import numpy as np
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the trained model
model = joblib.load('demi.joblib')

def predict_strand(input_array):
    # Convert the input array to a NumPy array if it's not already
    input_array = np.array(input_array).reshape(1, -1)  # Reshape to ensure compatibility with the model
    
    # Make a prediction using the trained model
    prediction = model.predict(input_array)
    
    return prediction

# Example usage:
input_array = [11, 15, 10, 8, 9, 13, 12]
predicted_strand = predict_strand(input_array)
print("Predicted strand:", predicted_strand)
