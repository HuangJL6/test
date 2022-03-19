
# coding: utf-8

# In[26]:


import requests
import json
import datetime
import time
from time import strftime,sleep


# In[27]:


url="https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/63dd903c-55b0-4c0d-a4a0-bf77e4bde8ea"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"}
RS=requests.get(url=url,headers=headers)
text =RS.text
json1=json.loads(text)
name=json1['data']['name']
Yprice=json1['data']['market_price']/100
Zprice=json1['data']['price']/100
GG=json1['data']['spec']
XQ=json1['data']['sub_title']


# In[30]:


print("--------"+name+"--------")
print("原价:"+str(Yprice))
print("折后价:"+str(Zprice))
print("规格:"+GG)
print("详情："+XQ)
print("\n\n--------"+name+"的价格波动--------")
i=1
for i in range(15):
    NowTime=time.strftime('%Y-%m-%d %H-%M-%S')
    print("现在时间为："+NowTime+","+name+":价格为："+str(price))
    sleep(5)

