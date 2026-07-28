import joblib

model = joblib.load(
    "freight_cost_prediction/models/predict_freight_model.pkl"
)

print("Expected Features:")
print(model.feature_names_in_)