import pandas as pd 
from pyodide.http import open_url
rl_content = open_url("https://raw.githubusercontent.com/woosuk-choi0523/genius/master/data.csv")
df=pd.read_csv(rl_content,names=["이름","내용"])
name = df['이름']
csv = Element('csv')
csv.write(df)
k = Element('result')

def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
    return -1
def Search(*args):
  userinput = Element("userinput")
  q = userinput.value
  a = linear_search(q,name)
  if(a >= 0):
    h = df.loc[a]
    k.write(h)
  else:
    j= "없음"
    k.write(j)

  userinput.clear()
