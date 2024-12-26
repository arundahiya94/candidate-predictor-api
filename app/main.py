from flask import Flask, request, jsonify
from model import predict
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# Configure the app using environment variables
app.config['MODEL_PATH'] = os.getenv('MODEL_PATH', 'model/logistic_model.pkl')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

@app.route("/predict", methods = ["POST"])
def predict_candidate():

    # Request should be in JSON Format
    data = request.get_json()

    # Hardcoding the required features for now
    # Need to find a way to make it dynamic
    required_features = [
        'reputation', 'reached', 'answers', 'questions', 'gold_badge_score',
        'silver_badge_score', 'bronze_badge_score', 'followers',
        'public_repos', 'total_stars', 'total_forks', 'total_contributions',
        'total_repos', 'commit_count', 'pull_request_count', 'issue_count',
        'member_exp'
    ]

    # Get the features from the request
    try:
        features = [data[feature] for feature in required_features]
    except KeyError as e:
        return jsonify({"Error": f"Missing feature {str(e)}"}), 400
    
    prediction = predict(features)

    response = data.copy()
    response['prediction'] = int(prediction)

    return jsonify(response), 200
