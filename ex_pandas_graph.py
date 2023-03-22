import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
df = pd.DataFrame({
    'Year': [2010, 2011, 2012, 2013, 2014, 2015],
    'Sales': [50, 70, 90, 120, 150, 180]
})

# Plot the data
df.plot(x='Year', y='Sales', kind='line')

# Add chart labels
plt.title('Sales over Time')
plt.xlabel('Year')
plt.ylabel('Sales')

# Display the chart
plt.show()