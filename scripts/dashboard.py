from flask import Flask, render_template
import pandas as pd
import joblib
import random

app = Flask(__name__)

# Load the trained model
model = joblib.load("/Users/viraajkochar/Eco-OptiChem/scripts/emissions_model.joblib")

@app.route('/')
def index():
    # Generate random data to simulate real-time process parameters
    data = {
        "Temperature": random.uniform(50, 300),
        "Pressure": random.uniform(1, 10),
        "Flow Rate": random.uniform(0.5, 5.0),
        "Energy Usage": random.uniform(100, 1000)
    }

    # Convert data to a DataFrame for model prediction
    df = pd.DataFrame([data])

    # Predict emissions
    predicted_emissions = model.predict(df)[0]
    data["Predicted Emissions"] = predicted_emissions

    # Set a flag if emissions are high
    high_emissions = predicted_emissions > 120  # Example threshold

    # Define simple optimization suggestions based on updated thresholds
    suggestions = []
    if high_emissions or data["Temperature"] > 150:
        suggestions.append("Consider lowering the temperature.")
    if high_emissions or data["Flow Rate"] > 3:
        suggestions.append("Consider reducing the flow rate.")
    if high_emissions or data["Pressure"] > 7:
        suggestions.append("Consider lowering the pressure.")

    return render_template("index.html", data=data, high_emissions=high_emissions, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
