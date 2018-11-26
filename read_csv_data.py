import pandas as pd


raw_data = pd.read_csv('list_of_cfi_awards_for_web.csv', encoding="ISO-8859-1")
df_raw = pd.DataFrame(raw_data)
df_raw = df_raw.reset_index()

print(df_raw.iloc[1])
print(df_raw.loc[1])
print(list(df_raw.columns.values))


