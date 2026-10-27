"""Entry point of the ML application: trains the model and prints its accuracy."""
from src.model import train_model

if __name__ == "__main__":
    accuracy = train_model()
    print(f"Model Accuracy: {accuracy:.4f}")
    print("ML application ran successfully.")
