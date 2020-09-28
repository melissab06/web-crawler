#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 이 공간(셀)에서 코드를 작성합니다
# shift + enter 또는 ctrl + enter 로 실행합니다
print('Hello World!')


# # 가장 큰 글자
# ##### ### 아주 작은 글자
# * 소제목 만드는 데 사용 가능

# ##### 딕셔너리 다루기
# * 딕셔너리 안의 딕셔너리

# In[9]:


data = {"results":{"sunrise":"5:32:31 AM","sunset":"7:12:56 PM","solar_noon":"12:22:44 PM","day_length":"13:40:25","civil_twilight_begin":"5:04:53 AM","civil_twilight_end":"7:40:34 PM","nautical_twilight_begin":"4:31:28 AM","nautical_twilight_end":"8:13:59 PM","astronomical_twilight_begin":"3:56:04 AM","astronomical_twilight_end":"8:49:23 PM"},"status":"OK"}
data['results']['day_length']


# In[14]:


for i in [0,1,2]:
    print(i)


# In[13]:


data = {"results":{"sunrise":"5:32:31 AM","sunset":"7:12:56 PM","solar_noon":"12:22:44 PM","day_length":"13:40:25","civil_twilight_begin":"5:04:53 AM","civil_twilight_end":"7:40:34 PM","nautical_twilight_begin":"4:31:28 AM","nautical_twilight_end":"8:13:59 PM","astronomical_twilight_begin":"3:56:04 AM","astronomical_twilight_end":"8:49:23 PM"},"status":"OK"}
for k in data['results'].keys():
    print(k)


# # request - 요청
# * 우리가 주소창에 naver.com 입력해서 네이버 홈페이지 들어갔다는 것은 
# * naver.com 내용으로 요청(request)을 한 결과가 내 컴퓨터로 왔고
# * 그 결과를 구글 크롬으로 해석하면 네이버 홈페이지 화면입니다
# * 스마트폰으로건 컴퓨터로건 알게 모르게 요청을 이용하고 있었습니다

# In[30]:


import requests


def by_date(date):
    url = 'https://api.sunrise-sunset.org/json?lat=37.5&lng=127.0'
    date_url = '&date='+date
    data = requests.get(url+date_url).json()['results']
    return data

by_date('2020-03-01')


# ##### 문자열 복습
# * 더하기, formatting 

# In[19]:


a = '야옹'
b = '멍멍'
c = a + b
print(c)


# # 데이터 프레임
# * 데이터를 가로 x 세로 직사각형 모양으로 틀을 갖춰서 저장하는 자료의 형태입니다.
# * 가로(행/row)
# * 세로(열/column)
# * 같은 column 안의 데이터들은 같은 속성을 갖고 있어요
# * 같은 row 안의 데이터들은 하나로 묶었을 때 특정 의미를 갖습니다

# ![KakaoTalk_20200811_212239170.png](attachment:KakaoTalk_20200811_212239170.png)

# * 한 row 당 한사람의 설명/정보, column은 특징
# * 이를 딕셔너리로 생각해본다면
# * 각 column들의 이름이 딕셔너리의 key
# * 한 key에 value들이 순서를 갖고 리스트처럼 들어있다고 볼 수 있다
# * 한 row 당 하나의 딕셔너리 
# * 딕셔너리에서 {key : 값} --> {column1 : [value1, value2, value3, ....]}

# In[25]:


dates = []
dates.append(by_date('2020-03-01'))
dates.append(by_date('2020-03-02'))
dates.append(by_date('2020-03-03'))

#dates라는 list에 dictionary 3개 입력
#딕셔너리들이 키가 동일

len(dates)


# In[26]:


import pandas as pd
pd.DataFrame(dates)


# In[27]:


by_date('2020-03-01')


# In[28]:


by_date('2020-03-01')['day_length']


# ##### by_date에 날짜 추가하기

# In[31]:


import requests


def by_date2(date):
    url = 'https://api.sunrise-sunset.org/json?lat=37.5&lng=127.0'
    date_url = '&date='+date
    data = requests.get(url+date_url).json()['results']
    data['date'] = date
    return data


# In[32]:


dates = []
dates.append(by_date2('2020-03-01'))
dates.append(by_date2('2020-03-02'))
dates.append(by_date2('2020-03-03'))


len(dates)


# In[33]:


pd.DataFrame(dates)


# In[ ]:




