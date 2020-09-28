#!/usr/bin/env python
# coding: utf-8

#    ## 어제 만들었던 by_date_2 이용해서 한 달간 모든 데이터 수집/저장
#   

# In[42]:


import requests

def by_date_2(date):
    url = 'https://api.sunrise-sunset.org/json?lat=37.5&lng=127.0'
    date_url = '&date='+date
    data = requests.get(url+date_url).json()['results']
    data['date'] = date

    return data


# In[41]:


import pandas as pd
all_dates = []
all_dates.append(by_date_2('2020-03-01'))
all_dates.append(by_date_2('2020-03-02'))
all_dates.append(by_date_2('2020-03-03'))

df = pd.DataFrame(all_dates)

df


# In[5]:


df.to_csv('my_sample.csv')
#______.csv
# csv 파일로 저장하기 --> 이 작업중인 파일이 있는 같은 폴더에 저장이 됨 


# In[7]:


#원하는 위치 주소 적기
# \ 표시 /로 바꾸기
path = 'C:/Users/gusan/OneDrive/바탕 화면/save/'
df.to_csv(path + 'my_sample.csv')


# ##### PERMISSION ERROR 라는 것이 발생한 경우?
# * 윈도우에서 엑셀이나 메모장으로 파일을 이미 열고 있는 경우 
# * 윈도우에서 파일을 사용하고 있는 것이므로 
# * 파이썬에서 해당 파일을 다룰 수 없기 때문에 권한이 없다는 표현이 나오는며 발생하는 에러

# ### 반복문 구현과 포메팅
# * 여러 날의 정보를 반복문으로 한 번에 모아서 일괄 저장 (loop?)

# ##### 가장 간단한 최신 포매팅 문법

# In[8]:


a = 10
for_format = f'가나다라{a}마바사'
#f 앞에 붙이고 중괄호 사이에 원하는 변수 넣기 --> 한 '' 안에 {} 중괄호 여러개 있어도 가능
#f'{a}' + f'{b}' == f'{a}{b}'

print(for_format)


# In[16]:


import pandas as pd
import time

all_dates = []
for i in range (5):
    i = i + 1
    all_dates.append(by_date_2(f'2020-03-{i}'))
    time.sleep(2) #한번 돌아갈때마다 2초씩 시간 늦추기
                     
df = pd.DataFrame(all_dates)
df.to_csv('five_days.csv')


# In[25]:


import pandas as pd
import time

all_dates = []
for i in range (31):
    i = i + 1
    all_dates.append(by_date_2(f'2020-03-{i}'))
    #time.sleep(2) #한번 돌아갈때마다 2초씩 시간 늦추기
                     
df = pd.DataFrame(all_dates)
df.to_csv('all_days.csv')


# ### 예외처리 (Exception)
# * 에러를 만나면 더 이상 코드가 실행되지 않는다 --> 멈춤 (break)
# * 따라서 멈추는 대신 대안을 만들어 주는 것이 예외 처리 
# * a 작업을 시켰는데 절차가 1->2->3->4 있습니다
# * 2단계 진행 중 서류에 적힌대로(SOP) 진행했는데 서류에 없는 내용이 발생
# * 일을 손에 놓고 회사 안나오고 잠수탑니다
# * 에러 발생 했을 때 손놓고 잠수타지 말고 이렇게도 해보렴? 이라고 하는게 예외 처리 

# In[18]:


print('안녕안녕')
'1' + 1
print('여기도 실행해줘요')


# * 이제 에러가 발생하더라도 손 놓고 놀지 말고 
# * 다른 곳의 코드를 실행할 수 있게 만들어 보려고 합니다

# In[21]:


try:
    print('안녕안녕')
    '1' + 1
    print('여기도 실행해줘요')
    
except:
    print('여기로 옵니다.')


# In[44]:


import pandas as pd
import time

all_dates = []
for i in range (31):
    i = i + 1
    
    try:
        all_dates.append(by_date_2(f'2020-02-{i}'))
        time.sleep(1) #한번 돌아갈때마다 2초씩 시간 늦추기
    
    except:
        continue
                     
df = pd.DataFrame(all_dates)
df.to_csv('feb_all_days.csv')


# ##### month_gather 이름의 함수 만들고
# * month_gather(2) --> 2020년도 2월 전체 수집/저장

# In[49]:


import pandas as pd
import time

all_dates=[]
def month_gather(month):
    for i in range (31):
        i = i + 1
        
        try:
            all_dates.append(by_date_2(f'2020-{month}-{i}'))
            time.sleep(1) #한번 돌아갈때마다 1초씩 시간 늦추기

        except:
            break
    df = pd.DataFrame(all_dates)
    df.to_csv(f'{month}_alldays.csv')
    
month_gather(2)


# ##### year_month 이름의 함수
# * year_month(2013, 3) --> 2012년도 3월 전체 수집 + 저장

# In[50]:


import pandas as pd
import time

all_dates=[]
def year_month(year, month):
    for i in range (31):
        i = i + 1
        
        try:
            all_dates.append(by_date_2(f'{year}-{month}-{i}'))
            time.sleep(1) #한번 돌아갈때마다 1초씩 시간 늦추기

        except:
            break
    df = pd.DataFrame(all_dates)
    df.to_csv(f'{year}_{month}_alldays.csv')
    
year_month(2020, 3)


# ##### 이번에 다룰 응답의 종류는 XML
# * !를 이용하면 마치 커맨드라인(cmd)에서 직접 명령어 입력하는 것과 같습니다
# * 파이썬 패키지(모듈, 라이브러리) 설치시 자주 이용하는 pip install
# * 이용해서 xmltodict 이름의 모듈을 설치해 줍니다

# In[51]:


get_ipython().system('pip install xmltodict')


# * 기본적으로 기존 JSON 다룰 때 진행한 순서와 동일합니다.
# * (요청을해서 받아온 이후에 딕셔너리처럼 사용한다는 것이)

# In[54]:


import requests
import xmltodict
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1168056500'
response = requests.get(url).text
weather_data = xmltodict.parse(response)


# In[59]:


weather_data['rss']['channel']['item'].keys()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




