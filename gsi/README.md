## GSI API

### using GSI API
GSI API examples.

#### get_max_depth(LAT, LON, key=None)
Please refer to original document if you'd like to about parameters. [ https://suiboumap.gsi.go.jp/pdf/Data-riyo_manual.pdf (p.9) ]
You can get json Data about Flood Depth and so on. If you need to the single parameter, you have to set the key as parameter name.

Demo:
```python
print("Kyushu University, Hakozaki campus.")
print( gsi.get_max_depth(33.62677707060762, 130.42496194503377) )
print( gsi.get_max_depth_keys() )
print( gsi.get_max_depth(33.62677707060762, 130.42496194503377, "Depth") )
```
Output : 
```python
Kyushu University, Hakozaki campus.
{'Depth': 0.31, 'OfficeCode': '10241', 'RiverCode': '4000190002', 'SubRiverCode': '_', 'CSVScale': 0}
['Depth', 'OfficeCode', 'RiverCode', 'SubRiverCode', 'CSVScale']
0.31
```

---
