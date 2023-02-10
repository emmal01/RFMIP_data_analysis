#! /usr/env/python 

from intake import open_catalog
cat = open_catalog("main.yml")

for m in list(cat.parameterized):
    for v in list(cat.parameterized[m]):
        print ("Model: ", m, " variant: ", v)
        for f in list(cat.parameterized[m][v]): 
            try: 
                x = cat.parameterized[m][v][f].to_dask()
            except: 
                print(f'{m} {v} {f} not available')
                print(cat.parameterized[m][v][f].urlpath)
