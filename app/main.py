from flask import Flask, request, jsonify
from app.model import predict

app = Flask(__name__)

# @app.route("/", methods=['GET'])
# def home():
#     return "Hello this is the home method"


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

if __name__ == "__main__":
    app.run()