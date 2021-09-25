#!/usr/bin/env python
# coding: utf-8

# <b>Python Scraping of Book Information</b>

# In[1]:


get_ipython().system('pip install bs4')


# In[2]:


get_ipython().system('pip install splinter')


# In[3]:


get_ipython().system('pip install webdriver_manager')


# In[1]:


# Setup splinter
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time 
import pandas as pd
import requests


# In[ ]:





# In[42]:


# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)

# url = 'http://books.toscrape.com/'
# browser.visit(url)



    
    
    
    
# for x in range(50):
#     html = browser.html
    
#     soup = BeautifulSoup(html, 'html.parser')
    
    
#     articles = soup.find_all('article', class_='product_pod')
    
#     for article in articles: 
#         h3 = article.find("h3")
#         link = h3.find("a")
#         href = link["href"]
#         title = link["title"]
#         print("----------")
#         print(title)
#         url = "http://books.toscrape.com/" + href
#         browser.visit(url)
        
    
#     try:        
        
#         current_page = current_page + 1
#         web_page_url = f"https://books.toscrape.com/catalogue/category/books_1/page-{current_page}.html"
#         browser.visit(web_page_url)
#         browser.links.find_by_partial_text("next").click()
        
#         print('It worked')
#     except:
#         print("Scraping Complete")
        
# browser.quit()
   


# In[57]:


# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)

# pageNumber= pageNumber + 1
# url = 'http://books.toscrape.com/'
# pageUrl = f'http://books.toscrape.com/catalogue/page-{pageNumber}.html'
# browser.visit(url)

# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')



# for x in range(20):
#     html = browser.html
    
#     soup = BeautifulSoup(html, 'html.parser')
    
    
#     articles = soup.find_all('article', class_='product_pod')
    
#     for article in articles: 
#         h3 = article.find("h3")
#         link = h3.find("a")
#         href = link["href"]
#         title = link["title"]
#         print("----------")
#         print(title)
#         #time.sleep(1)
#         url = "http://books.toscrape.com/" + href
#         browser.visit(url)
        
        
        
       
        
        
        
    
#     try: 
#         browser.visit(pageUrl)
#         browser.links.find_by_partial_text("next").click()
#     except:
#         print("Scraping Complete")
       
     
        
# browser.quit()   
   


# In[2]:


#Working through each book and page

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

pageUrl=""
for i in range(1,3):
    if(i == 1):
        pageUrl = f"https://books.toscrape.com/index.html"
    else: 
        pageUrl = f'https://books.toscrape.com/catalogue/page-{i}.html'
    print(pageUrl)
    
    
    browser.visit(pageUrl)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    articles = soup.find_all('article', class_='product_pod')
    
    for article in articles: 
        h3 = article.find("h3")
        link = h3.find("a")
        href = link["href"]
        title = link["title"]
        print("----------")
        print(title)
        #time.sleep(1)
        url = "http://books.toscrape.com/" + href
        browser.visit(url)
        

        
       
     
        
browser.quit()           
        
    


# In[97]:


#Proof of concept using books.toscrape.com

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

pageUrl=""
for i in range(1,2):
    if(i == 1):
        pageUrl = f"https://books.toscrape.com/index.html"
    else: 
        pageUrl = f'https://books.toscrape.com/catalogue/page-{i}.html'
    print(pageUrl)
    
    
    browser.visit(pageUrl)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    articles = soup.find_all('article', class_='product_pod')
    
    for article in articles: 
        h3 = article.find("h3")
        link = h3.find("a")
        href = link["href"]
        title = link["title"]
        print("----------")
        print(title)
        #time.sleep(1)
        url = "http://books.toscrape.com/" + href
        browser.visit(url)
        res=requests.get(url)
        soup = BeautifulSoup(res.content,'lxml')
        table = soup.find_all('table')[0] 
        df = pd.read_html(str(table))[0]
        print(df)
               
             
        
browser.quit()          


# In[20]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

pageUrl=""
table_of_tables = []



for i in list(50,75,100):
    
    table_on_page = []
    
    if(i == 25):
        pageUrl = f"https://books.toscrape.com/index.html"
    else: 
        pageUrl = f'https://books.toscrape.com/catalogue/page-{i}.html'
    print(pageUrl)
    
    
    browser.visit(pageUrl)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    articles = soup.find_all('article', class_='product_pod')
    
    for article in articles: 
        h3 = article.find("h3")
        link = h3.find("a")
        href = link["href"]
        title = link["title"]
        print("----------")
        print(title)
        #time.sleep(1)
        url = "http://books.toscrape.com/" + href
        browser.visit(url)
        res=requests.get(url)
        soup = BeautifulSoup(res.content,'lxml')
        table = soup.find_all('table')[0]
        table_on_page.append(table)
#         table_of_tables.append(table_on_page)
        df = pd.read_html(str(table))[0]
        print(df)
               
             
        
browser.quit()          


# In[61]:





# In[48]:


df = pd.DataFrame(table_on_page)
df.to_csv('books2scrape.csv')


# In[52]:


df_to_clean=pd.read_csv('books2scrape.csv')


# In[64]:


df_columns_cleaned = df_to_clean.drop(columns=['Unnamed: 0','0','2','4','6','8','10','12','14'])


# In[71]:


df_columns_cleaned.columns


# In[66]:


df_columns_cleaned.head()


# In[78]:


html_chars = ["<tr>","\n","</th>","<th>","<td>","</td>",
              "</tr>"]
for char in html_chars:
    df_columns_cleaned['1'] = df_columns_cleaned['1'].str.replace(char, ' ')
    df_columns_cleaned['3'] = df_columns_cleaned['3'].str.replace(char, ' ')
    df_columns_cleaned['5'] = df_columns_cleaned['5'].str.replace(char, ' ')
    df_columns_cleaned['7'] = df_columns_cleaned['7'].str.replace(char, ' ')
    df_columns_cleaned['9'] = df_columns_cleaned['9'].str.replace(char, ' ')
    df_columns_cleaned['11'] = df_columns_cleaned['11'].str.replace(char, ' ')
    df_columns_cleaned['13'] = df_columns_cleaned['13'].str.replace(char, ' ')


# In[79]:


df_columns_cleaned


# In[290]:


# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)

# pageUrl=""
# table_of_tables = []



# for i in range(1):
    
#     table_on_page = []
    
   
#     pageUrl = f'ttps://www.hpb.com/books/best-sellers/784-classics?&size=350&&&'
     
    
#     print(pageUrl)
    
    
#     browser.visit(pageUrl)
#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')
    
#     articles = soup.find_all('article', class_='product_pod')
    
#     for article in articles:
#         time.sleep(randint(1,3))
#         section = article.find("section")
#         link = section.find("a")
#         href = link["href"]
#         print(href)
#         title = link["title"]
#         print("----------")
#         print(title)
#         time.sleep(randint(1,3))
#         url = href
#         browser.visit(url)
#         res=requests.get(url)
#         time.sleep(randint(3,5))
#         soup = BeautifulSoup(res.content,'lxml')
#         table = soup.find_all('table')[0]
#         table_on_page.append(table)
# #         table_of_tables.append(table_on_page)
#         df = pd.read_html(str(table))[0]
#         print(df)
               
             
        
# browser.quit()          


# In[198]:


#https://stackoverflow.com/questions/31064981/python3-error-initial-value-must-be-str-or-none-with-stringio
import io


# In[267]:


#grab data from https://citylights.com/greek-roman/

import random



executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


table_of_data = []
    
pageUrl=""
for i in range(1,7):
    
    data_on_page = []
    
    if(i == 1):
        pageUrl = f"https://citylights.com/greek-roman/"
    else: 
        pageUrl = f'https://citylights.com/greek-roman/page/{i}/'
    print(pageUrl)
    
    time.sleep(1)
    browser.visit(pageUrl)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #https://stackoverflow.com/questions/52842778/find-partial-class-names-in-spans-with-beautiful-soup
    articles = soup.find_all('li', attrs={'class': lambda e: e.startswith('product type-product post') if e else False})
    
    for article in articles: 
        time.sleep(1)
        link = article.find('a')
        href = link["href"]
        print("----------")
        print(href)
        url = href
        browser.visit(url)
        time.sleep(randint(1,2))
        res=requests.get(url)
        soup = BeautifulSoup(res.content,'lxml')
        data = soup.find_all('div', attrs={'class': 'detail-text mb-50'})[0].get_text()
        data_on_page.append(data)
        table_of_data.append(data_on_page)
        df = pd.DataFrame(table_of_data)[0]
        print(data)

        
browser.quit()           
        
   


# In[268]:


df.to_csv('greek-roman.csv')


# In[269]:


df_greek_roman_to_clean=pd.read_csv('greek-roman.csv')

df_greek_roman_to_clean_columns = df_greek_roman_to_clean.drop(columns=['Unnamed: 0'])


# In[270]:


df_greek_roman_to_clean_columns


# In[271]:


df_greek_roman_to_clean_columns_split = df_greek_roman_to_clean_columns['0'].str.split("\n\t")


# In[272]:


df_greek_roman = df_greek_roman_to_clean_columns_split.to_list()
column_names = ['0','ISBN-10','ISBN-13','Publisher','Publish Date', 'Dimensions']
new_greek_roman_df = pd.DataFrame(df_greek_roman,columns=column_names)


# In[273]:


clean_greek_roman_df=new_greek_roman_df.drop(columns=['0','Dimensions'])


# In[274]:


clean_greek_roman_df.head()


# In[275]:


html_chars = ["<tr>","\n","</th>","<th>","<td>","</td>",
              "</tr>",'\t']
for char in html_chars:
    clean_greek_roman_df['ISBN-10'] = clean_greek_roman_df['ISBN-10'].str.replace(char, ' ')
    clean_greek_roman_df['ISBN-13'] = clean_greek_roman_df['ISBN-13'].str.replace(char, ' ')
    clean_greek_roman_df['Publisher'] = clean_greek_roman_df['Publisher'].str.replace(char, ' ')
    clean_greek_roman_df['Publish Date'] = clean_greek_roman_df['Publish Date'].str.replace(char, ' ')
   
    


# In[276]:


pd.set_option("max_colwidth", 1000)
clean_greek_roman_df.head()


# In[277]:


clean_greek_roman_df.to_csv('greek-roman-clean.csv')


# In[ ]:





# In[279]:


# grab data from https://citylights.com/asian/

import random



executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


table_of_data = []
    
pageUrl=""
for i in range(1,5):
    
    data_on_page = []
    
    if(i == 1):
        pageUrl = f"https://citylights.com/asian/"
    else: 
        pageUrl = f'https://citylights.com/asian/page/{i}/'
    print(pageUrl)
    
    time.sleep(1)
    browser.visit(pageUrl)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #https://stackoverflow.com/questions/52842778/find-partial-class-names-in-spans-with-beautiful-soup
    articles = soup.find_all('li', attrs={'class': lambda e: e.startswith('product type-product post') if e else False})
    
    for article in articles: 
        time.sleep(randint(1,2))
        link = article.find('a')
        href = link["href"]
        print("----------")
        print(href)
        url = href
        browser.visit(url)
        time.sleep(1)
        res=requests.get(url)
        soup = BeautifulSoup(res.content,'lxml')
        data = soup.find_all('div', attrs={'class': 'detail-text mb-50'})[0].get_text()
        data_on_page.append(data)
        table_of_data.append(data_on_page)
        df = pd.DataFrame(data_on_page)[0]
        print(data)

        
browser.quit()           


# In[280]:


df.to_csv('asian.csv')


# In[281]:


df_asian_classics_to_clean=pd.read_csv('asian.csv')

df_asian_classics_to_clean_columns = df_asian_classics_to_clean.drop(columns=['Unnamed: 0'])


# In[282]:


df_asian_classics_to_clean_columns


# In[283]:


df_asian_classics_to_clean_columns_split = df_asian_classics_to_clean_columns['0'].str.split("\n\t")


# In[284]:


df_asian_classics = df_asian_classics_to_clean_columns_split.to_list()
column_names = ['0','ISBN-10','ISBN-13','Publisher','Publish Date', 'Dimensions']
new_asian_classics_df = pd.DataFrame(df_asian_classics,columns=column_names)


# In[285]:


clean_asian_classics_df=new_asian_classics_df.drop(columns=['0','Dimensions'])


# In[286]:


clean_asian_classics_df.head()


# In[287]:


html_chars = ["<tr>","\n","</th>","<th>","<td>","</td>",
              "</tr>",'\t']
for char in html_chars:
    clean_asian_classics_df['ISBN-10'] = clean_asian_classics_df['ISBN-10'].str.replace(char, ' ')
    clean_asian_classics_df['ISBN-13'] = clean_asian_classics_df['ISBN-13'].str.replace(char, ' ')
    clean_asian_classics_df['Publisher'] = clean_asian_classics_df['Publisher'].str.replace(char, ' ')
    clean_asian_classics_df['Publish Date'] = clean_asian_classics_df['Publish Date'].str.replace(char, ' ')
   
    


# In[288]:


pd.set_option("max_colwidth", 1000)
clean_asian_classics_df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[391]:


greek_roman_clean_for_combine_df = pd.read_csv('greek-roman-clean.csv')


# In[392]:


greek_roman_clean_for_combine_df


# In[402]:


greek_roman_clean_for_combine_df['ISBN-10'] = greek_roman_clean_for_combine_df['ISBN-10'].map(lambda x: x.lstrip('ISBN-10: '))

greek_roman_clean_for_combine_df


# In[403]:


greek_roman_clean_for_combine_df.dtypes


# In[382]:





# In[ ]:





# In[404]:


greek_roman_clean_for_combine_df


# In[ ]:





# In[ ]:





# In[346]:


#https://stackoverflow.com/questions/18039057/python-pandas-error-tokenizing-data

books_df = pd.read_csv('Data/books.csv',error_bad_lines=False)


# In[347]:


books_df.head()


# In[ ]:





# In[352]:


#change column names
books_columns_df=books_df.rename(columns={"isbn": "ISBN-10", "isbn13": "ISBN-13"}) 


# In[397]:


books_columns_df.dtypes


# In[405]:


books_columns_df['ISBN-10'] = books_columns_df['ISBN-10'].map(lambda x: x.lstrip('0'))


# In[406]:


books_columns_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[421]:


merged_df = books_columns_df.merge(greek_roman_clean_for_combine_df,on='ISBN-10',how='outer')


# In[425]:


merged_df.tail()


# In[423]:


merged_drop_nan_df=merged_df.dropna()


# In[424]:


merged_drop_nan_df


# In[427]:


data1 = books_df.to_dict(orient = 'records')
data1


# In[428]:


data2 = greek_roman_clean_for_combine_df.to_dict(orient = 'records')
data2


# In[431]:


#books_df
#greek_roman_clean_for_combine_df
import pymongo
import pandas as pd 
import json

connection_string = "mongodb://localhost:27017"

client = pymongo.MongoClient(connection_string)

db = client["Project2"]
db.Books.insert_many(data1)
db.Greek_Roman.insert_many(data2)

print("ETL Complete")


# In[ ]:





# In[ ]:




