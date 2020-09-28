#!/usr/bin/env python
# coding: utf-8

# ##### 이번에 다룰 응답의 종류는 XML
# * !를 이용하면 마치 커맨드라인(cmd)에서 직접 명령어 입력하는 것과 같습니다
# * 파이썬 패키지(모듈, 라이브러리) 설치시 자주 이용하는 pip install
# * 이용해서 xmltodict 이름의 모듈을 설치해 줍니다

# #### 1. XML을 딕셔너리처럼 다루는 방법
# #### 2. 딕셔너리가 아닌 방법으로 다루는 방법
# * xmltodict --> xml 을 dict (딕셔너리)로 바꿈 
# 

# In[1]:


get_ipython().system('pip install xmltodict')


# In[6]:


import requests
import xmltodict
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168056500'
response = requests.get(url).text
weather_data = xmltodict.parse(response)


# * rss --> channel --> item --> description --> body --> data --> wfKor (날씨)

# In[7]:


weather_data['rss']['channel']['item']['description']['body'].keys()


# In[8]:


weather_data['rss']['channel']['item']['description']['body']['data'].keys()


# In[10]:


sample_list = [1,2,3]
sample_list.


# In[11]:


data_list = weather_data['rss']['channel']['item']['description']['body']['data']
data_list[0].keys()


# In[12]:


data_list = weather_data['rss']['channel']['item']['description']['body']['data']
data_list[0]['wfKor']


# In[21]:


data_list = weather_data['rss']['channel']['item']['description']['body']['data']
data_list[4]['day']


# ##### 코드 한번에

# In[15]:


import requests
import xmltodict
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168056500'
response = requests.get(url).text
weather_data = xmltodict.parse(response)
data_list = weather_data['rss']['channel']['item']['description']['body']['data']

for one in data_list:
    print(one['wfKor'])


# ##### wfKor에는 날씨 정보가 있고, day에는 요일 정보가 있습니다.
# ##### 요일 정보는 0, 1, 2가 들어있고 0은 오늘 1은, 1은 내일, 2는 모레입니다.
# ### 내일의 날씨 정보만 모두 선택해 화면에 출력해보세요.

# In[34]:


import requests
import xmltodict
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168056500'
response = requests.get(url).text
weather_data = xmltodict.parse(response)
data_list = weather_data['rss']['channel']['item']['description']['body']['data']

for one in data_list:
    if one['day'] == "1":
        print(one['wfKor'])


# In[37]:


import requests
import xmltodict
url = 'http://newssearch.naver.com/search.naver?where=rss&query=%ED%8E%AD%EC%88%98'
response = requests.get(url).text.encode('latin')
news_data = xmltodict.parse(response)


# In[38]:


news_data.keys()


# In[42]:


news_data['rss']['channel']['item'].keys()


# ### 이 안에 있는 모든 뉴스의 제목을 프린트

# In[60]:


import requests
import xmltodict
url = 'http://newssearch.naver.com/search.naver?where=rss&query=펭수'
response = requests.get(url).text.encode('latin')
news_data = xmltodict.parse(response)
data_list = news_data['rss']['channel']['item']

for one in data_list:
    print(one['title'])


# # BeautifulSoup
# * 딕셔너리가 아닌 방법으로 데이터를 다룹니다.
# * 단단계가 아무리 많더라도 3~5단계 이내로 원하는 정보 선택 가능

# In[52]:


import requests
import bs4
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168056500'
response = requests.get(url).text
weather_data = bs4.BeautifulSoup(response)
weather_data.find('language')


# In[50]:


import requests
import bs4
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168056500'
response = requests.get(url).text
weather_data = bs4.BeautifulSoup(response)
weather_data.find_all('wfkor')


# In[53]:


import requests
import bs4
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168056500'
response = requests.get(url).text
weather_data = bs4.BeautifulSoup(response)

for single in weather_data.find_all('wfkor'):
    print(single.text)


# In[57]:


import requests
import bs4
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168056500'
response = requests.get(url).text
weather_data = bs4.BeautifulSoup(response)

for single in weather_data.find_all('data'): #data = 태그 !! 
    d = single.find('day').text
    w = single.find('wfkor').text
    if d == "1":
        print(d, w)


# In[66]:


import requests
import bs4
url = 'http://newssearch.naver.com/search.naver?where=rss&query=펭수'
response = requests.get(url).text.encode('latin')
news_data = bs4.BeautifulSoup(response)

for news in news_data.find_all('item'):
    print(news.find('title').text)
    
    
#news_list = news_data.find_all('item')
#for news in news_list:
#    title = news.find('title').text
#    print(title)


# In[67]:


import requests
import bs4
url = 'http://newssearch.naver.com/search.naver?where=rss&query=펭수'
response = requests.get(url).text.encode('latin')
news_data = bs4.BeautifulSoup(response, 'xml')

for news in news_data.find_all('item'):
    print(news.find('description').text)


# In[68]:


help(bs4.BeautifulSoup)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




