# Imports
import pandas
from sklearn.linear_model import LinearRegression

# Reading the data
data = pandas.read_csv('antarctica_mass.csv')

# Defining the model
model = LinearRegression()

# Training the model
model.fit(data[['TIME']], data[['Antarctic mass']])

# Printing the predicted output
print(model.predict([[2030]]))