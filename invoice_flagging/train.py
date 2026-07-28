from data_preprocessing import (
    load_invoice_data,
    split_data,
    scale_features,
    apply_labels
)

from modeling_evaluation import (
    train_random_forest,
    evaluate_classifier
)

import joblib
import os


FEATURES = [
    "invoice_quantity",
    "invoice_dollars",
    "Freight",
    "total_item_quantity",
    "total_item_dollars"
]

TARGET = "flag_invoice"


def main():

    print("1. Loading data...")
    df = load_invoice_data()

    print("2. Applying labels...")
    df = apply_labels(df)

    print("3. Splitting data...")
    X_train, X_test, y_train, y_test = split_data(
        df,
        FEATURES,
        TARGET
    )

    print("4. Scaling features...")
    X_train_scaled, X_test_scaled = scale_features(
        X_train,
        X_test,
        "models/scaler.pkl"
    )

    print("Training Data Shape:", X_train_scaled.shape)
    print("\nTarget Distribution:")
    print(y_train.value_counts())

    print("5. Training Random Forest...")
    model = train_random_forest(
        X_train_scaled,
        y_train
    )

    print("6. Evaluating Model...")
    evaluate_classifier(
        model,
        X_test_scaled,
        y_test,
        "Random Forest Classifier"
    )

    print("7. Saving Model...")

    os.makedirs("models", exist_ok=True)

    joblib.dump(
        model,
        "models/predict_flag_invoice.pkl"
    )

    print("\n✅ Model saved successfully!")
    print("Location: models/predict_flag_invoice.pkl")


if __name__ == "__main__":
    main()