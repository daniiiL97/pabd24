# syntax=docker/dockerfile:1

FROM python:3.9
WORKDIR /app
COPY ./src/predict_app.py ./src/predict_app.py
COPY ./.env ./.env
COPY ./models/catboost.joblib ./models/catboost.joblib

RUN pip3 install flask flask-cors flask_httpauth catboost \
          scikit-learn python-dotenv joblib gunicorn

CMD ["python3", "src/predict_app.py"]
EXPOSE 5000