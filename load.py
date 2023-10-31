import pandas as pd


# CSV file with history of evations which initial needed.
csv_file = 'evasion.csv'

#  CSV gets into a pandas DataFrame
df = pd.read_csv(csv_file)

# Print the Data frame
print(df)
