import requests
import time
import pandas as pd
sizes = (
    (1, "0-35"),
    (2, "36-60"),
    (3, "61-90"),
    (4, "91+"),
)
rows = []
for size, size_label in sizes:
    for idx in range(0, 300):
        uri = f"https://dom.trojmiasto.pl/ajax/barometer.json?type=1&localization=d{idx}&size={size}&first_month=2010-07-01&last_month=2023-02-01"
        try:
            req = requests.get(uri)
            data = req.json()
            prices = data['sec']
            min_price = data['min']
            max_price = data['max']
            location = data['seo']['heading']
            print(f"{location}")
            print(f"min: {min_price}")
            print(f"max: {max_price}")
            print(f"prices: {prices}")
            if not min_price and not max_price:
                continue
            rows.append({
                "location": location,
                "min_price": min_price,
                "max_price": max_price,
                "size": size_label,
                "uri": uri,
                "prices": prices,
            })
            time.sleep(2)
        except Exception:
            ...
df = pd.DataFrame.from_records(data=rows)
df.location = df.location.str.replace('Barometr Cen Nieruchomości ', '')
df = df.sort_values('max_price', ascending=False)
df.to_csv('/Users/pythonicninja/PycharmProjects/realestate-prices-trojmiasto-PL/cached_df.csv')
