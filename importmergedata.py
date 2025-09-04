import pandas as pd
import os 

# merging thousands of files into one 
csv_directory = "/Users/melodyhway/Downloads/PORTFOLIO PROJECT/data cleaning projects/businesstrends"

csv_files = [i for i in os.listdir(csv_directory) if i.endswith('.csv')]

dfs = []
for csv_file in csv_files: 
    file_path = os.path.join(csv_directory, csv_file)
    df = pd.read_csv(file_path)
    dfs.append(df)

# combined df
combined_df = pd.concat(dfs,  ignore_index=True)
# involes 2396549 rows 
print(combined_df.info)
print(combined_df.columns)
print(combined_df.head())

combined_df.to_csv("merged.csv")
