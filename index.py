import pandas as pd 
from pyodide.http import open_url
url_content = open_url("192.168.0.5/genius/data.csv")
df = pd.read_csv(url_content)
#print(df)    
csv = Element('csv')
csv.write(df.head())