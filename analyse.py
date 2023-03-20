import pandas as pd

df = pd.read_csv('/Users/pythonicninja/PycharmProjects/realestate-prices-trojmiasto-PL/cached_df.csv')
df = df.sort_values('gain', ascending=False)
print(df)

top_10_locations = df.to_numpy()[:10]
print(f"top_10_locations {top_10_locations}")
