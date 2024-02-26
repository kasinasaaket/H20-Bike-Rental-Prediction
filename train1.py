from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from h2o.automl import H2OAutoML
import pandas as pd

day = pd.read_csv('day.csv')
hour= pd.read_csv('hour.csv')

X_day = day.drop(['instant', 'dteday', 'cnt'], axis=1)
y_day = day['cnt']

X_train_day, X_test_day, y_train_day, y_test_day = train_test_split(X_day, y_day, test_size=0.2, random_state=42)

# Model 1: Gradient Boosting
gb_model_day = GradientBoostingRegressor()
gb_model_day.fit(X_train_day, y_train_day)
gb_predictions_day = gb_model_day.predict(X_test_day)

# Evaluate Gradient Boosting model
mse_gb_day = mean_squared_error(y_test_day, gb_predictions_day)
print("Mean Squared Error (Gradient Boosting - Day Data):", mse_gb_day)

import h2o
h2o.init()
day_data_h2o = h2o.H2OFrame(day)
x_day = day_data_h2o.columns
y_day = 'cnt'
x_day.remove(y_day)

aml_day = H2OAutoML(max_models=10, seed=42)
aml_day.train(x=x_day, y=y_day, training_frame=day_data_h2o)

# View the AutoML leaderboard
lb_day = aml_day.leaderboard
print(lb_day)

# Load hourly data
hour_data = pd.read_csv('hour.csv')

# Split data into features (X) and target variable (y)
X_hour = hour_data.drop(['instant', 'dteday', 'cnt'], axis=1)
y_hour = hour_data['cnt']

# Split the data into training and testing sets
X_train_hour, X_test_hour, y_train_hour, y_test_hour = train_test_split(X_hour, y_hour, test_size=0.2, random_state=42)

# Model 1: Gradient Boosting
gb_model_hour = GradientBoostingRegressor()
gb_model_hour.fit(X_train_hour, y_train_hour)
gb_predictions_hour = gb_model_hour.predict(X_test_hour)

# Evaluate Gradient Boosting model
mse_gb_hour = mean_squared_error(y_test_hour, gb_predictions_hour)
print("Mean Squared Error (Gradient Boosting - Hourly Data):", mse_gb_hour)

# Model 2: AutoML with H2O.ai
hour_data_h2o = h2o.H2OFrame(hour_data)
x_hour = hour_data_h2o.columns
y_hour = 'cnt'
x_hour.remove(y_hour)

aml_hour = H2OAutoML(max_models=10, seed=42)
aml_hour.train(x=x_hour, y=y_hour, training_frame=hour_data_h2o)

# View the AutoML leaderboard
lb_hour = aml_hour.leaderboard
print(lb_hour)

# Shutdown H2O instance
#h2o.shutdown()

feature_importances_day = gb_model_day.feature_importances_

# Plotting feature importances
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(X_day.columns, feature_importances_day)
plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Feature Importance - Day Data (Gradient Boosting)')
plt.xticks(rotation=45)
plt.show()