import pandas as pd 
import timeit
from pyodide.http import open_url
rl_content = open_url("")
df=pd.read_csv("data.csv",names=["이름","내용"])
name = df['이름']
information = df['내용']
csv = Element('csv')
csv.write(df)
k = Element('result')

def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
    return -1
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2

        if element == some_list[mid_index]:
            return mid_index

        elif element < some_list[mid_index]:
            end_index = mid_index - 1

        else:
            start_index = mid_index + 1

    return -1
#def hash_search(element, some_list):
#  for i in range(len(some_list)):

def lin_Search(*args):
  userinput = Element("userinput")
  q = userinput.value
  start = float(timeit.default_timer())
  a = linear_search(q,name)
  c = linear_search(q,information)
  end=float(timeit.default_timer())
  total = str(end - start)
  if(a >= 0):
    h = df.loc[a]
    v = h['내용']
    k.write([v,total+"초"])
    userinput.clear()
  else:
    if(c >= 0):
      h = df.loc[c]
      v = h['이름']
      k.write([v,total+"초"])
    else:
      k.write(["없음",total + "초"])
      userinput.clear()

def bin_Search(*args):
  userinput = Element("userinput")
  q = userinput.value
  start = float(timeit.default_timer())
  a = binary_search(q,name)
  end=float(timeit.default_timer())
  total = str(end - start)
  if(a >= 0):
    h = df.loc[a]
    k.write([h,total+"초"])
    userinput.clear()
  else:
    k.write(["없음",total + "초"])
    userinput.clear()
