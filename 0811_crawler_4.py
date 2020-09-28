#!/usr/bin/env python
# coding: utf-8

# ##### get_news 이름이ㅡ 함수
# ##### get_news('펭수') 실행하면?
# * 펭수.csv 이름의 최신뉴스 검색결과 저장
# * 데이터 프레임 만들어야 함
# * 리스트에 딕셔너리 차곡차곡 넣어야 함
# * {'title': 뉴스제목 하나, 'desc' : 뉴스 내용 하나}
# * 엑셀에서 한글깨짐이 발생합니다

# In[27]:


import requests
import bs4
import pandas as pd

def get_news(keyword):
    url = 'http://newssearch.naver.com/search.naver?where=rss&query=' + keyword
    response = requests.get(url).text.encode('latin')
    news_data = bs4.BeautifulSoup(response, 'xml')
    news_list = news_data.find_all('item')

    news_compile = []

    for news in news_list:
        title = news.find('title').text
        desc = news.find('description').text
        news_compile.append({'Title' : title, 'Description' : desc})


    df = pd.DataFrame(news_compile)
    path = 'C:/Users/gusan/Downloads/0811_crawler_1_with_sub/'
    df.to_csv(path + keyword + '.csv',encoding='utf-8-sig')
    
get_news('펭수')

#pd.Dataframe(news_compile).to_csv(keyword + '.csv', encoding='utf-8-sig')


# # HTML
# * 기존에 다룬 XML과 많이 유사하지만 많이 복잡한 구조로 되어있는 HTML
# * 네이버 검색 후 내 컴퓨터 화면에 나오는 것은 HTML 데이터를 크롬이 해석한 것

# In[31]:


import requests
import bs4
url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%8E%AD%EC%88%98'
response = requests.get(url).text
one_page = bs4.BeautifulSoup(response) #페이지 검사 내용

    
one_page.find_all('span', class_= 'tit') #class는 class 설정한다는거


# In[33]:


import requests
import bs4
url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%8E%AD%EC%88%98'
response = requests.get(url).text
one_page = bs4.BeautifulSoup(response) #페이지 검사 내용
all_kw = []

for kw in one_page.find_all('span', class_='tit'):
    all_kw.append(kw.text)
    
all_kw
    


# # top_10 함수 만들기
# * top_10() 실행하면 실시간 인기 검색어 10개가 들어있는 리스트가 return 됩니다.

# In[2]:


import requests
import bs4
url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%8E%AD%EC%88%98'
response = requests.get(url).text
one_page = bs4.BeautifulSoup(response)
top_10_table = one_page.find('ol', class_="lst_realtime_srch _tab_area")
for single in top_10_table.find_all('li'):
    kw = single.find('a').find('span').find('span').text
    print(kw)


# In[13]:


import requests
import bs4

keyword_list = []

def top_10(keyword):
    url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='+ keyword
    response = requests.get(url).text
    one_page = bs4.BeautifulSoup(response)
    top_10_table = one_page.find('ol', class_="lst_realtime_srch _tab_area")
    
    for single in top_10_table.find_all('li'):
        kw = single.find('a').find('span').find('span').text #키워드 부분 찾으려고 타고 들어가는 거
        keyword_list.append(kw)

    print(keyword_list)
    
top_10('펭수')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




