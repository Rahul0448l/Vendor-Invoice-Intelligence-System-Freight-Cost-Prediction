from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


def train_random_forest(X_train, y_train):

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=1
    )

    model.fit(X_train, y_train)

    return model


def evaluate_classifier(model, X_test, y_test, model_name):

    preds = model.predict(X_test)

    accuracy = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)

    print(f"\n{model_name} Performance")
    print(f"Accuracy: {accuracy:.2f}")
    print(report)