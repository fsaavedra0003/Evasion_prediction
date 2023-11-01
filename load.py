import pandas as pd


# CSV file with history of evations

csv_file = 'evasion.csv'

#  CSV gets into a pandas DataFrame
df = pd.read_csv(csv_file)

# Print the CSV as Pandas Data Frame
print(df)
