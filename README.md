# candidate-predictor-api
A machine learning model that predicts candidate hirable status using logistic regression. This project exposes an API endpoint for real-time predictions and is deployed using Docker for scalable and easy deployment.

## Steps to download and run the docker image
1. docker pull arundahiya94/candidate-predictor-api
2. docker run -d -p 8000:8000 --name candidate-predictor arundahiya94/candidate-predictor-api
3. URL : localhost:8000/predict
4. Sample JSON File for post request

```json
    {
      "reputation": 100,
      "reached": 5,
      "answers": 10,
      "questions": 5,
      "gold_badge_score": 3,
      "silver_badge_score": 2,
      "bronze_badge_score": 1,
      "followers": 50,
      "public_repos": 10,
      "total_stars": 100,
      "total_forks": 50,
      "total_contributions": 20,
      "total_repos": 5,
      "commit_count": 30,
      "pull_request_count": 10,
      "issue_count": 5,
      "member_exp": 1
  }
5. docker stop candidate-predictor
6. docker rm candidate-predictor



