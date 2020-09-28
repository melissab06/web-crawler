#!/usr/bin/env python
# coding: utf-8

# #  물리 드라이버 - Selenium

# In[1]:


get_ipython().system('pip install selenium')


# In[19]:


from glob import glob
from selenium import webdriver
path = 'C:/Users/user/Downloads/chromedriver_win32'
#\ 표시 / 로 변경
full_path = glob(path + "/*")[0]
driver = webdriver.Chrome(full_path) #크롬창 제어


# In[37]:


driver.get('https://www.naver.com')


# In[16]:


driver.back() #뒤로가기


# In[17]:


driver.close()


# ##### 버튼을 눌러보려고 합니다
# * 사람 기준 순서
# * 1. 어디있나 알아야함
# * 2. 마우스 가져다 대고
# * 3. 클릭

# In[38]:


btn_path = '//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[9]/a' #네이버 메인 웹툰 버튼 위치 저장 / 버튼 마우스 우클릭 검사 후 Xpath 복붙
webtoon_btn = driver.find_element_by_xpath(btn_path)
webtoon_btn.click() #버튼은 click method 존재


# In[39]:


btn_path = '//*[@id="menu"]/ul/li[3]/a' #네이버 메인 웹툰 버튼 위치 저장 / 버튼 마우스 우클릭 검사 후 Xpath 복붙
webtoon_btn = driver.find_element_by_xpath(btn_path)
webtoon_btn.click() #버튼은 click method 존재


# In[70]:


from glob import glob
from selenium import webdriver
path = 'C:/Users/user/Downloads/chromedriver_win32'
#\ 표시 / 로 변경
full_path = glob(path + "/*")[0]
driver = webdriver.Chrome(full_path) #크롬창 제어


# In[71]:


driver.get('https://www.aladin.co.kr/home/wusedshopmain.aspx')


# In[72]:


search_path = '//*[@id="SearchWord"]'
search_box = driver.find_element_by_xpath(search_path)
search_box.send_keys('개념원리') #검색창에 입력


# In[73]:


btn_path = '//*[@id="global_search"]/input'
search_btn = driver.find_element_by_xpath(btn_path)
search_btn.click()


# In[80]:


#합친거
keyword = '기본영어'
search_path = '//*[@id="SearchWord"]'
search_box = driver.find_element_by_xpath(search_path)
search_box.send_keys(keyword)
btn_path = '//*[@id="global_search"]/input'
search_btn = driver.find_element_by_xpath(btn_path)
search_btn.click()


# In[76]:


import time
search_path = '//*[@id="SearchWord"]'
search_box = driver.find_element_by_xpath(search_path)
search_box.send_keys(Keys.CONTROL+'a')
time.sleep(2)
search_box.send_keys(Keys.DELETE)


# In[83]:


search_path = '//*[@id="SearchWord"]'
search_box = driver.find_element_by_xpath(search_path)
search_box.clear()


# In[90]:


from selenium.webdriver.common.action_chains import ActionChains
import time

first_path = '//*[@id="#head_used_layer"]/a/img'
second_path = '//*[@id="head_used_layer"]/div[1]/table/tbody/tr/td[1]/table/tbody/tr[4]/td/a'
action = ActionChains(driver)
mouse_go = driver.find_element_by_xpath(first_path) #마우스를 저 first_path의 위치로 옮겨야 한다
action.move_to_element(mouse_go).perform() #(mouse_go) 이 구성요소로 움직이겠다는 method #perform = 실행
time.sleep(5)
good_parents = driver.find_element_by_xpath(second_path)
good_parents.click()


# In[91]:


import bs4
response = driver.page_source
one_page = bs4.BeautifulSoup(response)


# In[ ]:





# In[ ]:





# In[ ]:




