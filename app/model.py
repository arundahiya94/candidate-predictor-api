import pickle
import numpy as np

MODEL_PATH = "model/logistic_model.pkl"

def load_model(file_path):
    """Load the model from the Pickle file and use it for the prediction"""

    with open(file_path, "rb") as file:
        model = pickle.load(file)
    
    return model

def predict(features):
    model = load_model(MODEL_PATH)
    features_array = np.array[features]
    prediction = model.predict(features_array)[0]
    return prediction
