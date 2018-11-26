import pandas as pd


raw_data = pd.read_csv('list_of_cfi_awards_for_web.csv', encoding="ISO-8859-1")
df_raw = pd.DataFrame(raw_data)
columns_list = []
for i in df_raw.loc[0]:
    i_split = i.split('/')
    columns_list.append(i_split[0])
print(columns_list)
df_raw.columns = columns_list
print(list(df_raw.columns.values))
df = pd.DataFrame(df_raw)
print(df['Area of Application'])
print(df.head())
print(df.dtypes)

