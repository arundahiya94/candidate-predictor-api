import pickle
import numpy as np
from flask import current_app


def load_model(file_path):
    """Load the model from the Pickle file and use it for the prediction"""

    with open(file_path, "rb") as file:
        model = pickle.load(file)
    
    return model

def predict(features):
    """Predict the eligibility of the candidate"""

    model = load_model(current_app.config['MODEL_PATH'])
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)[0]
    
    return prediction
