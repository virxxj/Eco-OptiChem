import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv("/Users/viraajkochar/Eco-OptiChem/data/sample_data.csv")

# Define features (X) and target (y)
X = df[["Temperature", "Pressure", "Flow Rate", "Energy Usage"]]
y = df["Emissions"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree model
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate and display the Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Save the model for future use (optional)
import joblib
joblib.dump(model, "/Users/viraajkochar/Eco-OptiChem/scripts/emissions_model.joblib")
print("Model trained and saved successfully!")
