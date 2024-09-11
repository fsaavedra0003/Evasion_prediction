#Imported the corresponding libraries 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# CSV file with history of evations for the last 2 years 

csv_file = 'evasion.csv'

#  Load CSV gets into a pandas DataFrame
df = pd.read_csv(Data_Evasions.csv)

# Print the CSV as Pandas Data Frame
print(df)


# Load the corresponding columns from  CSV  'feature' and 'target'
X = data[['feature']]
y = data['target']

# This is the logic to Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the acuracy of model using  MSE (mean squared error).
mse = mean_squared_error(y_test, y_pred)


# Print the results.
print(f'Mean Squared Error: {mse}')



# Plot the regression line using Matplolib of the predicted values
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Linear Regression Model')
plt.show()
