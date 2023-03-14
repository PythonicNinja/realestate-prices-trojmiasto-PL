# realestate-prices-trojmiasto-PL


```python
>>> df
                                          location  min_price  max_price  size                                             prices
0                      Barometr Cen Nieruchomości        4844      17280  0-35  [7075, 6415, 6652, 6633, 6822, 6870, 6845, 682...
1      Barometr Cen Nieruchomości Gdańsk Przymorze          0          0  0-35                                                 []
2       Barometr Cen Nieruchomości Gdańsk Wrzeszcz       5587      15739  0-35  [6555, 5974, 6360, 6188, 6277, 6289, 6308, 627...
3         Barometr Cen Nieruchomości Gdańsk Morena          0          0  0-35                                                 []
4    Barometr Cen Nieruchomości Gdynia Śródmieście          0          0  0-35                                                 []
..                                             ...        ...        ...   ...                                                ...
155   Barometr Cen Nieruchomości Gdańsk Matemblewo       5215      14269   91+  [6604, 6836, 6940, 7131, 7792, 7767, 8245, 771...
156      Barometr Cen Nieruchomości Gdańsk Siedlce       3973      14081   91+  [6479, 6040, 5539, 6428, 6304, 6100, 6055, 598...
157        Barometr Cen Nieruchomości Gdańsk Chełm       3944      10476   91+  [5794, 5839, 5553, 5448, 5478, 5504, 5541, 559...
158       Barometr Cen Nieruchomości Gdańsk Jasień       4281      10832   91+  [4936, 5309, 5276, 5439, 5334, 5341, 5341, 534...
159                    Barometr Cen Nieruchomości        4768      11698   91+  [6442, 6213, 6182, 6189, 6286, 6288, 6260, 622...

[160 rows x 5 columns]

>>> df.columns
Index(['location', 'min_price', 'max_price', 'size', 'prices'], dtype='object')

>>> df = df.sort_values('max_price', ascending=False)
>>> df
                                         location  min_price  max_price   size                                                uri                                             prices
69   Barometr Cen Nieruchomości Sopot Dolny Sopot       8423      43810  36-60  https://dom.trojmiasto.pl/ajax/barometer.json?...  [8423, None, None, 9428, 9926, 9894, 10120, 10...
29   Barometr Cen Nieruchomości Sopot Dolny Sopot       8989      41241   0-35  https://dom.trojmiasto.pl/ajax/barometer.json?...  [8989, 9782, 10197, 10583, 11293, 10774, 10284...
109  Barometr Cen Nieruchomości Sopot Dolny Sopot       8812      30023  61-90  https://dom.trojmiasto.pl/ajax/barometer.json?...  [10122, None, None, 10593, 10216, 10552, 10220...
149  Barometr Cen Nieruchomości Sopot Dolny Sopot       8020      30023    91+  https://dom.trojmiasto.pl/ajax/barometer.json?...  [8849, 9094, 9046, 9054, 8989, 9524, 9854, 987...
41    Barometr Cen Nieruchomości Gdańsk Przymorze       5846      23975  36-60  https://dom.trojmiasto.pl/ajax/barometer.json?...  [6732, 6824, 7083, 6347, 6590, 6644, 6698, 668...
..                                            ...        ...        ...    ...                                                ...                                                ...
134    Barometr Cen Nieruchomości Gdynia Chylonia       3655       6638    91+  https://dom.trojmiasto.pl/ajax/barometer.json?...  [5675, 5792, 5404, 5374, 5434, 5380, 4633, 488...
17     Barometr Cen Nieruchomości Gdynia Chwarzno       5449       6511   0-35  https://dom.trojmiasto.pl/ajax/barometer.json?...  [None, None, None, None, None, None, None, Non...
12   Barometr Cen Nieruchomości Gdynia Babie Doły       5188       6203   0-35  https://dom.trojmiasto.pl/ajax/barometer.json?...  [6203, 6117, 6036, None, 5898, 5670, 5916, 580...
132  Barometr Cen Nieruchomości Gdynia Babie Doły       3398       6098    91+  https://dom.trojmiasto.pl/ajax/barometer.json?...  [5018, 5001, 5015, 5012, 4936, 4937, 4937, 469...
136    Barometr Cen Nieruchomości Gdynia Demptowo       3678       5797    91+  https://dom.trojmiasto.pl/ajax/barometer.json?...  [5105, None, None, 5114, None, None, None, Non...

>>> df.to_csv('sorted_df.csv')

```