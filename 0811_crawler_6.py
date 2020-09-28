#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Robots.txt
# ### User-agent: 로봇의 이름(크롤러 이름)
# ### Allow: 어느 영역을(페이지) 허용할 것인가?
# ### Disallow: 어느 영역(페이지)을 허용하지 않을 것인가?
# ### Crawl-delay: 1회 크롤링(접속) 후 몇 초 쉬어야 하는가?

# ![robots.txt_example.png](attachment:robots.txt_example.png)

# * 권고 수준이고 지킬 의무는 없지만 사이트 주인 입장에서는 
# * 위 사항을 안 지킬 경우 아이피를 차단하는 수가 있으므로 지키는 것을 권장

# ![sites_example.png](attachment:sites_example.png)

# # 지난 5일간 내용을 종합하여 크롤러 만들기
# * 1. (requests, bs4) 알라딘 서점에서 베스트셀러 책 제목 50개를 가져옵니다.
# * 2. (selenium) 알라딘 중고서점에서 베스트셀러 책 제목을 검색합니다.
# * 3. 2번에 대해 50번 진행합니다.
# * 4. 검색어 - 검색결과 쌍을 데이터 프레임으로 저장합니다.

# ##### 1. (requests, bs4) 알라딘 서점에서 베스트셀러 책 제목 50개를 가져옵니다.

# In[1]:


import requests
import bs4
url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we'
response = requests.get(url).text
one_page = bs4.BeautifulSoup(response)
# 코딩 시간~


# In[6]:





# In[16]:


# 위 내용을 두 함수로 만들어 줍니다.

# best_page = get_best_page()
# 한 페이지의 response가 best_page변수에 들어갑니다.
def get_best_page():
    url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we'
    response = requests.get(url).text
    return response
    
    # 코딩 시간~

    return response
# all_books = get_one_page_books(best_page)
# all_books 변수에 50개의 베스트셀러 책이 들어있어야 합니다.
def get_one_page_books(one_page):
    url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we'
    response = requests.get(url).text
    one_page = bs4.BeautifulSoup(response)
    all_best = []
    for name in  one_page.find_all('div', class_='ss_book_box'):
        bk = name.find('b').text
        all_best.append(bk)

    return all_best


# In[17]:


best_page = get_best_page()
all_books = get_one_page_books(best_page)
len(all_books)


# ##### 2. (selenium) 알라딘 중고서점에서 베스트셀러 책 제목을 검색합니다.

# In[26]:


from selenium import webdriver
from glob import glob
import time

def initialize():
    path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
    driver = webdriver.Chrome(path)
    used_url = 'https://www.aladin.co.kr/home/wusedshopmain.aspx'
    driver.get(used_url)
    return driver

# all_books = find_used_books(중고책 검색어)
# all_books 변수에 중고책 검색 결과가 들어있어야 합니다.

def find_used_books(keyword, driver):
    search_box_path = '/html/body/div[1]/table/tbody/tr/td[2]/form/div/div[2]/input[2]'#full XPath
    search_box = driver.find_element_by_xpath(search_box_path) #입력창 선택
    search_box.clear()
    search_box.send_keys(keyword) #키워드 입력
    search_go_path = '/html/body/div[1]/table/tbody/tr/td[2]/form/div/input'
    search_go_button = driver.find_element_by_xpath(search_go_path)
    search_go_button.click() #검색 버튼 클릭
    time.sleep(2)
    return driver.page_source


# In[25]:


# 위 내용을 두 함수로 만들어 줍니다.

# driver = initialize()
# 크롬창을 하나 만들어 중고서점으로 접속합니다. 
# 이후 그 크롬창을 driver라는 변수로 제어합니다.
def initialize():
    path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe' #크롬 위치
    driver = webdriver.Chrome(path)
    used_url = 'https://www.aladin.co.kr/home/wusedshopmain.aspx?start=we_tab'
    dirver.get(used_url)
    return driver

    return driver
# all_books = find_used_books(중고책 검색어)
# all_books 변수에 중고책 검색 결과가 들어있어야 합니다.
def find_used_books(keyword, driver):
    

    return driver.page_source


# In[23]:


driver = initialize()
one_page = find_used_books('수학의 정석', driver)
get_one_page_books(one_page)
# 이 코드 실행 결과는 수학의 정석 검색했을 때 한 페이지에 나오는 모든 검색 결과가 나와야 합니다.


# ##### 3. 1 -> 2번에 대해 베스트셀러 50개를 진행합니다.

# In[31]:


import pandas as pd
def book_profit():
    best_page = get_best_page()
    best_books = get_one_page_books(best_page)
    driver = initialize()
    result = []
    for book in best_books:
        one_page = find_used_books(book, driver)
        search_result = get_one_page_books(one_page)
        search_dict = {'title' : book, 'result' : str(search_result)}
        result.append(search_dict)
    pd.DataFrame(result).to_csv('best_used.csv', encoding='utf-8-sig')
    
book_profit()


# In[ ]:





# ##### 4. 검색어 - 검색결과 쌍을 데이터 프레임으로 저장합니다.

# In[28]:


# 코딩 시간~


# In[ ]:





# In[ ]:





# In[ ]:




