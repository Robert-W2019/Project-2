<b>Python Scraping of Book Information</b>


```python
!pip install bs4
```

    Collecting bs4
      Downloading bs4-0.0.1.tar.gz (1.1 kB)
    Requirement already satisfied: beautifulsoup4 in c:\users\robertw\anaconda3\lib\site-packages (from bs4) (4.9.3)
    Requirement already satisfied: soupsieve>1.2 in c:\users\robertw\anaconda3\lib\site-packages (from beautifulsoup4->bs4) (2.2.1)
    Building wheels for collected packages: bs4
      Building wheel for bs4 (setup.py): started
      Building wheel for bs4 (setup.py): finished with status 'done'
      Created wheel for bs4: filename=bs4-0.0.1-py3-none-any.whl size=1273 sha256=733392a582f6458ecd932fb22dcb33a21064a3672652d14a6d66b067841f54e5
      Stored in directory: c:\users\robertw\appdata\local\pip\cache\wheels\75\78\21\68b124549c9bdc94f822c02fb9aa3578a669843f9767776bca
    Successfully built bs4
    Installing collected packages: bs4
    Successfully installed bs4-0.0.1
    


```python
!pip install splinter
```

    Collecting splinter
      Downloading splinter-0.15.0-py3-none-any.whl (37 kB)
    Requirement already satisfied: six in c:\users\robertw\anaconda3\lib\site-packages (from splinter) (1.15.0)
    Collecting selenium>=3.141.0
      Downloading selenium-3.141.0-py2.py3-none-any.whl (904 kB)
    Requirement already satisfied: urllib3 in c:\users\robertw\anaconda3\lib\site-packages (from selenium>=3.141.0->splinter) (1.26.4)
    Installing collected packages: selenium, splinter
    Successfully installed selenium-3.141.0 splinter-0.15.0
    


```python
!pip install webdriver_manager
```

    Collecting webdriver_manager
      Downloading webdriver_manager-3.4.2-py2.py3-none-any.whl (16 kB)
    Collecting configparser
      Downloading configparser-5.0.2-py3-none-any.whl (19 kB)
    Requirement already satisfied: requests in c:\users\robertw\anaconda3\lib\site-packages (from webdriver_manager) (2.25.1)
    Collecting crayons
      Downloading crayons-0.4.0-py2.py3-none-any.whl (4.6 kB)
    Requirement already satisfied: colorama in c:\users\robertw\anaconda3\lib\site-packages (from crayons->webdriver_manager) (0.4.4)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\robertw\anaconda3\lib\site-packages (from requests->webdriver_manager) (1.26.4)
    Requirement already satisfied: chardet<5,>=3.0.2 in c:\users\robertw\anaconda3\lib\site-packages (from requests->webdriver_manager) (4.0.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\robertw\anaconda3\lib\site-packages (from requests->webdriver_manager) (2020.12.5)
    Requirement already satisfied: idna<3,>=2.5 in c:\users\robertw\anaconda3\lib\site-packages (from requests->webdriver_manager) (2.10)
    Installing collected packages: crayons, configparser, webdriver-manager
    Successfully installed configparser-5.0.2 crayons-0.4.0 webdriver-manager-3.4.2
    


```python
# Setup splinter
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time 
import pandas as pd
import requests
```


```python

```


```python
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
   
```

    
    
    ====== WebDriver manager ======
    Current google-chrome version is 93.0.4577
    Get LATEST driver version for 93.0.4577
    Driver [C:\Users\RobertW\.wdm\drivers\chromedriver\win32\93.0.4577.63\chromedriver.exe] found in cache
    

    ----------
    A Light in the Attic
    ----------
    Tipping the Velvet
    ----------
    Soumission
    ----------
    Sharp Objects
    ----------
    Sapiens: A Brief History of Humankind
    ----------
    The Requiem Red
    ----------
    The Dirty Little Secrets of Getting Your Dream Job
    ----------
    The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull
    ----------
    The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics
    ----------
    The Black Maria
    ----------
    Starving Hearts (Triangular Trade Trilogy, #1)
    ----------
    Shakespeare's Sonnets
    ----------
    Set Me Free
    ----------
    Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)
    ----------
    Rip it Up and Start Again
    ----------
    Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991
    ----------
    Olio
    ----------
    Mesaerion: The Best Science Fiction Stories 1800-1849
    ----------
    Libertarianism for Beginners
    ----------
    It's Only the Himalayas
    Scraping Complete
    ----------
    Libertarianism for Beginners
    ----------
    Mesaerion: The Best Science Fiction Stories 1800-1849
    ----------
    Olio
    ----------
    Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991
    ----------
    Rip it Up and Start Again
    ----------
    Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    Scraping Complete
    


```python
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
   

```


```python
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
        
    
```

    
    
    ====== WebDriver manager ======
    Current google-chrome version is 93.0.4577
    Get LATEST driver version for 93.0.4577
    Get LATEST driver version for 93.0.4577
    Trying to download new driver from https://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_win32.zip
    Driver has been saved in cache [C:\Users\RobertW\.wdm\drivers\chromedriver\win32\93.0.4577.63]
    

    https://books.toscrape.com/index.html
    ----------
    A Light in the Attic
    ----------
    Tipping the Velvet
    ----------
    Soumission
    ----------
    Sharp Objects
    ----------
    Sapiens: A Brief History of Humankind
    ----------
    The Requiem Red
    ----------
    The Dirty Little Secrets of Getting Your Dream Job
    ----------
    The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull
    ----------
    The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics
    ----------
    The Black Maria
    ----------
    Starving Hearts (Triangular Trade Trilogy, #1)
    ----------
    Shakespeare's Sonnets
    ----------
    Set Me Free
    ----------
    Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)
    ----------
    Rip it Up and Start Again
    ----------
    Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991
    ----------
    Olio
    ----------
    Mesaerion: The Best Science Fiction Stories 1800-1849
    ----------
    Libertarianism for Beginners
    ----------
    It's Only the Himalayas
    https://books.toscrape.com/catalogue/page-2.html
    ----------
    In Her Wake
    ----------
    How Music Works
    ----------
    Foolproof Preserving: A Guide to Small Batch Jams, Jellies, Pickles, Condiments, and More: A Foolproof Guide to Making Small Batch Jams, Jellies, Pickles, Condiments, and More
    ----------
    Chase Me (Paris Nights #2)
    ----------
    Black Dust
    ----------
    Birdsong: A Story in Pictures
    ----------
    America's Cradle of Quarterbacks: Western Pennsylvania's Football Factory from Johnny Unitas to Joe Montana
    ----------
    Aladdin and His Wonderful Lamp
    ----------
    Worlds Elsewhere: Journeys Around Shakespeare???s Globe
    ----------
    Wall and Piece
    ----------
    The Four Agreements: A Practical Guide to Personal Freedom
    ----------
    The Five Love Languages: How to Express Heartfelt Commitment to Your Mate
    ----------
    The Elephant Tree
    ----------
    The Bear and the Piano
    ----------
    Sophie's World
    ----------
    Penny Maybe
    ----------
    Maude (1883-1993):She Grew Up with the country
    ----------
    In a Dark, Dark Wood
    ----------
    Behind Closed Doors
    ----------
    You can't bury them all: Poems
    


```python
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
```

    
    
    ====== WebDriver manager ======
    Current google-chrome version is 93.0.4577
    Get LATEST driver version for 93.0.4577
    Driver [C:\Users\RobertW\.wdm\drivers\chromedriver\win32\93.0.4577.63\chromedriver.exe] found in cache
    

    https://books.toscrape.com/index.html
    ----------
    A Light in the Attic
                       0                        1
    0                UPC         a897fe39b1053632
    1       Product Type                    Books
    2  Price (excl. tax)                   ??51.77
    3  Price (incl. tax)                   ??51.77
    4                Tax                    ??0.00
    5       Availability  In stock (22 available)
    6  Number of reviews                        0
    ----------
    Tipping the Velvet
                       0                        1
    0                UPC         90fa61229261140a
    1       Product Type                    Books
    2  Price (excl. tax)                   ??53.74
    3  Price (incl. tax)                   ??53.74
    4                Tax                    ??0.00
    5       Availability  In stock (20 available)
    6  Number of reviews                        0
    ----------
    Soumission
                       0                        1
    0                UPC         6957f44c3847a760
    1       Product Type                    Books
    2  Price (excl. tax)                   ??50.10
    3  Price (incl. tax)                   ??50.10
    4                Tax                    ??0.00
    5       Availability  In stock (20 available)
    6  Number of reviews                        0
    ----------
    Sharp Objects
                       0                        1
    0                UPC         e00eb4fd7b871a48
    1       Product Type                    Books
    2  Price (excl. tax)                   ??47.82
    3  Price (incl. tax)                   ??47.82
    4                Tax                    ??0.00
    5       Availability  In stock (20 available)
    6  Number of reviews                        0
    ----------
    Sapiens: A Brief History of Humankind
                       0                        1
    0                UPC         4165285e1663650f
    1       Product Type                    Books
    2  Price (excl. tax)                   ??54.23
    3  Price (incl. tax)                   ??54.23
    4                Tax                    ??0.00
    5       Availability  In stock (20 available)
    6  Number of reviews                        0
    ----------
    The Requiem Red
                       0                        1
    0                UPC         f77dbf2323deb740
    1       Product Type                    Books
    2  Price (excl. tax)                   ??22.65
    3  Price (incl. tax)                   ??22.65
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    The Dirty Little Secrets of Getting Your Dream Job
                       0                        1
    0                UPC         2597b5a345f45e1b
    1       Product Type                    Books
    2  Price (excl. tax)                   ??33.34
    3  Price (incl. tax)                   ??33.34
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull
                       0                        1
    0                UPC         e72a5dfc7e9267b2
    1       Product Type                    Books
    2  Price (excl. tax)                   ??17.93
    3  Price (incl. tax)                   ??17.93
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics
                       0                        1
    0                UPC         e10e1e165dc8be4a
    1       Product Type                    Books
    2  Price (excl. tax)                   ??22.60
    3  Price (incl. tax)                   ??22.60
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    The Black Maria
                       0                        1
    0                UPC         1dfe412b8ac00530
    1       Product Type                    Books
    2  Price (excl. tax)                   ??52.15
    3  Price (incl. tax)                   ??52.15
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Starving Hearts (Triangular Trade Trilogy, #1)
                       0                        1
    0                UPC         0312262ecafa5a40
    1       Product Type                    Books
    2  Price (excl. tax)                   ??13.99
    3  Price (incl. tax)                   ??13.99
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Shakespeare's Sonnets
                       0                        1
    0                UPC         30a7f60cd76ca58c
    1       Product Type                    Books
    2  Price (excl. tax)                   ??20.66
    3  Price (incl. tax)                   ??20.66
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Set Me Free
                       0                        1
    0                UPC         ce6396b0f23f6ecc
    1       Product Type                    Books
    2  Price (excl. tax)                   ??17.46
    3  Price (incl. tax)                   ??17.46
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)
                       0                        1
    0                UPC         3b1c02bac2a429e6
    1       Product Type                    Books
    2  Price (excl. tax)                   ??52.29
    3  Price (incl. tax)                   ??52.29
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Rip it Up and Start Again
                       0                        1
    0                UPC         a34ba96d4081e6a4
    1       Product Type                    Books
    2  Price (excl. tax)                   ??35.02
    3  Price (incl. tax)                   ??35.02
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991
                       0                        1
    0                UPC         deda3e61b9514b83
    1       Product Type                    Books
    2  Price (excl. tax)                   ??57.25
    3  Price (incl. tax)                   ??57.25
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Olio
                       0                        1
    0                UPC         feb7cc7701ecf901
    1       Product Type                    Books
    2  Price (excl. tax)                   ??23.88
    3  Price (incl. tax)                   ??23.88
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Mesaerion: The Best Science Fiction Stories 1800-1849
                       0                        1
    0                UPC         e30f54cea9b38190
    1       Product Type                    Books
    2  Price (excl. tax)                   ??37.59
    3  Price (incl. tax)                   ??37.59
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Libertarianism for Beginners
                       0                        1
    0                UPC         a18a4f574854aced
    1       Product Type                    Books
    2  Price (excl. tax)                   ??51.33
    3  Price (incl. tax)                   ??51.33
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    It's Only the Himalayas
                       0                        1
    0                UPC         a22124811bfa8350
    1       Product Type                    Books
    2  Price (excl. tax)                   ??45.17
    3  Price (incl. tax)                   ??45.17
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    


```python
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
```

    
    
    ====== WebDriver manager ======
    Current google-chrome version is 93.0.4577
    Get LATEST driver version for 93.0.4577
    Driver [C:\Users\RobertW\.wdm\drivers\chromedriver\win32\93.0.4577.63\chromedriver.exe] found in cache
    

    https://books.toscrape.com/index.html
    ----------
    A Light in the Attic
                       0                        1
    0                UPC         a897fe39b1053632
    1       Product Type                    Books
    2  Price (excl. tax)                   ??51.77
    3  Price (incl. tax)                   ??51.77
    4                Tax                    ??0.00
    5       Availability  In stock (22 available)
    6  Number of reviews                        0
    ----------
    Tipping the Velvet
                       0                        1
    0                UPC         90fa61229261140a
    1       Product Type                    Books
    2  Price (excl. tax)                   ??53.74
    3  Price (incl. tax)                   ??53.74
    4                Tax                    ??0.00
    5       Availability  In stock (20 available)
    6  Number of reviews                        0
    ----------
    Soumission
                       0                        1
    0                UPC         6957f44c3847a760
    1       Product Type                    Books
    2  Price (excl. tax)                   ??50.10
    3  Price (incl. tax)                   ??50.10
    4                Tax                    ??0.00
    5       Availability  In stock (20 available)
    6  Number of reviews                        0
    ----------
    Sharp Objects
                       0                        1
    0                UPC         e00eb4fd7b871a48
    1       Product Type                    Books
    2  Price (excl. tax)                   ??47.82
    3  Price (incl. tax)                   ??47.82
    4                Tax                    ??0.00
    5       Availability  In stock (20 available)
    6  Number of reviews                        0
    ----------
    Sapiens: A Brief History of Humankind
                       0                        1
    0                UPC         4165285e1663650f
    1       Product Type                    Books
    2  Price (excl. tax)                   ??54.23
    3  Price (incl. tax)                   ??54.23
    4                Tax                    ??0.00
    5       Availability  In stock (20 available)
    6  Number of reviews                        0
    ----------
    The Requiem Red
                       0                        1
    0                UPC         f77dbf2323deb740
    1       Product Type                    Books
    2  Price (excl. tax)                   ??22.65
    3  Price (incl. tax)                   ??22.65
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    The Dirty Little Secrets of Getting Your Dream Job
                       0                        1
    0                UPC         2597b5a345f45e1b
    1       Product Type                    Books
    2  Price (excl. tax)                   ??33.34
    3  Price (incl. tax)                   ??33.34
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull
                       0                        1
    0                UPC         e72a5dfc7e9267b2
    1       Product Type                    Books
    2  Price (excl. tax)                   ??17.93
    3  Price (incl. tax)                   ??17.93
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics
                       0                        1
    0                UPC         e10e1e165dc8be4a
    1       Product Type                    Books
    2  Price (excl. tax)                   ??22.60
    3  Price (incl. tax)                   ??22.60
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    The Black Maria
                       0                        1
    0                UPC         1dfe412b8ac00530
    1       Product Type                    Books
    2  Price (excl. tax)                   ??52.15
    3  Price (incl. tax)                   ??52.15
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Starving Hearts (Triangular Trade Trilogy, #1)
                       0                        1
    0                UPC         0312262ecafa5a40
    1       Product Type                    Books
    2  Price (excl. tax)                   ??13.99
    3  Price (incl. tax)                   ??13.99
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Shakespeare's Sonnets
                       0                        1
    0                UPC         30a7f60cd76ca58c
    1       Product Type                    Books
    2  Price (excl. tax)                   ??20.66
    3  Price (incl. tax)                   ??20.66
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Set Me Free
                       0                        1
    0                UPC         ce6396b0f23f6ecc
    1       Product Type                    Books
    2  Price (excl. tax)                   ??17.46
    3  Price (incl. tax)                   ??17.46
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)
                       0                        1
    0                UPC         3b1c02bac2a429e6
    1       Product Type                    Books
    2  Price (excl. tax)                   ??52.29
    3  Price (incl. tax)                   ??52.29
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Rip it Up and Start Again
                       0                        1
    0                UPC         a34ba96d4081e6a4
    1       Product Type                    Books
    2  Price (excl. tax)                   ??35.02
    3  Price (incl. tax)                   ??35.02
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991
                       0                        1
    0                UPC         deda3e61b9514b83
    1       Product Type                    Books
    2  Price (excl. tax)                   ??57.25
    3  Price (incl. tax)                   ??57.25
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Olio
                       0                        1
    0                UPC         feb7cc7701ecf901
    1       Product Type                    Books
    2  Price (excl. tax)                   ??23.88
    3  Price (incl. tax)                   ??23.88
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Mesaerion: The Best Science Fiction Stories 1800-1849
                       0                        1
    0                UPC         e30f54cea9b38190
    1       Product Type                    Books
    2  Price (excl. tax)                   ??37.59
    3  Price (incl. tax)                   ??37.59
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    Libertarianism for Beginners
                       0                        1
    0                UPC         a18a4f574854aced
    1       Product Type                    Books
    2  Price (excl. tax)                   ??51.33
    3  Price (incl. tax)                   ??51.33
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    ----------
    It's Only the Himalayas
                       0                        1
    0                UPC         a22124811bfa8350
    1       Product Type                    Books
    2  Price (excl. tax)                   ??45.17
    3  Price (incl. tax)                   ??45.17
    4                Tax                    ??0.00
    5       Availability  In stock (19 available)
    6  Number of reviews                        0
    


```python

```




    RangeIndex(start=0, stop=15, step=1)




```python
df = pd.DataFrame(table_on_page)
df.to_csv('books2scrape.csv')
```


```python
df_to_clean=pd.read_csv('books2scrape.csv')
```


```python
df_columns_cleaned = df_to_clean.drop(columns=['Unnamed: 0','0','2','4','6','8','10','12','14'])
```


```python
df_columns_cleaned.columns
```




    Index(['1', '3', '5', '7', '9', '11', '13'], dtype='object')




```python
df_columns_cleaned.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>3</th>
      <th>5</th>
      <th>7</th>
      <th>9</th>
      <th>11</th>
      <th>13</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>&lt;tr&gt;\n&lt;th&gt;UPC&lt;/th&gt;&lt;td&gt;a897fe39b1053632&lt;/td&gt;\n&lt;...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Product Type&lt;/th&gt;&lt;td&gt;Books&lt;/td&gt;\n&lt;/tr&gt;</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Price (excl. tax)&lt;/th&gt;&lt;td&gt;??51.77&lt;/td...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Price (incl. tax)&lt;/th&gt;&lt;td&gt;??51.77&lt;/td...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Tax&lt;/th&gt;&lt;td&gt;??0.00&lt;/td&gt;\n&lt;/tr&gt;</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Availability&lt;/th&gt;\n&lt;td&gt;In stock (22 ...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Number of reviews&lt;/th&gt;\n&lt;td&gt;0&lt;/td&gt;\n...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>&lt;tr&gt;\n&lt;th&gt;UPC&lt;/th&gt;&lt;td&gt;90fa61229261140a&lt;/td&gt;\n&lt;...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Product Type&lt;/th&gt;&lt;td&gt;Books&lt;/td&gt;\n&lt;/tr&gt;</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Price (excl. tax)&lt;/th&gt;&lt;td&gt;??53.74&lt;/td...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Price (incl. tax)&lt;/th&gt;&lt;td&gt;??53.74&lt;/td...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Tax&lt;/th&gt;&lt;td&gt;??0.00&lt;/td&gt;\n&lt;/tr&gt;</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Availability&lt;/th&gt;\n&lt;td&gt;In stock (20 ...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Number of reviews&lt;/th&gt;\n&lt;td&gt;0&lt;/td&gt;\n...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>&lt;tr&gt;\n&lt;th&gt;UPC&lt;/th&gt;&lt;td&gt;6957f44c3847a760&lt;/td&gt;\n&lt;...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Product Type&lt;/th&gt;&lt;td&gt;Books&lt;/td&gt;\n&lt;/tr&gt;</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Price (excl. tax)&lt;/th&gt;&lt;td&gt;??50.10&lt;/td...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Price (incl. tax)&lt;/th&gt;&lt;td&gt;??50.10&lt;/td...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Tax&lt;/th&gt;&lt;td&gt;??0.00&lt;/td&gt;\n&lt;/tr&gt;</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Availability&lt;/th&gt;\n&lt;td&gt;In stock (20 ...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Number of reviews&lt;/th&gt;\n&lt;td&gt;0&lt;/td&gt;\n...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>&lt;tr&gt;\n&lt;th&gt;UPC&lt;/th&gt;&lt;td&gt;e00eb4fd7b871a48&lt;/td&gt;\n&lt;...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Product Type&lt;/th&gt;&lt;td&gt;Books&lt;/td&gt;\n&lt;/tr&gt;</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Price (excl. tax)&lt;/th&gt;&lt;td&gt;??47.82&lt;/td...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Price (incl. tax)&lt;/th&gt;&lt;td&gt;??47.82&lt;/td...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Tax&lt;/th&gt;&lt;td&gt;??0.00&lt;/td&gt;\n&lt;/tr&gt;</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Availability&lt;/th&gt;\n&lt;td&gt;In stock (20 ...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Number of reviews&lt;/th&gt;\n&lt;td&gt;0&lt;/td&gt;\n...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>&lt;tr&gt;\n&lt;th&gt;UPC&lt;/th&gt;&lt;td&gt;4165285e1663650f&lt;/td&gt;\n&lt;...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Product Type&lt;/th&gt;&lt;td&gt;Books&lt;/td&gt;\n&lt;/tr&gt;</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Price (excl. tax)&lt;/th&gt;&lt;td&gt;??54.23&lt;/td...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Price (incl. tax)&lt;/th&gt;&lt;td&gt;??54.23&lt;/td...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Tax&lt;/th&gt;&lt;td&gt;??0.00&lt;/td&gt;\n&lt;/tr&gt;</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Availability&lt;/th&gt;\n&lt;td&gt;In stock (20 ...</td>
      <td>&lt;tr&gt;\n&lt;th&gt;Number of reviews&lt;/th&gt;\n&lt;td&gt;0&lt;/td&gt;\n...</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
df_columns_cleaned
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>3</th>
      <th>5</th>
      <th>7</th>
      <th>9</th>
      <th>11</th>
      <th>13</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>UPC  a897fe39b1053632</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??51.77</td>
      <td>Price (incl. tax)  ??51.77</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (22 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>UPC  90fa61229261140a</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??53.74</td>
      <td>Price (incl. tax)  ??53.74</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (20 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>UPC  6957f44c3847a760</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??50.10</td>
      <td>Price (incl. tax)  ??50.10</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (20 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>UPC  e00eb4fd7b871a48</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??47.82</td>
      <td>Price (incl. tax)  ??47.82</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (20 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>UPC  4165285e1663650f</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??54.23</td>
      <td>Price (incl. tax)  ??54.23</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (20 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>UPC  f77dbf2323deb740</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??22.65</td>
      <td>Price (incl. tax)  ??22.65</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>UPC  2597b5a345f45e1b</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??33.34</td>
      <td>Price (incl. tax)  ??33.34</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>UPC  e72a5dfc7e9267b2</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??17.93</td>
      <td>Price (incl. tax)  ??17.93</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>UPC  e10e1e165dc8be4a</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??22.60</td>
      <td>Price (incl. tax)  ??22.60</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>UPC  1dfe412b8ac00530</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??52.15</td>
      <td>Price (incl. tax)  ??52.15</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>UPC  0312262ecafa5a40</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??13.99</td>
      <td>Price (incl. tax)  ??13.99</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>UPC  30a7f60cd76ca58c</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??20.66</td>
      <td>Price (incl. tax)  ??20.66</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>UPC  ce6396b0f23f6ecc</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??17.46</td>
      <td>Price (incl. tax)  ??17.46</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>UPC  3b1c02bac2a429e6</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??52.29</td>
      <td>Price (incl. tax)  ??52.29</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>UPC  a34ba96d4081e6a4</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??35.02</td>
      <td>Price (incl. tax)  ??35.02</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>UPC  deda3e61b9514b83</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??57.25</td>
      <td>Price (incl. tax)  ??57.25</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>UPC  feb7cc7701ecf901</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??23.88</td>
      <td>Price (incl. tax)  ??23.88</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>UPC  e30f54cea9b38190</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??37.59</td>
      <td>Price (incl. tax)  ??37.59</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>UPC  a18a4f574854aced</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??51.33</td>
      <td>Price (incl. tax)  ??51.33</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>UPC  a22124811bfa8350</td>
      <td>Product Type  Books</td>
      <td>Price (excl. tax)  ??45.17</td>
      <td>Price (incl. tax)  ??45.17</td>
      <td>Tax  ??0.00</td>
      <td>Availability   In stock (19 available)</td>
      <td>Number of reviews   0</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```


```python
#https://stackoverflow.com/questions/31064981/python3-error-initial-value-must-be-str-or-none-with-stringio
import io

```


```python
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
        
   
```

    
    
    ====== WebDriver manager ======
    Current google-chrome version is 93.0.4577
    Get LATEST driver version for 93.0.4577
    Driver [C:\Users\RobertW\.wdm\drivers\chromedriver\win32\93.0.4577.63\chromedriver.exe] found in cache
    

    https://citylights.com/greek-roman/
    ----------
    https://citylights.com/greek-roman/ancient-rhetoric-aristotle-to-philostr/
    
    	                          ISBN-10: 0141392649
    	                          ISBN-13: 9780141392646
    	                          Publisher: Penguin Group 
    							                          Publish Date: 04/17/2018 
    							                          Dimensions: 7.70" L, 5.10" W, 0.80" H	                    
    ----------
    https://citylights.com/greek-roman/catilines-war-the-jugurthine-war-hist/
    
    	                          ISBN-10: 0140449485
    	                          ISBN-13: 9780140449488
    	                          Publisher: Penguin Group 
    							                          Publish Date: 02/26/2008 
    							                          Dimensions: 7.76" L, 5.22" W, 0.61" H	                    
    ----------
    https://citylights.com/greek-roman/ht-be-a-stoic/
    
    	                          ISBN-10: 0241475260
    	                          ISBN-13: 9780241475263
    	                          Publisher: Penguin Books 
    							                          Publish Date: 06/08/2021 
    							                          Dimensions: 7.00" L, 4.30" W, 0.40" H	                    
    ----------
    https://citylights.com/greek-roman/16-satires-tr-peter-green/
    
    	                          ISBN-10: 0140447040
    	                          ISBN-13: 9780140447040
    	                          Publisher: Penguin Group 
    							                          Publish Date: 02/01/1999 
    							                          Dimensions: 7.90" L, 5.06" W, 0.78" H	                    
    ----------
    https://citylights.com/greek-roman/aeneid/
    
    	                          ISBN-10: 1984854127
    	                          ISBN-13: 9781984854124
    	                          Publisher: Modern Library 
    							                          Publish Date: 09/14/2021 
    							                          Dimensions: 8.00" L, 5.19" W, 0.94" H	                    
    ----------
    https://citylights.com/greek-roman/art-of-happiness-tr-george-k-strodach/
    
    	                          ISBN-10: 0143107216
    	                          ISBN-13: 9780143107217
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/24/2012 
    							                          Dimensions: 7.70" L, 5.16" W, 0.72" H	                    
    ----------
    https://citylights.com/greek-roman/campaigns-of-alexander/
    
    	                          ISBN-10: 0140442537
    	                          ISBN-13: 9780140442533
    	                          Publisher: Penguin Group 
    							                          Publish Date: 10/28/1976 
    							                          Dimensions: 7.60" L, 5.00" W, 1.00" H	                    
    ----------
    https://citylights.com/greek-roman/hist-of-alexander-tr-john-yardley/
    
    	                          ISBN-10: 0140444122
    	                          ISBN-13: 9780140444124
    	                          Publisher: Penguin Group 
    							                          Publish Date: 11/06/1984 
    							                          Dimensions: 7.97" L, 4.89" W, 0.68" H	                    
    ----------
    https://citylights.com/greek-roman/homeric-hymns/
    
    	                          ISBN-10: 0140437827
    	                          ISBN-13: 9780140437829
    	                          Publisher: Penguin Group 
    							                          Publish Date: 10/28/2003 
    							                          Dimensions: 7.78" L, 5.08" W, 0.56" H	                    
    ----------
    https://citylights.com/greek-roman/later-roman-empire-ad-354-to-378/
    
    	                          ISBN-10: 0140444068
    	                          ISBN-13: 9780140444063
    	                          Publisher: Penguin Group 
    							                          Publish Date: 08/05/1986 
    							                          Dimensions: 7.88" L, 5.06" W, 0.90" H	                    
    ----------
    https://citylights.com/greek-roman/metaphysics/
    
    	                          ISBN-10: 0140446192
    	                          ISBN-13: 9780140446197
    	                          Publisher: Penguin Group 
    							                          Publish Date: 06/01/1999 
    							                          Dimensions: 7.82" L, 5.14" W, 0.91" H	                    
    ----------
    https://citylights.com/greek-roman/nature-of-things-tr-ae-stallings-2/
    
    	                          ISBN-10: 0140447962
    	                          ISBN-13: 9780140447965
    	                          Publisher: Penguin Group 
    							                          Publish Date: 01/01/2008 
    							                          Dimensions: 7.70" L, 5.00" W, 0.90" H	                    
    ----------
    https://citylights.com/greek-roman/oresteian-trilogy-vellacott-tr/
    
    	                          ISBN-10: 0140440674
    	                          ISBN-13: 9780140440676
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/30/1956 
    							                          Dimensions: 7.75" L, 5.09" W, 0.50" H	                    
    ----------
    https://citylights.com/greek-roman/roman-hist-the-reign-of-augustus/
    
    	                          ISBN-10: 0140444483
    	                          ISBN-13: 9780140444483
    	                          Publisher: Penguin Group 
    							                          Publish Date: 07/07/1987 
    							                          Dimensions: 7.77" L, 5.08" W, 0.88" H	                    
    ----------
    https://citylights.com/greek-roman/satyricon-senecas-apocolocyntosis/
    
    	                          ISBN-10: 0140444890
    	                          ISBN-13: 9780140444896
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/02/1986 
    							                          Dimensions: 7.78" L, 5.24" W, 0.63" H	                    
    ----------
    https://citylights.com/greek-roman/1-swallow-does-not-make-a-summer/
    
    	                          ISBN-10: 0241472865
    	                          ISBN-13: 9780241472866
    	                          Publisher: Penguin Books 
    							                          Publish Date: 06/08/2021 
    							                          Dimensions: 7.00" L, 4.30" W, 0.40" H	                    
    ----------
    https://citylights.com/greek-roman/alexander-the-great-his-life-his-mys/
    
    	                          ISBN-10: 0425286533
    	                          ISBN-13: 9780425286531
    	                          Publisher: Random House Trade 
    							                          Publish Date: 06/08/2021 
    							                          Dimensions: 7.90" L, 5.10" W, 1.10" H	                    
    ----------
    https://citylights.com/staff-picks-archive/bakkhai/
    
    	                          ISBN-10: 0811227103
    	                          ISBN-13: 9780811227100
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 12/12/2017 
    							                          Dimensions: 8.10" L, 5.40" W, 0.50" H	                    
    ----------
    https://citylights.com/greek-roman/chapmans-homer-the-odyssey/
    
    	                          ISBN-10: 0691048916
    	                          ISBN-13: 9780691048918
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 12/17/2000 
    							                          Dimensions: 9.20" L, 6.74" W, 1.06" H	                    
    ----------
    https://citylights.com/greek-roman/chapmans-homeric-hymns-other-homerica/
    
    	                          ISBN-10: 0691136769
    	                          ISBN-13: 9780691136769
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 06/01/2008 
    							                          Dimensions: 8.43" L, 6.54" W, 0.70" H	                    
    https://citylights.com/greek-roman/page/2/
    ----------
    https://citylights.com/greek-roman/ht-run-a-country/
    
    	                          ISBN-10: 0691156573
    	                          ISBN-13: 9780691156576
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 01/22/2013 
    							                          Dimensions: 7.41" L, 4.80" W, 0.65" H	                    
    ----------
    https://citylights.com/judaism/masada-from-jewish-revolt-to-modern-my/
    
    	                          ISBN-10: 0691216770
    	                          ISBN-13: 9780691216775
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 06/08/2021 
    							                          Dimensions: 7.90" L, 5.20" W, 1.00" H	                    
    ----------
    https://citylights.com/greek-roman/on-the-shortness-of-life-tr-cdn-costa/
    
    	                          ISBN-10: 0143036327
    	                          ISBN-13: 9780143036326
    	                          Publisher: Penguin Books 
    							                          Publish Date: 09/06/2005 
    							                          Dimensions: 7.08" L, 4.42" W, 0.32" H	                    
    ----------
    https://citylights.com/greek-roman/plutarchs-lives-v2-tr-john-dryden/
    
    	                          ISBN-10: 0375756779
    	                          ISBN-13: 9780375756771
    	                          Publisher: Modern Library 
    							                          Publish Date: 04/10/2001 
    							                          Dimensions: 8.00" L, 5.15" W, 1.15" H	                    
    ----------
    https://citylights.com/greek-roman/protagoras-meno-tr-adam-beresford/
    
    	                          ISBN-10: 0140449035
    	                          ISBN-13: 9780140449037
    	                          Publisher: Penguin Group 
    							                          Publish Date: 04/25/2006 
    							                          Dimensions: 7.76" L, 5.22" W, 0.51" H	                    
    ----------
    https://citylights.com/greek-roman/roman-triumph/
    
    	                          ISBN-10: 0674032187
    	                          ISBN-13: 9780674032187
    	                          Publisher: Belknap Press 
    							                          Publish Date: 05/01/2009 
    							                          Dimensions: 9.00" L, 6.10" W, 1.30" H	                    
    ----------
    https://citylights.com/greek-roman/aeneid-3/
    
    	                          ISBN-10: 0300240104
    	                          ISBN-13: 9780300240108
    	                          Publisher: Yale University Press 
    							                          Publish Date: 02/09/2021 
    							                          Dimensions: 8.40" L, 5.40" W, 1.10" H	                    
    ----------
    https://citylights.com/new-nonfiction-in-hardcover/stoic-wisdom-ancient-lessons-for-moder/
    
    	                          ISBN-10: 0197501834
    	                          ISBN-13: 9780197501832
    	                          Publisher: Oxford University Press, USA 
    							                          Publish Date: 06/01/2021 
    							                          Dimensions: 8.40" L, 5.80" W, 1.30" H	                    
    ----------
    https://citylights.com/poetry-criticism-biographies/classical-lit-criticism/
    
    	                          ISBN-10: 0140446516
    	                          ISBN-13: 9780140446517
    	                          Publisher: Penguin Group 
    							                          Publish Date: 05/01/2001 
    							                          Dimensions: 7.71" L, 5.04" W, 0.64" H	                    
    ----------
    https://citylights.com/greek-roman/cynicism/
    
    	                          ISBN-10: 0262537885
    	                          ISBN-13: 9780262537889
    	                          Publisher: MIT Press 
    							                          Publish Date: 05/05/2020 
    							                          Dimensions: 6.90" L, 5.00" W, 0.80" H	                    
    ----------
    https://citylights.com/christic/god-empire-jesus-against-rome/
    
    	                          ISBN-10: 0060858311
    	                          ISBN-13: 9780060858315
    	                          Publisher: HarperOne 
    							                          Publish Date: 02/26/2008 
    							                          Dimensions: 8.00" L, 5.30" W, 0.70" H	                    
    ----------
    https://citylights.com/europe/streams-of-gold-rivers-of-blood-rise/
    
    	                          ISBN-10: 0190053208
    	                          ISBN-13: 9780190053208
    	                          Publisher: Oxford University Press, USA 
    							                          Publish Date: 09/01/2019 
    							                          Dimensions: 9.20" L, 6.10" W, 1.20" H	                    
    ----------
    https://citylights.com/greek-roman/hiero-the-tyrant-other-treatises/
    
    	                          ISBN-10: 0140455256
    	                          ISBN-13: 9780140455250
    	                          Publisher: Penguin Group 
    							                          Publish Date: 09/01/2006 
    							                          Dimensions: 7.74" L, 5.08" W, 0.67" H	                    
    ----------
    https://citylights.com/greek-roman/conversations-of-socrates-tr-waterfield/
    
    	                          ISBN-10: 014044517X
    	                          ISBN-13: 9780140445176
    	                          Publisher: Penguin Group 
    							                          Publish Date: 07/03/1990 
    							                          Dimensions: 7.70" L, 5.00" W, 1.00" H	                    
    ----------
    https://citylights.com/greek-roman/hist-of-my-times-rev-ed-tr-rex-warner/
    
    	                          ISBN-10: 0140441751
    	                          ISBN-13: 9780140441758
    	                          Publisher: Penguin Group 
    							                          Publish Date: 05/31/1979 
    							                          Dimensions: 7.70" L, 5.20" W, 1.00" H	                    
    ----------
    https://citylights.com/greek-roman/mortal-republic-how-rome-fell-into-tyr/
    
    	                          ISBN-10: 1541646487
    	                          ISBN-13: 9781541646483
    	                          Publisher: Basic Books 
    							                          Publish Date: 08/25/2020 
    							                          Dimensions: 8.27" L, 5.51" W, 0.88" H	                    
    ----------
    https://citylights.com/greek-roman/homer-very-short-intro/
    
    	                          ISBN-10: 0199589941
    	                          ISBN-13: 9780199589944
    	                          Publisher: Oxford University Press, USA 
    							                          Publish Date: 05/01/2019 
    							                          Dimensions: 6.80" L, 4.30" W, 0.60" H	                    
    ----------
    https://citylights.com/greek-roman/aeneid-tr-robert-fagles/
    
    	                          ISBN-10: 0143105132
    	                          ISBN-13: 9780143105138
    	                          Publisher: Penguin Group 
    							                          Publish Date: 02/01/2008 
    							                          Dimensions: 8.40" L, 5.70" W, 1.30" H	                    
    ----------
    https://citylights.com/greek-roman/georgics/
    
    	                          ISBN-10: 0140455639
    	                          ISBN-13: 9780140455632
    	                          Publisher: Penguin Group 
    							                          Publish Date: 02/22/2011 
    							                          Dimensions: 7.60" L, 5.00" W, 0.60" H	                    
    ----------
    https://citylights.com/greek-roman/aeneid-2/
    
    	                          ISBN-10: 0143106295
    	                          ISBN-13: 9780143106296
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/28/2010 
    							                          Dimensions: 7.70" L, 5.10" W, 1.00" H	                    
    https://citylights.com/greek-roman/page/3/
    ----------
    https://citylights.com/greek-roman/myth-society-in-ancient-greece/
    
    	                          ISBN-10: 0942299175
    	                          ISBN-13: 9780942299175
    	                          Publisher: Zone Books 
    							                          Publish Date: 10/17/1990 
    							                          Dimensions: 8.90" L, 6.00" W, 0.90" H	                    
    ----------
    https://citylights.com/greek-roman/landmark-thucydides/
    
    	                          ISBN-10: 0684827905
    	                          ISBN-13: 9780684827902
    	                          Publisher: Free Press 
    							                          Publish Date: 09/10/1998 
    							                          Dimensions: 9.26" L, 7.34" W, 1.60" H	                    
    ----------
    https://citylights.com/greek-roman/hist-of-the-peloponnesian-war/
    
    	                          ISBN-10: 0140440399
    	                          ISBN-13: 9780140440393
    	                          Publisher: Penguin Group 
    							                          Publish Date: 09/30/1954 
    							                          Dimensions: 7.70" L, 5.00" W, 1.10" H	                    
    ----------
    https://citylights.com/new-nonfiction-in-hardcover/ht-think-about-war-ancient-guide/
    
    	                          ISBN-10: 0691190151
    	                          ISBN-13: 9780691190150
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 02/05/2019 
    							                          Dimensions: 7.50" L, 4.80" W, 1.30" H	                    
    ----------
    https://citylights.com/greek-roman/comedies-tr-bovie/
    
    	                          ISBN-10: 0801843545
    	                          ISBN-13: 9780801843549
    	                          Publisher: Johns Hopkins University Press 
    							                          Publish Date: 02/01/1992 
    							                          Dimensions: 9.04" L, 5.96" W, 0.92" H	                    
    ----------
    https://citylights.com/greek-roman/histories-tr-kenneth-wellesley/
    
    	                          ISBN-10: 0140449647
    	                          ISBN-13: 9780140449648
    	                          Publisher: Penguin Group 
    							                          Publish Date: 08/01/2009 
    							                          Dimensions: 7.74" L, 5.14" W, 0.93" H	                    
    ----------
    https://citylights.com/greek-roman/brutus-noble-conspirator/
    
    	                          ISBN-10: 0300246641
    	                          ISBN-13: 9780300246643
    	                          Publisher: Yale University Press 
    							                          Publish Date: 10/28/2019 
    							                          Dimensions: 8.90" L, 5.60" W, 1.00" H	                    
    ----------
    https://citylights.com/greek-roman/agricola-germania-tr-harold-mattingly/
    
    	                          ISBN-10: 014045540X
    	                          ISBN-13: 9780140455403
    	                          Publisher: Penguin Group 
    							                          Publish Date: 03/30/2010 
    							                          Dimensions: 7.60" L, 5.00" W, 0.50" H	                    
    ----------
    https://citylights.com/greek-roman/annals-tr-cynthia-damon/
    
    	                          ISBN-10: 0140455647
    	                          ISBN-13: 9780140455649
    	                          Publisher: Penguin Group 
    							                          Publish Date: 03/26/2013 
    							                          Dimensions: 7.80" L, 5.00" W, 1.10" H	                    
    ----------
    https://citylights.com/greek-roman/annals-of-imperial-rome-tr-michael-grant/
    
    	                          ISBN-10: 0140440607
    	                          ISBN-13: 9780140440607
    	                          Publisher: Penguin Group 
    							                          Publish Date: 06/30/1956 
    							                          Dimensions: 7.94" L, 5.04" W, 0.81" H	                    
    ----------
    https://citylights.com/greek-roman/annals/
    
    	                          ISBN-10: 0486452360
    	                          ISBN-13: 9780486452364
    	                          Publisher: Dover Publications 
    							                          Publish Date: 02/02/2007 
    							                          Dimensions: 8.36" L, 5.31" W, 0.82" H	                    
    ----------
    https://citylights.com/greek-roman/12-caesars/
    
    	                          ISBN-10: 0140455167
    	                          ISBN-13: 9780140455168
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/18/2007 
    							                          Dimensions: 7.80" L, 5.14" W, 0.78" H	                    
    ----------
    https://citylights.com/greek-roman/10-caesars-roman-emperors-from-august/
    
    	                          ISBN-10: 1451668848
    	                          ISBN-13: 9781451668841
    	                          Publisher: Simon & Schuster 
    							                          Publish Date: 03/03/2020 
    							                          Dimensions: 8.90" L, 6.10" W, 1.10" H	                    
    ----------
    https://citylights.com/greek-roman/story-of-greece-rome/
    
    	                          ISBN-10: 0300251645
    	                          ISBN-13: 9780300251647
    	                          Publisher: Yale University Press 
    							                          Publish Date: 03/17/2020 
    							                          Dimensions: 7.80" L, 5.10" W, 1.40" H	                    
    ----------
    https://citylights.com/greek-roman/3-theban-plays-antigoneoedipuscolonus/
    
    	                          ISBN-10: 0140444254
    	                          ISBN-13: 9780140444254
    	                          Publisher: Penguin Group 
    							                          Publish Date: 02/07/1984 
    							                          Dimensions: 7.76" L, 5.11" W, 0.77" H	                    
    ----------
    https://citylights.com/greek-roman/women-of-trachis/
    
    	                          ISBN-10: 0195070097
    	                          ISBN-13: 9780195070095
    	                          Publisher: Oxford University Press, USA 
    							                          Publish Date: 04/01/1991 
    							                          Dimensions: 8.50" L, 5.54" W, 0.30" H	                    
    ----------
    https://citylights.com/greek-roman/oedipus-at-kolonos-a-new-translation/
    
    	                          ISBN-10: 0062132105
    	                          ISBN-13: 9780062132109
    	                          Publisher: Harper Perennial 
    							                          Publish Date: 08/07/2012 
    							                          Dimensions: 7.90" L, 5.20" W, 0.50" H	                    
    ----------
    https://citylights.com/greek-roman/4-tragedies-octavia-tr-ef-watling/
    
    	                          ISBN-10: 0140441743
    	                          ISBN-13: 9780140441741
    	                          Publisher: Penguin Group 
    							                          Publish Date: 10/30/1966 
    							                          Dimensions: 7.77" L, 5.10" W, 0.60" H	                    
    ----------
    https://citylights.com/greek-roman/phaedra-other-plays-tr-r-scott-smith/
    
    	                          ISBN-10: 0140455515
    	                          ISBN-13: 9780140455519
    	                          Publisher: Penguin Group 
    							                          Publish Date: 10/25/2011 
    							                          Dimensions: 7.70" L, 5.00" W, 0.90" H	                    
    ----------
    https://citylights.com/greek-roman/dialogues-letters-tr-cdn-costa/
    
    	                          ISBN-10: 0140446796
    	                          ISBN-13: 9780140446791
    	                          Publisher: Penguin Group 
    							                          Publish Date: 11/01/1997 
    							                          Dimensions: 7.86" L, 5.08" W, 0.41" H	                    
    https://citylights.com/greek-roman/page/4/
    ----------
    https://citylights.com/greek-roman/letters-from-a-stoic-tr-robin-campbell/
    
    	                          ISBN-10: 0140442103
    	                          ISBN-13: 9780140442106
    	                          Publisher: Penguin Group 
    							                          Publish Date: 07/30/1969 
    							                          Dimensions: 7.77" L, 5.07" W, 0.64" H	                    
    ----------
    https://citylights.com/new-nonfiction-in-hardcover/ht-give-ancient-gt-giving/
    
    	                          ISBN-10: 069119209X
    	                          ISBN-13: 9780691192093
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 10/20/2020 
    							                          Dimensions: 6.90" L, 4.60" W, 1.10" H	                    
    ----------
    https://citylights.com/greek-roman/letters-from-a-stoic-epistulae-morales/
    
    	                          ISBN-10: 0141395850
    	                          ISBN-13: 9780141395852
    	                          Publisher: Penguin Group 
    							                          Publish Date: 04/28/2015 
    							                          Dimensions: 6.60" L, 4.40" W, 1.20" H	                    
    ----------
    https://citylights.com/greek-roman/pocket-stoic/
    
    	                          ISBN-10: 022668296X
    	                          ISBN-13: 9780226682969
    	                          Publisher: University of Chicago Press 
    							                          Publish Date: 10/06/2020 
    							                          Dimensions: 6.10" L, 4.50" W, 0.70" H	                    
    ----------
    https://citylights.com/greek-roman/1st-poets-lives-of-ancient-greek-poets/
    
    	                          ISBN-10: 0375725253
    	                          ISBN-13: 9780375725258
    	                          Publisher: Vintage 
    							                          Publish Date: 03/14/2006 
    							                          Dimensions: 8.00" L, 5.42" W, 0.97" H	                    
    ----------
    https://citylights.com/middle-eastern/poems-of-heaven-hell-from-ancient-meso/
    
    	                          ISBN-10: 0140442499
    	                          ISBN-13: 9780140442496
    	                          Publisher: Penguin Group 
    							                          Publish Date: 06/06/1989 
    							                          Dimensions: 7.76" L, 5.18" W, 0.45" H	                    
    ----------
    https://citylights.com/greek-roman/rise-of-music-in-the-ancient-world/
    
    	                          ISBN-10: 0486466612
    	                          ISBN-13: 9780486466613
    	                          Publisher: Dover Publications 
    							                          Publish Date: 07/24/2008 
    							                          Dimensions: 9.10" L, 6.00" W, 0.80" H	                    
    ----------
    https://citylights.com/greek-roman/plague-of-war-athens-sparta-the-st/
    
    	                          ISBN-10: 0190940883
    	                          ISBN-13: 9780190940881
    	                          Publisher: Oxford University Press, USA 
    							                          Publish Date: 05/01/2019 
    							                          Dimensions: 8.90" L, 5.70" W, 1.20" H	                    
    ----------
    https://citylights.com/greek-roman/poems-from-greek-antiquity/
    
    	                          ISBN-10: 1101908211
    	                          ISBN-13: 9781101908211
    	                          Publisher: Everyman's Library 
    							                          Publish Date: 11/10/2020 
    							                          Dimensions: 6.40" L, 4.40" W, 1.00" H	                    
    ----------
    https://citylights.com/greek-roman/secret-hist-tr-ga-williamson/
    
    	                          ISBN-10: 0140455280
    	                          ISBN-13: 9780140455281
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/18/2007 
    							                          Dimensions: 7.70" L, 6.47" W, 0.43" H	                    
    ----------
    https://citylights.com/middle-eastern/14-byzantine-rulers/
    
    	                          ISBN-10: 0140441697
    	                          ISBN-13: 9780140441697
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/20/1979 
    							                          Dimensions: 7.64" L, 5.54" W, 0.97" H	                    
    ----------
    https://citylights.com/greek-roman/rise-of-the-roman-empire/
    
    	                          ISBN-10: 0140443622
    	                          ISBN-13: 9780140443622
    	                          Publisher: Penguin Group 
    							                          Publish Date: 02/28/1980 
    							                          Dimensions: 7.84" L, 5.16" W, 1.05" H	                    
    ----------
    https://citylights.com/greek-roman/essays-plutarch-tr-robin-waterfield/
    
    	                          ISBN-10: 0140445641
    	                          ISBN-13: 9780140445640
    	                          Publisher: Penguin Group 
    							                          Publish Date: 04/06/1993 
    							                          Dimensions: 7.78" L, 5.12" W, 1.09" H	                    
    ----------
    https://citylights.com/greek-roman/fall-of-the-roman-republic-tr-rex-warner/
    
    	                          ISBN-10: 0140449345
    	                          ISBN-13: 9780140449341
    	                          Publisher: Penguin Group 
    							                          Publish Date: 04/25/2006 
    							                          Dimensions: 7.76" L, 5.18" W, 0.98" H	                    
    ----------
    https://citylights.com/greek-roman/rise-fall-of-athens-tr-scott-kilvert/
    
    	                          ISBN-10: 0140441026
    	                          ISBN-13: 9780140441024
    	                          Publisher: Penguin Group 
    							                          Publish Date: 09/30/1960 
    							                          Dimensions: 7.78" L, 5.14" W, 0.63" H	                    
    ----------
    https://citylights.com/greek-roman/on-sparta-tr-richard-j-a-talbert/
    
    	                          ISBN-10: 0140449434
    	                          ISBN-13: 9780140449433
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/27/2005 
    							                          Dimensions: 7.76" L, 5.18" W, 0.74" H	                    
    ----------
    https://citylights.com/greek-roman/makers-of-rome-9-lives/
    
    	                          ISBN-10: 0140441581
    	                          ISBN-13: 9780140441581
    	                          Publisher: Penguin Group 
    							                          Publish Date: 10/30/1965 
    							                          Dimensions: 7.79" L, 5.14" W, 0.70" H	                    
    ----------
    https://citylights.com/greek-roman/enneads-tr-stephen-mckenna/
    
    	                          ISBN-10: 014044520X
    	                          ISBN-13: 9780140445206
    	                          Publisher: Penguin Group 
    							                          Publish Date: 11/05/1991 
    							                          Dimensions: 7.79" L, 5.07" W, 1.23" H	                    
    ----------
    https://citylights.com/greek-roman/age-of-alexander-old-ed/
    
    	                          ISBN-10: 0140442863
    	                          ISBN-13: 9780140442861
    	                          Publisher: Penguin Group 
    							                          Publish Date: 09/30/1973 
    							                          Dimensions: 7.79" L, 4.98" W, 0.86" H	                    
    ----------
    https://citylights.com/greek-roman/natural-hist-a-sel-tr-john-healy/
    
    	                          ISBN-10: 0140444130
    	                          ISBN-13: 9780140444131
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/03/1991 
    							                          Dimensions: 7.72" L, 5.18" W, 1.11" H	                    
    https://citylights.com/greek-roman/page/5/
    ----------
    https://citylights.com/greek-roman/rope-other-plays/
    
    	                          ISBN-10: 0140441360
    	                          ISBN-13: 9780140441369
    	                          Publisher: Penguin Group 
    							                          Publish Date: 05/30/1964 
    							                          Dimensions: 7.76" L, 5.18" W, 0.72" H	                    
    ----------
    https://citylights.com/greek-roman/laws-tr-trevor-saunders/
    
    	                          ISBN-10: 0140449841
    	                          ISBN-13: 9780140449846
    	                          Publisher: Penguin Group 
    							                          Publish Date: 06/28/2005 
    							                          Dimensions: 7.84" L, 5.94" W, 1.07" H	                    
    ----------
    https://citylights.com/greek-roman/last-days-of-socrates-tr-chris-rowe/
    
    	                          ISBN-10: 0140455493
    	                          ISBN-13: 9780140455496
    	                          Publisher: Penguin Group 
    							                          Publish Date: 01/25/2011 
    							                          Dimensions: 7.73" L, 5.13" W, 0.63" H	                    
    ----------
    https://citylights.com/greek-roman/timaeus-critias-tr-desmond-lee/
    
    	                          ISBN-10: 0140455043
    	                          ISBN-13: 9780140455045
    	                          Publisher: Penguin Group 
    							                          Publish Date: 11/25/2008 
    							                          Dimensions: 7.80" L, 5.18" W, 0.43" H	                    
    ----------
    https://citylights.com/greek-roman/gorgias-tr-hamilton-emlyn-jones/
    
    	                          ISBN-10: 0140449043
    	                          ISBN-13: 9780140449044
    	                          Publisher: Penguin Group 
    							                          Publish Date: 06/29/2004 
    							                          Dimensions: 7.78" L, 5.10" W, 0.52" H	                    
    ----------
    https://citylights.com/greek-roman/symposium-tr-christopher-gill/
    
    	                          ISBN-10: 0140449272
    	                          ISBN-13: 9780140449273
    	                          Publisher: Penguin Group 
    							                          Publish Date: 04/29/2003 
    							                          Dimensions: 7.77" L, 5.10" W, 0.35" H	                    
    ----------
    https://citylights.com/greek-roman/last-days-of-socrates/
    
    	                          ISBN-10: 0140449280
    	                          ISBN-13: 9780140449280
    	                          Publisher: Penguin Group 
    							                          Publish Date: 04/29/2003 
    							                          Dimensions: 7.70" L, 5.00" W, 0.80" H	                    
    ----------
    https://citylights.com/greek-roman/odes/
    
    	                          ISBN-10: 014044209X
    	                          ISBN-13: 9780140442090
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/16/1982 
    							                          Dimensions: 7.70" L, 5.00" W, 0.70" H	                    
    ----------
    https://citylights.com/greek-roman/satyricon-tr-helen-morales/
    
    	                          ISBN-10: 0140448055
    	                          ISBN-13: 9780140448054
    	                          Publisher: Penguin Group 
    							                          Publish Date: 01/31/2012 
    							                          Dimensions: 7.70" L, 5.00" W, 0.60" H	                    
    ----------
    https://citylights.com/greek-roman/metamorphoses-tr-david-raeburn/
    
    	                          ISBN-10: 014044789X
    	                          ISBN-13: 9780140447897
    	                          Publisher: Penguin Group 
    							                          Publish Date: 08/01/2004 
    							                          Dimensions: 7.79" L, 5.07" W, 1.28" H	                    
    ----------
    https://citylights.com/greek-roman/metamorphoses-of-ovid/
    
    	                          ISBN-10: 0156001268
    	                          ISBN-13: 9780156001267
    	                          Publisher: Mariner Books 
    							                          Publish Date: 04/15/1995 
    							                          Dimensions: 8.90" L, 5.90" W, 2.00" H	                    
    ----------
    https://citylights.com/greek-roman/heroides/
    
    	                          ISBN-10: 0140423559
    	                          ISBN-13: 9780140423556
    	                          Publisher: Penguin Group 
    							                          Publish Date: 10/02/1990 
    							                          Dimensions: 7.77" L, 5.05" W, 0.70" H	                    
    ----------
    https://citylights.com/greek-roman/fasti-tr-boyle-woodard/
    
    	                          ISBN-10: 0140446907
    	                          ISBN-13: 9780140446906
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/01/2000 
    							                          Dimensions: 7.80" L, 5.10" W, 0.84" H	                    
    ----------
    https://citylights.com/greek-roman/rise-fall-of-classical-greece/
    
    	                          ISBN-10: 0691173141
    	                          ISBN-13: 9780691173146
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 10/04/2016 
    							                          Dimensions: 8.40" L, 5.40" W, 1.30" H	                    
    ----------
    https://citylights.com/greek-roman/therapy-of-desire-hellenistic-ethics/
    
    	                          ISBN-10: 0691181020
    	                          ISBN-13: 9780691181028
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 05/22/2018 
    							                          Dimensions: 8.40" L, 5.40" W, 1.70" H	                    
    ----------
    https://citylights.com/greek-roman/short-hist-of-byzantium/
    
    	                          ISBN-10: 0679772693
    	                          ISBN-13: 9780679772699
    	                          Publisher: Vintage 
    							                          Publish Date: 12/29/1998 
    							                          Dimensions: 8.06" L, 5.23" W, 0.99" H	                    
    ----------
    https://citylights.com/greek-roman/darkening-age-christian-destruction-of/
    
    	                          ISBN-10: 1328589285
    	                          ISBN-13: 9781328589286
    	                          Publisher: Mariner Books 
    							                          Publish Date: 04/16/2019 
    							                          Dimensions: 7.90" L, 5.20" W, 1.00" H	                    
    ----------
    https://citylights.com/greek-roman/ancient-greek-hero-in-24-hours/
    
    	                          ISBN-10: 0674241681
    	                          ISBN-13: 9780674241688
    	                          Publisher: Belknap Press 
    							                          Publish Date: 01/07/2020 
    							                          Dimensions: 9.20" L, 6.10" W, 1.70" H	                    
    ----------
    https://citylights.com/greek-roman/reading-homers-odyssey/
    
    	                          ISBN-10: 1684481368
    	                          ISBN-13: 9781684481361
    	                          Publisher: Bucknell University Press 
    							                          Publish Date: 04/05/2019 
    							                          Dimensions: 9.10" L, 6.20" W, 0.90" H	                    
    ----------
    https://citylights.com/greek-roman/plays-fragments-tr-norma-miller/
    
    	                          ISBN-10: 0140445013
    	                          ISBN-13: 9780140445015
    	                          Publisher: Penguin Group 
    							                          Publish Date: 02/02/1988 
    							                          Dimensions: 7.73" L, 5.04" W, 0.62" H	                    
    https://citylights.com/greek-roman/page/6/
    ----------
    https://citylights.com/greek-roman/poison-king-life-legend-of-mithradate/
    
    	                          ISBN-10: 0691150265
    	                          ISBN-13: 9780691150260
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 03/27/2011 
    							                          Dimensions: 8.97" L, 5.78" W, 1.21" H	                    
    ----------
    https://citylights.com/greek-roman/gods-robots-ancient-dreams-of-techno/
    
    	                          ISBN-10: 0691202265
    	                          ISBN-13: 9780691202266
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 04/21/2020 
    							                          Dimensions: 8.00" L, 5.20" W, 0.70" H	                    
    ----------
    https://citylights.com/greek-roman/martials-epigrams/
    
    	                          ISBN-10: 0143116274
    	                          ISBN-13: 9780143116271
    	                          Publisher: Penguin Group 
    							                          Publish Date: 10/01/2009 
    							                          Dimensions: 7.34" L, 4.76" W, 0.59" H	                    
    ----------
    https://citylights.com/poetry/epigrams-of-martial-tr-james-michie/
    
    	                          ISBN-10: 0375760423
    	                          ISBN-13: 9780375760426
    	                          Publisher: Modern Library 
    							                          Publish Date: 08/13/2002 
    							                          Dimensions: 8.10" L, 5.18" W, 0.52" H	                    
    ----------
    https://citylights.com/greek-roman/on-writing-hist-from-herodotus-to-herodi/
    
    	                          ISBN-10: 0141393572
    	                          ISBN-13: 9780141393575
    	                          Publisher: Penguin Group 
    							                          Publish Date: 03/20/2018 
    							                          Dimensions: 7.80" L, 5.10" W, 1.20" H	                    
    ----------
    https://citylights.com/greek-roman/nature-of-things-tr-ae-stallings/
    
    	                          ISBN-10: 0141396903
    	                          ISBN-13: 9780141396903
    	                          Publisher: Penguin Group 
    							                          Publish Date: 04/28/2015 
    							                          Dimensions: 6.80" L, 4.40" W, 1.20" H	                    
    ----------
    https://citylights.com/greek-roman/civil-war-tr-matthew-fox/
    
    	                          ISBN-10: 0143106236
    	                          ISBN-13: 9780143106234
    	                          Publisher: Penguin Group 
    							                          Publish Date: 01/31/2012 
    							                          Dimensions: 7.70" L, 5.10" W, 1.40" H	                    
    ----------
    https://citylights.com/greek-roman/daphnis-chloe/
    
    	                          ISBN-10: 0140440593
    	                          ISBN-13: 9780140440591
    	                          Publisher: Penguin Group 
    							                          Publish Date: 06/06/1989 
    							                          Dimensions: 7.68" L, 5.01" W, 0.34" H	                    
    ----------
    https://citylights.com/greek-roman/medea/
    
    	                          ISBN-10: 1854596020
    	                          ISBN-13: 9781854596024
    	                          Publisher: Nick Hern Books 
    							                          Publish Date: 04/01/2001 
    							                          Dimensions: 7.79" L, 4.93" W, 0.19" H	                    
    ----------
    https://citylights.com/greek-roman/rome-the-mediterranean-tr-bettenson/
    
    	                          ISBN-10: 0140443185
    	                          ISBN-13: 9780140443189
    	                          Publisher: Penguin Group 
    							                          Publish Date: 08/26/1976 
    							                          Dimensions: 7.78" L, 5.08" W, 1.20" H	                    
    ----------
    https://citylights.com/greek-roman/rome-italy/
    
    	                          ISBN-10: 0140443886
    	                          ISBN-13: 9780140443882
    	                          Publisher: Penguin Group 
    							                          Publish Date: 08/26/1982 
    							                          Dimensions: 7.70" L, 5.10" W, 1.00" H	                    
    ----------
    https://citylights.com/greek-roman/alexiad-tr-era-sewter/
    
    	                          ISBN-10: 0140455272
    	                          ISBN-13: 9780140455274
    	                          Publisher: Penguin Group 
    							                          Publish Date: 09/01/2009 
    							                          Dimensions: 7.96" L, 4.92" W, 1.07" H	                    
    ----------
    https://citylights.com/greek-roman/greeks/
    
    	                          ISBN-10: 0140135219
    	                          ISBN-13: 9780140135213
    	                          Publisher: Penguin Books 
    							                          Publish Date: 06/30/1950 
    							                          Dimensions: 7.77" L, 5.06" W, 0.62" H	                    
    ----------
    https://citylights.com/greek-roman/digest-of-roman-law/
    
    	                          ISBN-10: 0140443436
    	                          ISBN-13: 9780140443431
    	                          Publisher: Penguin Group 
    							                          Publish Date: 06/28/1979 
    							                          Dimensions: 7.87" L, 5.13" W, 0.49" H	                    
    ----------
    https://citylights.com/greek-roman/jewish-war-tr-ga-williamsonm-smallwood/
    
    	                          ISBN-10: 0140444203
    	                          ISBN-13: 9780140444209
    	                          Publisher: Penguin Group 
    							                          Publish Date: 02/07/1984 
    							                          Dimensions: 7.87" L, 5.01" W, 0.86" H	                    
    ----------
    https://citylights.com/greek-roman/helen-of-troy-goddess-princess-whore/
    
    	                          ISBN-10: 1400076005
    	                          ISBN-13: 9781400076000
    	                          Publisher: Vintage 
    							                          Publish Date: 11/01/2006 
    							                          Dimensions: 7.96" L, 5.26" W, 1.01" H	                    
    ----------
    https://citylights.com/greek-roman/satires-of-horace-persius-tr-niall-rud/
    
    	                          ISBN-10: 0140455086
    	                          ISBN-13: 9780140455083
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/27/2005 
    							                          Dimensions: 7.76" L, 5.14" W, 0.61" H	                    
    ----------
    https://citylights.com/new-nonfiction-in-hardcover/ht-be-content-ancient-poets-guide/
    
    	                          ISBN-10: 0691182523
    	                          ISBN-13: 9780691182520
    	                          Publisher: Princeton University Press 
    							                          Publish Date: 10/20/2020 
    							                          Dimensions: 6.90" L, 4.70" W, 1.10" H	                    
    ----------
    https://citylights.com/greek-roman/iliad-tr-peter-green/
    
    	                          ISBN-10: 0520281438
    	                          ISBN-13: 9780520281431
    	                          Publisher: University of California Press 
    							                          Publish Date: 02/23/2019 
    							                          Dimensions: 8.80" L, 5.90" W, 1.60" H	                    
    ----------
    https://citylights.com/new-nonfiction-in-hardcover/odyssey-tr-anthony-verity-2/
    
    	                          ISBN-10: 0199669104
    	                          ISBN-13: 9780199669103
    	                          Publisher: Oxford University Press, USA 
    							                          Publish Date: 01/01/2017 
    							                          Dimensions: 8.60" L, 5.40" W, 1.30" H	                    
    


```python
df.to_csv('greek-roman.csv')
```


```python
df_greek_roman_to_clean=pd.read_csv('greek-roman.csv')

df_greek_roman_to_clean_columns = df_greek_roman_to_clean.drop(columns=['Unnamed: 0'])
```


```python
df_greek_roman_to_clean_columns
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>\n\t                          ISBN-10: 0141392649\n\t                          ISBN-13: 9780141392646\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 04/17/2018 \n\t\t\t\t\t\t\t                          Dimensions: 7.70" L, 5.10" W, 0.80" H\t</td>
    </tr>
    <tr>
      <th>1</th>
      <td>\n\t                          ISBN-10: 0141392649\n\t                          ISBN-13: 9780141392646\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 04/17/2018 \n\t\t\t\t\t\t\t                          Dimensions: 7.70" L, 5.10" W, 0.80" H\t</td>
    </tr>
    <tr>
      <th>2</th>
      <td>\n\t                          ISBN-10: 0141392649\n\t                          ISBN-13: 9780141392646\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 04/17/2018 \n\t\t\t\t\t\t\t                          Dimensions: 7.70" L, 5.10" W, 0.80" H\t</td>
    </tr>
    <tr>
      <th>3</th>
      <td>\n\t                          ISBN-10: 0141392649\n\t                          ISBN-13: 9780141392646\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 04/17/2018 \n\t\t\t\t\t\t\t                          Dimensions: 7.70" L, 5.10" W, 0.80" H\t</td>
    </tr>
    <tr>
      <th>4</th>
      <td>\n\t                          ISBN-10: 0141392649\n\t                          ISBN-13: 9780141392646\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 04/17/2018 \n\t\t\t\t\t\t\t                          Dimensions: 7.70" L, 5.10" W, 0.80" H\t</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>115</th>
      <td>\n\t                          ISBN-10: 0691150265\n\t                          ISBN-13: 9780691150260\n\t                          Publisher: Princeton University Press \n\t\t\t\t\t\t\t                          Publish Date: 03/27/2011 \n\t\t\t\t\t\t\t                          Dimensions: 8.97" L, 5.78" W, 1.21" H\t</td>
    </tr>
    <tr>
      <th>116</th>
      <td>\n\t                          ISBN-10: 0691150265\n\t                          ISBN-13: 9780691150260\n\t                          Publisher: Princeton University Press \n\t\t\t\t\t\t\t                          Publish Date: 03/27/2011 \n\t\t\t\t\t\t\t                          Dimensions: 8.97" L, 5.78" W, 1.21" H\t</td>
    </tr>
    <tr>
      <th>117</th>
      <td>\n\t                          ISBN-10: 0691150265\n\t                          ISBN-13: 9780691150260\n\t                          Publisher: Princeton University Press \n\t\t\t\t\t\t\t                          Publish Date: 03/27/2011 \n\t\t\t\t\t\t\t                          Dimensions: 8.97" L, 5.78" W, 1.21" H\t</td>
    </tr>
    <tr>
      <th>118</th>
      <td>\n\t                          ISBN-10: 0691150265\n\t                          ISBN-13: 9780691150260\n\t                          Publisher: Princeton University Press \n\t\t\t\t\t\t\t                          Publish Date: 03/27/2011 \n\t\t\t\t\t\t\t                          Dimensions: 8.97" L, 5.78" W, 1.21" H\t</td>
    </tr>
    <tr>
      <th>119</th>
      <td>\n\t                          ISBN-10: 0691150265\n\t                          ISBN-13: 9780691150260\n\t                          Publisher: Princeton University Press \n\t\t\t\t\t\t\t                          Publish Date: 03/27/2011 \n\t\t\t\t\t\t\t                          Dimensions: 8.97" L, 5.78" W, 1.21" H\t</td>
    </tr>
  </tbody>
</table>
<p>120 rows ?? 1 columns</p>
</div>




```python
df_greek_roman_to_clean_columns_split = df_greek_roman_to_clean_columns['0'].str.split("\n\t")
```


```python
df_greek_roman = df_greek_roman_to_clean_columns_split.to_list()
column_names = ['0','ISBN-10','ISBN-13','Publisher','Publish Date', 'Dimensions']
new_greek_roman_df = pd.DataFrame(df_greek_roman,columns=column_names)
```


```python
clean_greek_roman_df=new_greek_roman_df.drop(columns=['0','Dimensions'])
```


```python
clean_greek_roman_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ISBN-10</th>
      <th>ISBN-13</th>
      <th>Publisher</th>
      <th>Publish Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>\t\t\t\t\t\t                          Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>\t\t\t\t\t\t                          Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>\t\t\t\t\t\t                          Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>\t\t\t\t\t\t                          Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>\t\t\t\t\t\t                          Publish Date: 04/17/2018</td>
    </tr>
  </tbody>
</table>
</div>




```python
html_chars = ["<tr>","\n","</th>","<th>","<td>","</td>",
              "</tr>",'\t']
for char in html_chars:
    clean_greek_roman_df['ISBN-10'] = clean_greek_roman_df['ISBN-10'].str.replace(char, ' ')
    clean_greek_roman_df['ISBN-13'] = clean_greek_roman_df['ISBN-13'].str.replace(char, ' ')
    clean_greek_roman_df['Publisher'] = clean_greek_roman_df['Publisher'].str.replace(char, ' ')
    clean_greek_roman_df['Publish Date'] = clean_greek_roman_df['Publish Date'].str.replace(char, ' ')
   
    
```


```python
pd.set_option("max_colwidth", 1000)
clean_greek_roman_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ISBN-10</th>
      <th>ISBN-13</th>
      <th>Publisher</th>
      <th>Publish Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
  </tbody>
</table>
</div>




```python
clean_greek_roman_df.to_csv('greek-roman-clean.csv')
```


```python

```


```python
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
```

    
    
    ====== WebDriver manager ======
    Current google-chrome version is 93.0.4577
    Get LATEST driver version for 93.0.4577
    Driver [C:\Users\RobertW\.wdm\drivers\chromedriver\win32\93.0.4577.63\chromedriver.exe] found in cache
    

    https://citylights.com/asian/
    ----------
    https://citylights.com/asian/gazing-at-the-moon-buddhist-poems-of-s/
    
    	                          ISBN-10: 1611809428
    	                          ISBN-13: 9781611809428
    	                          Publisher: Shambhala 
    							                          Publish Date: 09/07/2021 
    							                          Dimensions: 0.00" L, 0.00" W, 0.00" H	                    
    ----------
    https://citylights.com/theater-performing-arts/6-yuan-plays/
    
    	                          ISBN-10: 0140442626
    	                          ISBN-13: 9780140442625
    	                          Publisher: Penguin Group 
    							                          Publish Date: 09/30/1972 
    							                          Dimensions: 7.78" L, 5.07" W, 0.61" H	                    
    ----------
    https://citylights.com/asian/classic-of-mountains-seas/
    
    	                          ISBN-10: 0140447199
    	                          ISBN-13: 9780140447194
    	                          Publisher: Penguin Group 
    							                          Publish Date: 01/01/2000 
    							                          Dimensions: 7.79" L, 5.07" W, 0.69" H	                    
    ----------
    https://citylights.com/story-anthologies/anth-of-japanese-lit-earliest-to-mid-19/
    
    	                          ISBN-10: 0802150586
    	                          ISBN-13: 9780802150585
    	                          Publisher: Grove Press 
    							                          Publish Date: 01/11/1994 
    							                          Dimensions: 8.27" L, 5.42" W, 1.22" H	                    
    ----------
    https://citylights.com/asian/bushido-soul-of-japan/
    
    	                          ISBN-10: 0241472431
    	                          ISBN-13: 9780241472439
    	                          Publisher: Penguin Books 
    							                          Publish Date: 06/08/2021 
    							                          Dimensions: 7.00" L, 4.50" W, 0.50" H	                    
    ----------
    https://citylights.com/poetry/sel-poems-of-wang-wei-tr-david-hinton/
    
    	                          ISBN-10: 0811216187
    	                          ISBN-13: 9780811216180
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 06/28/2006 
    							                          Dimensions: 8.96" L, 6.14" W, 0.43" H	                    
    ----------
    https://citylights.com/asian/art-of-writing-lu-chis-wen-fu/
    
    	                          ISBN-10: 1571314121
    	                          ISBN-13: 9781571314123
    	                          Publisher: Milkweed Editions 
    							                          Publish Date: 08/01/2000 
    							                          Dimensions: 7.47" L, 5.37" W, 0.38" H	                    
    ----------
    https://citylights.com/asian/samurai-very-short-intro/
    
    	                          ISBN-10: 0190685077
    	                          ISBN-13: 9780190685072
    	                          Publisher: Oxford University Press, USA 
    							                          Publish Date: 08/01/2021 
    							                          Dimensions: 0.00" L, 0.00" W, 0.00" H	                    
    ----------
    https://citylights.com/asian/book-of-master-mo-tr-ian-johnston/
    
    	                          ISBN-10: 014139210X
    	                          ISBN-13: 9780141392103
    	                          Publisher: Penguin Group 
    							                          Publish Date: 07/29/2014 
    							                          Dimensions: 7.70" L, 5.00" W, 1.00" H	                    
    ----------
    https://citylights.com/travel-literature/south-of-the-yangtze/
    
    	                          ISBN-10: 1619027348
    	                          ISBN-13: 9781619027343
    	                          Publisher: Counterpoint LLC 
    							                          Publish Date: 08/09/2016 
    							                          Dimensions: 8.90" L, 5.90" W, 0.70" H	                    
    ----------
    https://citylights.com/travel-literature/silk-road-bus-to-pakistan/
    
    	                          ISBN-10: 1619027100
    	                          ISBN-13: 9781619027107
    	                          Publisher: Counterpoint LLC 
    							                          Publish Date: 02/09/2016 
    							                          Dimensions: 8.90" L, 5.90" W, 0.70" H	                    
    ----------
    https://citylights.com/taoism-buddhism/imagination-narrative-buddhist-asia/
    
    	                          ISBN-10: 6162151352
    	                          ISBN-13: 9786162151354
    	                          Publisher: Silkworm Books 
    							                          Publish Date: 10/01/2017 
    							                          Dimensions: 8.40" L, 5.60" W, 0.60" H	                    
    ----------
    https://citylights.com/taoism-buddhism/road-to-heaven-chinese-hermits/
    
    	                          ISBN-10: 1582435235
    	                          ISBN-13: 9781582435237
    	                          Publisher: Counterpoint LLC 
    							                          Publish Date: 09/29/2009 
    							                          Dimensions: 8.90" L, 5.90" W, 0.60" H	                    
    ----------
    https://citylights.com/asia/shinto-in-the-hist-culture-of-japan/
    
    	                          ISBN-10: 092430491X
    	                          ISBN-13: 9780924304910
    	                          Publisher: Association for Asian Studies 
    							                          Publish Date: 09/30/2020 
    							                          Dimensions: 8.70" L, 5.80" W, 0.50" H	                    
    ----------
    https://citylights.com/poetry/songs-of-the-south-ancient-chinese-ant/
    
    	                          ISBN-10: 0140443754
    	                          ISBN-13: 9780140443752
    	                          Publisher: Penguin Group 
    							                          Publish Date: 01/31/2012 
    							                          Dimensions: 7.77" L, 5.07" W, 0.67" H	                    
    ----------
    https://citylights.com/asian/monkey-the-monk-journey-to-the-west/
    
    	                          ISBN-10: 0226971562
    	                          ISBN-13: 9780226971568
    	                          Publisher: University of Chicago Press 
    							                          Publish Date: 11/15/2006 
    							                          Dimensions: 8.58" L, 5.92" W, 1.06" H	                    
    ----------
    https://citylights.com/asian/chinese-lit-3rd-edition/
    
    	                          ISBN-10: 0521186781
    	                          ISBN-13: 9780521186780
    	                          Publisher: Cambridge University Press 
    							                          Publish Date: 03/22/2012 
    							                          Dimensions: 9.00" L, 6.10" W, 0.60" H	                    
    ----------
    https://citylights.com/womens-studies-feminism/crossing-the-gate/
    
    	                          ISBN-10: 1438463200
    	                          ISBN-13: 9781438463209
    	                          Publisher: State University of New York Press 
    							                          Publish Date: 07/02/2017 
    							                          Dimensions: 8.90" L, 6.00" W, 1.00" H	                    
    ----------
    https://citylights.com/asian/monkey-tr-arthur-waley/
    
    	                          ISBN-10: 0802130860
    	                          ISBN-13: 9780802130860
    	                          Publisher: Grove Press 
    							                          Publish Date: 01/12/1994 
    							                          Dimensions: 8.22" L, 5.44" W, 0.82" H	                    
    ----------
    https://citylights.com/asian/kojiki-birth-of-japan-japanese-creat/
    
    	                          ISBN-10: 4805315393
    	                          ISBN-13: 9784805315392
    	                          Publisher: Tuttle Publishing 
    							                          Publish Date: 10/22/2019 
    							                          Dimensions: 12.20" L, 9.10" W, 0.50" H	                    
    https://citylights.com/asian/page/2/
    ----------
    https://citylights.com/poetry/in-such-hard-times-tr-red-pine/
    
    	                          ISBN-10: 1556592795
    	                          ISBN-13: 9781556592799
    	                          Publisher: Copper Canyon Press 
    							                          Publish Date: 07/01/2009 
    							                          Dimensions: 8.90" L, 5.90" W, 1.20" H	                    
    ----------
    https://citylights.com/poetry-anthologies/chinese-rhyme-prose/
    
    	                          ISBN-10: 9629965631
    	                          ISBN-13: 9789629965631
    	                          Publisher: New York Review of Books 
    							                          Publish Date: 01/13/2015 
    							                          Dimensions: 8.40" L, 5.30" W, 0.60" H	                    
    ----------
    https://citylights.com/poetry/late-poems-of-wang-an-shih-tr-d-hinton/
    
    	                          ISBN-10: 0811222632
    	                          ISBN-13: 9780811222631
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 03/17/2015 
    							                          Dimensions: 8.80" L, 5.90" W, 0.40" H	                    
    ----------
    https://citylights.com/taoism-buddhism/book-of-songs/
    
    	                          ISBN-10: 0802134777
    	                          ISBN-13: 9780802134776
    	                          Publisher: Grove Press 
    							                          Publish Date: 09/13/1996 
    							                          Dimensions: 8.20" L, 5.50" W, 1.20" H	                    
    ----------
    https://citylights.com/asian/japanese-no-dramas/
    
    	                          ISBN-10: 0140445390
    	                          ISBN-13: 9780140445398
    	                          Publisher: Penguin Group 
    							                          Publish Date: 06/01/1993 
    							                          Dimensions: 7.77" L, 5.09" W, 0.89" H	                    
    ----------
    https://citylights.com/asian/sel-poems-tr-david-hinton/
    
    	                          ISBN-10: 081122838X
    	                          ISBN-13: 9780811228381
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 02/25/2020 
    							                          Dimensions: 8.90" L, 6.00" W, 0.90" H	                    
    ----------
    https://citylights.com/poetry/little-primer-of-tu-fu-tr-david-hawkes/
    
    	                          ISBN-10: 962996659X
    	                          ISBN-13: 9789629966591
    	                          Publisher: New York Review of Books 
    							                          Publish Date: 06/14/2016 
    							                          Dimensions: 8.50" L, 5.60" W, 0.60" H	                    
    ----------
    https://citylights.com/asian/written-in-exile-tr-red-pine/
    
    	                          ISBN-10: 155659562X
    	                          ISBN-13: 9781556595622
    	                          Publisher: Copper Canyon Press 
    							                          Publish Date: 09/17/2019 
    							                          Dimensions: 9.00" L, 6.00" W, 1.00" H	                    
    ----------
    https://citylights.com/asian/art-of-war-tr-victor-mair/
    
    	                          ISBN-10: 0231133839
    	                          ISBN-13: 9780231133838
    	                          Publisher: Columbia University Press 
    							                          Publish Date: 03/01/2009 
    							                          Dimensions: 8.10" L, 5.40" W, 0.60" H	                    
    ----------
    https://citylights.com/poetry/sel-poems-of-tao-chien-tr-d-hinton/
    
    	                          ISBN-10: 1556590563
    	                          ISBN-13: 9781556590566
    	                          Publisher: Copper Canyon Press 
    							                          Publish Date: 05/01/2000 
    							                          Dimensions: 8.55" L, 5.61" W, 0.32" H	                    
    ----------
    https://citylights.com/asian/art-of-war-tr-john-minford/
    
    	                          ISBN-10: 0143105752
    	                          ISBN-13: 9780143105756
    	                          Publisher: Penguin Group 
    							                          Publish Date: 04/01/2009 
    							                          Dimensions: 7.60" L, 4.90" W, 0.80" H	                    
    ----------
    https://citylights.com/asian/lost-art-of-war-tr-thomas-cleary/
    
    	                          ISBN-10: 0062514059
    	                          ISBN-13: 9780062514059
    	                          Publisher: HarperOne 
    							                          Publish Date: 04/11/1997 
    							                          Dimensions: 8.01" L, 5.31" W, 0.41" H	                    
    ----------
    https://citylights.com/asian/sel-poems-of-su-tung-po-tr-b-watson/
    
    	                          ISBN-10: 1556590644
    	                          ISBN-13: 9781556590641
    	                          Publisher: Copper Canyon Press 
    							                          Publish Date: 02/01/1993 
    							                          Dimensions: 8.98" L, 6.03" W, 0.49" H	                    
    ----------
    https://citylights.com/asia/emperor-of-china-self-portrait-kang-hsi/
    
    	                          ISBN-10: 067972074X
    	                          ISBN-13: 9780679720744
    	                          Publisher: Vintage 
    							                          Publish Date: 10/22/1988 
    							                          Dimensions: 7.99" L, 5.26" W, 0.84" H	                    
    ----------
    https://citylights.com/asian/strange-tales-from-a-chinese-studio/
    
    	                          ISBN-10: 0140447407
    	                          ISBN-13: 9780140447408
    	                          Publisher: Penguin Group 
    							                          Publish Date: 10/31/2006 
    							                          Dimensions: 7.70" L, 5.00" W, 0.90" H	                    
    ----------
    https://citylights.com/asian/li-shangyin-sel-poems/
    
    	                          ISBN-10: 168137224X
    	                          ISBN-13: 9781681372242
    	                          Publisher: New York Review of Books 
    							                          Publish Date: 07/31/2018 
    							                          Dimensions: 6.90" L, 4.50" W, 0.50" H	                    
    ----------
    https://citylights.com/asian/peach-blossom-fan/
    
    	                          ISBN-10: 1590178769
    	                          ISBN-13: 9781590178768
    	                          Publisher: New York Review of Books 
    							                          Publish Date: 07/21/2015 
    							                          Dimensions: 8.00" L, 5.30" W, 0.90" H	                    
    ----------
    https://citylights.com/staff-picks-archive/pillow-book-tr-meredith-mckinney/
    
    	                          ISBN-10: 0140448063
    	                          ISBN-13: 9780140448061
    	                          Publisher: Penguin Group 
    							                          Publish Date: 11/01/2007 
    							                          Dimensions: 7.76" L, 5.16" W, 0.94" H	                    
    ----------
    https://citylights.com/asian/liking-in-silence-poems-of-kim-sa-in/
    
    	                          ISBN-10: 1945680342
    	                          ISBN-13: 9781945680342
    	                          Publisher: White Pine Press (NY) 
    							                          Publish Date: 09/17/2019 
    							                          Dimensions: 9.00" L, 6.00" W, 0.40" H	                    
    ----------
    https://citylights.com/asian/hist-of-art-in-japan/
    
    	                          ISBN-10: 0231193416
    	                          ISBN-13: 9780231193412
    	                          Publisher: Columbia University Press 
    							                          Publish Date: 10/08/2019 
    							                          Dimensions: 8.90" L, 6.00" W, 1.50" H	                    
    https://citylights.com/asian/page/3/
    ----------
    https://citylights.com/asian/norton-anth-of-world-religions-daoism/
    
    	                          ISBN-10: 0393355004
    	                          ISBN-13: 9780393355000
    	                          Publisher: W. W. Norton & Company 
    							                          Publish Date: 09/26/2017 
    							                          Dimensions: 9.10" L, 5.90" W, 0.90" H	                    
    ----------
    https://citylights.com/mythology-folklore/chinese-fairy-tales-fantasies/
    
    	                          ISBN-10: 0394739949
    	                          ISBN-13: 9780394739946
    	                          Publisher: Pantheon Books 
    							                          Publish Date: 07/12/1980 
    							                          Dimensions: 9.22" L, 6.22" W, 0.62" H	                    
    ----------
    https://citylights.com/poetry-anthologies/100-more-poems-from-the-chinese-love/
    
    	                          ISBN-10: 0811201791
    	                          ISBN-13: 9780811201797
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 01/17/1970 
    							                          Dimensions: 7.95" L, 5.18" W, 0.45" H	                    
    ----------
    https://citylights.com/poetry/100-poems-from-the-chinese/
    
    	                          ISBN-10: 0811201805
    	                          ISBN-13: 9780811201803
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 01/17/1971 
    							                          Dimensions: 8.00" L, 5.23" W, 0.43" H	                    
    ----------
    https://citylights.com/asian/written-on-the-sky-japanese-poems/
    
    	                          ISBN-10: 0811218376
    	                          ISBN-13: 9780811218375
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 04/21/2009 
    							                          Dimensions: 5.90" L, 3.90" W, 0.60" H	                    
    ----------
    https://citylights.com/asian/songs-of-love-moon-wind-chinese-poems/
    
    	                          ISBN-10: 0811218368
    	                          ISBN-13: 9780811218368
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 04/21/2009 
    							                          Dimensions: 5.90" L, 3.90" W, 0.40" H	                    
    ----------
    https://citylights.com/poetry/women-poets-of-china/
    
    	                          ISBN-10: 0811208214
    	                          ISBN-13: 9780811208215
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 02/17/1982 
    							                          Dimensions: 8.06" L, 5.25" W, 0.43" H	                    
    ----------
    https://citylights.com/poetry-anthologies/women-poets-of-japan/
    
    	                          ISBN-10: 0811208206
    	                          ISBN-13: 9780811208208
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 02/17/1982 
    							                          Dimensions: 7.95" L, 5.19" W, 0.53" H	                    
    ----------
    https://citylights.com/asian/poems-of-the-masters-tang-sung/
    
    	                          ISBN-10: 1556591950
    	                          ISBN-13: 9781556591952
    	                          Publisher: Copper Canyon Press 
    							                          Publish Date: 09/01/2003 
    							                          Dimensions: 8.98" L, 5.90" W, 1.44" H	                    
    ----------
    https://citylights.com/poetry/mountain-poems-of-stonehouse/
    
    	                          ISBN-10: 1556594550
    	                          ISBN-13: 9781556594557
    	                          Publisher: Copper Canyon Press 
    							                          Publish Date: 05/27/2014 
    							                          Dimensions: 8.90" L, 5.40" W, 0.70" H	                    
    ----------
    https://citylights.com/asian/finding-them-gone-visiting-chinas-poe/
    
    	                          ISBN-10: 1556594895
    	                          ISBN-13: 9781556594892
    	                          Publisher: Copper Canyon Press 
    							                          Publish Date: 01/26/2016 
    							                          Dimensions: 8.70" L, 6.20" W, 1.00" H	                    
    ----------
    https://citylights.com/asian/hundred-verses-from-old-japan-bilingual/
    
    	                          ISBN-10: 4805308532
    	                          ISBN-13: 9784805308530
    	                          Publisher: Tuttle Publishing 
    							                          Publish Date: 09/15/2007 
    							                          Dimensions: 8.00" L, 5.10" W, 0.70" H	                    
    ----------
    https://citylights.com/poetry/sel-poems-po-chu-i-tr-david-hinton/
    
    	                          ISBN-10: 0811214125
    	                          ISBN-13: 9780811214124
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 06/17/1999 
    							                          Dimensions: 8.85" L, 5.88" W, 0.59" H	                    
    ----------
    https://citylights.com/asian/book-of-tea-2/
    
    	                          ISBN-10: 0141191848
    	                          ISBN-13: 9780141191843
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/28/2010 
    							                          Dimensions: 7.50" L, 5.00" W, 0.40" H	                    
    ----------
    https://citylights.com/asian/song-of-kieu-new-lament/
    
    	                          ISBN-10: 0241360668
    	                          ISBN-13: 9780241360668
    	                          Publisher: Penguin Group 
    							                          Publish Date: 07/09/2019 
    							                          Dimensions: 7.70" L, 5.00" W, 0.60" H	                    
    ----------
    https://citylights.com/asian/tale-of-genji-tr-royall-tyler-2/
    
    	                          ISBN-10: 0143039490
    	                          ISBN-13: 9780143039495
    	                          Publisher: Penguin Group 
    							                          Publish Date: 02/28/2006 
    							                          Dimensions: 7.76" L, 5.20" W, 0.63" H	                    
    ----------
    https://citylights.com/asian/tale-of-genji-tr-dennis-washburn/
    
    	                          ISBN-10: 0393353397
    	                          ISBN-13: 9780393353396
    	                          Publisher: W. W. Norton & Company 
    							                          Publish Date: 12/06/2016 
    							                          Dimensions: 9.10" L, 6.10" W, 2.50" H	                    
    ----------
    https://citylights.com/asian/diary-of-lady-murasaki-tr-rich-bowring/
    
    	                          ISBN-10: 014043576X
    	                          ISBN-13: 9780140435764
    	                          Publisher: Penguin Group 
    							                          Publish Date: 10/01/1996 
    							                          Dimensions: 8.00" L, 4.84" W, 0.37" H	                    
    ----------
    https://citylights.com/asian/tale-of-genji-tr-royall-tyler/
    
    	                          ISBN-10: 014243714X
    	                          ISBN-13: 9780142437148
    	                          Publisher: Penguin Group 
    							                          Publish Date: 11/26/2002 
    							                          Dimensions: 9.16" L, 6.29" W, 1.99" H	                    
    ----------
    https://citylights.com/asian/world-of-the-shining-prince-paper-origin/
    
    	                          ISBN-10: 0345803906
    	                          ISBN-13: 9780345803900
    	                          Publisher: Vintage 
    							                          Publish Date: 05/21/2013 
    							                          Dimensions: 7.73" L, 5.51" W, 0.80" H	                    
    https://citylights.com/asian/page/4/
    ----------
    https://citylights.com/asian/as-i-crossed-a-bridge-of-dreams-woman-in/
    
    	                          ISBN-10: 0140442820
    	                          ISBN-13: 9780140442823
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/05/1989 
    							                          Dimensions: 7.70" L, 5.00" W, 0.50" H	                    
    ----------
    https://citylights.com/poetry-anthologies/wild-geese-returning-chinese-reversibl/
    
    	                          ISBN-10: 9629968002
    	                          ISBN-13: 9789629968007
    	                          Publisher: New York Review of Books 
    							                          Publish Date: 03/14/2017 
    							                          Dimensions: 8.40" L, 5.50" W, 0.80" H	                    
    ----------
    https://citylights.com/asian/mencius-tr-dc-lau/
    
    	                          ISBN-10: 014044971X
    	                          ISBN-13: 9780140449716
    	                          Publisher: Penguin Group 
    							                          Publish Date: 06/28/2005 
    							                          Dimensions: 7.82" L, 5.86" W, 0.76" H	                    
    ----------
    https://citylights.com/asian/travels-with-a-writing-brush-japanese/
    
    	                          ISBN-10: 0241310873
    	                          ISBN-13: 9780241310878
    	                          Publisher: Penguin Group 
    							                          Publish Date: 07/14/2020 
    							                          Dimensions: 7.70" L, 5.00" W, 1.00" H	                    
    ----------
    https://citylights.com/asian/9-cloud-dream-tr-heinz-insu-fenkl/
    
    	                          ISBN-10: 0143131273
    	                          ISBN-13: 9780143131274
    	                          Publisher: Penguin Group 
    							                          Publish Date: 02/12/2019 
    							                          Dimensions: 7.60" L, 5.00" W, 0.90" H	                    
    ----------
    https://citylights.com/asian/100-poets-1-poem-each/
    
    	                          ISBN-10: 0141395931
    	                          ISBN-13: 9780141395937
    	                          Publisher: Penguin Group 
    							                          Publish Date: 08/14/2018 
    							                          Dimensions: 7.70" L, 5.00" W, 0.80" H	                    
    ----------
    https://citylights.com/asian/tales-of-ise-tr-donald-keene/
    
    	                          ISBN-10: 0141392576
    	                          ISBN-13: 9780141392578
    	                          Publisher: Penguin Group 
    							                          Publish Date: 12/06/2016 
    							                          Dimensions: 7.70" L, 5.10" W, 0.90" H	                    
    ----------
    https://citylights.com/asian/essence-of-budo/
    
    	                          ISBN-10: 1590308468
    	                          ISBN-13: 9781590308462
    	                          Publisher: Shambhala 
    							                          Publish Date: 10/12/2010 
    							                          Dimensions: 8.34" L, 5.54" W, 0.54" H	                    
    ----------
    https://citylights.com/poetry/sel-poems-of-li-po-tr-david-hinton/
    
    	                          ISBN-10: 0811213234
    	                          ISBN-13: 9780811213233
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 05/17/1996 
    							                          Dimensions: 7.99" L, 5.29" W, 0.50" H	                    
    ----------
    https://citylights.com/poetry/complete-poems-li-ching-chao/
    
    	                          ISBN-10: 0811207455
    	                          ISBN-13: 9780811207454
    	                          Publisher: New Directions Publishing Corporation 
    							                          Publish Date: 01/17/1980 
    							                          Dimensions: 0.00" L, 0.00" W, 0.00" H	                    
    ----------
    https://citylights.com/asian/plum-shadows-plank-bridge-2-memoir/
    
    	                          ISBN-10: 0231186851
    	                          ISBN-13: 9780231186858
    	                          Publisher: Columbia University Press 
    							                          Publish Date: 01/21/2020 
    							                          Dimensions: 8.40" L, 5.50" W, 1.20" H	                    
    ----------
    https://citylights.com/poetry/coll-poems-of-li-he-tr-jd-frodsham/
    
    	                          ISBN-10: 9629966603
    	                          ISBN-13: 9789629966607
    	                          Publisher: New York Review of Books 
    							                          Publish Date: 03/14/2017 
    							                          Dimensions: 8.40" L, 5.50" W, 0.80" H	                    
    ----------
    https://citylights.com/asian/arvind-krishna-mehrotra/
    
    	                          ISBN-10: 1681374013
    	                          ISBN-13: 9781681374017
    	                          Publisher: New York Review of Books 
    							                          Publish Date: 11/12/2019 
    							                          Dimensions: 7.10" L, 4.60" W, 0.50" H	                    
    ----------
    https://citylights.com/asian/far-eastern-lit/
    
    	                          ISBN-10: 0804463522
    	                          ISBN-13: 9780804463522
    	                          Publisher: Frederick Ungar 
    							                          Publish Date: 01/01/1986 
    							                          Dimensions: 0.00" L, 0.00" W, 0.00" H	                    
    ----------
    https://citylights.com/asian/penguin-book-of-haiku/
    
    	                          ISBN-10: 0140424768
    	                          ISBN-13: 9780140424768
    	                          Publisher: Penguin Group 
    							                          Publish Date: 08/14/2018 
    							                          Dimensions: 7.70" L, 5.10" W, 1.10" H	                    
    ----------
    https://citylights.com/food-culture/chinese-food/
    
    	                          ISBN-10: 0521186749
    	                          ISBN-13: 9780521186742
    	                          Publisher: Cambridge University Press 
    							                          Publish Date: 09/01/2011 
    							                          Dimensions: 9.00" L, 6.10" W, 0.30" H	                    
    ----------
    https://citylights.com/asian/banished-immortal-life-of-li-bai-li-p/
    
    	                          ISBN-10: 0525562435
    	                          ISBN-13: 9780525562436
    	                          Publisher: Vintage 
    							                          Publish Date: 12/03/2019 
    							                          Dimensions: 7.90" L, 5.10" W, 0.80" H	                    
    ----------
    https://citylights.com/critical-studies/unbinding-the-pillow-book-many-lives-o/
    
    	                          ISBN-10: 0231187998
    	                          ISBN-13: 9780231187992
    	                          Publisher: Columbia University Press 
    							                          Publish Date: 04/06/2021 
    							                          Dimensions: 8.90" L, 5.90" W, 0.70" H	                    
    ----------
    https://citylights.com/poetry/spring-of-my-life-tr-sam-hamill/
    
    	                          ISBN-10: 1570621446
    	                          ISBN-13: 9781570621444
    	                          Publisher: Shambhala 
    							                          Publish Date: 10/15/1997 
    							                          Dimensions: 8.89" L, 5.21" W, 0.53" H	                    
    ----------
    https://citylights.com/asian/lit-mind-the-carving-of-dragons/
    
    	                          ISBN-10: 9629965852
    	                          ISBN-13: 9789629965853
    	                          Publisher: New York Review of Books 
    							                          Publish Date: 01/13/2015 
    							                          Dimensions: 8.40" L, 5.50" W, 0.80" H	                    
    


```python
df.to_csv('asian.csv')
```


```python
df_asian_classics_to_clean=pd.read_csv('asian.csv')

df_asian_classics_to_clean_columns = df_asian_classics_to_clean.drop(columns=['Unnamed: 0'])
```


```python
df_asian_classics_to_clean_columns
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>\n\t                          ISBN-10: 0140442820\n\t                          ISBN-13: 9780140442823\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 12/05/1989 \n\t\t\t\t\t\t\t                          Dimensions: 7.70" L, 5.00" W, 0.50" H\t</td>
    </tr>
    <tr>
      <th>1</th>
      <td>\n\t                          ISBN-10: 9629968002\n\t                          ISBN-13: 9789629968007\n\t                          Publisher: New York Review of Books \n\t\t\t\t\t\t\t                          Publish Date: 03/14/2017 \n\t\t\t\t\t\t\t                          Dimensions: 8.40" L, 5.50" W, 0.80" H\t</td>
    </tr>
    <tr>
      <th>2</th>
      <td>\n\t                          ISBN-10: 014044971X\n\t                          ISBN-13: 9780140449716\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 06/28/2005 \n\t\t\t\t\t\t\t                          Dimensions: 7.82" L, 5.86" W, 0.76" H\t</td>
    </tr>
    <tr>
      <th>3</th>
      <td>\n\t                          ISBN-10: 0241310873\n\t                          ISBN-13: 9780241310878\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 07/14/2020 \n\t\t\t\t\t\t\t                          Dimensions: 7.70" L, 5.00" W, 1.00" H\t</td>
    </tr>
    <tr>
      <th>4</th>
      <td>\n\t                          ISBN-10: 0143131273\n\t                          ISBN-13: 9780143131274\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 02/12/2019 \n\t\t\t\t\t\t\t                          Dimensions: 7.60" L, 5.00" W, 0.90" H\t</td>
    </tr>
    <tr>
      <th>5</th>
      <td>\n\t                          ISBN-10: 0141395931\n\t                          ISBN-13: 9780141395937\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 08/14/2018 \n\t\t\t\t\t\t\t                          Dimensions: 7.70" L, 5.00" W, 0.80" H\t</td>
    </tr>
    <tr>
      <th>6</th>
      <td>\n\t                          ISBN-10: 0141392576\n\t                          ISBN-13: 9780141392578\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 12/06/2016 \n\t\t\t\t\t\t\t                          Dimensions: 7.70" L, 5.10" W, 0.90" H\t</td>
    </tr>
    <tr>
      <th>7</th>
      <td>\n\t                          ISBN-10: 1590308468\n\t                          ISBN-13: 9781590308462\n\t                          Publisher: Shambhala \n\t\t\t\t\t\t\t                          Publish Date: 10/12/2010 \n\t\t\t\t\t\t\t                          Dimensions: 8.34" L, 5.54" W, 0.54" H\t</td>
    </tr>
    <tr>
      <th>8</th>
      <td>\n\t                          ISBN-10: 0811213234\n\t                          ISBN-13: 9780811213233\n\t                          Publisher: New Directions Publishing Corporation \n\t\t\t\t\t\t\t                          Publish Date: 05/17/1996 \n\t\t\t\t\t\t\t                          Dimensions: 7.99" L, 5.29" W, 0.50" H\t</td>
    </tr>
    <tr>
      <th>9</th>
      <td>\n\t                          ISBN-10: 0811207455\n\t                          ISBN-13: 9780811207454\n\t                          Publisher: New Directions Publishing Corporation \n\t\t\t\t\t\t\t                          Publish Date: 01/17/1980 \n\t\t\t\t\t\t\t                          Dimensions: 0.00" L, 0.00" W, 0.00" H\t</td>
    </tr>
    <tr>
      <th>10</th>
      <td>\n\t                          ISBN-10: 0231186851\n\t                          ISBN-13: 9780231186858\n\t                          Publisher: Columbia University Press \n\t\t\t\t\t\t\t                          Publish Date: 01/21/2020 \n\t\t\t\t\t\t\t                          Dimensions: 8.40" L, 5.50" W, 1.20" H\t</td>
    </tr>
    <tr>
      <th>11</th>
      <td>\n\t                          ISBN-10: 9629966603\n\t                          ISBN-13: 9789629966607\n\t                          Publisher: New York Review of Books \n\t\t\t\t\t\t\t                          Publish Date: 03/14/2017 \n\t\t\t\t\t\t\t                          Dimensions: 8.40" L, 5.50" W, 0.80" H\t</td>
    </tr>
    <tr>
      <th>12</th>
      <td>\n\t                          ISBN-10: 1681374013\n\t                          ISBN-13: 9781681374017\n\t                          Publisher: New York Review of Books \n\t\t\t\t\t\t\t                          Publish Date: 11/12/2019 \n\t\t\t\t\t\t\t                          Dimensions: 7.10" L, 4.60" W, 0.50" H\t</td>
    </tr>
    <tr>
      <th>13</th>
      <td>\n\t                          ISBN-10: 0804463522\n\t                          ISBN-13: 9780804463522\n\t                          Publisher: Frederick Ungar \n\t\t\t\t\t\t\t                          Publish Date: 01/01/1986 \n\t\t\t\t\t\t\t                          Dimensions: 0.00" L, 0.00" W, 0.00" H\t</td>
    </tr>
    <tr>
      <th>14</th>
      <td>\n\t                          ISBN-10: 0140424768\n\t                          ISBN-13: 9780140424768\n\t                          Publisher: Penguin Group \n\t\t\t\t\t\t\t                          Publish Date: 08/14/2018 \n\t\t\t\t\t\t\t                          Dimensions: 7.70" L, 5.10" W, 1.10" H\t</td>
    </tr>
    <tr>
      <th>15</th>
      <td>\n\t                          ISBN-10: 0521186749\n\t                          ISBN-13: 9780521186742\n\t                          Publisher: Cambridge University Press \n\t\t\t\t\t\t\t                          Publish Date: 09/01/2011 \n\t\t\t\t\t\t\t                          Dimensions: 9.00" L, 6.10" W, 0.30" H\t</td>
    </tr>
    <tr>
      <th>16</th>
      <td>\n\t                          ISBN-10: 0525562435\n\t                          ISBN-13: 9780525562436\n\t                          Publisher: Vintage \n\t\t\t\t\t\t\t                          Publish Date: 12/03/2019 \n\t\t\t\t\t\t\t                          Dimensions: 7.90" L, 5.10" W, 0.80" H\t</td>
    </tr>
    <tr>
      <th>17</th>
      <td>\n\t                          ISBN-10: 0231187998\n\t                          ISBN-13: 9780231187992\n\t                          Publisher: Columbia University Press \n\t\t\t\t\t\t\t                          Publish Date: 04/06/2021 \n\t\t\t\t\t\t\t                          Dimensions: 8.90" L, 5.90" W, 0.70" H\t</td>
    </tr>
    <tr>
      <th>18</th>
      <td>\n\t                          ISBN-10: 1570621446\n\t                          ISBN-13: 9781570621444\n\t                          Publisher: Shambhala \n\t\t\t\t\t\t\t                          Publish Date: 10/15/1997 \n\t\t\t\t\t\t\t                          Dimensions: 8.89" L, 5.21" W, 0.53" H\t</td>
    </tr>
    <tr>
      <th>19</th>
      <td>\n\t                          ISBN-10: 9629965852\n\t                          ISBN-13: 9789629965853\n\t                          Publisher: New York Review of Books \n\t\t\t\t\t\t\t                          Publish Date: 01/13/2015 \n\t\t\t\t\t\t\t                          Dimensions: 8.40" L, 5.50" W, 0.80" H\t</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_asian_classics_to_clean_columns_split = df_asian_classics_to_clean_columns['0'].str.split("\n\t")
```


```python
df_asian_classics = df_asian_classics_to_clean_columns_split.to_list()
column_names = ['0','ISBN-10','ISBN-13','Publisher','Publish Date', 'Dimensions']
new_asian_classics_df = pd.DataFrame(df_asian_classics,columns=column_names)
```


```python
clean_asian_classics_df=new_asian_classics_df.drop(columns=['0','Dimensions'])
```


```python
clean_asian_classics_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ISBN-10</th>
      <th>ISBN-13</th>
      <th>Publisher</th>
      <th>Publish Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ISBN-10: 0140442820</td>
      <td>ISBN-13: 9780140442823</td>
      <td>Publisher: Penguin Group</td>
      <td>\t\t\t\t\t\t                          Publish Date: 12/05/1989</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ISBN-10: 9629968002</td>
      <td>ISBN-13: 9789629968007</td>
      <td>Publisher: New York Review of Books</td>
      <td>\t\t\t\t\t\t                          Publish Date: 03/14/2017</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ISBN-10: 014044971X</td>
      <td>ISBN-13: 9780140449716</td>
      <td>Publisher: Penguin Group</td>
      <td>\t\t\t\t\t\t                          Publish Date: 06/28/2005</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ISBN-10: 0241310873</td>
      <td>ISBN-13: 9780241310878</td>
      <td>Publisher: Penguin Group</td>
      <td>\t\t\t\t\t\t                          Publish Date: 07/14/2020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ISBN-10: 0143131273</td>
      <td>ISBN-13: 9780143131274</td>
      <td>Publisher: Penguin Group</td>
      <td>\t\t\t\t\t\t                          Publish Date: 02/12/2019</td>
    </tr>
  </tbody>
</table>
</div>




```python
html_chars = ["<tr>","\n","</th>","<th>","<td>","</td>",
              "</tr>",'\t']
for char in html_chars:
    clean_asian_classics_df['ISBN-10'] = clean_asian_classics_df['ISBN-10'].str.replace(char, ' ')
    clean_asian_classics_df['ISBN-13'] = clean_asian_classics_df['ISBN-13'].str.replace(char, ' ')
    clean_asian_classics_df['Publisher'] = clean_asian_classics_df['Publisher'].str.replace(char, ' ')
    clean_asian_classics_df['Publish Date'] = clean_asian_classics_df['Publish Date'].str.replace(char, ' ')
   
    
```


```python
pd.set_option("max_colwidth", 1000)
clean_asian_classics_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ISBN-10</th>
      <th>ISBN-13</th>
      <th>Publisher</th>
      <th>Publish Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ISBN-10: 0140442820</td>
      <td>ISBN-13: 9780140442823</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 12/05/1989</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ISBN-10: 9629968002</td>
      <td>ISBN-13: 9789629968007</td>
      <td>Publisher: New York Review of Books</td>
      <td>Publish Date: 03/14/2017</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ISBN-10: 014044971X</td>
      <td>ISBN-13: 9780140449716</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 06/28/2005</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ISBN-10: 0241310873</td>
      <td>ISBN-13: 9780241310878</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 07/14/2020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ISBN-10: 0143131273</td>
      <td>ISBN-13: 9780143131274</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 02/12/2019</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```


```python

```


```python
greek_roman_clean_for_combine_df = pd.read_csv('greek-roman-clean.csv')
```


```python
greek_roman_clean_for_combine_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>ISBN-10</th>
      <th>ISBN-13</th>
      <th>Publisher</th>
      <th>Publish Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>ISBN-10: 0141392649</td>
      <td>ISBN-13: 9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>115</th>
      <td>115</td>
      <td>ISBN-10: 0691150265</td>
      <td>ISBN-13: 9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>116</th>
      <td>116</td>
      <td>ISBN-10: 0691150265</td>
      <td>ISBN-13: 9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>117</th>
      <td>117</td>
      <td>ISBN-10: 0691150265</td>
      <td>ISBN-13: 9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>118</th>
      <td>118</td>
      <td>ISBN-10: 0691150265</td>
      <td>ISBN-13: 9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>119</th>
      <td>119</td>
      <td>ISBN-10: 0691150265</td>
      <td>ISBN-13: 9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
  </tbody>
</table>
<p>120 rows ?? 5 columns</p>
</div>




```python
greek_roman_clean_for_combine_df['ISBN-10'] = greek_roman_clean_for_combine_df['ISBN-10'].map(lambda x: x.lstrip('ISBN-10: '))

greek_roman_clean_for_combine_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>ISBN-10</th>
      <th>ISBN-13</th>
      <th>Publisher</th>
      <th>Publish Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>41392649</td>
      <td>9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>41392649</td>
      <td>9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>41392649</td>
      <td>9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>41392649</td>
      <td>9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>41392649</td>
      <td>9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>115</th>
      <td>115</td>
      <td>691150265</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>116</th>
      <td>116</td>
      <td>691150265</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>117</th>
      <td>117</td>
      <td>691150265</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>118</th>
      <td>118</td>
      <td>691150265</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>119</th>
      <td>119</td>
      <td>691150265</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
  </tbody>
</table>
<p>120 rows ?? 5 columns</p>
</div>




```python
greek_roman_clean_for_combine_df.dtypes
```




    Unnamed: 0       int64
    ISBN-10         object
    ISBN-13         object
    Publisher       object
    Publish Date    object
    dtype: object




```python

```


```python

```


```python
greek_roman_clean_for_combine_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>ISBN-10</th>
      <th>ISBN-13</th>
      <th>Publisher</th>
      <th>Publish Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>41392649</td>
      <td>9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>41392649</td>
      <td>9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>41392649</td>
      <td>9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>41392649</td>
      <td>9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>41392649</td>
      <td>9780141392646</td>
      <td>Publisher: Penguin Group</td>
      <td>Publish Date: 04/17/2018</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>115</th>
      <td>115</td>
      <td>691150265</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>116</th>
      <td>116</td>
      <td>691150265</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>117</th>
      <td>117</td>
      <td>691150265</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>118</th>
      <td>118</td>
      <td>691150265</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>119</th>
      <td>119</td>
      <td>691150265</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
  </tbody>
</table>
<p>120 rows ?? 5 columns</p>
</div>




```python

```


```python

```


```python
#https://stackoverflow.com/questions/18039057/python-pandas-error-tokenizing-data

books_df = pd.read_csv('Data/books.csv',error_bad_lines=False)
```

    b'Skipping line 3350: expected 12 fields, saw 13\nSkipping line 4704: expected 12 fields, saw 13\nSkipping line 5879: expected 12 fields, saw 13\nSkipping line 8981: expected 12 fields, saw 13\n'
    


```python
books_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>bookID</th>
      <th>title</th>
      <th>authors</th>
      <th>average_rating</th>
      <th>isbn</th>
      <th>isbn13</th>
      <th>language_code</th>
      <th>num_pages</th>
      <th>ratings_count</th>
      <th>text_reviews_count</th>
      <th>publication_date</th>
      <th>publisher</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Harry Potter and the Half-Blood Prince (Harry Potter  #6)</td>
      <td>J.K. Rowling/Mary GrandPr??</td>
      <td>4.57</td>
      <td>0439785960</td>
      <td>9780439785969</td>
      <td>eng</td>
      <td>652</td>
      <td>2095690</td>
      <td>27591</td>
      <td>9/16/2006</td>
      <td>Scholastic Inc.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Harry Potter and the Order of the Phoenix (Harry Potter  #5)</td>
      <td>J.K. Rowling/Mary GrandPr??</td>
      <td>4.49</td>
      <td>0439358078</td>
      <td>9780439358071</td>
      <td>eng</td>
      <td>870</td>
      <td>2153167</td>
      <td>29221</td>
      <td>9/1/2004</td>
      <td>Scholastic Inc.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Harry Potter and the Chamber of Secrets (Harry Potter  #2)</td>
      <td>J.K. Rowling</td>
      <td>4.42</td>
      <td>0439554896</td>
      <td>9780439554893</td>
      <td>eng</td>
      <td>352</td>
      <td>6333</td>
      <td>244</td>
      <td>11/1/2003</td>
      <td>Scholastic</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>Harry Potter and the Prisoner of Azkaban (Harry Potter  #3)</td>
      <td>J.K. Rowling/Mary GrandPr??</td>
      <td>4.56</td>
      <td>043965548X</td>
      <td>9780439655484</td>
      <td>eng</td>
      <td>435</td>
      <td>2339585</td>
      <td>36325</td>
      <td>5/1/2004</td>
      <td>Scholastic Inc.</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>Harry Potter Boxed Set  Books 1-5 (Harry Potter  #1-5)</td>
      <td>J.K. Rowling/Mary GrandPr??</td>
      <td>4.78</td>
      <td>0439682584</td>
      <td>9780439682589</td>
      <td>eng</td>
      <td>2690</td>
      <td>41428</td>
      <td>164</td>
      <td>9/13/2004</td>
      <td>Scholastic</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
#change column names
books_columns_df=books_df.rename(columns={"isbn": "ISBN-10", "isbn13": "ISBN-13"}) 
```


```python
books_columns_df.dtypes
```




    bookID                  int64
    title                  object
    authors                object
    average_rating        float64
    ISBN-10                object
    ISBN-13               float64
    language_code          object
      num_pages             int64
    ratings_count           int64
    text_reviews_count      int64
    publication_date       object
    publisher              object
    dtype: object




```python
books_columns_df['ISBN-10'] = books_columns_df['ISBN-10'].map(lambda x: x.lstrip('0'))
```


```python
books_columns_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>bookID</th>
      <th>title</th>
      <th>authors</th>
      <th>average_rating</th>
      <th>ISBN-10</th>
      <th>ISBN-13</th>
      <th>language_code</th>
      <th>num_pages</th>
      <th>ratings_count</th>
      <th>text_reviews_count</th>
      <th>publication_date</th>
      <th>publisher</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Harry Potter and the Half-Blood Prince (Harry Potter  #6)</td>
      <td>J.K. Rowling/Mary GrandPr??</td>
      <td>4.57</td>
      <td>439785960</td>
      <td>9.780440e+12</td>
      <td>eng</td>
      <td>652</td>
      <td>2095690</td>
      <td>27591</td>
      <td>9/16/2006</td>
      <td>Scholastic Inc.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Harry Potter and the Order of the Phoenix (Harry Potter  #5)</td>
      <td>J.K. Rowling/Mary GrandPr??</td>
      <td>4.49</td>
      <td>439358078</td>
      <td>9.780439e+12</td>
      <td>eng</td>
      <td>870</td>
      <td>2153167</td>
      <td>29221</td>
      <td>9/1/2004</td>
      <td>Scholastic Inc.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>Harry Potter and the Chamber of Secrets (Harry Potter  #2)</td>
      <td>J.K. Rowling</td>
      <td>4.42</td>
      <td>439554896</td>
      <td>9.780440e+12</td>
      <td>eng</td>
      <td>352</td>
      <td>6333</td>
      <td>244</td>
      <td>11/1/2003</td>
      <td>Scholastic</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>Harry Potter and the Prisoner of Azkaban (Harry Potter  #3)</td>
      <td>J.K. Rowling/Mary GrandPr??</td>
      <td>4.56</td>
      <td>43965548X</td>
      <td>9.780440e+12</td>
      <td>eng</td>
      <td>435</td>
      <td>2339585</td>
      <td>36325</td>
      <td>5/1/2004</td>
      <td>Scholastic Inc.</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8</td>
      <td>Harry Potter Boxed Set  Books 1-5 (Harry Potter  #1-5)</td>
      <td>J.K. Rowling/Mary GrandPr??</td>
      <td>4.78</td>
      <td>439682584</td>
      <td>9.780440e+12</td>
      <td>eng</td>
      <td>2690</td>
      <td>41428</td>
      <td>164</td>
      <td>9/13/2004</td>
      <td>Scholastic</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>11118</th>
      <td>45631</td>
      <td>Expelled from Eden: A William T. Vollmann Reader</td>
      <td>William T. Vollmann/Larry McCaffery/Michael Hemmingson</td>
      <td>4.06</td>
      <td>1560254416</td>
      <td>9.781560e+12</td>
      <td>eng</td>
      <td>512</td>
      <td>156</td>
      <td>20</td>
      <td>12/21/2004</td>
      <td>Da Capo Press</td>
    </tr>
    <tr>
      <th>11119</th>
      <td>45633</td>
      <td>You Bright and Risen Angels</td>
      <td>William T. Vollmann</td>
      <td>4.08</td>
      <td>140110879</td>
      <td>9.780140e+12</td>
      <td>eng</td>
      <td>635</td>
      <td>783</td>
      <td>56</td>
      <td>12/1/1988</td>
      <td>Penguin Books</td>
    </tr>
    <tr>
      <th>11120</th>
      <td>45634</td>
      <td>The Ice-Shirt (Seven Dreams #1)</td>
      <td>William T. Vollmann</td>
      <td>3.96</td>
      <td>140131965</td>
      <td>9.780140e+12</td>
      <td>eng</td>
      <td>415</td>
      <td>820</td>
      <td>95</td>
      <td>8/1/1993</td>
      <td>Penguin Books</td>
    </tr>
    <tr>
      <th>11121</th>
      <td>45639</td>
      <td>Poor People</td>
      <td>William T. Vollmann</td>
      <td>3.72</td>
      <td>60878827</td>
      <td>9.780061e+12</td>
      <td>eng</td>
      <td>434</td>
      <td>769</td>
      <td>139</td>
      <td>2/27/2007</td>
      <td>Ecco</td>
    </tr>
    <tr>
      <th>11122</th>
      <td>45641</td>
      <td>Las aventuras de Tom Sawyer</td>
      <td>Mark Twain</td>
      <td>3.91</td>
      <td>8497646983</td>
      <td>9.788498e+12</td>
      <td>spa</td>
      <td>272</td>
      <td>113</td>
      <td>12</td>
      <td>5/28/2006</td>
      <td>Edimat Libros</td>
    </tr>
  </tbody>
</table>
<p>11123 rows ?? 12 columns</p>
</div>




```python

```


```python

```


```python

```


```python
merged_df = books_columns_df.merge(greek_roman_clean_for_combine_df,on='ISBN-10',how='outer')
```


```python
merged_df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>bookID</th>
      <th>title</th>
      <th>authors</th>
      <th>average_rating</th>
      <th>ISBN-10</th>
      <th>ISBN-13_x</th>
      <th>language_code</th>
      <th>num_pages</th>
      <th>ratings_count</th>
      <th>text_reviews_count</th>
      <th>publication_date</th>
      <th>publisher</th>
      <th>Unnamed: 0</th>
      <th>ISBN-13_y</th>
      <th>Publisher</th>
      <th>Publish Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11238</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>691150265</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>115.0</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>11239</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>691150265</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>116.0</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>11240</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>691150265</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>117.0</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>11241</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>691150265</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>118.0</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
    <tr>
      <th>11242</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>691150265</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>119.0</td>
      <td>9780691150260</td>
      <td>Publisher: Princeton University Press</td>
      <td>Publish Date: 03/27/2011</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged_drop_nan_df=merged_df.dropna()
```


```python
merged_drop_nan_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>bookID</th>
      <th>title</th>
      <th>authors</th>
      <th>average_rating</th>
      <th>ISBN-10</th>
      <th>ISBN-13_x</th>
      <th>language_code</th>
      <th>num_pages</th>
      <th>ratings_count</th>
      <th>text_reviews_count</th>
      <th>publication_date</th>
      <th>publisher</th>
      <th>Unnamed: 0</th>
      <th>ISBN-13_y</th>
      <th>Publisher</th>
      <th>Publish Date</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>




```python
data1 = books_df.to_dict(orient = 'records')
data1
```




    [{'bookID': 1,
      'title': 'Harry Potter and the Half-Blood Prince (Harry Potter  #6)',
      'authors': 'J.K. Rowling/Mary GrandPr??',
      'average_rating': 4.57,
      'isbn': '0439785960',
      'isbn13': 9780439785969,
      'language_code': 'eng',
      '  num_pages': 652,
      'ratings_count': 2095690,
      'text_reviews_count': 27591,
      'publication_date': '9/16/2006',
      'publisher': 'Scholastic Inc.'},
     {'bookID': 2,
      'title': 'Harry Potter and the Order of the Phoenix (Harry Potter  #5)',
      'authors': 'J.K. Rowling/Mary GrandPr??',
      'average_rating': 4.49,
      'isbn': '0439358078',
      'isbn13': 9780439358071,
      'language_code': 'eng',
      '  num_pages': 870,
      'ratings_count': 2153167,
      'text_reviews_count': 29221,
      'publication_date': '9/1/2004',
      'publisher': 'Scholastic Inc.'},
     {'bookID': 4,
      'title': 'Harry Potter and the Chamber of Secrets (Harry Potter  #2)',
      'authors': 'J.K. Rowling',
      'average_rating': 4.42,
      'isbn': '0439554896',
      'isbn13': 9780439554893,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 6333,
      'text_reviews_count': 244,
      'publication_date': '11/1/2003',
      'publisher': 'Scholastic'},
     {'bookID': 5,
      'title': 'Harry Potter and the Prisoner of Azkaban (Harry Potter  #3)',
      'authors': 'J.K. Rowling/Mary GrandPr??',
      'average_rating': 4.56,
      'isbn': '043965548X',
      'isbn13': 9780439655484,
      'language_code': 'eng',
      '  num_pages': 435,
      'ratings_count': 2339585,
      'text_reviews_count': 36325,
      'publication_date': '5/1/2004',
      'publisher': 'Scholastic Inc.'},
     {'bookID': 8,
      'title': 'Harry Potter Boxed Set  Books 1-5 (Harry Potter  #1-5)',
      'authors': 'J.K. Rowling/Mary GrandPr??',
      'average_rating': 4.78,
      'isbn': '0439682584',
      'isbn13': 9780439682589,
      'language_code': 'eng',
      '  num_pages': 2690,
      'ratings_count': 41428,
      'text_reviews_count': 164,
      'publication_date': '9/13/2004',
      'publisher': 'Scholastic'},
     {'bookID': 9,
      'title': 'Unauthorized Harry Potter Book Seven News: "Half-Blood Prince" Analysis and Speculation',
      'authors': 'W. Frederick Zimmerman',
      'average_rating': 3.74,
      'isbn': '0976540606',
      'isbn13': 9780976540601,
      'language_code': 'en-US',
      '  num_pages': 152,
      'ratings_count': 19,
      'text_reviews_count': 1,
      'publication_date': '4/26/2005',
      'publisher': 'Nimble Books'},
     {'bookID': 10,
      'title': 'Harry Potter Collection (Harry Potter  #1-6)',
      'authors': 'J.K. Rowling',
      'average_rating': 4.73,
      'isbn': '0439827604',
      'isbn13': 9780439827607,
      'language_code': 'eng',
      '  num_pages': 3342,
      'ratings_count': 28242,
      'text_reviews_count': 808,
      'publication_date': '9/12/2005',
      'publisher': 'Scholastic'},
     {'bookID': 12,
      'title': "The Ultimate Hitchhiker's Guide: Five Complete Novels and One Story (Hitchhiker's Guide to the Galaxy  #1-5)",
      'authors': 'Douglas Adams',
      'average_rating': 4.38,
      'isbn': '0517226952',
      'isbn13': 9780517226957,
      'language_code': 'eng',
      '  num_pages': 815,
      'ratings_count': 3628,
      'text_reviews_count': 254,
      'publication_date': '11/1/2005',
      'publisher': 'Gramercy Books'},
     {'bookID': 13,
      'title': "The Ultimate Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy  #1-5)",
      'authors': 'Douglas Adams',
      'average_rating': 4.38,
      'isbn': '0345453743',
      'isbn13': 9780345453747,
      'language_code': 'eng',
      '  num_pages': 815,
      'ratings_count': 249558,
      'text_reviews_count': 4080,
      'publication_date': '4/30/2002',
      'publisher': 'Del Rey Books'},
     {'bookID': 14,
      'title': "The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy  #1)",
      'authors': 'Douglas Adams',
      'average_rating': 4.22,
      'isbn': '1400052920',
      'isbn13': 9781400052929,
      'language_code': 'eng',
      '  num_pages': 215,
      'ratings_count': 4930,
      'text_reviews_count': 460,
      'publication_date': '8/3/2004',
      'publisher': 'Crown'},
     {'bookID': 16,
      'title': "The Hitchhiker's Guide to the Galaxy (Hitchhiker's Guide to the Galaxy  #1)",
      'authors': 'Douglas Adams/Stephen Fry',
      'average_rating': 4.22,
      'isbn': '0739322206',
      'isbn13': 9780739322208,
      'language_code': 'eng',
      '  num_pages': 6,
      'ratings_count': 1266,
      'text_reviews_count': 253,
      'publication_date': '3/23/2005',
      'publisher': 'Random House Audio'},
     {'bookID': 18,
      'title': "The Ultimate Hitchhiker's Guide (Hitchhiker's Guide to the Galaxy  #1-5)",
      'authors': 'Douglas Adams',
      'average_rating': 4.38,
      'isbn': '0517149257',
      'isbn13': 9780517149256,
      'language_code': 'eng',
      '  num_pages': 815,
      'ratings_count': 2877,
      'text_reviews_count': 195,
      'publication_date': '1/17/1996',
      'publisher': 'Wings Books'},
     {'bookID': 21,
      'title': 'A Short History of Nearly Everything',
      'authors': 'Bill Bryson',
      'average_rating': 4.21,
      'isbn': '076790818X',
      'isbn13': 9780767908184,
      'language_code': 'eng',
      '  num_pages': 544,
      'ratings_count': 248558,
      'text_reviews_count': 9396,
      'publication_date': '9/14/2004',
      'publisher': 'Broadway Books'},
     {'bookID': 22,
      'title': "Bill Bryson's African Diary",
      'authors': 'Bill Bryson',
      'average_rating': 3.44,
      'isbn': '0767915062',
      'isbn13': 9780767915069,
      'language_code': 'eng',
      '  num_pages': 55,
      'ratings_count': 7270,
      'text_reviews_count': 499,
      'publication_date': '12/3/2002',
      'publisher': 'Broadway Books'},
     {'bookID': 23,
      'title': "Bryson's Dictionary of Troublesome Words: A Writer's Guide to Getting It Right",
      'authors': 'Bill Bryson',
      'average_rating': 3.87,
      'isbn': '0767910435',
      'isbn13': 9780767910439,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 2088,
      'text_reviews_count': 131,
      'publication_date': '9/14/2004',
      'publisher': 'Broadway Books'},
     {'bookID': 24,
      'title': 'In a Sunburned Country',
      'authors': 'Bill Bryson',
      'average_rating': 4.07,
      'isbn': '0767903862',
      'isbn13': 9780767903868,
      'language_code': 'eng',
      '  num_pages': 335,
      'ratings_count': 72451,
      'text_reviews_count': 4245,
      'publication_date': '5/15/2001',
      'publisher': 'Broadway Books'},
     {'bookID': 25,
      'title': "I'm a Stranger Here Myself: Notes on Returning to America After Twenty Years Away",
      'authors': 'Bill Bryson',
      'average_rating': 3.9,
      'isbn': '076790382X',
      'isbn13': 9780767903820,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 49240,
      'text_reviews_count': 2211,
      'publication_date': '6/28/2000',
      'publisher': 'Broadway Books'},
     {'bookID': 26,
      'title': 'The Lost Continent: Travels in Small Town America',
      'authors': 'Bill Bryson',
      'average_rating': 3.83,
      'isbn': '0060920084',
      'isbn13': 9780060920081,
      'language_code': 'eng',
      '  num_pages': 299,
      'ratings_count': 45712,
      'text_reviews_count': 2257,
      'publication_date': '8/28/1990',
      'publisher': 'William Morrow Paperbacks'},
     {'bookID': 27,
      'title': 'Neither Here nor There: Travels in Europe',
      'authors': 'Bill Bryson',
      'average_rating': 3.86,
      'isbn': '0380713802',
      'isbn13': 9780380713806,
      'language_code': 'eng',
      '  num_pages': 254,
      'ratings_count': 48701,
      'text_reviews_count': 2238,
      'publication_date': '3/28/1993',
      'publisher': 'William Morrow Paperbacks'},
     {'bookID': 28,
      'title': 'Notes from a Small Island',
      'authors': 'Bill Bryson',
      'average_rating': 3.91,
      'isbn': '0380727501',
      'isbn13': 9780380727506,
      'language_code': 'eng',
      '  num_pages': 324,
      'ratings_count': 80609,
      'text_reviews_count': 3301,
      'publication_date': '5/28/1997',
      'publisher': 'William Morrow Paperbacks'},
     {'bookID': 29,
      'title': 'The Mother Tongue: English and How It Got That Way',
      'authors': 'Bill Bryson',
      'average_rating': 3.93,
      'isbn': '0380715430',
      'isbn13': 9780380715435,
      'language_code': 'eng',
      '  num_pages': 270,
      'ratings_count': 28489,
      'text_reviews_count': 2085,
      'publication_date': '9/28/1991',
      'publisher': 'William Morrow Paperbacks'},
     {'bookID': 30,
      'title': 'J.R.R. Tolkien 4-Book Boxed Set: The Hobbit and The Lord of the Rings',
      'authors': 'J.R.R. Tolkien',
      'average_rating': 4.59,
      'isbn': '0345538374',
      'isbn13': 9780345538376,
      'language_code': 'eng',
      '  num_pages': 1728,
      'ratings_count': 101233,
      'text_reviews_count': 1550,
      'publication_date': '9/25/2012',
      'publisher': 'Ballantine Books'},
     {'bookID': 31,
      'title': 'The Lord of the Rings (The Lord of the Rings  #1-3)',
      'authors': 'J.R.R. Tolkien',
      'average_rating': 4.5,
      'isbn': '0618517650',
      'isbn13': 9780618517657,
      'language_code': 'eng',
      '  num_pages': 1184,
      'ratings_count': 1710,
      'text_reviews_count': 91,
      'publication_date': '10/21/2004',
      'publisher': 'Houghton Mifflin Harcourt'},
     {'bookID': 34,
      'title': 'The Fellowship of the Ring (The Lord of the Rings  #1)',
      'authors': 'J.R.R. Tolkien',
      'average_rating': 4.36,
      'isbn': '0618346252',
      'isbn13': 9780618346257,
      'language_code': 'eng',
      '  num_pages': 398,
      'ratings_count': 2128944,
      'text_reviews_count': 13670,
      'publication_date': '9/5/2003',
      'publisher': 'Houghton Mifflin Harcourt'},
     {'bookID': 35,
      'title': 'The Lord of the Rings (The Lord of the Rings  #1-3)',
      'authors': 'J.R.R. Tolkien/Alan  Lee',
      'average_rating': 4.5,
      'isbn': '0618260587',
      'isbn13': 9780618260584,
      'language_code': 'en-US',
      '  num_pages': 1216,
      'ratings_count': 1618,
      'text_reviews_count': 140,
      'publication_date': '10/1/2002',
      'publisher': 'Houghton Mifflin Harcourt'},
     {'bookID': 36,
      'title': 'The Lord of the Rings: Weapons and Warfare',
      'authors': 'Chris   Smith/Christopher  Lee/Richard Taylor',
      'average_rating': 4.53,
      'isbn': '0618391002',
      'isbn13': 9780618391004,
      'language_code': 'eng',
      '  num_pages': 218,
      'ratings_count': 19822,
      'text_reviews_count': 46,
      'publication_date': '11/5/2003',
      'publisher': 'Houghton Mifflin Harcourt'},
     {'bookID': 37,
      'title': 'The Lord of the Rings: Complete Visual Companion',
      'authors': 'Jude Fisher',
      'average_rating': 4.5,
      'isbn': '0618510826',
      'isbn13': 9780618510825,
      'language_code': 'eng',
      '  num_pages': 224,
      'ratings_count': 359,
      'text_reviews_count': 6,
      'publication_date': '11/15/2004',
      'publisher': 'Houghton Mifflin Harcourt'},
     {'bookID': 45,
      'title': 'Agile Web Development with Rails: A Pragmatic Guide',
      'authors': 'Dave Thomas/David Heinemeier Hansson/Leon Breedt/Mike Clark/Thomas  Fuchs/Andreas  Schwarz',
      'average_rating': 3.84,
      'isbn': '097669400X',
      'isbn13': 9780976694007,
      'language_code': 'eng',
      '  num_pages': 558,
      'ratings_count': 1430,
      'text_reviews_count': 59,
      'publication_date': '7/28/2005',
      'publisher': 'Pragmatic Bookshelf'},
     {'bookID': 50,
      'title': "Hatchet (Brian's Saga  #1)",
      'authors': 'Gary Paulsen',
      'average_rating': 3.72,
      'isbn': '0689840926',
      'isbn13': 9780689840920,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 270244,
      'text_reviews_count': 12017,
      'publication_date': '4/1/2000',
      'publisher': 'Atheneum Books for Young Readers: Richard Jackson Books'},
     {'bookID': 51,
      'title': 'Hatchet: A Guide for Using "Hatchet" in the Classroom',
      'authors': 'Donna Ickes/Edward Sciranko/Keith Vasconcelles',
      'average_rating': 4.0,
      'isbn': '1557344493',
      'isbn13': 9781557344496,
      'language_code': 'eng',
      '  num_pages': 48,
      'ratings_count': 36,
      'text_reviews_count': 2,
      'publication_date': '8/28/1994',
      'publisher': 'Teacher Created Resources'},
     {'bookID': 53,
      'title': 'Guts: The True Stories behind Hatchet and the Brian Books',
      'authors': 'Gary Paulsen',
      'average_rating': 3.88,
      'isbn': '0385326505',
      'isbn13': 9780385326506,
      'language_code': 'eng',
      '  num_pages': 144,
      'ratings_count': 2067,
      'text_reviews_count': 334,
      'publication_date': '1/23/2001',
      'publisher': 'Delacorte Press'},
     {'bookID': 54,
      'title': 'Molly Hatchet - 5 of the Best',
      'authors': 'Molly Hatchet',
      'average_rating': 4.33,
      'isbn': '1575606240',
      'isbn13': 9781575606248,
      'language_code': 'eng',
      '  num_pages': 56,
      'ratings_count': 6,
      'text_reviews_count': 0,
      'publication_date': '6/10/2003',
      'publisher': 'Cherry Lane Music Company'},
     {'bookID': 55,
      'title': 'Hatchet Jobs: Writings on Contemporary Fiction',
      'authors': 'Dale Peck',
      'average_rating': 3.45,
      'isbn': '1595580271',
      'isbn13': 9781595580276,
      'language_code': 'en-US',
      '  num_pages': 228,
      'ratings_count': 99,
      'text_reviews_count': 16,
      'publication_date': '11/1/2005',
      'publisher': 'The New Press'},
     {'bookID': 57,
      'title': 'A Changeling for All Seasons (Changeling Seasons #1)',
      'authors': 'Angela Knight/Sahara Kelly/Judy Mays/Marteeka Karland/Kate Douglas/Shelby Morgen/Lacey Savage/Kate Hill/Willa Okati',
      'average_rating': 3.76,
      'isbn': '1595962808',
      'isbn13': 9781595962805,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 167,
      'text_reviews_count': 4,
      'publication_date': '11/1/2005',
      'publisher': 'Changeling Press'},
     {'bookID': 58,
      'title': 'Changeling (Changeling  #1)',
      'authors': 'Delia Sherman',
      'average_rating': 3.6,
      'isbn': '0670059676',
      'isbn13': 9780670059676,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 978,
      'text_reviews_count': 111,
      'publication_date': '8/17/2006',
      'publisher': 'Viking Juvenile'},
     {'bookID': 59,
      'title': 'The Changeling Sea',
      'authors': 'Patricia A. McKillip',
      'average_rating': 4.06,
      'isbn': '0141312629',
      'isbn13': 9780141312620,
      'language_code': 'eng',
      '  num_pages': 137,
      'ratings_count': 4454,
      'text_reviews_count': 302,
      'publication_date': '4/14/2003',
      'publisher': 'Firebird'},
     {'bookID': 61,
      'title': 'The Changeling',
      'authors': 'Zilpha Keatley Snyder',
      'average_rating': 4.17,
      'isbn': '0595321801',
      'isbn13': 9780595321803,
      'language_code': 'eng',
      '  num_pages': 228,
      'ratings_count': 1176,
      'text_reviews_count': 96,
      'publication_date': '6/8/2004',
      'publisher': 'iUniverse'},
     {'bookID': 63,
      'title': 'The Changeling',
      'authors': 'Kate Horsley',
      'average_rating': 3.55,
      'isbn': '1590301943',
      'isbn13': 9781590301944,
      'language_code': 'eng',
      '  num_pages': 339,
      'ratings_count': 301,
      'text_reviews_count': 43,
      'publication_date': '4/12/2005',
      'publisher': 'Shambhala'},
     {'bookID': 66,
      'title': 'The Changeling (Daughters of England  #15)',
      'authors': 'Philippa Carr',
      'average_rating': 3.98,
      'isbn': '0449146979',
      'isbn13': 9780449146972,
      'language_code': 'eng',
      '  num_pages': 369,
      'ratings_count': 345,
      'text_reviews_count': 12,
      'publication_date': '8/28/1990',
      'publisher': 'Ivy Books'},
     {'bookID': 67,
      'title': 'The Known World',
      'authors': 'Edward P. Jones',
      'average_rating': 3.83,
      'isbn': '0061159174',
      'isbn13': 9780061159176,
      'language_code': 'eng',
      '  num_pages': 388,
      'ratings_count': 29686,
      'text_reviews_count': 2626,
      'publication_date': '8/29/2006',
      'publisher': 'Amistad'},
     {'bookID': 68,
      'title': 'The Known World',
      'authors': 'Edward P. Jones/Kevin R. Free',
      'average_rating': 3.83,
      'isbn': '006076273X',
      'isbn13': 9780060762735,
      'language_code': 'en-US',
      '  num_pages': 14,
      'ratings_count': 55,
      'text_reviews_count': 12,
      'publication_date': '6/15/2004',
      'publisher': 'HarperAudio'},
     {'bookID': 69,
      'title': 'The Known World',
      'authors': 'Edward P. Jones',
      'average_rating': 3.83,
      'isbn': '0060749911',
      'isbn13': 9780060749910,
      'language_code': 'eng',
      '  num_pages': 576,
      'ratings_count': 22,
      'text_reviews_count': 3,
      'publication_date': '6/15/2004',
      'publisher': 'Harper'},
     {'bookID': 71,
      'title': 'Traders  Guns & Money: Knowns and Unknowns in the Dazzling World of Derivatives',
      'authors': 'Satyajit Das',
      'average_rating': 3.83,
      'isbn': '0273704745',
      'isbn13': 9780273704744,
      'language_code': 'eng',
      '  num_pages': 334,
      'ratings_count': 1456,
      'text_reviews_count': 82,
      'publication_date': '5/15/2006',
      'publisher': 'FT Press'},
     {'bookID': 72,
      'title': 'Artesia: Adventures in the Known World',
      'authors': 'Mark Smylie',
      'average_rating': 4.13,
      'isbn': '1932386106',
      'isbn13': 9781932386103,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 52,
      'text_reviews_count': 4,
      'publication_date': '12/14/2005',
      'publisher': 'Archaia'},
     {'bookID': 74,
      'title': 'The John McPhee Reader (John McPhee Reader  #1)',
      'authors': 'John McPhee/William Howarth',
      'average_rating': 4.42,
      'isbn': '0374517193',
      'isbn13': 9780374517199,
      'language_code': 'eng',
      '  num_pages': 416,
      'ratings_count': 562,
      'text_reviews_count': 37,
      'publication_date': '6/1/1982',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 75,
      'title': 'Uncommon Carriers',
      'authors': 'John McPhee',
      'average_rating': 3.95,
      'isbn': '0374280398',
      'isbn13': 9780374280390,
      'language_code': 'en-US',
      '  num_pages': 248,
      'ratings_count': 1630,
      'text_reviews_count': 203,
      'publication_date': '5/16/2006',
      'publisher': 'Farrar Straus Giroux'},
     {'bookID': 76,
      'title': 'Heirs of General Practice',
      'authors': 'John McPhee',
      'average_rating': 4.17,
      'isbn': '0374519749',
      'isbn13': 9780374519742,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 268,
      'text_reviews_count': 22,
      'publication_date': '4/1/1986',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 77,
      'title': 'The Control of Nature',
      'authors': 'John McPhee',
      'average_rating': 4.24,
      'isbn': '0374522596',
      'isbn13': 9780374522599,
      'language_code': 'en-US',
      '  num_pages': 288,
      'ratings_count': 3498,
      'text_reviews_count': 305,
      'publication_date': '9/1/1990',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 78,
      'title': 'Annals of the Former World',
      'authors': 'John McPhee',
      'average_rating': 4.34,
      'isbn': '0374518734',
      'isbn13': 9780374518738,
      'language_code': 'eng',
      '  num_pages': 720,
      'ratings_count': 3115,
      'text_reviews_count': 228,
      'publication_date': '1/6/1999',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 79,
      'title': 'Coming Into the Country',
      'authors': 'John McPhee',
      'average_rating': 4.22,
      'isbn': '0374522871',
      'isbn13': 9780374522872,
      'language_code': 'eng',
      '  num_pages': 448,
      'ratings_count': 5704,
      'text_reviews_count': 261,
      'publication_date': '4/1/1991',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 80,
      'title': 'La Place de la Concorde Suisse',
      'authors': 'John McPhee',
      'average_rating': 3.92,
      'isbn': '0374519323',
      'isbn13': 9780374519322,
      'language_code': 'fre',
      '  num_pages': 160,
      'ratings_count': 698,
      'text_reviews_count': 52,
      'publication_date': '4/1/1994',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 81,
      'title': 'Giving Good Weight',
      'authors': 'John McPhee',
      'average_rating': 4.23,
      'isbn': '0374516006',
      'isbn13': 9780374516000,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 542,
      'text_reviews_count': 36,
      'publication_date': '4/1/1994',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 83,
      'title': 'Rising from the Plains',
      'authors': 'John McPhee',
      'average_rating': 4.23,
      'isbn': '0374520658',
      'isbn13': 9780374520656,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 1341,
      'text_reviews_count': 98,
      'publication_date': '11/1/1987',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 85,
      'title': 'The Heidi Chronicles',
      'authors': 'Wendy Wasserstein',
      'average_rating': 3.75,
      'isbn': '0822205106',
      'isbn13': 9780822205104,
      'language_code': 'eng',
      '  num_pages': 81,
      'ratings_count': 1423,
      'text_reviews_count': 70,
      'publication_date': '3/1/2002',
      'publisher': 'Dramatists Play Service'},
     {'bookID': 86,
      'title': "The Heidi Chronicles: Uncommon Women and Others & Isn't It Romantic",
      'authors': 'Wendy Wasserstein',
      'average_rating': 3.84,
      'isbn': '0679734996',
      'isbn13': 9780679734994,
      'language_code': 'eng',
      '  num_pages': 249,
      'ratings_count': 2766,
      'text_reviews_count': 64,
      'publication_date': '7/2/1991',
      'publisher': 'Vintage'},
     {'bookID': 89,
      'title': 'Active Literacy Across the Curriculum: Strategies for Reading  Writing  Speaking  and Listening',
      'authors': 'Heidi Hayes Jacobs',
      'average_rating': 3.94,
      'isbn': '1596670231',
      'isbn13': 9781596670235,
      'language_code': 'eng',
      '  num_pages': 138,
      'ratings_count': 31,
      'text_reviews_count': 1,
      'publication_date': '3/29/2006',
      'publisher': 'Routledge'},
     {'bookID': 90,
      'title': 'Simply Beautiful Beaded Jewelry',
      'authors': 'Heidi Boyd',
      'average_rating': 3.77,
      'isbn': '1581807740',
      'isbn13': 9781581807745,
      'language_code': 'en-US',
      '  num_pages': 128,
      'ratings_count': 62,
      'text_reviews_count': 4,
      'publication_date': '3/14/2006',
      'publisher': 'North Light Books'},
     {'bookID': 91,
      'title': "Always Enough: God's Miraculous Provision Among the Poorest Children on Earth",
      'authors': 'Heidi Baker/Rolland Baker',
      'average_rating': 4.46,
      'isbn': '0800793617',
      'isbn13': 9780800793616,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 860,
      'text_reviews_count': 53,
      'publication_date': '9/1/2003',
      'publisher': 'Chosen Books'},
     {'bookID': 92,
      'title': 'Mapping the Big Picture: Integrating Curriculum & Assessment K-12',
      'authors': 'Heidi Hayes Jacobs',
      'average_rating': 3.68,
      'isbn': '0871202867',
      'isbn13': 9780871202864,
      'language_code': 'en-US',
      '  num_pages': 108,
      'ratings_count': 77,
      'text_reviews_count': 2,
      'publication_date': '1/28/1997',
      'publisher': 'Association for Supervision & Curriculum Development'},
     {'bookID': 93,
      'title': 'Heidi (Heidi  #1-2)',
      'authors': 'Johanna Spyri/Beverly Cleary/Angelo  Rinaldi',
      'average_rating': 3.99,
      'isbn': '0753454947',
      'isbn13': 9780753454947,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 153317,
      'text_reviews_count': 2257,
      'publication_date': '11/15/2002',
      'publisher': 'Kingfisher'},
     {'bookID': 94,
      'title': 'Getting Results with Curriculum Mapping',
      'authors': 'Heidi Hayes Jacobs',
      'average_rating': 3.25,
      'isbn': '0871209993',
      'isbn13': 9780871209993,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 55,
      'text_reviews_count': 5,
      'publication_date': '11/15/2004',
      'publisher': 'ASCD'},
     {'bookID': 96,
      'title': "There's Always Enough: The Miraculous Move of God in Mozambique",
      'authors': 'Rolland Baker/Heidi Baker',
      'average_rating': 4.46,
      'isbn': '1852402873',
      'isbn13': 9781852402877,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 34,
      'text_reviews_count': 6,
      'publication_date': '4/28/2003',
      'publisher': 'Sovereign World'},
     {'bookID': 98,
      'title': 'What to Expect the First Year (What to Expect)',
      'authors': 'Heidi Murkoff/Sharon Mazel/Arlene Eisenberg/Sandee Hathaway/Mark D. Widome',
      'average_rating': 3.89,
      'isbn': '0761129588',
      'isbn13': 9780761129585,
      'language_code': 'eng',
      '  num_pages': 832,
      'ratings_count': 11797,
      'text_reviews_count': 659,
      'publication_date': '10/16/2003',
      'publisher': 'Workman Publishing Company'},
     {'bookID': 99,
      'title': "The Player's Handbook: The Ultimate Guide on Dating and Relationships",
      'authors': 'Heidi Fleiss/Libby Keatinge',
      'average_rating': 3.82,
      'isbn': '0972016414',
      'isbn13': 9780972016414,
      'language_code': 'eng',
      '  num_pages': 123,
      'ratings_count': 34,
      'text_reviews_count': 8,
      'publication_date': '5/10/2004',
      'publisher': 'One Hour Entertainment'},
     {'bookID': 100,
      'title': 'Simply Beautiful Beading: 53 Quick and Easy Projects',
      'authors': 'Heidi Boyd',
      'average_rating': 3.78,
      'isbn': '1581805632',
      'isbn13': 9781581805635,
      'language_code': 'en-US',
      '  num_pages': 128,
      'ratings_count': 78,
      'text_reviews_count': 4,
      'publication_date': '8/19/2004',
      'publisher': 'North Light Books'},
     {'bookID': 103,
      'title': 'God Emperor of Dune (Dune Chronicles  #4)',
      'authors': 'Frank Herbert',
      'average_rating': 3.84,
      'isbn': '0441294677',
      'isbn13': 9780441294671,
      'language_code': 'eng',
      '  num_pages': 423,
      'ratings_count': 2785,
      'text_reviews_count': 166,
      'publication_date': '6/15/1987',
      'publisher': 'Ace Books'},
     {'bookID': 105,
      'title': 'Chapterhouse: Dune (Dune Chronicles #6)',
      'authors': 'Frank Herbert',
      'average_rating': 3.91,
      'isbn': '0441102670',
      'isbn13': 9780441102679,
      'language_code': 'eng',
      '  num_pages': 436,
      'ratings_count': 38778,
      'text_reviews_count': 568,
      'publication_date': '7/1/1987',
      'publisher': 'Ace Books'},
     {'bookID': 106,
      'title': 'Dune Messiah (Dune Chronicles #2)',
      'authors': 'Frank Herbert',
      'average_rating': 3.88,
      'isbn': '0441172695',
      'isbn13': 9780441172696,
      'language_code': 'eng',
      '  num_pages': 331,
      'ratings_count': 97494,
      'text_reviews_count': 2359,
      'publication_date': '7/15/1987',
      'publisher': 'Ace Books'},
     {'bookID': 107,
      'title': 'Dreamer of Dune: The Biography of Frank Herbert',
      'authors': 'Brian Herbert',
      'average_rating': 4.01,
      'isbn': '0765306476',
      'isbn13': 9780765306470,
      'language_code': 'en-US',
      '  num_pages': 592,
      'ratings_count': 784,
      'text_reviews_count': 21,
      'publication_date': '7/1/2004',
      'publisher': 'Tor Books'},
     {'bookID': 109,
      'title': 'Heretics of Dune (Dune Chronicles  #5)',
      'authors': 'Frank Herbert',
      'average_rating': 3.86,
      'isbn': '0399128980',
      'isbn13': 9780399128981,
      'language_code': 'eng',
      '  num_pages': 480,
      'ratings_count': 272,
      'text_reviews_count': 20,
      'publication_date': '4/16/1984',
      'publisher': 'Putnam'},
     {'bookID': 110,
      'title': 'The Road to Dune',
      'authors': 'Frank Herbert/Brian Herbert/Kevin J. Anderson',
      'average_rating': 3.88,
      'isbn': '0765353709',
      'isbn13': 9780765353702,
      'language_code': 'eng',
      '  num_pages': 426,
      'ratings_count': 4789,
      'text_reviews_count': 83,
      'publication_date': '8/29/2006',
      'publisher': 'Tor Science Fiction'},
     {'bookID': 117,
      'title': 'Heretics of Dune (Dune Chronicles #5)',
      'authors': 'Frank Herbert',
      'average_rating': 3.86,
      'isbn': '0441328008',
      'isbn13': 9780441328000,
      'language_code': 'eng',
      '  num_pages': 471,
      'ratings_count': 45388,
      'text_reviews_count': 644,
      'publication_date': '8/15/1987',
      'publisher': 'Ace Books'},
     {'bookID': 119,
      'title': 'The Lord of the Rings: The Art of the Fellowship of the Ring',
      'authors': 'Gary Russell',
      'average_rating': 4.59,
      'isbn': '0618212906',
      'isbn13': 9780618212903,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 26153,
      'text_reviews_count': 102,
      'publication_date': '6/12/2002',
      'publisher': 'Houghton Mifflin Harcourt'},
     {'bookID': 122,
      'title': 'The Power of One (The Power of One  #1)',
      'authors': 'Bryce Courtenay',
      'average_rating': 4.35,
      'isbn': '034541005X',
      'isbn13': 9780345410054,
      'language_code': 'eng',
      '  num_pages': 544,
      'ratings_count': 69167,
      'text_reviews_count': 4551,
      'publication_date': '9/29/1996',
      'publisher': 'Ballantine Books'},
     {'bookID': 123,
      'title': 'The Power of One (The Power of One  #1)',
      'authors': 'Bryce Courtenay',
      'average_rating': 4.35,
      'isbn': '0385732546',
      'isbn13': 9780385732543,
      'language_code': 'eng',
      '  num_pages': 291,
      'ratings_count': 45,
      'text_reviews_count': 13,
      'publication_date': '9/13/2005',
      'publisher': 'Delacorte Books for Young Readers'},
     {'bookID': 129,
      'title': 'The Power of One: One Person  One Rule  One Month',
      'authors': 'John C. Maxwell/Stephen R. Graves/Thomas G. Addington',
      'average_rating': 4.28,
      'isbn': '0785260056',
      'isbn13': 9780785260059,
      'language_code': 'en-US',
      '  num_pages': 256,
      'ratings_count': 16,
      'text_reviews_count': 1,
      'publication_date': '11/1/2004',
      'publisher': 'Thomas Nelson'},
     {'bookID': 130,
      'title': 'Power of an Hour: Business and Life Mastery in One Hour a Week',
      'authors': 'Dave Lakhani',
      'average_rating': 3.34,
      'isbn': '0471780936',
      'isbn13': 9780471780939,
      'language_code': 'eng',
      '  num_pages': 205,
      'ratings_count': 174,
      'text_reviews_count': 16,
      'publication_date': '5/19/2006',
      'publisher': 'Wiley'},
     {'bookID': 131,
      'title': 'The Power of One: The Solo Play for Playwrights  Actors  and Directors',
      'authors': 'Louis E. Catron',
      'average_rating': 3.67,
      'isbn': '0325001537',
      'isbn13': 9780325001531,
      'language_code': 'eng',
      '  num_pages': 240,
      'ratings_count': 10,
      'text_reviews_count': 0,
      'publication_date': '2/7/2000',
      'publisher': 'Heinemann Drama'},
     {'bookID': 132,
      'title': 'How to Buy  Sell & Profit on eBay: Kick-Start Your Home-Based Business in Just Thirty Days',
      'authors': 'Adam Ginsberg',
      'average_rating': 3.48,
      'isbn': '006076287X',
      'isbn13': 9780060762872,
      'language_code': 'eng',
      '  num_pages': 336,
      'ratings_count': 76,
      'text_reviews_count': 9,
      'publication_date': '5/3/2005',
      'publisher': 'William Morrow Paperbacks'},
     {'bookID': 133,
      'title': 'eBay for Dummies',
      'authors': 'Marsha Collier',
      'average_rating': 3.5,
      'isbn': '0470045299',
      'isbn13': 9780470045299,
      'language_code': 'eng',
      '  num_pages': 386,
      'ratings_count': 111,
      'text_reviews_count': 9,
      'publication_date': '10/30/2006',
      'publisher': 'Wiley'},
     {'bookID': 135,
      'title': 'What to Sell on ebay and Where to Get It: The Definitive Guide to Product Sourcing for eBay and Beyond',
      'authors': 'Chris Malta/Lisa Suttora',
      'average_rating': 3.62,
      'isbn': '0072262788',
      'isbn13': 9780072262780,
      'language_code': 'eng',
      '  num_pages': 260,
      'ratings_count': 24,
      'text_reviews_count': 0,
      'publication_date': '1/24/2006',
      'publisher': 'McGraw-Hill'},
     {'bookID': 137,
      'title': 'Starting an eBay Business for Dummies',
      'authors': 'Marsha Collier',
      'average_rating': 3.55,
      'isbn': '0764569244',
      'isbn13': 9780764569241,
      'language_code': 'eng',
      '  num_pages': 384,
      'ratings_count': 55,
      'text_reviews_count': 4,
      'publication_date': '9/17/2004',
      'publisher': 'Wiley'},
     {'bookID': 138,
      'title': 'eBay: Top 100 Simplified Tips & Tricks',
      'authors': 'Julia Wilkinson',
      'average_rating': 4.27,
      'isbn': '0471933821',
      'isbn13': 9780471933823,
      'language_code': 'eng',
      '  num_pages': 260,
      'ratings_count': 9,
      'text_reviews_count': 0,
      'publication_date': '6/6/2006',
      'publisher': 'Wiley'},
     {'bookID': 139,
      'title': 'ebay Timesaving Techniques for Dummies',
      'authors': 'Marsha Collier',
      'average_rating': 3.39,
      'isbn': '0764559915',
      'isbn13': 9780764559914,
      'language_code': 'en-US',
      '  num_pages': 391,
      'ratings_count': 22,
      'text_reviews_count': 1,
      'publication_date': '5/31/2004',
      'publisher': 'Wiley'},
     {'bookID': 140,
      'title': 'eBay Business All-in-One Desk Reference for Dummies',
      'authors': 'Marsha Collier',
      'average_rating': 3.89,
      'isbn': '0764584383',
      'isbn13': 9780764584381,
      'language_code': 'en-US',
      '  num_pages': 864,
      'ratings_count': 17,
      'text_reviews_count': 3,
      'publication_date': '4/25/2005',
      'publisher': 'Wiley'},
     {'bookID': 141,
      'title': 'Ruby Cookbook',
      'authors': 'Lucas Carlson/Leonard Richardson',
      'average_rating': 3.84,
      'isbn': '0596523696',
      'isbn13': 9780596523695,
      'language_code': 'eng',
      '  num_pages': 873,
      'ratings_count': 166,
      'text_reviews_count': 4,
      'publication_date': '7/29/2006',
      'publisher': "O'Reilly Media"},
     {'bookID': 142,
      'title': "Ruby Ann's Down Home Trailer Park Cookbook",
      'authors': 'Ruby Ann Boxcar',
      'average_rating': 4.12,
      'isbn': '0806523492',
      'isbn13': 9780806523491,
      'language_code': 'eng',
      '  num_pages': 240,
      'ratings_count': 50,
      'text_reviews_count': 5,
      'publication_date': '5/3/2005',
      'publisher': 'Citadel'},
     {'bookID': 144,
      'title': "Ruby Ann's Down Home Trailer Park BBQin' Cookbook",
      'authors': 'Ruby Ann Boxcar',
      'average_rating': 4.08,
      'isbn': '0806525363',
      'isbn13': 9780806525365,
      'language_code': 'eng',
      '  num_pages': 206,
      'ratings_count': 13,
      'text_reviews_count': 2,
      'publication_date': '5/3/2005',
      'publisher': 'Citadel'},
     {'bookID': 147,
      'title': 'Rails Cookbook: Recipes for Rapid Web Development with Ruby',
      'authors': 'Rob Orsini',
      'average_rating': 3.48,
      'isbn': '0596527314',
      'isbn13': 9780596527310,
      'language_code': 'eng',
      '  num_pages': 514,
      'ratings_count': 64,
      'text_reviews_count': 1,
      'publication_date': '1/1/2007',
      'publisher': "O'Reilly Media"},
     {'bookID': 151,
      'title': 'Anna Karenina',
      'authors': 'Leo Tolstoy/Richard Pevear/Larissa Volokhonsky',
      'average_rating': 4.05,
      'isbn': '0143035002',
      'isbn13': 9780143035008,
      'language_code': 'eng',
      '  num_pages': 838,
      'ratings_count': 16643,
      'text_reviews_count': 1851,
      'publication_date': '5/31/2004',
      'publisher': 'Penguin Classics'},
     {'bookID': 152,
      'title': 'Anna Karenina',
      'authors': 'Leo Tolstoy/David Magarshack/Priscilla Meyer',
      'average_rating': 4.05,
      'isbn': '0451528611',
      'isbn13': 9780451528612,
      'language_code': 'eng',
      '  num_pages': 960,
      'ratings_count': 109420,
      'text_reviews_count': 5696,
      'publication_date': '11/5/2002',
      'publisher': 'Signet'},
     {'bookID': 153,
      'title': 'Anna Karenina',
      'authors': 'Leo Tolstoy/Richard Pevear/Larissa Volokhonsky/John Bayley',
      'average_rating': 4.05,
      'isbn': '0140449175',
      'isbn13': 9780140449174,
      'language_code': 'eng',
      '  num_pages': 837,
      'ratings_count': 2904,
      'text_reviews_count': 309,
      'publication_date': '1/30/2003',
      'publisher': 'Penguin Books'},
     {'bookID': 154,
      'title': "CliffsNotes on Tolstoy's Anna Karenina",
      'authors': 'Marianne Sturman/Leo Tolstoy',
      'average_rating': 3.85,
      'isbn': '0822001837',
      'isbn13': 9780822001836,
      'language_code': 'eng',
      '  num_pages': 80,
      'ratings_count': 16,
      'text_reviews_count': 3,
      'publication_date': '11/26/1965',
      'publisher': 'Cliffs Notes'},
     {'bookID': 155,
      'title': 'Anna Karenina',
      'authors': 'Leo Tolstoy/Amy Mandelker/Constance Garnett',
      'average_rating': 4.05,
      'isbn': '1593080271',
      'isbn13': 9781593080273,
      'language_code': 'eng',
      '  num_pages': 803,
      'ratings_count': 9564,
      'text_reviews_count': 726,
      'publication_date': '7/1/2003',
      'publisher': 'Barnes & Noble Classics'},
     {'bookID': 156,
      'title': 'Anna Karenina',
      'authors': 'Leo Tolstoy/Louise Maude/Aylmer Maude',
      'average_rating': 4.05,
      'isbn': '0486437965',
      'isbn13': 9780486437965,
      'language_code': 'eng',
      '  num_pages': 752,
      'ratings_count': 474,
      'text_reviews_count': 72,
      'publication_date': '11/23/2004',
      'publisher': 'Dover Publications'},
     {'bookID': 157,
      'title': 'Anna Karenina',
      'authors': 'Leo Tolstoy/Constance Garnett/Amy Mandelker',
      'average_rating': 4.05,
      'isbn': '1593081774',
      'isbn13': 9781593081775,
      'language_code': 'eng',
      '  num_pages': 803,
      'ratings_count': 303,
      'text_reviews_count': 48,
      'publication_date': '8/26/2004',
      'publisher': 'Barnes & Noble'},
     {'bookID': 159,
      'title': 'Dinner with Anna Karenina',
      'authors': 'Gloria Goldreich',
      'average_rating': 2.99,
      'isbn': '0778322270',
      'isbn13': 9780778322276,
      'language_code': 'eng',
      '  num_pages': 360,
      'ratings_count': 411,
      'text_reviews_count': 65,
      'publication_date': '1/28/2006',
      'publisher': 'Mira Books'},
     {'bookID': 160,
      'title': 'Tolstoy: Anna Karenina',
      'authors': 'Anthony Thorlby',
      'average_rating': 4.19,
      'isbn': '0521313252',
      'isbn13': 9780521313254,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 1204,
      'text_reviews_count': 33,
      'publication_date': '11/26/1987',
      'publisher': 'Cambridge University Press'},
     {'bookID': 162,
      'title': 'Untouchable',
      'authors': 'Mulk Raj Anand/E.M. Forster',
      'average_rating': 3.71,
      'isbn': '0140183957',
      'isbn13': 9780140183955,
      'language_code': 'eng',
      '  num_pages': 160,
      'ratings_count': 3429,
      'text_reviews_count': 279,
      'publication_date': '7/3/1990',
      'publisher': 'Penguin Books'},
     {'bookID': 163,
      'title': 'The Untouchable',
      'authors': 'John Banville',
      'average_rating': 3.95,
      'isbn': '0679767479',
      'isbn13': 9780679767473,
      'language_code': 'eng',
      '  num_pages': 367,
      'ratings_count': 2163,
      'text_reviews_count': 216,
      'publication_date': '6/30/1998',
      'publisher': 'Vintage'},
     {'bookID': 164,
      'title': 'The Untouchables',
      'authors': 'Eliot Ness/Oscar Fraley',
      'average_rating': 3.89,
      'isbn': '1568491980',
      'isbn13': 9781568491981,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 613,
      'text_reviews_count': 31,
      'publication_date': '2/1/1996',
      'publisher': 'Buccaneer Books'},
     {'bookID': 165,
      'title': "Untouchables: My Family's Triumphant Journey Out of the Caste System in Modern India",
      'authors': 'Narendra Jadhav',
      'average_rating': 3.82,
      'isbn': '0743270797',
      'isbn13': 9780743270793,
      'language_code': 'en-US',
      '  num_pages': 320,
      'ratings_count': 308,
      'text_reviews_count': 40,
      'publication_date': '9/27/2005',
      'publisher': 'Scribner'},
     {'bookID': 166,
      'title': 'Dalit: The Black Untaouchables of India',
      'authors': 'V.T. Rajshekar/Y.N. Kly',
      'average_rating': 4.2,
      'isbn': '0932863051',
      'isbn13': 9780932863058,
      'language_code': 'eng',
      '  num_pages': 100,
      'ratings_count': 10,
      'text_reviews_count': 0,
      'publication_date': '1/28/1995',
      'publisher': 'Clarity Press'},
     {'bookID': 168,
      'title': 'Growing Up Untouchable in India: A Dalit Autobiography',
      'authors': 'Vasant Moon/Gail Omvedt/Eleanor Zelliot',
      'average_rating': 3.65,
      'isbn': '0742508803',
      'isbn13': 9780742508804,
      'language_code': 'eng',
      '  num_pages': 224,
      'ratings_count': 16,
      'text_reviews_count': 4,
      'publication_date': '12/20/2000',
      'publisher': 'Rowman & Littlefield Publishers'},
     {'bookID': 171,
      'title': 'The Evidence-Based Social Work Skills Book',
      'authors': 'Barry R. Cournoyer',
      'average_rating': 3.4,
      'isbn': '0205358624',
      'isbn13': 9780205358625,
      'language_code': 'eng',
      '  num_pages': 216,
      'ratings_count': 10,
      'text_reviews_count': 0,
      'publication_date': '9/22/2003',
      'publisher': 'Pearson'},
     {'bookID': 177,
      'title': 'A Wrinkle in Time: A Guide for Using "A Wrinkle in Time" in the Classroom',
      'authors': 'John Carratello/Patty Carratello/Theresa Wright',
      'average_rating': 4.0,
      'isbn': '1557344035',
      'isbn13': 9781557344038,
      'language_code': 'eng',
      '  num_pages': 48,
      'ratings_count': 17,
      'text_reviews_count': 0,
      'publication_date': '9/28/1991',
      'publisher': 'Teacher Created Resources'},
     {'bookID': 180,
      'title': 'Wrinkles in Time',
      'authors': 'George Smoot/Keay Davidson',
      'average_rating': 4.01,
      'isbn': '0380720442',
      'isbn13': 9780380720446,
      'language_code': 'eng',
      '  num_pages': 360,
      'ratings_count': 1035,
      'text_reviews_count': 23,
      'publication_date': '10/1/1994',
      'publisher': 'Harper Perennial'},
     {'bookID': 181,
      'title': 'A Wrinkle in Time: With Related Readings (A Wrinkle in Time Quintet #1)',
      'authors': "Madeleine L'Engle",
      'average_rating': 4.0,
      'isbn': '0821925326',
      'isbn13': 9780821925324,
      'language_code': 'eng',
      '  num_pages': 250,
      'ratings_count': 36,
      'text_reviews_count': 6,
      'publication_date': '5/1/2002',
      'publisher': 'EMC/Paradigm Publishing'},
     {'bookID': 182,
      'title': 'Literature Circle Guide: A Wrinkle in Time',
      'authors': 'Tara MacCarthy',
      'average_rating': 3.6,
      'isbn': '043927169X',
      'isbn13': 9780439271691,
      'language_code': 'eng',
      '  num_pages': 32,
      'ratings_count': 15,
      'text_reviews_count': 0,
      'publication_date': '1/1/2002',
      'publisher': 'Teaching Resources'},
     {'bookID': 201,
      'title': 'Una arruga en el tiempo ??? A Wrinkle in Time',
      'authors': "Madeleine L'Engle",
      'average_rating': 4.0,
      'isbn': '0606105263',
      'isbn13': 9780606105262,
      'language_code': 'spa',
      '  num_pages': 205,
      'ratings_count': 6,
      'text_reviews_count': 1,
      'publication_date': '6/1/1984',
      'publisher': 'Turtleback Books'},
     {'bookID': 204,
      'title': 'The Long Shadow (The Morland Dynasty  #6)',
      'authors': 'Cynthia Harrod-Eagles',
      'average_rating': 4.12,
      'isbn': '0751506435',
      'isbn13': 9780751506433,
      'language_code': 'eng',
      '  num_pages': 367,
      'ratings_count': 376,
      'text_reviews_count': 17,
      'publication_date': '6/1/1994',
      'publisher': 'Little  Brown Book Group'},
     {'bookID': 205,
      'title': 'A Long Shadow (Inspector Ian Rutledge  #8)',
      'authors': 'Charles Todd',
      'average_rating': 4.11,
      'isbn': '006078671X',
      'isbn13': 9780060786717,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 3086,
      'text_reviews_count': 237,
      'publication_date': '1/3/2006',
      'publisher': 'William Morrow'},
     {'bookID': 207,
      'title': 'Long Way Round: Chasing Shadows Across the World',
      'authors': 'Ewan McGregor/Charley Boorman/Robert Uhlig',
      'average_rating': 3.94,
      'isbn': '0743499344',
      'isbn13': 9780743499347,
      'language_code': 'en-US',
      '  num_pages': 320,
      'ratings_count': 352,
      'text_reviews_count': 44,
      'publication_date': '11/1/2005',
      'publisher': 'Atria Books'},
     {'bookID': 208,
      'title': 'A Shadow in Summer (Long Price Quartet  #1)',
      'authors': 'Daniel Abraham',
      'average_rating': 3.6,
      'isbn': '0765313405',
      'isbn13': 9780765313409,
      'language_code': 'eng',
      '  num_pages': 331,
      'ratings_count': 9852,
      'text_reviews_count': 633,
      'publication_date': '3/7/2006',
      'publisher': 'Tor Books'},
     {'bookID': 213,
      'title': 'New Hope for the Dead (Hoke Mosely #2)',
      'authors': 'Charles Willeford/James Lee Burke',
      'average_rating': 3.9,
      'isbn': '1400032490',
      'isbn13': 9781400032495,
      'language_code': 'eng',
      '  num_pages': 244,
      'ratings_count': 821,
      'text_reviews_count': 78,
      'publication_date': '8/10/2004',
      'publisher': 'Vintage Crime/Black Lizard'},
     {'bookID': 214,
      'title': 'Sideswipe: A Hoke Moseley Novel',
      'authors': 'Charles Willeford/Lawrence Block',
      'average_rating': 4.05,
      'isbn': '1400032482',
      'isbn13': 9781400032488,
      'language_code': 'eng',
      '  num_pages': 215,
      'ratings_count': 731,
      'text_reviews_count': 72,
      'publication_date': '3/8/2005',
      'publisher': 'Vintage Crime/Black Lizard'},
     {'bookID': 216,
      'title': 'Miami Blues (Hoke Moseley #1)',
      'authors': 'Charles Willeford/Elmore Leonard',
      'average_rating': 3.94,
      'isbn': '1400032466',
      'isbn13': 9781400032464,
      'language_code': 'eng',
      '  num_pages': 191,
      'ratings_count': 2897,
      'text_reviews_count': 178,
      'publication_date': '8/10/2004',
      'publisher': 'Vintage Crime/Black Lizard'},
     {'bookID': 230,
      'title': 'The Burnt Orange Heresy (Vintage Crime/Black Lizard)',
      'authors': 'Charles Willeford',
      'average_rating': 3.89,
      'isbn': '0679732527',
      'isbn13': 9780679732525,
      'language_code': 'eng',
      '  num_pages': 144,
      'ratings_count': 98,
      'text_reviews_count': 11,
      'publication_date': '10/3/1990',
      'publisher': 'Vintage'},
     {'bookID': 231,
      'title': 'I am Charlotte Simmons',
      'authors': 'Tom Wolfe',
      'average_rating': 3.42,
      'isbn': '0312424442',
      'isbn13': 9780312424442,
      'language_code': 'eng',
      '  num_pages': 738,
      'ratings_count': 20888,
      'text_reviews_count': 1688,
      'publication_date': '8/30/2005',
      'publisher': 'Picador USA'},
     {'bookID': 237,
      'title': 'Poetry for Young People: Edward Lear',
      'authors': 'Edward Lear/Laura Huliska-Beith/Edward Mendelson',
      'average_rating': 3.91,
      'isbn': '0806930772',
      'isbn13': 9780806930770,
      'language_code': 'eng',
      '  num_pages': 48,
      'ratings_count': 66,
      'text_reviews_count': 19,
      'publication_date': '10/1/2001',
      'publisher': 'Sterling'},
     {'bookID': 244,
      'title': 'The Puffin Book of Nonsense Verse',
      'authors': 'Quentin Blake',
      'average_rating': 4.02,
      'isbn': '0140366601',
      'isbn13': 9780140366600,
      'language_code': 'eng',
      '  num_pages': 287,
      'ratings_count': 81,
      'text_reviews_count': 6,
      'publication_date': '10/3/1996',
      'publisher': 'Puffin'},
     {'bookID': 245,
      'title': 'Henry Miller on Writing',
      'authors': 'Henry Miller/Thomas H. Moore',
      'average_rating': 4.22,
      'isbn': '0811201120',
      'isbn13': 9780811201124,
      'language_code': 'eng',
      '  num_pages': 217,
      'ratings_count': 981,
      'text_reviews_count': 52,
      'publication_date': '2/1/1964',
      'publisher': 'New Directions Publishing'},
     {'bookID': 247,
      'title': 'Quiet Days in Clichy',
      'authors': 'Henry Miller',
      'average_rating': 3.69,
      'isbn': '080213016X',
      'isbn13': 9780802130167,
      'language_code': 'eng',
      '  num_pages': 154,
      'ratings_count': 3381,
      'text_reviews_count': 141,
      'publication_date': '1/13/1994',
      'publisher': 'Grove Press'},
     {'bookID': 249,
      'title': 'Tropic of Cancer',
      'authors': 'Henry Miller/Ji???? N??l',
      'average_rating': 3.68,
      'isbn': '0802131786',
      'isbn13': 9780802131782,
      'language_code': 'eng',
      '  num_pages': 318,
      'ratings_count': 53206,
      'text_reviews_count': 2376,
      'publication_date': '1/6/1994',
      'publisher': 'Grove Press'},
     {'bookID': 250,
      'title': 'Tropic of Capricorn',
      'authors': 'Henry Miller',
      'average_rating': 3.78,
      'isbn': '0802151825',
      'isbn13': 9780802151827,
      'language_code': 'eng',
      '  num_pages': 348,
      'ratings_count': 14872,
      'text_reviews_count': 459,
      'publication_date': '1/13/1994',
      'publisher': 'Grove Press'},
     {'bookID': 251,
      'title': 'Nexus (The Rosy Crucifixion  #3)',
      'authors': 'Henry Miller',
      'average_rating': 4.1,
      'isbn': '0802151787',
      'isbn13': 9780802151780,
      'language_code': 'eng',
      '  num_pages': 316,
      'ratings_count': 3261,
      'text_reviews_count': 58,
      'publication_date': '1/13/1994',
      'publisher': 'Grove Press'},
     {'bookID': 252,
      'title': 'Sexus (The Rosy Crucifixion  #1)',
      'authors': 'Henry Miller',
      'average_rating': 3.98,
      'isbn': '0802151809',
      'isbn13': 9780802151803,
      'language_code': 'eng',
      '  num_pages': 506,
      'ratings_count': 7805,
      'text_reviews_count': 251,
      'publication_date': '1/12/1994',
      'publisher': 'Grove Press'},
     {'bookID': 253,
      'title': 'The Air-Conditioned Nightmare',
      'authors': 'Henry Miller',
      'average_rating': 3.83,
      'isbn': '0811201066',
      'isbn13': 9780811201063,
      'language_code': 'eng',
      '  num_pages': 292,
      'ratings_count': 2699,
      'text_reviews_count': 142,
      'publication_date': '1/17/1970',
      'publisher': 'New Directions'},
     {'bookID': 264,
      'title': 'The Portrait of a Lady',
      'authors': 'Henry James/Patricia Crick',
      'average_rating': 3.78,
      'isbn': '0141439637',
      'isbn13': 9780141439631,
      'language_code': 'eng',
      '  num_pages': 797,
      'ratings_count': 61640,
      'text_reviews_count': 1951,
      'publication_date': '9/30/2003',
      'publisher': 'Penguin Classics'},
     {'bookID': 269,
      'title': 'The Portrait of a Lady',
      'authors': 'Henry James/Gabriel Brownstein/Mary Cregan',
      'average_rating': 3.78,
      'isbn': '1593080964',
      'isbn13': 9781593080969,
      'language_code': 'eng',
      '  num_pages': 635,
      'ratings_count': 392,
      'text_reviews_count': 41,
      'publication_date': '1/16/2004',
      'publisher': 'Barnes  Noble Classics'},
     {'bookID': 277,
      'title': 'Writing',
      'authors': 'Marguerite Duras',
      'average_rating': 3.75,
      'isbn': '1571290532',
      'isbn13': 9781571290533,
      'language_code': 'eng',
      '  num_pages': 91,
      'ratings_count': 778,
      'text_reviews_count': 44,
      'publication_date': '5/6/1999',
      'publisher': 'Brookline Books'},
     {'bookID': 278,
      'title': 'The War',
      'authors': 'Marguerite Duras/Barbara Bray',
      'average_rating': 3.85,
      'isbn': '1565842219',
      'isbn13': 9781565842212,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 963,
      'text_reviews_count': 65,
      'publication_date': '8/1/1994',
      'publisher': 'The New Press'},
     {'bookID': 280,
      'title': 'The Ravishing of Lol Stein',
      'authors': 'Marguerite Duras/Richard Seever',
      'average_rating': 3.66,
      'isbn': '0394743040',
      'isbn13': 9780394743042,
      'language_code': 'en-US',
      '  num_pages': 181,
      'ratings_count': 2057,
      'text_reviews_count': 128,
      'publication_date': '3/12/1986',
      'publisher': 'Pantheon'},
     {'bookID': 285,
      'title': 'Love Letters',
      'authors': 'Kahlil Gibran/Suheil Bushrui/Salma H. Al-Kuzbari',
      'average_rating': 3.68,
      'isbn': '1851681825',
      'isbn13': 9781851681822,
      'language_code': 'eng',
      '  num_pages': 178,
      'ratings_count': 203,
      'text_reviews_count': 8,
      'publication_date': '7/1/1999',
      'publisher': 'One World (UK)'},
     {'bookID': 288,
      'title': 'Kahlil Gibran: His Life and World',
      'authors': 'Jean Gibran/?????????? ???????? ??????????/Kahlil Gibran',
      'average_rating': 4.21,
      'isbn': '156656249X',
      'isbn13': 9781566562492,
      'language_code': 'eng',
      '  num_pages': 464,
      'ratings_count': 35,
      'text_reviews_count': 2,
      'publication_date': '4/1/1998',
      'publisher': 'Interlink Publishing Group'},
     {'bookID': 289,
      'title': 'The Beloved: Reflections on the Path of the Heart',
      'authors': 'Kahlil Gibran/John Walbridge/Robin Waterfield',
      'average_rating': 4.19,
      'isbn': '014019553X',
      'isbn13': 9780140195538,
      'language_code': 'eng',
      '  num_pages': 102,
      'ratings_count': 328,
      'text_reviews_count': 16,
      'publication_date': '1/1/1998',
      'publisher': 'Penguin Books'},
     {'bookID': 290,
      'title': 'Jesus the Son of Man',
      'authors': 'Kahlil Gibran/?????????? ???????? ??????????',
      'average_rating': 3.98,
      'isbn': '0394431243',
      'isbn13': 9780394431246,
      'language_code': 'eng',
      '  num_pages': 216,
      'ratings_count': 1308,
      'text_reviews_count': 82,
      'publication_date': '2/21/1995',
      'publisher': 'Knopf'},
     {'bookID': 291,
      'title': 'The Broken Wings',
      'authors': 'Kahlil Gibran/?????????? ???????? ??????????/Anthony Rizcallah Ferris',
      'average_rating': 3.92,
      'isbn': '0806501901',
      'isbn13': 9780806501901,
      'language_code': 'eng',
      '  num_pages': 132,
      'ratings_count': 6432,
      'text_reviews_count': 517,
      'publication_date': '3/3/2003',
      'publisher': 'Citadel'},
     {'bookID': 292,
      'title': 'Sand and Foam',
      'authors': 'Kahlil Gibran/?????????? ???????? ??????????',
      'average_rating': 4.08,
      'isbn': '067943920X',
      'isbn13': 9780679439202,
      'language_code': 'eng',
      '  num_pages': 100,
      'ratings_count': 3015,
      'text_reviews_count': 217,
      'publication_date': '6/14/2011',
      'publisher': 'Knopf'},
     {'bookID': 295,
      'title': 'Treasure Island',
      'authors': 'Robert Louis Stevenson',
      'average_rating': 3.83,
      'isbn': '0753453800',
      'isbn13': 9780753453803,
      'language_code': 'eng',
      '  num_pages': 311,
      'ratings_count': 318753,
      'text_reviews_count': 6734,
      'publication_date': '9/15/2001',
      'publisher': 'Kingfisher'},
     {'bookID': 296,
      'title': 'Treasure Island',
      'authors': 'Robert Louis Stevenson/Scott McKowen',
      'average_rating': 3.83,
      'isbn': '1402714572',
      'isbn13': 9781402714573,
      'language_code': 'en-US',
      '  num_pages': 213,
      'ratings_count': 420,
      'text_reviews_count': 42,
      'publication_date': '10/1/2004',
      'publisher': "Sterling Children's Books"},
     {'bookID': 297,
      'title': 'Treasure Island',
      'authors': 'Robert Louis Stevenson',
      'average_rating': 3.83,
      'isbn': '1416500294',
      'isbn13': 9781416500292,
      'language_code': 'eng',
      '  num_pages': 245,
      'ratings_count': 5967,
      'text_reviews_count': 276,
      'publication_date': '6/1/2005',
      'publisher': 'Simon & Schuster'},
     {'bookID': 298,
      'title': 'Treasure Island',
      'authors': 'Robert Louis Stevenson/N.C. Wyeth/Timothy Meis',
      'average_rating': 3.83,
      'isbn': '0689854684',
      'isbn13': 9780689854682,
      'language_code': 'eng',
      '  num_pages': 64,
      'ratings_count': 104,
      'text_reviews_count': 14,
      'publication_date': '7/1/2003',
      'publisher': 'Atheneum Books for Young Readers'},
     {'bookID': 299,
      'title': 'Treasure Island',
      'authors': 'Robert Louis Stevenson/Milo Winter',
      'average_rating': 3.83,
      'isbn': '0517221144',
      'isbn13': 9780517221143,
      'language_code': 'en-US',
      '  num_pages': 272,
      'ratings_count': 56,
      'text_reviews_count': 4,
      'publication_date': '9/3/2002',
      'publisher': 'Gramercy Books'},
     {'bookID': 302,
      'title': 'Treasure Island (Great Illustrated Classics)',
      'authors': 'Deidre S. Laiken/A.J. McAllister/Robert Louis Stevenson',
      'average_rating': 4.05,
      'isbn': '1577658051',
      'isbn13': 9781577658054,
      'language_code': 'eng',
      '  num_pages': 232,
      'ratings_count': 91,
      'text_reviews_count': 16,
      'publication_date': '1/31/2006',
      'publisher': 'Abdo Publishing Company'},
     {'bookID': 313,
      'title': '100 Years of Lynchings',
      'authors': 'Ralph Ginzburg',
      'average_rating': 4.61,
      'isbn': '0933121180',
      'isbn13': 9780933121188,
      'language_code': 'eng',
      '  num_pages': 270,
      'ratings_count': 88,
      'text_reviews_count': 4,
      'publication_date': '11/22/1996',
      'publisher': 'Black Classic Press'},
     {'bookID': 324,
      'title': 'Cien a??os de soledad',
      'authors': 'Gabriel Garc??a M??rquez',
      'average_rating': 4.07,
      'isbn': '0785950109',
      'isbn13': 9780785950103,
      'language_code': 'spa',
      '  num_pages': 448,
      'ratings_count': 63,
      'text_reviews_count': 7,
      'publication_date': '1/1/1990',
      'publisher': 'French & European'},
     {'bookID': 330,
      'title': 'On Beyond Zebra!',
      'authors': 'Dr. Seuss',
      'average_rating': 4.04,
      'isbn': '0394800842',
      'isbn13': 9780394800844,
      'language_code': 'eng',
      '  num_pages': 64,
      'ratings_count': 2815,
      'text_reviews_count': 164,
      'publication_date': '9/12/1955',
      'publisher': 'Random House Books for Young Readers'},
     {'bookID': 332,
      'title': 'The Wedding Clause',
      'authors': 'Debbie Raleigh',
      'average_rating': 3.6,
      'isbn': '0821778250',
      'isbn13': 9780821778258,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 95,
      'text_reviews_count': 13,
      'publication_date': '6/7/2005',
      'publisher': 'Zebra'},
     {'bookID': 333,
      'title': 'The Zebra Wall',
      'authors': 'Kevin Henkes',
      'average_rating': 3.44,
      'isbn': '0060733039',
      'isbn13': 9780060733032,
      'language_code': 'eng',
      '  num_pages': 147,
      'ratings_count': 217,
      'text_reviews_count': 24,
      'publication_date': '2/15/2005',
      'publisher': 'Greenwillow Books'},
     {'bookID': 337,
      'title': 'El perfume: Historia de un asesino',
      'authors': 'Patrick S??skind',
      'average_rating': 4.02,
      'isbn': '8432216062',
      'isbn13': 9788432216060,
      'language_code': 'spa',
      '  num_pages': 239,
      'ratings_count': 4136,
      'text_reviews_count': 255,
      'publication_date': '6/1/2002',
      'publisher': 'Booket'},
     {'bookID': 348,
      'title': 'The Door Into Summer',
      'authors': 'Robert A. Heinlein',
      'average_rating': 4.01,
      'isbn': '0345413997',
      'isbn13': 9780345413994,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 17232,
      'text_reviews_count': 649,
      'publication_date': '6/17/1997',
      'publisher': 'Del Rey'},
     {'bookID': 350,
      'title': 'Stranger in a Strange Land',
      'authors': 'Robert A. Heinlein',
      'average_rating': 3.92,
      'isbn': '0441788386',
      'isbn13': 9780441788385,
      'language_code': 'eng',
      '  num_pages': 528,
      'ratings_count': 251872,
      'text_reviews_count': 6241,
      'publication_date': '10/1/1991',
      'publisher': 'Ace'},
     {'bookID': 354,
      'title': 'To Sail Beyond the Sunset',
      'authors': 'Robert A. Heinlein',
      'average_rating': 3.87,
      'isbn': '0441748600',
      'isbn13': 9780441748600,
      'language_code': 'en-US',
      '  num_pages': 434,
      'ratings_count': 10293,
      'text_reviews_count': 193,
      'publication_date': '6/1/1988',
      'publisher': 'Ace Books'},
     {'bookID': 355,
      'title': 'Job: A Comedy of Justice',
      'authors': 'Robert A. Heinlein',
      'average_rating': 3.78,
      'isbn': '0345316509',
      'isbn13': 9780345316509,
      'language_code': 'en-US',
      '  num_pages': 439,
      'ratings_count': 15970,
      'text_reviews_count': 438,
      'publication_date': '10/12/1985',
      'publisher': 'Del Rey'},
     {'bookID': 356,
      'title': "Time for the Stars (Heinlein's Juveniles  #10)",
      'authors': 'Robert A. Heinlein',
      'average_rating': 3.97,
      'isbn': '0765314932',
      'isbn13': 9780765314932,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 6898,
      'text_reviews_count': 200,
      'publication_date': '8/8/2006',
      'publisher': 'Tor Books'},
     {'bookID': 357,
      'title': 'The Long Dark Tea-Time of the Soul (Dirk Gently  #2)',
      'authors': 'Douglas Adams',
      'average_rating': 4.06,
      'isbn': '0671742515',
      'isbn13': 9780671742515,
      'language_code': 'en-US',
      '  num_pages': 307,
      'ratings_count': 67803,
      'text_reviews_count': 1401,
      'publication_date': '2/15/1991',
      'publisher': 'Pocket Books'},
     {'bookID': 359,
      'title': 'The Salmon of Doubt (Dirk Gently  #3)',
      'authors': 'Douglas Adams',
      'average_rating': 3.93,
      'isbn': '0345455290',
      'isbn13': 9780345455291,
      'language_code': 'eng',
      '  num_pages': 298,
      'ratings_count': 22091,
      'text_reviews_count': 746,
      'publication_date': '4/26/2005',
      'publisher': 'Del Rey'},
     {'bookID': 362,
      'title': 'Wish You Were Here: The Official Biography of Douglas Adams',
      'authors': 'Nick  Webb',
      'average_rating': 4.14,
      'isbn': '0345476514',
      'isbn13': 9780345476517,
      'language_code': 'eng',
      '  num_pages': 368,
      'ratings_count': 2623,
      'text_reviews_count': 49,
      'publication_date': '12/27/2005',
      'publisher': 'Del Rey'},
     {'bookID': 367,
      'title': "Douglas Adams's Starship Titanic",
      'authors': 'Terry Jones',
      'average_rating': 3.6,
      'isbn': '0345368436',
      'isbn13': 9780345368430,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 885,
      'text_reviews_count': 84,
      'publication_date': '10/27/1998',
      'publisher': 'Ballantine Books'},
     {'bookID': 377,
      'title': 'Salmon of Doubt: Hitchhiking the Galaxy One Last Time',
      'authors': 'Douglas Adams/Christopher Cerf',
      'average_rating': 3.93,
      'isbn': '1417622857',
      'isbn13': 9781417622856,
      'language_code': 'eng',
      '  num_pages': 336,
      'ratings_count': 5,
      'text_reviews_count': 0,
      'publication_date': '7/1/2003',
      'publisher': 'Turtleback Books'},
     {'bookID': 382,
      'title': "The Phantom Tollbooth: A Children's Play in Two Acts",
      'authors': 'Susan Nanus/Norton Juster',
      'average_rating': 4.13,
      'isbn': '0573650969',
      'isbn13': 9780573650963,
      'language_code': 'eng',
      '  num_pages': 72,
      'ratings_count': 100,
      'text_reviews_count': 13,
      'publication_date': '1/12/2011',
      'publisher': 'Samuel French  Inc.'},
     {'bookID': 385,
      'title': 'On Bullshit',
      'authors': 'Harry G. Frankfurt',
      'average_rating': 3.57,
      'isbn': '0691122946',
      'isbn13': 9780691122946,
      'language_code': 'eng',
      '  num_pages': 67,
      'ratings_count': 9358,
      'text_reviews_count': 995,
      'publication_date': '1/30/2005',
      'publisher': 'Princeton University Press'},
     {'bookID': 386,
      'title': 'Another Bullshit Night in Suck City',
      'authors': 'Nick Flynn',
      'average_rating': 3.78,
      'isbn': '0393329402',
      'isbn13': 9780393329407,
      'language_code': 'eng',
      '  num_pages': 347,
      'ratings_count': 9318,
      'text_reviews_count': 907,
      'publication_date': '9/12/2005',
      'publisher': 'W. W. Norton & Company'},
     {'bookID': 394,
      'title': 'Lincoln at Gettysburg: The Words That Remade America',
      'authors': 'Garry Wills',
      'average_rating': 4.14,
      'isbn': '0671867423',
      'isbn13': 9780671867423,
      'language_code': 'en-US',
      '  num_pages': 317,
      'ratings_count': 120,
      'text_reviews_count': 15,
      'publication_date': '6/12/1993',
      'publisher': 'Simon & Schuster'},
     {'bookID': 397,
      'title': 'The Gettysburg Address',
      'authors': 'Abraham Lincoln/Michael McCurdy',
      'average_rating': 4.53,
      'isbn': '0395883970',
      'isbn13': 9780395883976,
      'language_code': 'eng',
      '  num_pages': 32,
      'ratings_count': 5239,
      'text_reviews_count': 76,
      'publication_date': '2/2/1998',
      'publisher': 'HMH Books for Young Readers'},
     {'bookID': 399,
      'title': 'Underworld',
      'authors': 'Don DeLillo',
      'average_rating': 3.92,
      'isbn': '0684848155',
      'isbn13': 9780684848150,
      'language_code': 'eng',
      '  num_pages': 827,
      'ratings_count': 1505,
      'text_reviews_count': 175,
      'publication_date': '7/9/1998',
      'publisher': 'Scribner'},
     {'bookID': 400,
      'title': 'Libra',
      'authors': 'Don DeLillo',
      'average_rating': 3.99,
      'isbn': '0140156046',
      'isbn13': 9780140156041,
      'language_code': 'eng',
      '  num_pages': 480,
      'ratings_count': 11857,
      'text_reviews_count': 564,
      'publication_date': '5/1/1991',
      'publisher': 'Penguin'},
     {'bookID': 403,
      'title': 'Americana',
      'authors': 'Don DeLillo',
      'average_rating': 3.43,
      'isbn': '0140119485',
      'isbn13': 9780140119480,
      'language_code': 'eng',
      '  num_pages': 377,
      'ratings_count': 393,
      'text_reviews_count': 55,
      'publication_date': '7/6/1989',
      'publisher': 'Penguin Books'},
     {'bookID': 404,
      'title': 'Running Dog',
      'authors': 'Don DeLillo',
      'average_rating': 3.43,
      'isbn': '0679722947',
      'isbn13': 9780679722946,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 1356,
      'text_reviews_count': 72,
      'publication_date': '7/17/1989',
      'publisher': 'Vintage Contemporaries'},
     {'bookID': 406,
      'title': 'Cosmopolis',
      'authors': 'Don DeLillo',
      'average_rating': 3.22,
      'isbn': '0743244257',
      'isbn13': 9780743244251,
      'language_code': 'eng',
      '  num_pages': 224,
      'ratings_count': 460,
      'text_reviews_count': 41,
      'publication_date': '4/6/2004',
      'publisher': 'Scribner'},
     {'bookID': 407,
      'title': 'Great Jones Street',
      'authors': 'Don DeLillo',
      'average_rating': 3.48,
      'isbn': '0140179178',
      'isbn13': 9780140179170,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 2492,
      'text_reviews_count': 145,
      'publication_date': '1/1/1994',
      'publisher': 'Penguin Books'},
     {'bookID': 408,
      'title': 'The Names',
      'authors': 'Don DeLillo',
      'average_rating': 3.64,
      'isbn': '0679722955',
      'isbn13': 9780679722953,
      'language_code': 'eng',
      '  num_pages': 339,
      'ratings_count': 3100,
      'text_reviews_count': 212,
      'publication_date': '7/17/1989',
      'publisher': 'Vintage'},
     {'bookID': 409,
      'title': 'Against the Day',
      'authors': 'Thomas Pynchon',
      'average_rating': 4.13,
      'isbn': '159420120X',
      'isbn13': 9781594201202,
      'language_code': 'eng',
      '  num_pages': 1085,
      'ratings_count': 5296,
      'text_reviews_count': 587,
      'publication_date': '11/21/2006',
      'publisher': 'Penguin Press'},
     {'bookID': 410,
      'title': 'V.',
      'authors': 'Thomas Pynchon',
      'average_rating': 3.96,
      'isbn': '0060930217',
      'isbn13': 9780060930219,
      'language_code': 'eng',
      '  num_pages': 547,
      'ratings_count': 1415,
      'text_reviews_count': 177,
      'publication_date': '7/5/2005',
      'publisher': 'Harper Perennial Modern Classics'},
     {'bookID': 411,
      'title': 'The Crying of Lot 49',
      'authors': 'Thomas Pynchon',
      'average_rating': 3.69,
      'isbn': '0060931671',
      'isbn13': 9780060931674,
      'language_code': 'eng',
      '  num_pages': 152,
      'ratings_count': 2161,
      'text_reviews_count': 230,
      'publication_date': '4/1/1999',
      'publisher': 'Harper Perennial'},
     {'bookID': 412,
      'title': "Gravity's Rainbow",
      'authors': 'Thomas Pynchon',
      'average_rating': 4.01,
      'isbn': '0140283382',
      'isbn13': 9780140283389,
      'language_code': 'eng',
      '  num_pages': 784,
      'ratings_count': 762,
      'text_reviews_count': 213,
      'publication_date': '1/1/2000',
      'publisher': 'Penguin Books'},
     {'bookID': 413,
      'title': 'Mason & Dixon',
      'authors': 'Thomas Pynchon/Christophe Claro/Brice Matthieussent',
      'average_rating': 4.07,
      'isbn': '0312423209',
      'isbn13': 9780312423209,
      'language_code': 'eng',
      '  num_pages': 773,
      'ratings_count': 8086,
      'text_reviews_count': 602,
      'publication_date': '1/3/2004',
      'publisher': 'Picador USA'},
     {'bookID': 414,
      'title': 'Vineland',
      'authors': 'Thomas Pynchon',
      'average_rating': 3.69,
      'isbn': '0141180633',
      'isbn13': 9780141180632,
      'language_code': 'en-US',
      '  num_pages': 385,
      'ratings_count': 702,
      'text_reviews_count': 69,
      'publication_date': '9/1/1997',
      'publisher': 'Penguin Classics'},
     {'bookID': 415,
      'title': "Gravity's Rainbow",
      'authors': 'Thomas Pynchon',
      'average_rating': 4.01,
      'isbn': '0143039946',
      'isbn13': 9780143039945,
      'language_code': 'eng',
      '  num_pages': 776,
      'ratings_count': 29764,
      'text_reviews_count': 2164,
      'publication_date': '10/31/2006',
      'publisher': 'Penguin Books'},
     {'bookID': 416,
      'title': 'Slow Learner: Early Stories',
      'authors': 'Thomas Pynchon',
      'average_rating': 3.5,
      'isbn': '0316724432',
      'isbn13': 9780316724432,
      'language_code': 'eng',
      '  num_pages': 193,
      'ratings_count': 334,
      'text_reviews_count': 34,
      'publication_date': '4/30/1985',
      'publisher': 'Back Bay Books'},
     {'bookID': 418,
      'title': 'Been Down So Long It Looks Like Up To Me',
      'authors': 'Richard Fari??a/Thomas Pynchon',
      'average_rating': 3.8,
      'isbn': '0140189300',
      'isbn13': 9780140189308,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 2473,
      'text_reviews_count': 220,
      'publication_date': '8/29/1996',
      'publisher': 'Penguin Classics'},
     {'bookID': 420,
      'title': 'The Year of Magical Thinking',
      'authors': 'Joan Didion',
      'average_rating': 3.89,
      'isbn': '140004314X',
      'isbn13': 9781400043149,
      'language_code': 'en-US',
      '  num_pages': 227,
      'ratings_count': 2656,
      'text_reviews_count': 336,
      'publication_date': '10/4/2005',
      'publisher': 'Knopf Publishing Group'},
     {'bookID': 421,
      'title': 'The White Album',
      'authors': 'Joan Didion',
      'average_rating': 4.17,
      'isbn': '0374522219',
      'isbn13': 9780374522216,
      'language_code': 'eng',
      '  num_pages': 222,
      'ratings_count': 11889,
      'text_reviews_count': 738,
      'publication_date': '10/1/1990',
      'publisher': 'Farrar Straus Giroux'},
     {'bookID': 422,
      'title': 'A Book of Common Prayer',
      'authors': 'Joan Didion',
      'average_rating': 3.8,
      'isbn': '0679754865',
      'isbn13': 9780679754862,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 2962,
      'text_reviews_count': 255,
      'publication_date': '4/11/1995',
      'publisher': 'Vintage International'},
     {'bookID': 423,
      'title': 'Where I Was From',
      'authors': 'Joan Didion',
      'average_rating': 3.86,
      'isbn': '0679752862',
      'isbn13': 9780679752868,
      'language_code': 'eng',
      '  num_pages': 240,
      'ratings_count': 2842,
      'text_reviews_count': 292,
      'publication_date': '9/14/2004',
      'publisher': 'Vintage'},
     {'bookID': 424,
      'title': 'Slouching Towards Bethlehem',
      'authors': 'Joan Didion',
      'average_rating': 4.21,
      'isbn': '0374521727',
      'isbn13': 9780374521721,
      'language_code': 'eng',
      '  num_pages': 238,
      'ratings_count': 26934,
      'text_reviews_count': 1825,
      'publication_date': '10/1/1990',
      'publisher': 'Farrar Straus Giroux'},
     {'bookID': 425,
      'title': 'Democracy',
      'authors': 'Joan Didion',
      'average_rating': 3.81,
      'isbn': '0679754857',
      'isbn13': 9780679754855,
      'language_code': 'en-US',
      '  num_pages': 234,
      'ratings_count': 2070,
      'text_reviews_count': 169,
      'publication_date': '4/25/1995',
      'publisher': 'Vintage International'},
     {'bookID': 426,
      'title': 'We Tell Ourselves Stories in Order to Live: Collected Nonfiction',
      'authors': 'Joan Didion/John Leonard',
      'average_rating': 4.5,
      'isbn': '0307264874',
      'isbn13': 9780307264879,
      'language_code': 'eng',
      '  num_pages': 1122,
      'ratings_count': 1564,
      'text_reviews_count': 108,
      'publication_date': '10/17/2006',
      'publisher': "Everyman's Library"},
     {'bookID': 428,
      'title': 'Play It As It Lays',
      'authors': 'Joan Didion/David Thomson',
      'average_rating': 3.87,
      'isbn': '0374529949',
      'isbn13': 9780374529949,
      'language_code': 'eng',
      '  num_pages': 231,
      'ratings_count': 23656,
      'text_reviews_count': 1706,
      'publication_date': '11/15/2005',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 431,
      'title': 'The New York Trilogy',
      'authors': 'Paul Auster/Art Spiegelman/Luc Sante',
      'average_rating': 3.89,
      'isbn': '0143039830',
      'isbn13': 9780143039839,
      'language_code': 'eng',
      '  num_pages': 308,
      'ratings_count': 43200,
      'text_reviews_count': 1873,
      'publication_date': '3/28/2006',
      'publisher': 'Penguin Classics'},
     {'bookID': 432,
      'title': 'City of Glass (The New York Trilogy  #1)',
      'authors': 'Paul Auster',
      'average_rating': 3.79,
      'isbn': '0140097317',
      'isbn13': 9780140097313,
      'language_code': 'eng',
      '  num_pages': 203,
      'ratings_count': 12410,
      'text_reviews_count': 734,
      'publication_date': '4/7/1987',
      'publisher': 'Penguin Books'},
     {'bookID': 434,
      'title': 'Ghosts (The New York Trilogy  #2)',
      'authors': 'Paul Auster',
      'average_rating': 3.64,
      'isbn': '014009735X',
      'isbn13': 9780140097351,
      'language_code': 'eng',
      '  num_pages': 96,
      'ratings_count': 3672,
      'text_reviews_count': 195,
      'publication_date': '7/7/1987',
      'publisher': 'Penguin Books'},
     {'bookID': 435,
      'title': 'The Locked Room (The New York Trilogy  #3)',
      'authors': 'Paul Auster',
      'average_rating': 3.89,
      'isbn': '0940650762',
      'isbn13': 9780940650763,
      'language_code': 'eng',
      '  num_pages': 179,
      'ratings_count': 2998,
      'text_reviews_count': 164,
      'publication_date': '11/1/1986',
      'publisher': 'Sun and Moon Press'},
     {'bookID': 444,
      'title': 'Pyramids of Montauk: Explorations in Consciousness',
      'authors': 'Peter Moon/Preston B. Nichols/Nina Helms',
      'average_rating': 3.89,
      'isbn': '0963188925',
      'isbn13': 9780963188922,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 74,
      'text_reviews_count': 2,
      'publication_date': '1/1/1995',
      'publisher': 'Sky Books (NY)'},
     {'bookID': 446,
      'title': 'The Brooklyn Follies',
      'authors': 'Paul Auster',
      'average_rating': 3.84,
      'isbn': '0312426232',
      'isbn13': 9780312426231,
      'language_code': 'eng',
      '  num_pages': 306,
      'ratings_count': 17977,
      'text_reviews_count': 1157,
      'publication_date': '10/17/2006',
      'publisher': 'Picador'},
     {'bookID': 447,
      'title': 'Moon Palace',
      'authors': 'Paul Auster',
      'average_rating': 3.94,
      'isbn': '0140115854',
      'isbn13': 9780140115857,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 16099,
      'text_reviews_count': 503,
      'publication_date': '4/1/1990',
      'publisher': 'Penguin Books'},
     {'bookID': 453,
      'title': 'The Music of Chance',
      'authors': 'Paul Auster',
      'average_rating': 3.9,
      'isbn': '0140154078',
      'isbn13': 9780140154078,
      'language_code': 'en-US',
      '  num_pages': 217,
      'ratings_count': 361,
      'text_reviews_count': 36,
      'publication_date': '12/1/1991',
      'publisher': 'Penguin Books'},
     {'bookID': 454,
      'title': 'Travels in the Scriptorium',
      'authors': 'Paul Auster',
      'average_rating': 3.23,
      'isbn': '0805081453',
      'isbn13': 9780805081459,
      'language_code': 'eng',
      '  num_pages': 145,
      'ratings_count': 6688,
      'text_reviews_count': 562,
      'publication_date': '1/23/2007',
      'publisher': 'Henry Holt & Company'},
     {'bookID': 456,
      'title': 'Leviathan',
      'authors': 'Paul Auster',
      'average_rating': 3.96,
      'isbn': '0140178139',
      'isbn13': 9780140178135,
      'language_code': 'eng',
      '  num_pages': 275,
      'ratings_count': 11744,
      'text_reviews_count': 443,
      'publication_date': '9/1/1993',
      'publisher': 'Penguin Books'},
     {'bookID': 463,
      'title': 'The Red Notebook: True Stories',
      'authors': 'Paul Auster',
      'average_rating': 3.77,
      'isbn': '0811214982',
      'isbn13': 9780811214988,
      'language_code': 'eng',
      '  num_pages': 104,
      'ratings_count': 2390,
      'text_reviews_count': 120,
      'publication_date': '6/17/2002',
      'publisher': 'New Directions'},
     {'bookID': 466,
      'title': 'Timbuktu / Leviathan / Moon Palace',
      'authors': 'Paul Auster',
      'average_rating': 4.38,
      'isbn': '2742741461',
      'isbn13': 9782742741465,
      'language_code': 'fre',
      '  num_pages': 1075,
      'ratings_count': 21,
      'text_reviews_count': 1,
      'publication_date': '11/7/2002',
      'publisher': 'Actes Sud'},
     {'bookID': 475,
      'title': 'Collapse: How Societies Choose to Fail or Succeed',
      'authors': 'Jared Diamond',
      'average_rating': 3.93,
      'isbn': '0143036556',
      'isbn13': 9780143036555,
      'language_code': 'eng',
      '  num_pages': 608,
      'ratings_count': 52522,
      'text_reviews_count': 2780,
      'publication_date': '12/27/2005',
      'publisher': 'Penguin Books Ltd. (London)'},
     {'bookID': 476,
      'title': 'The Coming Economic Collapse: How You Can Thrive When Oil Costs $200 a Barrel',
      'authors': 'Stephen Leeb/Glen C. Strathy',
      'average_rating': 3.4,
      'isbn': '0446579785',
      'isbn13': 9780446579780,
      'language_code': 'en-US',
      '  num_pages': 211,
      'ratings_count': 213,
      'text_reviews_count': 26,
      'publication_date': '2/1/2006',
      'publisher': 'Business Plus'},
     {'bookID': 477,
      'title': 'Collapse of Complex Societies',
      'authors': 'Joseph A. Tainter',
      'average_rating': 4.15,
      'isbn': '052138673X',
      'isbn13': 9780521386739,
      'language_code': 'eng',
      '  num_pages': 262,
      'ratings_count': 719,
      'text_reviews_count': 86,
      'publication_date': '3/29/1990',
      'publisher': 'Cambridge University Press'},
     {'bookID': 478,
      'title': 'Bowling Alone: The Collapse and Revival of American Community',
      'authors': 'Robert D. Putnam',
      'average_rating': 3.8,
      'isbn': '0743203046',
      'isbn13': 9780743203043,
      'language_code': 'eng',
      '  num_pages': 544,
      'ratings_count': 4762,
      'text_reviews_count': 512,
      'publication_date': '8/7/2001',
      'publisher': 'Simon  Schuster'},
     {'bookID': 481,
      'title': "The Collapse of the Common Good: How America's Lawsuit Culture Undermines Our Freedom",
      'authors': 'Philip K. Howard',
      'average_rating': 3.91,
      'isbn': '034543871X',
      'isbn13': 9780345438713,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 62,
      'text_reviews_count': 4,
      'publication_date': '1/29/2002',
      'publisher': 'Ballantine Books'},
     {'bookID': 484,
      'title': "Reinventing the Enemy's Language: Contemporary Native Women's Writings of North America",
      'authors': 'Joy Harjo/Gloria Bird/Beth Cuthand/Valerie Martinez/Patricia Blanco',
      'average_rating': 4.39,
      'isbn': '0393318281',
      'isbn13': 9780393318289,
      'language_code': 'eng',
      '  num_pages': 576,
      'ratings_count': 278,
      'text_reviews_count': 20,
      'publication_date': '9/17/1998',
      'publisher': 'W. W. Norton  Company'},
     {'bookID': 493,
      'title': 'My Inventions',
      'authors': 'Nikola Tesla',
      'average_rating': 4.01,
      'isbn': '1599869942',
      'isbn13': 9781599869940,
      'language_code': 'eng',
      '  num_pages': 88,
      'ratings_count': 2862,
      'text_reviews_count': 262,
      'publication_date': '5/17/2006',
      'publisher': 'Filiquarian Publishing  LLC.'},
     {'bookID': 494,
      'title': 'Wizard: The Life and Times of Nikola Tesla: Biography of a Genius',
      'authors': 'Marc J.  Seifer/William H. Terbo',
      'average_rating': 3.78,
      'isbn': '0806519606',
      'isbn13': 9780806519609,
      'language_code': 'eng',
      '  num_pages': 542,
      'ratings_count': 2829,
      'text_reviews_count': 334,
      'publication_date': '2/1/2001',
      'publisher': 'Citadel'},
     {'bookID': 497,
      'title': 'Nikola Tesla: A Spark of Genius',
      'authors': 'Carol Dommermuth-Costa',
      'average_rating': 3.93,
      'isbn': '0822549204',
      'isbn13': 9780822549208,
      'language_code': 'eng',
      '  num_pages': 144,
      'ratings_count': 105,
      'text_reviews_count': 5,
      'publication_date': '10/1/1994',
      'publisher': 'Lerner Publications'},
     {'bookID': 498,
      'title': 'Tesla Papers',
      'authors': 'Nikola Tesla/David Hatcher Childress',
      'average_rating': 4.13,
      'isbn': '0932813860',
      'isbn13': 9780932813862,
      'language_code': 'eng',
      '  num_pages': 100,
      'ratings_count': 102,
      'text_reviews_count': 2,
      'publication_date': '12/1/2000',
      'publisher': 'Adventures Unlimited Press'},
     {'bookID': 511,
      'title': 'Boys of Summer',
      'authors': 'Julie Elizabeth Leto/Leslie Kelly/Kimberly Raye',
      'average_rating': 3.77,
      'isbn': '0373792689',
      'isbn13': 9780373792689,
      'language_code': 'eng',
      '  num_pages': 249,
      'ratings_count': 478,
      'text_reviews_count': 12,
      'publication_date': '6/27/2006',
      'publisher': 'Harlequin Blaze'},
     {'bookID': 515,
      'title': "Programming Ruby: The Pragmatic Programmers' Guide",
      'authors': 'Dave Thomas/Chad Fowler/Andy Hunt',
      'average_rating': 4.03,
      'isbn': '0974514055',
      'isbn13': 9780974514055,
      'language_code': 'en-US',
      '  num_pages': 828,
      'ratings_count': 1577,
      'text_reviews_count': 49,
      'publication_date': '10/11/2004',
      'publisher': 'Pragmatic Bookshelf'},
     {'bookID': 523,
      'title': "Golding's Lord of the Flies (Cliffs Notes)",
      'authors': 'Maureen Kelly/CliffsNotes/William Golding',
      'average_rating': 3.95,
      'isbn': '0764585975',
      'isbn13': 9780764585975,
      'language_code': 'eng',
      '  num_pages': 112,
      'ratings_count': 73,
      'text_reviews_count': 8,
      'publication_date': '6/13/2000',
      'publisher': 'Cliffs Notes'},
     {'bookID': 524,
      'title': 'Lord of the Flies',
      'authors': 'William Golding',
      'average_rating': 3.68,
      'isbn': '0307281701',
      'isbn13': 9780307281708,
      'language_code': 'eng',
      '  num_pages': 6,
      'ratings_count': 408,
      'text_reviews_count': 96,
      'publication_date': '10/11/2005',
      'publisher': 'Listening Library (Audio)'},
     {'bookID': 531,
      'title': 'A War Like No Other: How the Athenians & Spartans Fought the Peloponnesian War',
      'authors': 'Victor Davis Hanson',
      'average_rating': 4.11,
      'isbn': '0812969707',
      'isbn13': 9780812969702,
      'language_code': 'eng',
      '  num_pages': 397,
      'ratings_count': 1693,
      'text_reviews_count': 100,
      'publication_date': '9/12/2006',
      'publisher': 'Random House'},
     {'bookID': 534,
      'title': 'We Were Not Like Other People',
      'authors': 'Ephraim Sevela/Antonina W. Bouis',
      'average_rating': 4.14,
      'isbn': '0060255080',
      'isbn13': 9780060255084,
      'language_code': 'eng',
      '  num_pages': 216,
      'ratings_count': 1,
      'text_reviews_count': 0,
      'publication_date': '1/1/1989',
      'publisher': 'HarperCollins Publishers'},
     {'bookID': 537,
      'title': 'The Lovely Bones',
      'authors': 'Alice Sebold',
      'average_rating': 3.81,
      'isbn': '0330485385',
      'isbn13': 9780330485388,
      'language_code': 'en-GB',
      '  num_pages': 328,
      'ratings_count': 6485,
      'text_reviews_count': 966,
      'publication_date': '6/1/2003',
      'publisher': 'Picador'},
     {'bookID': 538,
      'title': 'The Lovely Bones',
      'authors': 'Alice Sebold',
      'average_rating': 3.81,
      'isbn': '159413023X',
      'isbn13': 9781594130236,
      'language_code': 'en-US',
      '  num_pages': 532,
      'ratings_count': 367,
      'text_reviews_count': 73,
      'publication_date': '4/1/2004',
      'publisher': 'Large Print Press'},
     {'bookID': 539,
      'title': 'Lovely in Her Bones (Elizabeth MacPherson  #2)',
      'authors': 'Sharyn McCrumb',
      'average_rating': 3.8,
      'isbn': '0345360354',
      'isbn13': 9780345360359,
      'language_code': 'eng',
      '  num_pages': 224,
      'ratings_count': 1371,
      'text_reviews_count': 43,
      'publication_date': '5/13/1990',
      'publisher': 'Ballantine Books'},
     {'bookID': 565,
      'title': 'The Zen of CSS Design: Visual Enlightenment for the Web',
      'authors': 'Dave Shea/Molly E. Holzschlag',
      'average_rating': 3.98,
      'isbn': '0321303474',
      'isbn13': 785342303476,
      'language_code': 'en-US',
      '  num_pages': 296,
      'ratings_count': 793,
      'text_reviews_count': 28,
      'publication_date': '2/17/2005',
      'publisher': 'Peachpit Press'},
     {'bookID': 570,
      'title': 'HTML  XHTML  and CSS (Visual Quickstart Guide)',
      'authors': 'Elizabeth Castro',
      'average_rating': 3.8,
      'isbn': '0321430840',
      'isbn13': 9780321430847,
      'language_code': 'en-US',
      '  num_pages': 456,
      'ratings_count': 549,
      'text_reviews_count': 42,
      'publication_date': '8/1/2006',
      'publisher': 'Peachpit Press'},
     {'bookID': 576,
      'title': '1000 Record Covers',
      'authors': 'Michael Ochs/Patrick Javault/Ulrike Wasel',
      'average_rating': 3.85,
      'isbn': '3822840858',
      'isbn13': 9783822840856,
      'language_code': 'mul',
      '  num_pages': 575,
      'ratings_count': 288,
      'text_reviews_count': 31,
      'publication_date': '5/15/2005',
      'publisher': 'Taschen'},
     {'bookID': 597,
      'title': 'Killing Yourself to Live: 85% of a True Story',
      'authors': 'Chuck Klosterman',
      'average_rating': 3.81,
      'isbn': '0743264460',
      'isbn13': 9780743264464,
      'language_code': 'eng',
      '  num_pages': 245,
      'ratings_count': 26381,
      'text_reviews_count': 1109,
      'publication_date': '6/13/2006',
      'publisher': 'Scribner'},
     {'bookID': 599,
      'title': 'Sex  Drugs  and Cocoa Puffs: A Low Culture Manifesto',
      'authors': 'Chuck Klosterman',
      'average_rating': 3.73,
      'isbn': '0743236017',
      'isbn13': 9780743236010,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 62089,
      'text_reviews_count': 3324,
      'publication_date': '7/2/2004',
      'publisher': 'Scribner'},
     {'bookID': 619,
      'title': 'Vice (V  #8)',
      'authors': 'Jane Feather',
      'average_rating': 3.51,
      'isbn': '0553572490',
      'isbn13': 9780553572490,
      'language_code': 'eng',
      '  num_pages': 419,
      'ratings_count': 474,
      'text_reviews_count': 19,
      'publication_date': '5/2/1996',
      'publisher': 'Bantam'},
     {'bookID': 629,
      'title': 'Zen and the Art of Motorcycle Maintenance: An Inquiry Into Values (Phaedrus  #1)',
      'authors': 'Robert M. Pirsig',
      'average_rating': 3.77,
      'isbn': '0060589469',
      'isbn13': 9780060589462,
      'language_code': 'eng',
      '  num_pages': 540,
      'ratings_count': 166046,
      'text_reviews_count': 6446,
      'publication_date': '4/25/2006',
      'publisher': 'HarperTorch'},
     {'bookID': 639,
      'title': 'Once Upon a Cool Motorcycle Dude',
      'authors': "Kevin O'Malley/Carol Heyer/Scott Goto",
      'average_rating': 4.08,
      'isbn': '0802789471',
      'isbn13': 9780802789471,
      'language_code': 'eng',
      '  num_pages': 32,
      'ratings_count': 1773,
      'text_reviews_count': 274,
      'publication_date': '4/1/2005',
      'publisher': 'Walker & Company'},
     {'bookID': 642,
      'title': 'Guidebook to Zen and the Art of Motorcycle Maintenance',
      'authors': 'Ronald L. DiSanto/Thomas J. Steele',
      'average_rating': 3.72,
      'isbn': '0688060692',
      'isbn13': 9780688060695,
      'language_code': 'en-GB',
      '  num_pages': 408,
      'ratings_count': 286,
      'text_reviews_count': 10,
      'publication_date': '11/19/1990',
      'publisher': 'William Morrow Paperbacks'},
     {'bookID': 643,
      'title': 'Motorcycle Basics Techbook',
      'authors': 'John Harold Haynes',
      'average_rating': 3.85,
      'isbn': '185960515X',
      'isbn13': 9781859605158,
      'language_code': 'eng',
      '  num_pages': 222,
      'ratings_count': 40,
      'text_reviews_count': 2,
      'publication_date': '7/5/2002',
      'publisher': 'Haynes Manuals N. America  Inc.'},
     {'bookID': 650,
      'title': 'LOGO Lounge: 2 000 International Identities by Leading Designers',
      'authors': 'Catharine M. Fishel/Bill Gardner',
      'average_rating': 3.93,
      'isbn': '1592530877',
      'isbn13': 9781592530878,
      'language_code': 'eng',
      '  num_pages': 191,
      'ratings_count': 27,
      'text_reviews_count': 0,
      'publication_date': '9/1/2004',
      'publisher': 'Rockport Publishers'},
     {'bookID': 655,
      'title': 'The Death of Ivan Ilych And Other Stories',
      'authors': 'Leo Tolstoy/Hugh McLean',
      'average_rating': 4.11,
      'isbn': '0451528808',
      'isbn13': 9780451528803,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 7300,
      'text_reviews_count': 266,
      'publication_date': '4/1/2003',
      'publisher': 'Signet Classics'},
     {'bookID': 656,
      'title': 'War and Peace',
      'authors': 'Leo Tolstoy/Henry Gifford/Aylmer Maude/Louise Maude',
      'average_rating': 4.11,
      'isbn': '0192833987',
      'isbn13': 9780192833983,
      'language_code': 'eng',
      '  num_pages': 1392,
      'ratings_count': 211671,
      'text_reviews_count': 6245,
      'publication_date': '6/25/1998',
      'publisher': 'Oxford University Press'},
     {'bookID': 658,
      'title': 'The Kingdom of God Is Within You',
      'authors': 'Leo Tolstoy/Constance Garnett',
      'average_rating': 4.13,
      'isbn': '0486451380',
      'isbn13': 9780486451381,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 2403,
      'text_reviews_count': 210,
      'publication_date': '9/8/2006',
      'publisher': 'Dover Publications'},
     {'bookID': 662,
      'title': 'Atlas Shrugged',
      'authors': 'Ayn Rand/Leonard Peikoff',
      'average_rating': 3.69,
      'isbn': '0452011876',
      'isbn13': 9780452011878,
      'language_code': 'eng',
      '  num_pages': 1168,
      'ratings_count': 322483,
      'text_reviews_count': 14702,
      'publication_date': '8/1/1999',
      'publisher': 'Plume'},
     {'bookID': 663,
      'title': 'For the New Intellectual: The Philosophy of Ayn Rand',
      'authors': 'Ayn Rand',
      'average_rating': 3.68,
      'isbn': '0451163087',
      'isbn13': 9780451163080,
      'language_code': 'eng',
      '  num_pages': 224,
      'ratings_count': 2750,
      'text_reviews_count': 108,
      'publication_date': '12/1/1963',
      'publisher': 'Signet Book'},
     {'bookID': 664,
      'title': 'The Fountainhead',
      'authors': 'Ayn Rand',
      'average_rating': 3.87,
      'isbn': '0452286751',
      'isbn13': 9780452286757,
      'language_code': 'en-US',
      '  num_pages': 752,
      'ratings_count': 1886,
      'text_reviews_count': 229,
      'publication_date': '4/26/2005',
      'publisher': 'Dutton'},
     {'bookID': 665,
      'title': 'The Virtue of Selfishness: A New Concept of Egoism',
      'authors': 'Ayn Rand/Nathaniel Branden',
      'average_rating': 3.51,
      'isbn': '0451163931',
      'isbn13': 9780451163936,
      'language_code': 'eng',
      '  num_pages': 176,
      'ratings_count': 11462,
      'text_reviews_count': 467,
      'publication_date': '11/1/1964',
      'publisher': 'Signet'},
     {'bookID': 667,
      'title': 'Anthem',
      'authors': 'Ayn Rand',
      'average_rating': 3.63,
      'isbn': '0452281253',
      'isbn13': 9780452281257,
      'language_code': 'eng',
      '  num_pages': 105,
      'ratings_count': 110952,
      'text_reviews_count': 7277,
      'publication_date': '12/1/1999',
      'publisher': 'NAL'},
     {'bookID': 668,
      'title': 'We the Living',
      'authors': 'Ayn Rand/Leonard Peikoff',
      'average_rating': 3.91,
      'isbn': '0451187849',
      'isbn13': 9780451187840,
      'language_code': 'eng',
      '  num_pages': 464,
      'ratings_count': 23199,
      'text_reviews_count': 1086,
      'publication_date': '1/1/1996',
      'publisher': 'Signet'},
     {'bookID': 669,
      'title': 'Capitalism: The Unknown Ideal',
      'authors': 'Ayn Rand/Nathaniel Branden/Alan Greenspan/Robert Hessen',
      'average_rating': 3.88,
      'isbn': '0451147952',
      'isbn13': 9780451147950,
      'language_code': 'eng',
      '  num_pages': 340,
      'ratings_count': 3501,
      'text_reviews_count': 153,
      'publication_date': '7/15/1986',
      'publisher': 'Signet'},
     {'bookID': 670,
      'title': 'Letters of Ayn Rand',
      'authors': 'Ayn Rand/Michael S. Berliner/Leonard Peikoff',
      'average_rating': 3.96,
      'isbn': '0452274044',
      'isbn13': 9780452274044,
      'language_code': 'eng',
      '  num_pages': 681,
      'ratings_count': 18,
      'text_reviews_count': 2,
      'publication_date': '2/1/1997',
      'publisher': 'NAL'},
     {'bookID': 672,
      'title': 'Sailing for Dummies',
      'authors': 'J.J. Isler/Peter Isler',
      'average_rating': 3.95,
      'isbn': '0471791431',
      'isbn13': 9780471791430,
      'language_code': 'eng',
      '  num_pages': 416,
      'ratings_count': 150,
      'text_reviews_count': 7,
      'publication_date': '6/1/2006',
      'publisher': 'For Dummies'},
     {'bookID': 675,
      'title': 'Sailing from Byzantium: How a Lost Empire Shaped the World',
      'authors': 'Colin  Wells',
      'average_rating': 3.88,
      'isbn': '0553803816',
      'isbn13': 9780553803815,
      'language_code': 'eng',
      '  num_pages': 368,
      'ratings_count': 646,
      'text_reviews_count': 83,
      'publication_date': '7/25/2006',
      'publisher': 'Delacorte Press'},
     {'bookID': 676,
      'title': 'Sailing Alone Around the Room: New and Selected Poems',
      'authors': 'Billy Collins',
      'average_rating': 4.23,
      'isbn': '0375755195',
      'isbn13': 9780375755194,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 12180,
      'text_reviews_count': 630,
      'publication_date': '9/17/2002',
      'publisher': 'Random House Trade Paperbacks'},
     {'bookID': 678,
      'title': 'The Greatest Sailing Stories Ever Told: Twenty-Seven Unforgettable Stories',
      'authors': 'Christopher Caswell',
      'average_rating': 3.62,
      'isbn': '1592283195',
      'isbn13': 9781592283194,
      'language_code': 'eng',
      '  num_pages': 286,
      'ratings_count': 51,
      'text_reviews_count': 5,
      'publication_date': '4/1/2004',
      'publisher': 'Lyons Press'},
     {'bookID': 681,
      'title': 'Natural Cures "They" Don\'t Want You to Know about',
      'authors': 'Kevin Trudeau',
      'average_rating': 3.09,
      'isbn': '0975599518',
      'isbn13': 9780975599518,
      'language_code': 'en-US',
      '  num_pages': 571,
      'ratings_count': 1601,
      'text_reviews_count': 284,
      'publication_date': '1/1/2004',
      'publisher': 'Alliance Publishing'},
     {'bookID': 685,
      'title': 'The Natural',
      'authors': 'Bernard Malamud/Kevin Baker',
      'average_rating': 3.63,
      'isbn': '0374502005',
      'isbn13': 9780374502003,
      'language_code': 'eng',
      '  num_pages': 231,
      'ratings_count': 8854,
      'text_reviews_count': 672,
      'publication_date': '7/7/2003',
      'publisher': 'Farrar Straus Giroux'},
     {'bookID': 698,
      'title': 'Digging to America',
      'authors': 'Anne Tyler',
      'average_rating': 3.55,
      'isbn': '0307263940',
      'isbn13': 9780307263940,
      'language_code': 'eng',
      '  num_pages': 277,
      'ratings_count': 17155,
      'text_reviews_count': 1841,
      'publication_date': '5/2/2006',
      'publisher': 'Alfred A. Knopf'},
     {'bookID': 700,
      'title': 'Rereading America: Cultural Contexts for Critical Thinking and Writing',
      'authors': 'Gary Colombo/Bonnie Lisle',
      'average_rating': 3.77,
      'isbn': '0312405545',
      'isbn13': 9780312405540,
      'language_code': 'eng',
      '  num_pages': 826,
      'ratings_count': 44,
      'text_reviews_count': 3,
      'publication_date': '1/21/2004',
      'publisher': 'Bedford Books'},
     {'bookID': 702,
      'title': 'Modern Latin America',
      'authors': 'Thomas E. Skidmore/Peter H. Smith',
      'average_rating': 3.59,
      'isbn': '019517013X',
      'isbn13': 9780195170139,
      'language_code': 'en-US',
      '  num_pages': 528,
      'ratings_count': 234,
      'text_reviews_count': 11,
      'publication_date': '10/7/2004',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 703,
      'title': 'The Plot Against America',
      'authors': 'Philip Roth',
      'average_rating': 3.77,
      'isbn': '1400079497',
      'isbn13': 9781400079490,
      'language_code': 'eng',
      '  num_pages': 391,
      'ratings_count': 33321,
      'text_reviews_count': 2925,
      'publication_date': '9/27/2005',
      'publisher': 'Vintage International'},
     {'bookID': 707,
      'title': 'Naked Pictures of Famous People',
      'authors': 'Jon   Stewart',
      'average_rating': 3.59,
      'isbn': '0688171621',
      'isbn13': 9780688171629,
      'language_code': 'en-GB',
      '  num_pages': 164,
      'ratings_count': 8703,
      'text_reviews_count': 417,
      'publication_date': '9/22/1999',
      'publisher': 'Dey Street Books'},
     {'bookID': 759,
      'title': 'Collected Stories',
      'authors': 'Gabriel Garc??a M??rquez/Gregory Rabassa/J.S. Bernstein',
      'average_rating': 4.19,
      'isbn': '0060932686',
      'isbn13': 9780060932688,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 6375,
      'text_reviews_count': 179,
      'publication_date': '5/13/2008',
      'publisher': 'Harper Perennial Modern Classics'},
     {'bookID': 762,
      'title': 'Cr??nica de una muerte anunciada',
      'authors': 'Gabriel Garc??a M??rquez',
      'average_rating': 3.97,
      'isbn': '1400034957',
      'isbn13': 9781400034956,
      'language_code': 'spa',
      '  num_pages': 118,
      'ratings_count': 7888,
      'text_reviews_count': 411,
      'publication_date': '10/14/2003',
      'publisher': 'Vintage Espanol'},
     {'bookID': 763,
      'title': 'Cien a??os de soledad',
      'authors': 'Gabriel Garc??a M??rquez',
      'average_rating': 4.07,
      'isbn': '0307350428',
      'isbn13': 9780307350428,
      'language_code': 'spa',
      '  num_pages': 496,
      'ratings_count': 130,
      'text_reviews_count': 5,
      'publication_date': '2/7/2006',
      'publisher': 'Plaza y Janes'},
     {'bookID': 764,
      'title': 'Del amor y otros demonios',
      'authors': 'Gabriel Garc??a M??rquez',
      'average_rating': 3.98,
      'isbn': '0307350444',
      'isbn13': 9780307350442,
      'language_code': 'spa',
      '  num_pages': 176,
      'ratings_count': 4508,
      'text_reviews_count': 278,
      'publication_date': '2/7/2006',
      'publisher': 'Plaza y Janes'},
     {'bookID': 765,
      'title': 'Living to Tell the Tale',
      'authors': 'Gabriel Garc??a M??rquez/Edith Grossman',
      'average_rating': 3.99,
      'isbn': '140003454X',
      'isbn13': 9781400034543,
      'language_code': 'eng',
      '  num_pages': 533,
      'ratings_count': 397,
      'text_reviews_count': 47,
      'publication_date': '10/12/2004',
      'publisher': 'Vintage'},
     {'bookID': 766,
      'title': 'Memoria de mis putas tristes',
      'authors': 'Gabriel Garc??a M??rquez',
      'average_rating': 3.6,
      'isbn': '1400095808',
      'isbn13': 9781400095803,
      'language_code': 'spa',
      '  num_pages': 112,
      'ratings_count': 5856,
      'text_reviews_count': 377,
      'publication_date': '10/19/2004',
      'publisher': 'Vintage Espanol'},
     {'bookID': 771,
      'title': 'The Elegant Universe: Superstrings  Hidden Dimensions  and the Quest for the Ultimate Theory',
      'authors': 'Brian Greene',
      'average_rating': 4.07,
      'isbn': '0375708111',
      'isbn13': 9780375708114,
      'language_code': 'eng',
      '  num_pages': 425,
      'ratings_count': 32569,
      'text_reviews_count': 1058,
      'publication_date': '9/2/2004',
      'publisher': 'Vintage Books USA'},
     {'bookID': 775,
      'title': 'Pure and Simple: The Extraordinary Teachings of a Thai Buddhist Laywoman',
      'authors': 'Upasika Kee Nanayon/Thanissaro Bhikkhu',
      'average_rating': 4.29,
      'isbn': '086171492X',
      'isbn13': 9780861714926,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 37,
      'text_reviews_count': 6,
      'publication_date': '5/15/2005',
      'publisher': 'Wisdom Publications'},
     {'bookID': 787,
      'title': 'The Mini Rough Guide to London',
      'authors': 'Rob Humphreys/Beth Chaplin/Rebecca Morrill',
      'average_rating': 3.75,
      'isbn': '184353584X',
      'isbn13': 9781843535843,
      'language_code': 'eng',
      '  num_pages': 363,
      'ratings_count': 1,
      'text_reviews_count': 0,
      'publication_date': '4/1/2006',
      'publisher': 'Rough Guides'},
     {'bookID': 793,
      'title': 'Best of London (Lonely Planet Best Of)',
      'authors': 'Lonely Planet/Sarah Johnstone/Steve Fallon',
      'average_rating': 3.83,
      'isbn': '1740594770',
      'isbn13': 9781740594776,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 11,
      'text_reviews_count': 0,
      'publication_date': '9/1/2004',
      'publisher': 'Lonely Planet'},
     {'bookID': 797,
      'title': 'Lonely Planet Londres',
      'authors': 'Lonely Planet/Sarah Johnstone/Tom Masters',
      'average_rating': 4.03,
      'isbn': '8408064762',
      'isbn13': 9788408064763,
      'language_code': 'spa',
      '  num_pages': 480,
      'ratings_count': 0,
      'text_reviews_count': 0,
      'publication_date': '5/1/2006',
      'publisher': 'Geoplaneta'},
     {'bookID': 799,
      'title': 'Out to Eat London 2002 (Lonely Planet Out to Eat)',
      'authors': 'Lonely Planet/Mark Honan',
      'average_rating': 0.0,
      'isbn': '1740592050',
      'isbn13': 9781740592055,
      'language_code': 'eng',
      '  num_pages': 295,
      'ratings_count': 0,
      'text_reviews_count': 0,
      'publication_date': '9/1/2001',
      'publisher': 'Lonely Planet'},
     {'bookID': 815,
      'title': 'Three Nights in August: Strategy  Heartbreak  and Joy Inside the Mind of a Manager',
      'authors': 'H.G. Bissinger',
      'average_rating': 3.88,
      'isbn': '0618710531',
      'isbn13': 9780618710539,
      'language_code': 'eng',
      '  num_pages': 287,
      'ratings_count': 6870,
      'text_reviews_count': 237,
      'publication_date': '4/4/2006',
      'publisher': 'Mariner Books'},
     {'bookID': 816,
      'title': 'Cryptonomicon',
      'authors': 'Neal Stephenson',
      'average_rating': 4.25,
      'isbn': '0060512806',
      'isbn13': 9780060512804,
      'language_code': 'eng',
      '  num_pages': 1139,
      'ratings_count': 83184,
      'text_reviews_count': 4249,
      'publication_date': '11/1/2002',
      'publisher': 'Avon'},
     {'bookID': 821,
      'title': 'Le R??seau Kinakuta (Cryptonomicon  #2)',
      'authors': 'Neal Stephenson',
      'average_rating': 4.1,
      'isbn': '2228894168',
      'isbn13': 9782228894166,
      'language_code': 'fre',
      '  num_pages': 418,
      'ratings_count': 5,
      'text_reviews_count': 0,
      'publication_date': '3/31/2001',
      'publisher': 'Payot'},
     {'bookID': 822,
      'title': 'The Confusion (The Baroque Cycle  #2)',
      'authors': 'Neal Stephenson',
      'average_rating': 4.26,
      'isbn': '0060733357',
      'isbn13': 9780060733353,
      'language_code': 'en-US',
      '  num_pages': 815,
      'ratings_count': 19320,
      'text_reviews_count': 565,
      'publication_date': '6/14/2005',
      'publisher': 'William Morrow Paperbacks'},
     {'bookID': 823,
      'title': 'Quicksilver (The Baroque Cycle  #1)',
      'authors': 'Neal Stephenson',
      'average_rating': 3.93,
      'isbn': '0060593083',
      'isbn13': 9780060593087,
      'language_code': 'eng',
      '  num_pages': 927,
      'ratings_count': 30872,
      'text_reviews_count': 1735,
      'publication_date': '9/21/2004',
      'publisher': 'HarperCollins Perennial'},
     {'bookID': 824,
      'title': 'The Cobweb',
      'authors': 'Neal Stephenson/J. Frederick George',
      'average_rating': 3.61,
      'isbn': '0553383442',
      'isbn13': 9780553383447,
      'language_code': 'eng',
      '  num_pages': 448,
      'ratings_count': 2465,
      'text_reviews_count': 137,
      'publication_date': '5/31/2005',
      'publisher': 'Spectra Books'},
     {'bookID': 826,
      'title': 'The Big U',
      'authors': 'Neal Stephenson',
      'average_rating': 3.25,
      'isbn': '0380816032',
      'isbn13': 9780380816033,
      'language_code': 'en-US',
      '  num_pages': 308,
      'ratings_count': 4657,
      'text_reviews_count': 223,
      'publication_date': '2/6/2001',
      'publisher': 'William Morrow Paperbacks'},
     {'bookID': 827,
      'title': "The Diamond Age: Or  A Young Lady's Illustrated Primer",
      'authors': 'Neal Stephenson/Pedro Jorge Romero',
      'average_rating': 4.19,
      'isbn': '0553380966',
      'isbn13': 9780553380965,
      'language_code': 'eng',
      '  num_pages': 499,
      'ratings_count': 71042,
      'text_reviews_count': 2767,
      'publication_date': '5/2/2000',
      'publisher': 'Spectra'},
     {'bookID': 828,
      'title': 'Interface',
      'authors': 'Neal Stephenson/George F. Jewsbury/Stephen  Bury',
      'average_rating': 3.68,
      'isbn': '0553383434',
      'isbn13': 9780553383430,
      'language_code': 'eng',
      '  num_pages': 640,
      'ratings_count': 4731,
      'text_reviews_count': 270,
      'publication_date': '5/31/2005',
      'publisher': 'Spectra'},
     {'bookID': 829,
      'title': 'Odalisque (The Baroque Cycle  Vol. 1  Book 3)',
      'authors': 'Neal Stephenson',
      'average_rating': 4.2,
      'isbn': '0060833181',
      'isbn13': 9780060833183,
      'language_code': 'en-US',
      '  num_pages': 464,
      'ratings_count': 1567,
      'text_reviews_count': 65,
      'publication_date': '3/28/2006',
      'publisher': 'HarperTorch'},
     {'bookID': 830,
      'title': 'Snow Crash',
      'authors': 'Neal Stephenson/Guy Abadia',
      'average_rating': 4.03,
      'isbn': '0553380958',
      'isbn13': 9780553380958,
      'language_code': 'eng',
      '  num_pages': 438,
      'ratings_count': 188100,
      'text_reviews_count': 6612,
      'publication_date': '8/2/2000',
      'publisher': 'Bantam Books'},
     {'bookID': 834,
      'title': "Harrington on Hold 'em: Expert Strategy for No-Limit Tournaments  Volume II: The Endgame",
      'authors': 'Dan Harrington/Bill Robertie',
      'average_rating': 4.16,
      'isbn': '1880685353',
      'isbn13': 9781880685358,
      'language_code': 'eng',
      '  num_pages': 450,
      'ratings_count': 1474,
      'text_reviews_count': 30,
      'publication_date': '6/1/2005',
      'publisher': 'Two Plus Two Publishing LLC'},
     {'bookID': 835,
      'title': "Harrington on Hold 'em: Expert Strategy for No-Limit Tournaments  Volume I: Strategic Play",
      'authors': 'Dan Harrington/Bill Robertie',
      'average_rating': 4.24,
      'isbn': '1880685337',
      'isbn13': 9781880685334,
      'language_code': 'eng',
      '  num_pages': 381,
      'ratings_count': 1929,
      'text_reviews_count': 72,
      'publication_date': '12/1/2004',
      'publisher': 'Two Plus Two Publishing LLC'},
     {'bookID': 840,
      'title': 'The Design of Everyday Things',
      'authors': 'Donald A. Norman',
      'average_rating': 4.17,
      'isbn': '0465067107',
      'isbn13': 9780465067107,
      'language_code': 'eng',
      '  num_pages': 240,
      'ratings_count': 18602,
      'text_reviews_count': 1379,
      'publication_date': '9/19/2002',
      'publisher': 'Basic Books'},
     {'bookID': 841,
      'title': 'Emotional Design: Why We Love (or Hate) Everyday Things',
      'authors': 'Donald A. Norman',
      'average_rating': 3.95,
      'isbn': '0465051367',
      'isbn13': 9780465051366,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 3702,
      'text_reviews_count': 149,
      'publication_date': '5/11/2005',
      'publisher': 'Basic Books'},
     {'bookID': 842,
      'title': 'The Psychology of Everyday Things',
      'authors': 'Donald A. Norman',
      'average_rating': 4.17,
      'isbn': '0465067093',
      'isbn13': 9780465067091,
      'language_code': 'eng',
      '  num_pages': 257,
      'ratings_count': 265,
      'text_reviews_count': 31,
      'publication_date': '6/13/1988',
      'publisher': 'Basic Books'},
     {'bookID': 848,
      'title': 'No Price Too High: A Pentecostal Preacher Becomes Catholic - The Inspirational Story of Alex Jones as Told to Diane Hanson',
      'authors': 'Alex C. Jones/Diane M. Hanson/Stephen K. Ray',
      'average_rating': 4.27,
      'isbn': '0898709199',
      'isbn13': 9780898709193,
      'language_code': 'en-GB',
      '  num_pages': 259,
      'ratings_count': 51,
      'text_reviews_count': 7,
      'publication_date': '4/30/2006',
      'publisher': 'Ignatius Press'},
     {'bookID': 864,
      'title': 'The Alchemist',
      'authors': 'Paulo Coelho/Alan R. Clarke/James Noel Smith',
      'average_rating': 3.86,
      'isbn': '0060887966',
      'isbn13': 9780060887964,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 920,
      'text_reviews_count': 76,
      'publication_date': '5/2/2006',
      'publisher': 'HarperOne'},
     {'bookID': 865,
      'title': 'The Alchemist',
      'authors': 'Paulo Coelho/Alan R. Clarke/??zdemir ??nce',
      'average_rating': 3.86,
      'isbn': '0061122416',
      'isbn13': 9780061122415,
      'language_code': 'eng',
      '  num_pages': 197,
      'ratings_count': 1631221,
      'text_reviews_count': 55843,
      'publication_date': '5/1/1993',
      'publisher': 'HarperCollins'},
     {'bookID': 866,
      'title': 'Fullmetal Alchemist  Vol. 9 (Fullmetal Alchemist  #9)',
      'authors': 'Hiromu Arakawa/Akira Watanabe',
      'average_rating': 4.57,
      'isbn': '142150460X',
      'isbn13': 9781421504605,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 9013,
      'text_reviews_count': 153,
      'publication_date': '9/19/2006',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 868,
      'title': 'Fullmetal Alchemist  Vol. 3 (Fullmetal Alchemist  #3)',
      'authors': 'Hiromu Arakawa/Akira Watanabe',
      'average_rating': 4.56,
      'isbn': '1591169259',
      'isbn13': 9781591169253,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 16666,
      'text_reviews_count': 299,
      'publication_date': '9/13/2005',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 869,
      'title': 'Fullmetal Alchemist  Vol. 8 (Fullmetal Alchemist  #8)',
      'authors': 'Hiromu Arakawa/Akira Watanabe',
      'average_rating': 4.57,
      'isbn': '1421504596',
      'isbn13': 9781421504599,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 11451,
      'text_reviews_count': 161,
      'publication_date': '7/18/2006',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 870,
      'title': 'Fullmetal Alchemist  Vol. 1 (Fullmetal Alchemist  #1)',
      'authors': 'Hiromu Arakawa/Akira Watanabe',
      'average_rating': 4.5,
      'isbn': '1591169208',
      'isbn13': 9781591169208,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 111091,
      'text_reviews_count': 1427,
      'publication_date': '5/3/2005',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 871,
      'title': 'Fullmetal Alchemist  Vol. 4 (Fullmetal Alchemist  #4)',
      'authors': 'Hiromu Arakawa/Akira Watanabe',
      'average_rating': 4.55,
      'isbn': '1591169291',
      'isbn13': 9781591169291,
      'language_code': 'eng',
      '  num_pages': 200,
      'ratings_count': 10752,
      'text_reviews_count': 294,
      'publication_date': '11/8/2005',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 872,
      'title': 'The Illustrated Alchemist: A Fable about Following Your Dream',
      'authors': 'Paulo Coelho/Alan R. Clarke/M??bius',
      'average_rating': 3.86,
      'isbn': '006019250X',
      'isbn13': 9780060192501,
      'language_code': 'en-US',
      '  num_pages': 198,
      'ratings_count': 251,
      'text_reviews_count': 32,
      'publication_date': '11/1/1998',
      'publisher': 'HarperCollins Publishers'},
     {'bookID': 873,
      'title': 'Fullmetal Alchemist  Vol. 2 (Fullmetal Alchemist  #2)',
      'authors': 'Hiromu Arakawa/Akira Watanabe',
      'average_rating': 4.52,
      'isbn': '1591169232',
      'isbn13': 9781591169239,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 14923,
      'text_reviews_count': 419,
      'publication_date': '7/5/2005',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 880,
      'title': 'Pompeii',
      'authors': 'Robert   Harris',
      'average_rating': 3.82,
      'isbn': '0812974611',
      'isbn13': 9780812974614,
      'language_code': 'eng',
      '  num_pages': 274,
      'ratings_count': 26922,
      'text_reviews_count': 1726,
      'publication_date': '11/8/2005',
      'publisher': 'Random House Trade Paperbacks'},
     {'bookID': 888,
      'title': 'The Last Days of Pompeii',
      'authors': 'Edward Bulwer-Lytton/John Gregory Betancourt',
      'average_rating': 3.6,
      'isbn': '158715739X',
      'isbn13': 9781587157394,
      'language_code': 'eng',
      '  num_pages': 360,
      'ratings_count': 1156,
      'text_reviews_count': 68,
      'publication_date': '12/3/2002',
      'publisher': 'Borgo Press'},
     {'bookID': 890,
      'title': 'Of Mice and Men',
      'authors': 'John Steinbeck',
      'average_rating': 3.87,
      'isbn': '0142000671',
      'isbn13': 9780142000670,
      'language_code': 'eng',
      '  num_pages': 103,
      'ratings_count': 1755253,
      'text_reviews_count': 25554,
      'publication_date': '1/8/2002',
      'publisher': 'Penguin Books'},
     {'bookID': 900,
      'title': 'The Game: Penetrating the Secret Society of Pickup Artists',
      'authors': 'Neil Strauss',
      'average_rating': 3.74,
      'isbn': '0060554738',
      'isbn13': 9780060554736,
      'language_code': 'en-US',
      '  num_pages': 464,
      'ratings_count': 20529,
      'text_reviews_count': 1592,
      'publication_date': '9/6/2005',
      'publisher': 'It Books'},
     {'bookID': 902,
      'title': 'The Westing Game',
      'authors': 'Ellen Raskin',
      'average_rating': 4.02,
      'isbn': '014240120X',
      'isbn13': 9780142401200,
      'language_code': 'eng',
      '  num_pages': 182,
      'ratings_count': 142121,
      'text_reviews_count': 8782,
      'publication_date': '4/12/2004',
      'publisher': 'Puffin'},
     {'bookID': 903,
      'title': 'The Egypt Game',
      'authors': 'Zilpha Keatley Snyder',
      'average_rating': 3.83,
      'isbn': '0808553038',
      'isbn13': 9780808553038,
      'language_code': 'eng',
      '  num_pages': 215,
      'ratings_count': 30231,
      'text_reviews_count': 1130,
      'publication_date': '7/7/2009',
      'publisher': 'Turtleback Books'},
     {'bookID': 929,
      'title': 'Memoirs of a Geisha',
      'authors': 'Arthur Golden',
      'average_rating': 4.11,
      'isbn': '1400096898',
      'isbn13': 9781400096893,
      'language_code': 'eng',
      '  num_pages': 503,
      'ratings_count': 280309,
      'text_reviews_count': 3703,
      'publication_date': '11/22/2005',
      'publisher': 'Vintage Books USA'},
     {'bookID': 930,
      'title': 'Memoirs of a Geisha',
      'authors': 'Arthur Golden',
      'average_rating': 4.11,
      'isbn': '0739326228',
      'isbn13': 9780739326220,
      'language_code': 'eng',
      '  num_pages': 434,
      'ratings_count': 1301083,
      'text_reviews_count': 19296,
      'publication_date': '11/15/2005',
      'publisher': 'Random House Large Print Publishing'},
     {'bookID': 931,
      'title': 'Memoirs of a Geisha',
      'authors': 'Arthur Golden',
      'average_rating': 4.11,
      'isbn': '0099498189',
      'isbn13': 9780099498186,
      'language_code': 'en-US',
      '  num_pages': 497,
      'ratings_count': 2122,
      'text_reviews_count': 256,
      'publication_date': '12/1/2005',
      'publisher': 'Vintage'},
     {'bookID': 932,
      'title': 'Memoirs of a Geisha: A Portrait of the Film',
      'authors': 'David        James/Peggy Mulloy/Rob Marshall/Arthur Golden',
      'average_rating': 4.08,
      'isbn': '1557046832',
      'isbn13': 9781557046833,
      'language_code': 'eng',
      '  num_pages': 144,
      'ratings_count': 145,
      'text_reviews_count': 8,
      'publication_date': '10/20/2005',
      'publisher': 'Newmarket Press'},
     {'bookID': 933,
      'title': 'Memoirs of a Geisha',
      'authors': 'Arthur Golden',
      'average_rating': 4.11,
      'isbn': '0099771519',
      'isbn13': 9780099771517,
      'language_code': 'eng',
      '  num_pages': 497,
      'ratings_count': 4189,
      'text_reviews_count': 462,
      'publication_date': '6/4/1998',
      'publisher': 'Vintage'},
     {'bookID': 935,
      'title': 'Geisha of Gion',
      'authors': 'Mineko Iwasaki/Rande Brown',
      'average_rating': 3.93,
      'isbn': '074343059X',
      'isbn13': 9780743430593,
      'language_code': 'eng',
      '  num_pages': 334,
      'ratings_count': 1556,
      'text_reviews_count': 158,
      'publication_date': '5/6/2003',
      'publisher': 'Pocket Books'},
     {'bookID': 941,
      'title': 'Love As A Foreign Language #5',
      'authors': 'J. Torres/Eric  Kim',
      'average_rating': 3.44,
      'isbn': '1932664394',
      'isbn13': 9781932664393,
      'language_code': 'eng',
      '  num_pages': 58,
      'ratings_count': 9,
      'text_reviews_count': 2,
      'publication_date': '2/1/2006',
      'publisher': 'Oni Press'},
     {'bookID': 944,
      'title': 'Jungle Love',
      'authors': 'Margaret Johnson/Philip Prowse',
      'average_rating': 3.41,
      'isbn': '0521750849',
      'isbn13': 9780521750844,
      'language_code': 'eng',
      '  num_pages': 95,
      'ratings_count': 59,
      'text_reviews_count': 7,
      'publication_date': '8/1/2002',
      'publisher': 'Cambridge University Press'},
     {'bookID': 955,
      'title': 'The 5 Love Languages / The 5 Love Languages Journal',
      'authors': 'Gary Chapman',
      'average_rating': 4.7,
      'isbn': '0802415318',
      'isbn13': 9780802415318,
      'language_code': 'eng',
      '  num_pages': 0,
      'ratings_count': 22,
      'text_reviews_count': 4,
      'publication_date': '1/1/2005',
      'publisher': 'Moody Publishers'},
     {'bookID': 960,
      'title': 'Angels & Demons (Robert Langdon  #1)',
      'authors': 'Dan Brown',
      'average_rating': 3.89,
      'isbn': '1416524797',
      'isbn13': 9781416524793,
      'language_code': 'eng',
      '  num_pages': 736,
      'ratings_count': 2418736,
      'text_reviews_count': 21303,
      'publication_date': '4/1/2006',
      'publisher': 'Pocket Books'},
     {'bookID': 965,
      'title': '??ngeles y demonios (Robert Langdon  #1)',
      'authors': 'Dan Brown',
      'average_rating': 3.89,
      'isbn': '849561877X',
      'isbn13': 9788495618771,
      'language_code': 'spa',
      '  num_pages': 508,
      'ratings_count': 196,
      'text_reviews_count': 20,
      'publication_date': '12/1/2005',
      'publisher': 'Umbriel'},
     {'bookID': 966,
      'title': 'Angeles & Demonios',
      'authors': 'Dan Brown/Ra??l Amundaray',
      'average_rating': 3.89,
      'isbn': '0972859896',
      'isbn13': 9780972859899,
      'language_code': 'spa',
      '  num_pages': 18,
      'ratings_count': 65,
      'text_reviews_count': 7,
      'publication_date': '12/1/2005',
      'publisher': 'FonoLibro'},
     {'bookID': 968,
      'title': 'The Da Vinci Code (Robert Langdon  #2)',
      'authors': 'Dan Brown',
      'average_rating': 3.84,
      'isbn': '0307277674',
      'isbn13': 9780307277671,
      'language_code': 'eng',
      '  num_pages': 489,
      'ratings_count': 1679706,
      'text_reviews_count': 35877,
      'publication_date': '3/28/2006',
      'publisher': 'Anchor'},
     {'bookID': 969,
      'title': 'The Da Vinci Code',
      'authors': 'Dan Brown',
      'average_rating': 3.84,
      'isbn': '076792603X',
      'isbn13': 9780767926034,
      'language_code': 'eng',
      '  num_pages': 467,
      'ratings_count': 1120,
      'text_reviews_count': 105,
      'publication_date': '3/28/2006',
      'publisher': 'Broadway Books'},
     {'bookID': 972,
      'title': 'Da Vinci Code (Robert Langdon  #2)',
      'authors': 'Dan Brown/Daniel Roche',
      'average_rating': 3.84,
      'isbn': '2266144340',
      'isbn13': 9782266144346,
      'language_code': 'fre',
      '  num_pages': 744,
      'ratings_count': 377,
      'text_reviews_count': 16,
      'publication_date': '5/3/2005',
      'publisher': 'Pocket'},
     {'bookID': 975,
      'title': 'Deception Point',
      'authors': 'Dan Brown',
      'average_rating': 3.71,
      'isbn': '1416524800',
      'isbn13': 9781416524809,
      'language_code': 'eng',
      '  num_pages': 736,
      'ratings_count': 4919,
      'text_reviews_count': 410,
      'publication_date': '4/1/2006',
      'publisher': 'Pocket Books'},
     {'bookID': 977,
      'title': 'Deception Point',
      'authors': 'Dan Brown',
      'average_rating': 3.71,
      'isbn': '0552151769',
      'isbn13': 9780552151764,
      'language_code': 'eng',
      '  num_pages': 585,
      'ratings_count': 3353,
      'text_reviews_count': 183,
      'publication_date': '5/1/2004',
      'publisher': 'Corgi Books'},
     {'bookID': 980,
      'title': 'Deception Point',
      'authors': 'Dan Brown',
      'average_rating': 3.71,
      'isbn': '0593055071',
      'isbn13': 9780593055076,
      'language_code': 'eng',
      '  num_pages': 448,
      'ratings_count': 61,
      'text_reviews_count': 4,
      'publication_date': '8/1/2005',
      'publisher': 'Bantam Press'},
     {'bookID': 987,
      'title': 'A Killing Rain (Louis Kincaid  #6)',
      'authors': 'P.J. Parrish',
      'average_rating': 4.04,
      'isbn': '078601606X',
      'isbn13': 9780786016068,
      'language_code': 'eng',
      '  num_pages': 383,
      'ratings_count': 456,
      'text_reviews_count': 41,
      'publication_date': '2/1/2005',
      'publisher': 'Pinnacle'},
     {'bookID': 998,
      'title': "The Millionaire Next Door: The Surprising Secrets of America's Wealthy",
      'authors': 'Thomas J. Stanley/William D. Danko',
      'average_rating': 4.03,
      'isbn': '0671015206',
      'isbn13': 9780671015206,
      'language_code': 'eng',
      '  num_pages': 258,
      'ratings_count': 61760,
      'text_reviews_count': 2600,
      'publication_date': '10/1/1998',
      'publisher': 'Gallery Books'},
     {'bookID': 1005,
      'title': 'Think and Grow Rich: The Landmark Bestseller Now Revised and Updated for the 21st Century',
      'authors': 'Napoleon Hill',
      'average_rating': 4.18,
      'isbn': '1585424331',
      'isbn13': 9781585424337,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 88897,
      'text_reviews_count': 2334,
      'publication_date': '9/1/2005',
      'publisher': 'Tarcherperigee'},
     {'bookID': 1007,
      'title': 'Think and Grow Rich',
      'authors': 'Napoleon Hill',
      'average_rating': 4.18,
      'isbn': '1932429239',
      'isbn13': 9781932429237,
      'language_code': 'eng',
      '  num_pages': 368,
      'ratings_count': 48,
      'text_reviews_count': 9,
      'publication_date': '8/7/2004',
      'publisher': 'High Roads Media'},
     {'bookID': 1014,
      'title': 'Pragmatic Version Control: Using Subversion (The Pragmatic Starter Kit Series)',
      'authors': 'Mike   Mason',
      'average_rating': 3.58,
      'isbn': '0977616657',
      'isbn13': 9780977616657,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 173,
      'text_reviews_count': 14,
      'publication_date': '6/7/2006',
      'publisher': 'Pragmatic Bookshelf'},
     {'bookID': 1022,
      'title': 'Read My Lips: Sexual Subversion and the End of Gender',
      'authors': 'Riki Anne Wilchins',
      'average_rating': 3.95,
      'isbn': '1563410907',
      'isbn13': 9781563410901,
      'language_code': 'en-US',
      '  num_pages': 288,
      'ratings_count': 253,
      'text_reviews_count': 17,
      'publication_date': '6/1/2005',
      'publisher': 'Firebrand Books'},
     {'bookID': 1032,
      'title': 'Trump: The Art of the Deal',
      'authors': 'Donald J. Trump/Tony Schwartz',
      'average_rating': 3.66,
      'isbn': '0345479173',
      'isbn13': 9780345479174,
      'language_code': 'en-US',
      '  num_pages': 384,
      'ratings_count': 12748,
      'text_reviews_count': 948,
      'publication_date': '12/28/2004',
      'publisher': 'Ballantine Books'},
     {'bookID': 1052,
      'title': 'The Richest Man in Babylon',
      'authors': 'George S. Clason',
      'average_rating': 4.26,
      'isbn': '0451205367',
      'isbn13': 9780451205360,
      'language_code': 'eng',
      '  num_pages': 194,
      'ratings_count': 76451,
      'text_reviews_count': 3400,
      'publication_date': '2/1/2008',
      'publisher': 'Berkley Books'},
     {'bookID': 1053,
      'title': 'The Richest Man in Babylon',
      'authors': 'George S. Clason',
      'average_rating': 4.26,
      'isbn': '1419349996',
      'isbn13': 9781419349997,
      'language_code': 'eng',
      '  num_pages': 4,
      'ratings_count': 86,
      'text_reviews_count': 15,
      'publication_date': '6/17/2005',
      'publisher': 'Recorded Books  Inc.'},
     {'bookID': 1059,
      'title': 'Shibumi',
      'authors': 'Trevanian/Gisela Stege',
      'average_rating': 4.21,
      'isbn': '1400098033',
      'isbn13': 9781400098033,
      'language_code': 'eng',
      '  num_pages': 480,
      'ratings_count': 9498,
      'text_reviews_count': 637,
      'publication_date': '5/10/2005',
      'publisher': 'Broadway Books'},
     {'bookID': 1067,
      'title': '1776',
      'authors': 'David McCullough',
      'average_rating': 4.07,
      'isbn': '0743226720',
      'isbn13': 9780743226721,
      'language_code': 'eng',
      '  num_pages': 386,
      'ratings_count': 166916,
      'text_reviews_count': 6243,
      'publication_date': '7/4/2006',
      'publisher': 'Simon  Schuster'},
     {'bookID': 1068,
      'title': '1776',
      'authors': 'Peter  Stone/Sherman Edwards',
      'average_rating': 4.22,
      'isbn': '0140481397',
      'isbn13': 9780140481396,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 1299,
      'text_reviews_count': 30,
      'publication_date': '11/18/1976',
      'publisher': 'Penguin Books'},
     {'bookID': 1073,
      'title': 'The Crescent Obscured: The United States and the Muslim World  1776-1815',
      'authors': 'Robert J. Allison',
      'average_rating': 3.62,
      'isbn': '0226014908',
      'isbn13': 9780226014906,
      'language_code': 'eng',
      '  num_pages': 284,
      'ratings_count': 31,
      'text_reviews_count': 5,
      'publication_date': '7/15/2000',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1078,
      'title': 'The Good Earth (House of Earth  #1)',
      'authors': 'Pearl S. Buck',
      'average_rating': 3.98,
      'isbn': '1416500189',
      'isbn13': 9781416500186,
      'language_code': 'eng',
      '  num_pages': 418,
      'ratings_count': 200744,
      'text_reviews_count': 7656,
      'publication_date': '3/4/2009',
      'publisher': 'Howard Publishing Co'},
     {'bookID': 1090,
      'title': 'Purpose Driven Life - For Commuters: What on Earth Am I Here For?',
      'authors': 'Rick Warren',
      'average_rating': 3.93,
      'isbn': '0310258979',
      'isbn13': 9780310258971,
      'language_code': 'eng',
      '  num_pages': 5,
      'ratings_count': 26,
      'text_reviews_count': 2,
      'publication_date': '3/15/2005',
      'publisher': 'Zondervan'},
     {'bookID': 1097,
      'title': 'Fast Food Nation: The Dark Side of the All-American Meal',
      'authors': 'Eric Schlosser',
      'average_rating': 3.74,
      'isbn': '0060838582',
      'isbn13': 9780060838584,
      'language_code': 'eng',
      '  num_pages': 399,
      'ratings_count': 190039,
      'text_reviews_count': 4922,
      'publication_date': '7/5/2005',
      'publisher': 'Harper Perennial'},
     {'bookID': 1099,
      'title': 'Fast Food Nation: What The All-American Meal is Doing to the World',
      'authors': 'Eric Schlosser',
      'average_rating': 3.74,
      'isbn': '0141006870',
      'isbn13': 9780141006871,
      'language_code': 'eng',
      '  num_pages': 384,
      'ratings_count': 811,
      'text_reviews_count': 77,
      'publication_date': '4/4/2002',
      'publisher': 'Penguin Books'},
     {'bookID': 1103,
      'title': 'Snow Flower and the Secret Fan',
      'authors': 'Lisa See',
      'average_rating': 4.07,
      'isbn': '0812968069',
      'isbn13': 9780812968064,
      'language_code': 'eng',
      '  num_pages': 269,
      'ratings_count': 297533,
      'text_reviews_count': 14935,
      'publication_date': '2/21/2006',
      'publisher': 'Random House'},
     {'bookID': 1110,
      'title': 'The Broker',
      'authors': 'John Grisham',
      'average_rating': 3.78,
      'isbn': '0385340540',
      'isbn13': 9780385340540,
      'language_code': 'eng',
      '  num_pages': 422,
      'ratings_count': 72361,
      'text_reviews_count': 2334,
      'publication_date': '9/26/2006',
      'publisher': 'Delta'},
     {'bookID': 1111,
      'title': 'The Power Broker: Robert Moses and the Fall of New York',
      'authors': 'Robert A. Caro',
      'average_rating': 4.51,
      'isbn': '0394720245',
      'isbn13': 9780394720241,
      'language_code': 'eng',
      '  num_pages': 1344,
      'ratings_count': 11208,
      'text_reviews_count': 1237,
      'publication_date': '7/12/1975',
      'publisher': 'Vintage'},
     {'bookID': 1117,
      'title': 'The Power Broker: A Novel (Christian Gillette  #3)',
      'authors': 'Stephen W. Frey',
      'average_rating': 3.75,
      'isbn': '0345480600',
      'isbn13': 9780345480606,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 28,
      'text_reviews_count': 1,
      'publication_date': '7/25/2006',
      'publisher': 'Ballantine Books'},
     {'bookID': 1120,
      'title': 'Body For Life: 12 Weeks to Mental and Physical Strength',
      'authors': "Bill Phillips/Michael D'Orso",
      'average_rating': 3.74,
      'isbn': '0060193395',
      'isbn13': 9780060193393,
      'language_code': 'en-US',
      '  num_pages': 201,
      'ratings_count': 3877,
      'text_reviews_count': 275,
      'publication_date': '6/10/1999',
      'publisher': 'HarperCollins Publishers  Inc.'},
     {'bookID': 1121,
      'title': "Body for Life for Women: A Woman's Plan for Physical and Mental Transformation",
      'authors': 'Pamela Peeke/Cindy Crawford',
      'average_rating': 3.65,
      'isbn': '1579546013',
      'isbn13': 9781579546014,
      'language_code': 'en-US',
      '  num_pages': 288,
      'ratings_count': 401,
      'text_reviews_count': 63,
      'publication_date': '4/1/2005',
      'publisher': 'Rodale Books'},
     {'bookID': 1123,
      'title': 'Eating for Life: Your Guide to Great Health  Fat Loss and Increased Energy!',
      'authors': 'Bill Phillips',
      'average_rating': 3.95,
      'isbn': '0972018417',
      'isbn13': 9780972018418,
      'language_code': 'eng',
      '  num_pages': 405,
      'ratings_count': 814,
      'text_reviews_count': 51,
      'publication_date': '11/26/2003',
      'publisher': 'High Point Media'},
     {'bookID': 1130,
      'title': 'The Warren Buffett Way',
      'authors': 'Robert G. Hagstrom/Bill Miller/Kenneth L. Fisher',
      'average_rating': 4.13,
      'isbn': '0471743674',
      'isbn13': 9780471743675,
      'language_code': 'en-US',
      '  num_pages': 245,
      'ratings_count': 228,
      'text_reviews_count': 16,
      'publication_date': '10/1/2005',
      'publisher': 'John Wiley & Sons'},
     {'bookID': 1138,
      'title': 'The Warren Buffett CEO: Secrets from the Berkshire Hathaway Managers',
      'authors': 'Robert P. Miles/Tom Osborne',
      'average_rating': 4.07,
      'isbn': '0471430455',
      'isbn13': 9780471430452,
      'language_code': 'eng',
      '  num_pages': 432,
      'ratings_count': 39,
      'text_reviews_count': 1,
      'publication_date': '4/18/2003',
      'publisher': 'Wiley'},
     {'bookID': 1164,
      'title': 'Monkey Business: True Story of the Scopes Trial',
      'authors': 'Marvin N. Olasky/John R. Perry',
      'average_rating': 3.15,
      'isbn': '0805431578',
      'isbn13': 9780805431575,
      'language_code': 'eng',
      '  num_pages': 368,
      'ratings_count': 26,
      'text_reviews_count': 8,
      'publication_date': '5/15/2005',
      'publisher': 'B Books'},
     {'bookID': 1167,
      'title': 'Junie B. Jones and a Little Monkey Business (Junie B. Jones  #2)',
      'authors': 'Barbara Park/Denise Brunkus',
      'average_rating': 3.99,
      'isbn': '0679838864',
      'isbn13': 9780679838869,
      'language_code': 'en-US',
      '  num_pages': 68,
      'ratings_count': 11178,
      'text_reviews_count': 623,
      'publication_date': '2/16/1993',
      'publisher': 'Random House Books for Young Readers'},
     {'bookID': 1169,
      'title': 'Monkey Business',
      'authors': 'Sarah Mlynowski',
      'average_rating': 3.67,
      'isbn': '0373250711',
      'isbn13': 9780373250714,
      'language_code': 'eng',
      '  num_pages': 392,
      'ratings_count': 3379,
      'text_reviews_count': 67,
      'publication_date': '9/24/2004',
      'publisher': 'Red Dress Ink'},
     {'bookID': 1171,
      'title': "Liar's Poker",
      'authors': 'Michael   Lewis',
      'average_rating': 4.15,
      'isbn': '0140143459',
      'isbn13': 9780140143454,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 22843,
      'text_reviews_count': 936,
      'publication_date': '10/1/1990',
      'publisher': 'Penguin Books'},
     {'bookID': 1177,
      'title': "Liar's Poker: A Harry Garnish Mystery",
      'authors': 'Frank McConnell',
      'average_rating': 3.31,
      'isbn': '0802732291',
      'isbn13': 9780802732293,
      'language_code': 'eng',
      '  num_pages': 214,
      'ratings_count': 13,
      'text_reviews_count': 1,
      'publication_date': '6/1/1993',
      'publisher': 'Walker & Company'},
     {'bookID': 1188,
      'title': 'Risotto: 30 Simply Delicious Vegetarian Recipes from an Italian Kitchen',
      'authors': 'Ursula Ferrigno/Jason Lowe/Maxine  Clark',
      'average_rating': 4.08,
      'isbn': '1841721476',
      'isbn13': 694055000612,
      'language_code': 'eng',
      '  num_pages': 64,
      'ratings_count': 8,
      'text_reviews_count': 2,
      'publication_date': '3/1/2001',
      'publisher': 'Ryland Peters & Small'},
     {'bookID': 1191,
      'title': "Giada's Family Dinners",
      'authors': 'Giada De Laurentiis/Victoria Pearson',
      'average_rating': 3.96,
      'isbn': '030723827X',
      'isbn13': 9780307238276,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 14103,
      'text_reviews_count': 74,
      'publication_date': '4/4/2006',
      'publisher': 'Clarkson Potter'},
     {'bookID': 1192,
      'title': 'Everyday Italian: 125 Simple and Delicious Recipes',
      'authors': 'Giada De Laurentiis',
      'average_rating': 3.95,
      'isbn': '1400052580',
      'isbn13': 9781400052585,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 40125,
      'text_reviews_count': 217,
      'publication_date': '2/22/2005',
      'publisher': 'Clarkson Potter'},
     {'bookID': 1193,
      'title': 'Everyday Pasta',
      'authors': 'Giada De Laurentiis/Victoria Pearson',
      'average_rating': 4.09,
      'isbn': '0307346587',
      'isbn13': 9780307346582,
      'language_code': 'eng',
      '  num_pages': 240,
      'ratings_count': 8822,
      'text_reviews_count': 55,
      'publication_date': '4/3/2007',
      'publisher': 'Clarkson Potter'},
     {'bookID': 1196,
      'title': "Tyler's Ultimate: Brilliant Simple Food to Make Any Time",
      'authors': 'Tyler Florence/Petrina Tinslay',
      'average_rating': 4.09,
      'isbn': '1400052386',
      'isbn13': 9781400052387,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 3697,
      'text_reviews_count': 34,
      'publication_date': '9/26/2006',
      'publisher': 'Clarkson Potter'},
     {'bookID': 1197,
      'title': "Tyler Florence's Real Kitchen: An Indespensible Guide for Anybody Who Likes to Cook",
      'authors': 'Tyler Florence/JoAnn Cianciulli/Bill Bettencourt/Bobby Flay',
      'average_rating': 4.06,
      'isbn': '0609609971',
      'isbn13': 9780609609972,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 1426,
      'text_reviews_count': 16,
      'publication_date': '3/25/2003',
      'publisher': 'Clarkson Potter Publishers'},
     {'bookID': 1198,
      'title': 'Eat This Book: Cooking with Global Fresh Flavors',
      'authors': 'Tyler Florence/Petrina Tinslay',
      'average_rating': 3.92,
      'isbn': '1400052378',
      'isbn13': 9781400052370,
      'language_code': 'eng',
      '  num_pages': 287,
      'ratings_count': 275,
      'text_reviews_count': 15,
      'publication_date': '10/1/2004',
      'publisher': 'Clarkson Potter Publishers'},
     {'bookID': 1202,
      'title': 'Freakonomics: A Rogue Economist Explores the Hidden Side of Everything',
      'authors': 'Steven D. Levitt/Stephen J. Dubner',
      'average_rating': 3.97,
      'isbn': '0061234001',
      'isbn13': 9780061234002,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 628745,
      'text_reviews_count': 13034,
      'publication_date': '10/17/2006',
      'publisher': 'William Morrow'},
     {'bookID': 1204,
      'title': 'Freakonomics: Un economista pol??ticamente incorrecto explora el lado oculto de lo que nos afecta',
      'authors': 'Steven D. Levitt/Stephen J. Dubner',
      'average_rating': 3.97,
      'isbn': '8466625127',
      'isbn13': 9788466625128,
      'language_code': 'spa',
      '  num_pages': 250,
      'ratings_count': 193,
      'text_reviews_count': 23,
      'publication_date': '8/1/2006',
      'publisher': 'Ediciones B'},
     {'bookID': 1206,
      'title': 'Freakonomics: A Rogue Economist Explores the Hidden Side of Everything',
      'authors': 'Steven D. Levitt/Stephen J. Dubner',
      'average_rating': 3.97,
      'isbn': '0061245135',
      'isbn13': 9780061245138,
      'language_code': 'en-US',
      '  num_pages': 496,
      'ratings_count': 98,
      'text_reviews_count': 5,
      'publication_date': '12/8/2006',
      'publisher': 'Harper'},
     {'bookID': 1218,
      'title': 'The Last Assassin (John Rain  #5)',
      'authors': 'Barry Eisler',
      'average_rating': 4.27,
      'isbn': '0399153594',
      'isbn13': 9780399153594,
      'language_code': 'eng',
      '  num_pages': 338,
      'ratings_count': 189,
      'text_reviews_count': 25,
      'publication_date': '6/1/2006',
      'publisher': 'Putnam Publishing Group'},
     {'bookID': 1226,
      'title': 'Life of Pi',
      'authors': 'Yann Martel',
      'average_rating': 3.91,
      'isbn': '0156030209',
      'isbn13': 9780156030205,
      'language_code': 'en-US',
      '  num_pages': 401,
      'ratings_count': 4318,
      'text_reviews_count': 668,
      'publication_date': '5/3/2004',
      'publisher': 'Mariner Books / Harvest Books'},
     {'bookID': 1230,
      'title': "L'Histoire de Pi",
      'authors': 'Yann Martel/Nicole Martel/Emile Martel',
      'average_rating': 3.91,
      'isbn': '0828808392',
      'isbn13': 9780828808392,
      'language_code': 'fre',
      '  num_pages': 448,
      'ratings_count': 177,
      'text_reviews_count': 26,
      'publication_date': '11/24/2005',
      'publisher': 'Gallimard'},
     {'bookID': 1234,
      'title': 'Shadows and Wind: A View of Modern Vietnam',
      'authors': 'Robert Templer',
      'average_rating': 3.49,
      'isbn': '0140285970',
      'isbn13': 9780140285970,
      'language_code': 'eng',
      '  num_pages': 400,
      'ratings_count': 102,
      'text_reviews_count': 8,
      'publication_date': '9/1/1999',
      'publisher': 'Penguin Books'},
     {'bookID': 1241,
      'title': 'A Million Little Pieces',
      'authors': 'James Frey',
      'average_rating': 3.65,
      'isbn': '0307276902',
      'isbn13': 9780307276902,
      'language_code': 'eng',
      '  num_pages': 515,
      'ratings_count': 206011,
      'text_reviews_count': 10821,
      'publication_date': '9/22/2005',
      'publisher': 'Anchor Books'},
     {'bookID': 1242,
      'title': 'A Million Little Pieces of Feces',
      'authors': 'Python Bonkers',
      'average_rating': 3.56,
      'isbn': '1411677315',
      'isbn13': 9781411677319,
      'language_code': 'en-US',
      '  num_pages': 256,
      'ratings_count': 43,
      'text_reviews_count': 6,
      'publication_date': '2/10/2006',
      'publisher': 'Lulu.com'},
     {'bookID': 1243,
      'title': 'A Million Little Lies',
      'authors': 'James Pinocchio/Pablo Fenjves',
      'average_rating': 3.41,
      'isbn': '0061171468',
      'isbn13': 9780061171468,
      'language_code': 'en-US',
      '  num_pages': 191,
      'ratings_count': 201,
      'text_reviews_count': 24,
      'publication_date': '3/28/2006',
      'publisher': 'William Morrow Paperbacks'},
     {'bookID': 1246,
      'title': 'The Leadership Challenge',
      'authors': 'James M. Kouzes/Barry Z. Posner',
      'average_rating': 4.05,
      'isbn': '0787968331',
      'isbn13': 9780787968335,
      'language_code': 'en-US',
      '  num_pages': 458,
      'ratings_count': 873,
      'text_reviews_count': 40,
      'publication_date': '8/7/2003',
      'publisher': 'Jossey-Bass'},
     {'bookID': 1252,
      'title': 'Lincoln on Leadership: Executive Strategies for Tough Times',
      'authors': 'Donald T. Phillips',
      'average_rating': 4.14,
      'isbn': '0446394599',
      'isbn13': 9780446394598,
      'language_code': 'eng',
      '  num_pages': 193,
      'ratings_count': 5354,
      'text_reviews_count': 281,
      'publication_date': '2/1/1993',
      'publisher': 'Business Plus'},
     {'bookID': 1255,
      'title': 'Leadership in Organizations',
      'authors': 'Gary Yukl',
      'average_rating': 3.68,
      'isbn': '0131494848',
      'isbn13': 9780131494848,
      'language_code': 'en-GB',
      '  num_pages': 542,
      'ratings_count': 55,
      'text_reviews_count': 4,
      'publication_date': '7/7/2005',
      'publisher': 'Prentice Hall'},
     {'bookID': 1265,
      'title': 'Leadership',
      'authors': 'Rudolph W. Giuliani',
      'average_rating': 3.72,
      'isbn': '0316861014',
      'isbn13': 9780316861014,
      'language_code': 'eng',
      '  num_pages': 397,
      'ratings_count': 1820,
      'text_reviews_count': 147,
      'publication_date': '10/1/2002',
      'publisher': 'Little  Brown'},
     {'bookID': 1274,
      'title': 'Men Are from Mars  Women Are from Venus',
      'authors': 'John Gray',
      'average_rating': 3.55,
      'isbn': '0060574216',
      'isbn13': 9780060574215,
      'language_code': 'eng',
      '  num_pages': 368,
      'ratings_count': 132062,
      'text_reviews_count': 3303,
      'publication_date': '4/3/2012',
      'publisher': 'Harper Paperbacks'},
     {'bookID': 1276,
      'title': 'Mars and Venus Book of Days: 365 Inspriations to Enrich Your Relationships',
      'authors': 'John Gray',
      'average_rating': 3.62,
      'isbn': '0060192771',
      'isbn13': 9780060192778,
      'language_code': 'en-US',
      '  num_pages': 368,
      'ratings_count': 18,
      'text_reviews_count': 1,
      'publication_date': '10/21/1998',
      'publisher': 'Harper'},
     {'bookID': 1281,
      'title': 'Men Are from Mars  Women Are from Venus',
      'authors': 'John Gray',
      'average_rating': 3.55,
      'isbn': '006123205X',
      'isbn13': 9780061232053,
      'language_code': 'eng',
      '  num_pages': 2,
      'ratings_count': 43,
      'text_reviews_count': 3,
      'publication_date': '4/3/2007',
      'publisher': 'HarperAudio'},
     {'bookID': 1290,
      'title': 'How to Succeed with Women',
      'authors': 'Ron  Louis/David Copeland',
      'average_rating': 3.76,
      'isbn': '0735200300',
      'isbn13': 9780735200302,
      'language_code': 'en-US',
      '  num_pages': 320,
      'ratings_count': 82,
      'text_reviews_count': 13,
      'publication_date': '10/29/1998',
      'publisher': 'Prentice Hall Press'},
     {'bookID': 1295,
      'title': "The Clan of the Cave Bear (Earth's Children  #1)",
      'authors': 'Jean M. Auel',
      'average_rating': 4.05,
      'isbn': '0553381679',
      'isbn13': 9780553381672,
      'language_code': 'eng',
      '  num_pages': 512,
      'ratings_count': 184418,
      'text_reviews_count': 4432,
      'publication_date': '6/25/2002',
      'publisher': 'Bantam'},
     {'bookID': 1296,
      'title': "The Clan of the Cave Bear (Earth's Children  #1)",
      'authors': 'Jean M. Auel',
      'average_rating': 4.05,
      'isbn': '0517542021',
      'isbn13': 9780517542026,
      'language_code': 'eng',
      '  num_pages': 468,
      'ratings_count': 495,
      'text_reviews_count': 67,
      'publication_date': '5/4/1980',
      'publisher': 'Crown Publishing Group'},
     {'bookID': 1301,
      'title': 'Moneyball: The Art of Winning an Unfair Game',
      'authors': 'Michael   Lewis',
      'average_rating': 4.26,
      'isbn': '0393324818',
      'isbn13': 9780393324815,
      'language_code': 'eng',
      '  num_pages': 317,
      'ratings_count': 85094,
      'text_reviews_count': 4155,
      'publication_date': '3/17/2004',
      'publisher': 'W. W. Norton  Company'},
     {'bookID': 1302,
      'title': 'Juiced Official Strategy Guide',
      'authors': 'Doug Walsh',
      'average_rating': 0.0,
      'isbn': '0744005612',
      'isbn13': 9780744005615,
      'language_code': 'eng',
      '  num_pages': 112,
      'ratings_count': 0,
      'text_reviews_count': 0,
      'publication_date': '6/1/2005',
      'publisher': 'BradyGames'},
     {'bookID': 1303,
      'title': 'The 48 Laws of Power',
      'authors': 'Robert Greene/Joost Elffers',
      'average_rating': 4.18,
      'isbn': '0140280197',
      'isbn13': 9780140280197,
      'language_code': 'eng',
      '  num_pages': 452,
      'ratings_count': 60946,
      'text_reviews_count': 3167,
      'publication_date': '9/1/2000',
      'publisher': 'Penguin (Business)'},
     {'bookID': 1305,
      'title': 'Gates of Fire',
      'authors': 'Steven Pressfield',
      'average_rating': 4.42,
      'isbn': '055338368X',
      'isbn13': 9780553383683,
      'language_code': 'eng',
      '  num_pages': 392,
      'ratings_count': 21934,
      'text_reviews_count': 1629,
      'publication_date': '9/27/2005',
      'publisher': 'Bantam'},
     {'bookID': 1307,
      'title': 'Fire Sea (The Death Gate Cycle  #3)',
      'authors': 'Margaret Weis/Tracy Hickman',
      'average_rating': 4.07,
      'isbn': '0553295411',
      'isbn13': 9780553295412,
      'language_code': 'eng',
      '  num_pages': 414,
      'ratings_count': 16312,
      'text_reviews_count': 175,
      'publication_date': '3/1/1992',
      'publisher': 'Spectra Books'},
     {'bookID': 1312,
      'title': 'The Gate of Fire (Oath Of Empire Book Two)',
      'authors': 'Thomas Harlan',
      'average_rating': 3.58,
      'isbn': '0812590104',
      'isbn13': 9780812590104,
      'language_code': 'en-US',
      '  num_pages': 721,
      'ratings_count': 146,
      'text_reviews_count': 4,
      'publication_date': '6/18/2001',
      'publisher': 'Tor Classics'},
     {'bookID': 1315,
      'title': 'The Afghan Campaign',
      'authors': 'Steven Pressfield',
      'average_rating': 3.96,
      'isbn': '038551641X',
      'isbn13': 9780385516419,
      'language_code': 'eng',
      '  num_pages': 354,
      'ratings_count': 3002,
      'text_reviews_count': 198,
      'publication_date': '7/1/2006',
      'publisher': 'Doubleday Books'},
     {'bookID': 1317,
      'title': 'Tides of War',
      'authors': 'Steven Pressfield',
      'average_rating': 3.9,
      'isbn': '0553381393',
      'isbn13': 9780553381399,
      'language_code': 'eng',
      '  num_pages': 448,
      'ratings_count': 3422,
      'text_reviews_count': 157,
      'publication_date': '8/28/2001',
      'publisher': 'Bantam'},
     {'bookID': 1318,
      'title': 'Last of the Amazons',
      'authors': 'Steven Pressfield',
      'average_rating': 3.76,
      'isbn': '0553382047',
      'isbn13': 9780553382044,
      'language_code': 'eng',
      '  num_pages': 400,
      'ratings_count': 2138,
      'text_reviews_count': 125,
      'publication_date': '7/1/2003',
      'publisher': 'Bantam'},
     {'bookID': 1319,
      'title': 'The War of Art: Break Through the Blocks & Win Your Inner Creative Battles',
      'authors': 'Steven Pressfield/Robert McKee',
      'average_rating': 4.0,
      'isbn': '0446691437',
      'isbn13': 9780446691437,
      'language_code': 'eng',
      '  num_pages': 168,
      'ratings_count': 53653,
      'text_reviews_count': 4702,
      'publication_date': '4/1/2003',
      'publisher': 'Warner Books'},
     {'bookID': 1320,
      'title': 'Gita on the Green',
      'authors': 'Stephen J. Rosen/Steven Pressfield',
      'average_rating': 3.78,
      'isbn': '0826413013',
      'isbn13': 9780826413017,
      'language_code': 'en-US',
      '  num_pages': 176,
      'ratings_count': 14,
      'text_reviews_count': 2,
      'publication_date': '5/30/2002',
      'publisher': 'Continuum'},
     {'bookID': 1322,
      'title': "Blood Stripes: The Grunt's View of the War in Iraq",
      'authors': 'David J. Danelo/Steven Pressfield',
      'average_rating': 3.91,
      'isbn': '0811701646',
      'isbn13': 9780811701648,
      'language_code': 'eng',
      '  num_pages': 340,
      'ratings_count': 85,
      'text_reviews_count': 6,
      'publication_date': '4/24/2006',
      'publisher': 'Stackpole Books'},
     {'bookID': 1326,
      'title': 'Phaedrus and Letters VII and VIII',
      'authors': 'Plato/Walter Hamilton',
      'average_rating': 4.1,
      'isbn': '0140442758',
      'isbn13': 9780140442755,
      'language_code': 'en-US',
      '  num_pages': 160,
      'ratings_count': 226,
      'text_reviews_count': 20,
      'publication_date': '1/30/1973',
      'publisher': 'Penguin Classics'},
     {'bookID': 1327,
      'title': 'Phaedrus',
      'authors': 'Plato/Robin Waterfield',
      'average_rating': 3.92,
      'isbn': '0192802771',
      'isbn13': 9780192802774,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 29,
      'text_reviews_count': 6,
      'publication_date': '1/16/2003',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 1328,
      'title': 'Phaedrus',
      'authors': 'Plato/C.J. Rowe',
      'average_rating': 3.92,
      'isbn': '0140449744',
      'isbn13': 9780140449747,
      'language_code': 'eng',
      '  num_pages': 176,
      'ratings_count': 236,
      'text_reviews_count': 22,
      'publication_date': '8/25/2005',
      'publisher': 'Penguin Classics'},
     {'bookID': 1334,
      'title': 'Lysis/Phaedrus/Symposium: Plato on Homosexuality',
      'authors': 'Plato/Benjamin Jowett',
      'average_rating': 4.47,
      'isbn': '0879756322',
      'isbn13': 9780879756321,
      'language_code': 'eng',
      '  num_pages': 157,
      'ratings_count': 14,
      'text_reviews_count': 0,
      'publication_date': '12/1/1991',
      'publisher': 'Prometheus Books'},
     {'bookID': 1337,
      'title': 'Enthusiasm and Divine Madness',
      'authors': 'Josef Pieper/Richard Winston/Clara Winston',
      'average_rating': 4.5,
      'isbn': '189031823X',
      'isbn13': 9781890318239,
      'language_code': 'eng',
      '  num_pages': 125,
      'ratings_count': 26,
      'text_reviews_count': 4,
      'publication_date': '2/11/2019',
      'publisher': 'St. Augustines Press'},
     {'bookID': 1338,
      'title': 'On Love: Lysis/Symposium/Phaedrus/Alcibiades/Selections from Republic & Laws',
      'authors': 'Plato/C.D.C. Reeve',
      'average_rating': 4.06,
      'isbn': '0872207889',
      'isbn13': 9780872207882,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 154,
      'text_reviews_count': 4,
      'publication_date': '6/15/2006',
      'publisher': 'Hackett Publishing Company  Inc.'},
     {'bookID': 1342,
      'title': 'Gorgias/Phaedrus (Agora)',
      'authors': 'Plato/James H. Nichols Jr.',
      'average_rating': 4.35,
      'isbn': '0801435307',
      'isbn13': 9780801435300,
      'language_code': 'eng',
      '  num_pages': 233,
      'ratings_count': 18,
      'text_reviews_count': 1,
      'publication_date': '9/1/1998',
      'publisher': 'Cornell University Press'},
     {'bookID': 1351,
      'title': 'Statesman',
      'authors': 'Plato/C.J. Rowe',
      'average_rating': 3.85,
      'isbn': '0872204626',
      'isbn13': 9780872204621,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 28,
      'text_reviews_count': 7,
      'publication_date': '3/15/1999',
      'publisher': 'Hackett Publishing Company  Inc.'},
     {'bookID': 1354,
      'title': 'Gorgias',
      'authors': 'Plato/Walter Hamilton/Chris Emlyn-Jones',
      'average_rating': 3.95,
      'isbn': '0140449043',
      'isbn13': 9780140449044,
      'language_code': 'en-GB',
      '  num_pages': 208,
      'ratings_count': 8186,
      'text_reviews_count': 198,
      'publication_date': '1/29/2004',
      'publisher': 'Penguin Classics'},
     {'bookID': 1362,
      'title': 'The Histories',
      'authors': 'Herodotus/Aubrey de S??lincourt/John M. Marincola',
      'average_rating': 3.99,
      'isbn': '0140449086',
      'isbn13': 9780140449082,
      'language_code': 'eng',
      '  num_pages': 716,
      'ratings_count': 34727,
      'text_reviews_count': 597,
      'publication_date': '1/30/2003',
      'publisher': 'Penguin Books'},
     {'bookID': 1363,
      'title': 'The Histories',
      'authors': 'Herodotus/Aubrey de S??lincourt/John M. Marincola',
      'average_rating': 3.99,
      'isbn': '0140446389',
      'isbn13': 9780140446388,
      'language_code': 'eng',
      '  num_pages': 622,
      'ratings_count': 227,
      'text_reviews_count': 18,
      'publication_date': '9/1/1954',
      'publisher': 'Penguin Classics'},
     {'bookID': 1364,
      'title': 'The History (Great Minds)',
      'authors': 'Herodotus/Henry Francis Cary',
      'average_rating': 3.99,
      'isbn': '0879757779',
      'isbn13': 9780879757779,
      'language_code': 'en-US',
      '  num_pages': 613,
      'ratings_count': 2,
      'text_reviews_count': 0,
      'publication_date': '11/1/1992',
      'publisher': 'Prometheus Books'},
     {'bookID': 1365,
      'title': 'The Histories',
      'authors': 'Herodotus/Carolyn Dewald/Robin Waterfield',
      'average_rating': 3.99,
      'isbn': '0192824252',
      'isbn13': 9780192824257,
      'language_code': 'eng',
      '  num_pages': 772,
      'ratings_count': 271,
      'text_reviews_count': 41,
      'publication_date': '11/19/1998',
      'publisher': 'Oxford University Press'},
     {'bookID': 1366,
      'title': 'The Histories',
      'authors': 'Herodotus/Aubrey de S??lincourt/Andrew Robert Burn',
      'average_rating': 3.99,
      'isbn': '0140440348',
      'isbn13': 9780140440348,
      'language_code': 'en-US',
      '  num_pages': 653,
      'ratings_count': 143,
      'text_reviews_count': 17,
      'publication_date': '8/30/1970',
      'publisher': 'Penguin Classics'},
     {'bookID': 1367,
      'title': 'The Histories',
      'authors': 'Herodotus/Jennifer Tolbert Roberts/Walter Blanco',
      'average_rating': 3.99,
      'isbn': '0393959465',
      'isbn13': 9780393959468,
      'language_code': 'en-US',
      '  num_pages': 464,
      'ratings_count': 40,
      'text_reviews_count': 5,
      'publication_date': '1/17/1992',
      'publisher': 'W.W. Norton & Company'},
     {'bookID': 1368,
      'title': 'The Histories',
      'authors': 'Herodotus/Edward Henry Blakeney/George Rawlinson/Rosalind Thomas',
      'average_rating': 3.99,
      'isbn': '0375400613',
      'isbn13': 9780375400612,
      'language_code': 'en-US',
      '  num_pages': 816,
      'ratings_count': 132,
      'text_reviews_count': 10,
      'publication_date': '3/25/1997',
      'publisher': "Everyman's Library 234"},
     {'bookID': 1369,
      'title': 'The History',
      'authors': 'Herodotus/Peter Grene',
      'average_rating': 3.99,
      'isbn': '0226327701',
      'isbn13': 9780226327709,
      'language_code': 'en-US',
      '  num_pages': 710,
      'ratings_count': 36,
      'text_reviews_count': 6,
      'publication_date': '3/14/1987',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1371,
      'title': 'The Iliad',
      'authors': 'Homer/Robert Fagles/Bernard Knox',
      'average_rating': 3.86,
      'isbn': '0140275363',
      'isbn13': 9780140275360,
      'language_code': 'eng',
      '  num_pages': 683,
      'ratings_count': 288792,
      'text_reviews_count': 3423,
      'publication_date': '4/29/1999',
      'publisher': 'Penguin Classics'},
     {'bookID': 1373,
      'title': 'Iliad',
      'authors': 'Homer/Stanley Lombardo/Sheila Murnaghan',
      'average_rating': 3.86,
      'isbn': '0872203522',
      'isbn13': 9780872203525,
      'language_code': 'en-US',
      '  num_pages': 574,
      'ratings_count': 1058,
      'text_reviews_count': 137,
      'publication_date': '3/12/1997',
      'publisher': 'Hackett Publishing Company  Inc.'},
     {'bookID': 1374,
      'title': 'The Iliad',
      'authors': 'Homer/Robert Fitzgerald/Andrew Ford',
      'average_rating': 3.86,
      'isbn': '0374529051',
      'isbn13': 9780374529055,
      'language_code': 'en-US',
      '  num_pages': 588,
      'ratings_count': 692,
      'text_reviews_count': 81,
      'publication_date': '4/3/2004',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 1375,
      'title': 'The Iliad/The Odyssey',
      'authors': 'Homer/Robert Fagles/Bernard Knox',
      'average_rating': 4.04,
      'isbn': '0147712556',
      'isbn13': 9780147712554,
      'language_code': 'eng',
      '  num_pages': 1556,
      'ratings_count': 54939,
      'text_reviews_count': 380,
      'publication_date': '11/1/1999',
      'publisher': 'Penguin Classics'},
     {'bookID': 1376,
      'title': 'The Iliad',
      'authors': 'Homer/E.V. Rieu/Peter Jones/D.C.H. Rieu',
      'average_rating': 3.86,
      'isbn': '0140447946',
      'isbn13': 9780140447941,
      'language_code': 'eng',
      '  num_pages': 462,
      'ratings_count': 1919,
      'text_reviews_count': 118,
      'publication_date': '1/30/2003',
      'publisher': 'Penguin Classics'},
     {'bookID': 1377,
      'title': 'The Iliad',
      'authors': 'Homer/W.H.D. Rouse',
      'average_rating': 3.86,
      'isbn': '0451527372',
      'isbn13': 9780451527370,
      'language_code': 'en-US',
      '  num_pages': 312,
      'ratings_count': 158,
      'text_reviews_count': 15,
      'publication_date': '8/1/1999',
      'publisher': 'Signet Classics'},
     {'bookID': 1378,
      'title': 'The Essential Iliad',
      'authors': 'Homer/Sheila Murnaghan/Stanley Lombardo',
      'average_rating': 3.86,
      'isbn': '0872205428',
      'isbn13': 9780872205420,
      'language_code': 'en-US',
      '  num_pages': 216,
      'ratings_count': 212,
      'text_reviews_count': 18,
      'publication_date': '9/15/2000',
      'publisher': 'Hackett Publishing Company  Inc.'},
     {'bookID': 1381,
      'title': 'The Odyssey',
      'authors': 'Homer/Robert Fagles/Bernard Knox',
      'average_rating': 3.76,
      'isbn': '0143039954',
      'isbn13': 9780143039952,
      'language_code': 'eng',
      '  num_pages': 541,
      'ratings_count': 760871,
      'text_reviews_count': 6557,
      'publication_date': '11/30/2006',
      'publisher': 'Penguin Classics'},
     {'bookID': 1382,
      'title': 'The Odyssey',
      'authors': 'Homer/Robert Fitzgerald/D.S. Carne-Ross',
      'average_rating': 3.76,
      'isbn': '0374525749',
      'isbn13': 9780374525743,
      'language_code': 'eng',
      '  num_pages': 515,
      'ratings_count': 1713,
      'text_reviews_count': 179,
      'publication_date': '11/5/1998',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 1383,
      'title': 'The Odyssey',
      'authors': 'Homer/Richmond Lattimore',
      'average_rating': 3.76,
      'isbn': '0060931957',
      'isbn13': 9780060931957,
      'language_code': 'eng',
      '  num_pages': 374,
      'ratings_count': 1131,
      'text_reviews_count': 78,
      'publication_date': '6/1/1999',
      'publisher': 'Harper Perennial'},
     {'bookID': 1384,
      'title': 'The Odyssey',
      'authors': 'Homer/E.V. Rieu/Peter Jones/D.C.H. Rieu',
      'average_rating': 3.76,
      'isbn': '0140449116',
      'isbn13': 9780140449112,
      'language_code': 'eng',
      '  num_pages': 324,
      'ratings_count': 2543,
      'text_reviews_count': 167,
      'publication_date': '1/30/2003',
      'publisher': 'Penguin Classics'},
     {'bookID': 1387,
      'title': 'The Odyssey',
      'authors': 'Homer/W.H.D. Rouse',
      'average_rating': 3.76,
      'isbn': '0451527364',
      'isbn13': 9780451527363,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 262,
      'text_reviews_count': 24,
      'publication_date': '8/1/1999',
      'publisher': 'Signet Classics'},
     {'bookID': 1391,
      'title': 'Aeneid: Selections from Books 1  2  4  6  10  12',
      'authors': 'Virgil/Barbara Weiden Boyd',
      'average_rating': 4.35,
      'isbn': '086516584X',
      'isbn13': 9780865165847,
      'language_code': 'eng',
      '  num_pages': 161,
      'ratings_count': 69,
      'text_reviews_count': 6,
      'publication_date': '1/1/2001',
      'publisher': 'Bolchazy-Carducci Publishers'},
     {'bookID': 1402,
      'title': 'Eclogues. Georgics. Aeneid: Books 1-6',
      'authors': 'Virgil/Henry Rushton Fairclough/G.P. Goold',
      'average_rating': 4.22,
      'isbn': '067499583X',
      'isbn13': 9780674995833,
      'language_code': 'mul',
      '  num_pages': 607,
      'ratings_count': 414,
      'text_reviews_count': 10,
      'publication_date': '10/1/1999',
      'publisher': 'Harvard University Press'},
     {'bookID': 1403,
      'title': 'City Eclogue',
      'authors': 'Ed Roberson',
      'average_rating': 4.13,
      'isbn': '1891190237',
      'isbn13': 9781891190230,
      'language_code': 'eng',
      '  num_pages': 136,
      'ratings_count': 67,
      'text_reviews_count': 7,
      'publication_date': '1/30/2006',
      'publisher': 'Atelos Press'},
     {'bookID': 1405,
      'title': 'The Eclogues and The Georgics',
      'authors': 'Virgil/Cecil Day-Lewis',
      'average_rating': 3.8,
      'isbn': '0192837680',
      'isbn13': 9780192837684,
      'language_code': 'eng',
      '  num_pages': 180,
      'ratings_count': 259,
      'text_reviews_count': 15,
      'publication_date': '9/2/1999',
      'publisher': 'Oxford University Press'},
     {'bookID': 1408,
      'title': "Paul Kirk's Championship Barbecue Sauces: 175 Make-Your-Own Sauces  Marinades  Dry Rubs  Wet Rubs  Mops and Salsas",
      'authors': 'Paul  Kirk',
      'average_rating': 3.94,
      'isbn': '155832125X',
      'isbn13': 9781558321250,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 55,
      'text_reviews_count': 0,
      'publication_date': '12/3/1997',
      'publisher': 'Harvard Common Press'},
     {'bookID': 1417,
      'title': 'The Complete Pelican Shakespeare',
      'authors': 'William Shakespeare/Stephen Orgel/A.R. Braunmuller',
      'average_rating': 4.5,
      'isbn': '0141000589',
      'isbn13': 9780141000589,
      'language_code': 'eng',
      '  num_pages': 1808,
      'ratings_count': 578,
      'text_reviews_count': 25,
      'publication_date': '11/7/2002',
      'publisher': 'Viking'},
     {'bookID': 1419,
      'title': 'The Complete Works',
      'authors': 'William Shakespeare',
      'average_rating': 4.5,
      'isbn': '0517092948',
      'isbn13': 9780517092941,
      'language_code': 'eng',
      '  num_pages': 1248,
      'ratings_count': 62,
      'text_reviews_count': 6,
      'publication_date': '10/13/1991',
      'publisher': 'Gramercy'},
     {'bookID': 1420,
      'title': 'Hamlet',
      'authors': 'William Shakespeare/Harold Bloom/Rex Gibson',
      'average_rating': 4.02,
      'isbn': '0521618746',
      'isbn13': 9780521618748,
      'language_code': 'eng',
      '  num_pages': 289,
      'ratings_count': 609271,
      'text_reviews_count': 7139,
      'publication_date': '8/1/2005',
      'publisher': 'Cambridge University Press'},
     {'bookID': 1423,
      'title': 'The Compleat Works of Wllm Shkspr (abridged)',
      'authors': 'Reduced Shakespeare Company/Adam Long/Daniel Singer/Jess Winfield',
      'average_rating': 4.44,
      'isbn': '1557831572',
      'isbn13': 9781557831576,
      'language_code': 'eng',
      '  num_pages': 137,
      'ratings_count': 8159,
      'text_reviews_count': 118,
      'publication_date': '2/1/1994',
      'publisher': 'Applause Books'},
     {'bookID': 1424,
      'title': 'The Pilgrimage: A Contemporary Quest for Ancient Wisdom',
      'authors': 'Paulo Coelho/Alan R. Clarke',
      'average_rating': 3.64,
      'isbn': '006251279X',
      'isbn13': 9780062512796,
      'language_code': 'en-US',
      '  num_pages': 272,
      'ratings_count': 888,
      'text_reviews_count': 92,
      'publication_date': '5/1/1995',
      'publisher': 'HarperOne'},
     {'bookID': 1425,
      'title': 'The Valkyries',
      'authors': 'Paulo Coelho/Alan R. Clarke',
      'average_rating': 3.31,
      'isbn': '0062513346',
      'isbn13': 9780062513342,
      'language_code': 'en-US',
      '  num_pages': 212,
      'ratings_count': 1204,
      'text_reviews_count': 79,
      'publication_date': '9/28/1996',
      'publisher': 'HarperOne'},
     {'bookID': 1426,
      'title': 'Warrior of the Light',
      'authors': 'Paulo Coelho',
      'average_rating': 3.7,
      'isbn': '0060527986',
      'isbn13': 9780060527983,
      'language_code': 'en-US',
      '  num_pages': 142,
      'ratings_count': 22662,
      'text_reviews_count': 945,
      'publication_date': '3/30/2004',
      'publisher': 'HarperOne'},
     {'bookID': 1427,
      'title': 'The Zahir',
      'authors': 'Paulo Coelho/Margaret Jull Costa',
      'average_rating': 3.57,
      'isbn': '0060832819',
      'isbn13': 9780060832810,
      'language_code': 'eng',
      '  num_pages': 336,
      'ratings_count': 58917,
      'text_reviews_count': 2575,
      'publication_date': '7/3/2006',
      'publisher': 'HarperOne'},
     {'bookID': 1428,
      'title': 'By the River Piedra I Sat Down and Wept',
      'authors': 'Paulo Coelho/Alan R. Clarke',
      'average_rating': 3.57,
      'isbn': '0061122092',
      'isbn13': 9780061122095,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 70760,
      'text_reviews_count': 2702,
      'publication_date': '5/23/2006',
      'publisher': 'HarperOne'},
     {'bookID': 1429,
      'title': 'The Fifth Mountain',
      'authors': 'Paulo Coelho/Clifford E. Landers',
      'average_rating': 3.62,
      'isbn': '0060930136',
      'isbn13': 9780060930134,
      'language_code': 'en-US',
      '  num_pages': 256,
      'ratings_count': 1415,
      'text_reviews_count': 68,
      'publication_date': '4/26/2000',
      'publisher': 'HarperOne'},
     {'bookID': 1431,
      'title': 'Veronika Decides to Die',
      'authors': 'Paulo Coelho/Margaret Jull Costa/K??muran ??ipal',
      'average_rating': 3.7,
      'isbn': '0061124265',
      'isbn13': 9780061124266,
      'language_code': 'eng',
      '  num_pages': 210,
      'ratings_count': 132064,
      'text_reviews_count': 5452,
      'publication_date': '6/1/2006',
      'publisher': 'Harper Perennial'},
     {'bookID': 1433,
      'title': 'Hamlet',
      'authors': 'William Shakespeare/Stephen Orgel/A.R. Braunmuller',
      'average_rating': 4.02,
      'isbn': '0140714545',
      'isbn13': 9780140714548,
      'language_code': 'eng',
      '  num_pages': 148,
      'ratings_count': 1658,
      'text_reviews_count': 125,
      'publication_date': '12/1/2001',
      'publisher': 'Penguin Books'},
     {'bookID': 1437,
      'title': "Cliffs Notes on Shakespeare's Hamlet",
      'authors': 'Carla Lynn Stockton',
      'average_rating': 3.69,
      'isbn': '0764586033',
      'isbn13': 9780764586033,
      'language_code': 'en-US',
      '  num_pages': 129,
      'ratings_count': 65,
      'text_reviews_count': 6,
      'publication_date': '5/30/2000',
      'publisher': 'Cliffs Notes'},
     {'bookID': 1438,
      'title': "Shakespeare's Hamlet",
      'authors': 'William Shakespeare/Terri Mategrano',
      'average_rating': 4.02,
      'isbn': '0764585681',
      'isbn13': 9780764585685,
      'language_code': 'eng',
      '  num_pages': 240,
      'ratings_count': 102,
      'text_reviews_count': 16,
      'publication_date': '5/29/2000',
      'publisher': 'Cliffs Notes'},
     {'bookID': 1439,
      'title': "Hamlet's Mill: An Essay Investigating the Origins of Human Knowledge and Its Transmission Through Myth",
      'authors': 'Giorgio De Santillana/Hertha Von Dechend',
      'average_rating': 4.29,
      'isbn': '0879232153',
      'isbn13': 9780879232153,
      'language_code': 'eng',
      '  num_pages': 450,
      'ratings_count': 489,
      'text_reviews_count': 57,
      'publication_date': '3/24/2015',
      'publisher': 'Nonpareil Books'},
     {'bookID': 1440,
      'title': 'History of the Peloponnesian War: Bk. 1-2',
      'authors': 'Thucydides/C.F. Smith',
      'average_rating': 4.32,
      'isbn': '0674991206',
      'isbn13': 9780674991200,
      'language_code': 'mul',
      '  num_pages': 496,
      'ratings_count': 208,
      'text_reviews_count': 7,
      'publication_date': '1/1/1919',
      'publisher': 'Harvard University Press'},
     {'bookID': 1441,
      'title': 'On Justice  Power and Human Nature: Selections from The History of the Peloponnesian War',
      'authors': 'Thucydides/Paul Woodruff',
      'average_rating': 3.72,
      'isbn': '0872201686',
      'isbn13': 9780872201682,
      'language_code': 'eng',
      '  num_pages': 172,
      'ratings_count': 610,
      'text_reviews_count': 15,
      'publication_date': '10/1/1993',
      'publisher': 'Hackett Publishing Company  Inc.'},
     {'bookID': 1444,
      'title': 'History of the Peloponnesian War: Bk. 5-6',
      'authors': 'Thucydides/C.F. Smith',
      'average_rating': 4.35,
      'isbn': '0674991222',
      'isbn13': 9780674991224,
      'language_code': 'mul',
      '  num_pages': 400,
      'ratings_count': 38,
      'text_reviews_count': 0,
      'publication_date': '1/1/1921',
      'publisher': 'Harvard University Press'},
     {'bookID': 1445,
      'title': 'The Peloponnesian War',
      'authors': 'Thucydides/Steven Lattimore',
      'average_rating': 3.9,
      'isbn': '0872203948',
      'isbn13': 9780872203945,
      'language_code': 'eng',
      '  num_pages': 530,
      'ratings_count': 154,
      'text_reviews_count': 21,
      'publication_date': '6/1/1998',
      'publisher': 'Hackett Publishing Company  Inc.'},
     {'bookID': 1449,
      'title': 'The Peloponnesian War: A New Translation  Backgrounds  Interpretations',
      'authors': 'Thucydides/Jennifer Tolbert Roberts/Walter Blanco',
      'average_rating': 3.9,
      'isbn': '0393971678',
      'isbn13': 9780393971675,
      'language_code': 'eng',
      '  num_pages': 554,
      'ratings_count': 24,
      'text_reviews_count': 4,
      'publication_date': '7/17/1998',
      'publisher': 'W. W. Norton & Company'},
     {'bookID': 1459,
      'title': 'History of the Peloponnesian War  Bk. 7-8',
      'authors': 'Thucydides/C.F. Smith',
      'average_rating': 4.29,
      'isbn': '0674991877',
      'isbn13': 9780674991873,
      'language_code': 'eng',
      '  num_pages': 480,
      'ratings_count': 35,
      'text_reviews_count': 0,
      'publication_date': '1/1/1923',
      'publisher': 'Harvard University Press'},
     {'bookID': 1461,
      'title': 'Thucydides  Book 6 Commentary',
      'authors': 'Cynthia W. Shelmerdine',
      'average_rating': 4.5,
      'isbn': '0929524357',
      'isbn13': 9780929524351,
      'language_code': 'eng',
      '  num_pages': 34,
      'ratings_count': 2,
      'text_reviews_count': 0,
      'publication_date': '1/30/1989',
      'publisher': 'Bryn Mawr Commentaries'},
     {'bookID': 1462,
      'title': 'Euripides I: Alcestis / The Medea / The Heracleidae / Hippolytus',
      'authors': 'Euripides/Richmond Lattimore/David Grene/Rex Warner/Ralph Gladstone',
      'average_rating': 4.03,
      'isbn': '0226307808',
      'isbn13': 9780226307800,
      'language_code': 'eng',
      '  num_pages': 221,
      'ratings_count': 4483,
      'text_reviews_count': 56,
      'publication_date': '2/15/1955',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1463,
      'title': 'Euripides V: Electra / The Phoenician Women / The Bacchae',
      'authors': 'Euripides/David Grene/Richmond Lattimore/Emily Townsend Vermeule/Elizabeth Wyckoff/William Arrowsmith',
      'average_rating': 4.21,
      'isbn': '0226307840',
      'isbn13': 9780226307848,
      'language_code': 'eng',
      '  num_pages': 228,
      'ratings_count': 3334,
      'text_reviews_count': 46,
      'publication_date': '1/15/1969',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1465,
      'title': 'Euripides IV: Rhesus / The Suppliant Women / Orestes / Iphigenia in Aulis',
      'authors': 'Euripides/David Grene/Richmond Lattimore/William Arrowsmith/Frank William Jones/Charles R. Walker',
      'average_rating': 4.21,
      'isbn': '0226307832',
      'isbn13': 9780226307831,
      'language_code': 'eng',
      '  num_pages': 307,
      'ratings_count': 560,
      'text_reviews_count': 8,
      'publication_date': '11/15/1968',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1466,
      'title': 'Grief Lessons: Four Plays by Euripides',
      'authors': 'Anne Carson/Euripides',
      'average_rating': 4.4,
      'isbn': '1590171802',
      'isbn13': 9781590171806,
      'language_code': 'eng',
      '  num_pages': 312,
      'ratings_count': 679,
      'text_reviews_count': 85,
      'publication_date': '8/1/2006',
      'publisher': 'New York Review of Books'},
     {'bookID': 1467,
      'title': 'Ten Plays',
      'authors': 'Euripides/Moses Hadas/John Maclean',
      'average_rating': 4.17,
      'isbn': '0553213636',
      'isbn13': 9780553213638,
      'language_code': 'en-US',
      '  num_pages': 432,
      'ratings_count': 1464,
      'text_reviews_count': 21,
      'publication_date': '8/1/1990',
      'publisher': 'Bantam Classics'},
     {'bookID': 1468,
      'title': 'Euripides III: Hecuba / Andromache / The Trojan Women / Ion (Complete Greek Tragedies  #7)',
      'authors': 'Euripides/David Grene/Richmond Lattimore/William Arrowsmith/John Frederick Nims/Ronald Frederick Willetts',
      'average_rating': 4.0,
      'isbn': '0226307824',
      'isbn13': 9780226307824,
      'language_code': 'eng',
      '  num_pages': 255,
      'ratings_count': 541,
      'text_reviews_count': 15,
      'publication_date': '1/15/1992',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1470,
      'title': 'Euripides II: The Cyclops / Heracles / Iphigenia in Tauris / Helen',
      'authors': 'Euripides/David Grene/Richmond Lattimore/Witter Bynner/William Arrowsmith',
      'average_rating': 4.31,
      'isbn': '0226307816',
      'isbn13': 9780226307817,
      'language_code': 'eng',
      '  num_pages': 264,
      'ratings_count': 790,
      'text_reviews_count': 12,
      'publication_date': '4/15/2002',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1473,
      'title': 'Medea and Other Plays',
      'authors': 'Euripides/John Davie/Richard Rutherford',
      'average_rating': 4.03,
      'isbn': '0140449299',
      'isbn13': 9780140449297,
      'language_code': 'eng',
      '  num_pages': 206,
      'ratings_count': 9197,
      'text_reviews_count': 120,
      'publication_date': '3/27/2003',
      'publisher': 'Penguin Books'},
     {'bookID': 1474,
      'title': 'Cyclops / Alcestis / Medea',
      'authors': 'Euripides/David Kovacs',
      'average_rating': 4.23,
      'isbn': '0674995600',
      'isbn13': 9780674995604,
      'language_code': 'mul',
      '  num_pages': 432,
      'ratings_count': 61,
      'text_reviews_count': 4,
      'publication_date': '1/1/1994',
      'publisher': 'Loeb Classical Library'},
     {'bookID': 1475,
      'title': 'Medea',
      'authors': 'Euripides/Donald J. Mastronarde',
      'average_rating': 3.87,
      'isbn': '0521643864',
      'isbn13': 9780521643863,
      'language_code': 'grc',
      '  num_pages': 431,
      'ratings_count': 201,
      'text_reviews_count': 9,
      'publication_date': '9/16/2002',
      'publisher': 'Cambridge University Press'},
     {'bookID': 1476,
      'title': 'The Bacchae and Other Plays',
      'authors': 'Euripides/John Davie/Richard Rutherford',
      'average_rating': 4.14,
      'isbn': '0140447261',
      'isbn13': 9780140447262,
      'language_code': 'eng',
      '  num_pages': 360,
      'ratings_count': 164,
      'text_reviews_count': 8,
      'publication_date': '1/26/2006',
      'publisher': 'Penguin Classics'},
     {'bookID': 1479,
      'title': 'Bakkhai',
      'authors': 'Euripides/Reginald Gibbons/Peter H. Burian',
      'average_rating': 3.88,
      'isbn': '0195125983',
      'isbn13': 9780195125986,
      'language_code': 'eng',
      '  num_pages': 160,
      'ratings_count': 154,
      'text_reviews_count': 13,
      'publication_date': '2/22/2001',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 1480,
      'title': 'Plays 1: Medea/The Phoenician Women/Bacchae',
      'authors': 'Euripides/David Thompson/J. Michael Walton',
      'average_rating': 3.78,
      'isbn': '0413752801',
      'isbn13': 9780413752802,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 9,
      'text_reviews_count': 0,
      'publication_date': '11/9/2000',
      'publisher': 'Bloomsbury Methuen Drama'},
     {'bookID': 1486,
      'title': 'The Trojan Women and Hippolytus',
      'authors': 'Euripides',
      'average_rating': 3.63,
      'isbn': '0486424626',
      'isbn13': 9780486424620,
      'language_code': 'eng',
      '  num_pages': 64,
      'ratings_count': 34,
      'text_reviews_count': 4,
      'publication_date': '7/17/2002',
      'publisher': 'Dover Publications'},
     {'bookID': 1488,
      'title': 'The Bacchae of Euripides: A Communion Rite',
      'authors': 'Wole Soyinka',
      'average_rating': 3.86,
      'isbn': '0393325830',
      'isbn13': 9780393325836,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 116,
      'text_reviews_count': 6,
      'publication_date': '7/17/2004',
      'publisher': 'W. W. Norton  Company'},
     {'bookID': 1489,
      'title': 'Orestes and Other Plays',
      'authors': 'Euripides/James Morwood/Robin Waterfield',
      'average_rating': 4.1,
      'isbn': '0192832603',
      'isbn13': 9780192832603,
      'language_code': 'eng',
      '  num_pages': 282,
      'ratings_count': 158,
      'text_reviews_count': 2,
      'publication_date': '12/20/2001',
      'publisher': 'Oxford University Press'},
     {'bookID': 1491,
      'title': 'Children of Heracles / Hippolytus / Andromache / Hecuba',
      'authors': 'Euripides/David Kovacs',
      'average_rating': 4.26,
      'isbn': '0674995333',
      'isbn13': 9780674995338,
      'language_code': 'mul',
      '  num_pages': 528,
      'ratings_count': 27,
      'text_reviews_count': 5,
      'publication_date': '2/15/1995',
      'publisher': 'Loeb Classical Library'},
     {'bookID': 1494,
      'title': 'Alcestis',
      'authors': 'Euripides/William Arrowsmith',
      'average_rating': 3.83,
      'isbn': '0195061667',
      'isbn13': 9780195061666,
      'language_code': 'eng',
      '  num_pages': 142,
      'ratings_count': 1950,
      'text_reviews_count': 95,
      'publication_date': '2/1/1990',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 1495,
      'title': 'Suppliant Women / Electra / Heracles',
      'authors': 'Euripides/David Kovacs',
      'average_rating': 4.47,
      'isbn': '067499566X',
      'isbn13': 9780674995666,
      'language_code': 'mul',
      '  num_pages': 464,
      'ratings_count': 30,
      'text_reviews_count': 4,
      'publication_date': '9/1/1998',
      'publisher': 'Loeb Classical Library'},
     {'bookID': 1499,
      'title': 'Medea',
      'authors': 'Euripides/Georgia Ann Machemer/Michael   Collier',
      'average_rating': 3.87,
      'isbn': '0195145666',
      'isbn13': 9780195145663,
      'language_code': 'eng',
      '  num_pages': 116,
      'ratings_count': 367,
      'text_reviews_count': 35,
      'publication_date': '8/10/2006',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 1504,
      'title': 'Euripides: Medea',
      'authors': 'William Allan',
      'average_rating': 4.04,
      'isbn': '071563187X',
      'isbn13': 9780715631874,
      'language_code': 'eng',
      '  num_pages': 160,
      'ratings_count': 23,
      'text_reviews_count': 1,
      'publication_date': '10/31/2002',
      'publisher': 'Bristol Classical Press'},
     {'bookID': 1506,
      'title': "CliffsNotes on Euripides' Medea and Electra",
      'authors': 'Robert J. Milch',
      'average_rating': 4.2,
      'isbn': '0822004240',
      'isbn13': 9780822004240,
      'language_code': 'eng',
      '  num_pages': 69,
      'ratings_count': 5,
      'text_reviews_count': 0,
      'publication_date': '9/13/1965',
      'publisher': 'Cliffs Notes'},
     {'bookID': 1509,
      'title': 'Trojan Women / Iphigenia Among the Taurians / Ion',
      'authors': 'Euripides/David Kovacs',
      'average_rating': 4.03,
      'isbn': '0674995740',
      'isbn13': 9780674995741,
      'language_code': 'mul',
      '  num_pages': 528,
      'ratings_count': 29,
      'text_reviews_count': 2,
      'publication_date': '12/1/1999',
      'publisher': 'Loeb Classical Library'},
     {'bookID': 1510,
      'title': 'Helen / Phoenician Women / Orestes',
      'authors': 'Euripides/David Kovacs',
      'average_rating': 4.07,
      'isbn': '0674996003',
      'isbn13': 9780674996007,
      'language_code': 'mul',
      '  num_pages': 605,
      'ratings_count': 25,
      'text_reviews_count': 3,
      'publication_date': '6/15/2002',
      'publisher': 'Loeb Classical Library'},
     {'bookID': 1511,
      'title': 'Euripides: Iphigenia at Aulis (Companions to Greek & Roman Tragedy)',
      'authors': 'Euripides/Pantelis Michelakis',
      'average_rating': 4.03,
      'isbn': '0715629948',
      'isbn13': 9780715629949,
      'language_code': 'eng',
      '  num_pages': 144,
      'ratings_count': 12,
      'text_reviews_count': 1,
      'publication_date': '3/9/2006',
      'publisher': 'Bristol Classical Press'},
     {'bookID': 1515,
      'title': 'The Complete Greek Tragedies  Volume 3: Euripides',
      'authors': 'Euripides/David Grene/Richmond Lattimore',
      'average_rating': 4.43,
      'isbn': '0226307662',
      'isbn13': 9780226307664,
      'language_code': 'eng',
      '  num_pages': 672,
      'ratings_count': 46,
      'text_reviews_count': 7,
      'publication_date': '8/1/1992',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1516,
      'title': 'Aeschylus I: Oresteia (Agamemnon  The Libation Bearers  The Eumenides)',
      'authors': 'Aeschylus/David Grene/Richmond Lattimore',
      'average_rating': 4.02,
      'isbn': '0226307786',
      'isbn13': 9780226307787,
      'language_code': 'en-US',
      '  num_pages': 171,
      'ratings_count': 712,
      'text_reviews_count': 53,
      'publication_date': '5/15/1969',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1517,
      'title': 'Aeschylus II: The Suppliant Maidens  The Persians  Seven against Thebes  and Prometheus Bound (The Complete Greek Tragedies)',
      'authors': 'Aeschylus/David Grene/Richmond Lattimore/Seth Benardete',
      'average_rating': 4.1,
      'isbn': '0226307948',
      'isbn13': 9780226307947,
      'language_code': 'eng',
      '  num_pages': 188,
      'ratings_count': 389,
      'text_reviews_count': 26,
      'publication_date': '2/1/1992',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1518,
      'title': 'The Oresteia',
      'authors': 'Aeschylus/Alan Shapiro/Peter H. Burian',
      'average_rating': 4.02,
      'isbn': '019513592X',
      'isbn13': 9780195135923,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 77,
      'text_reviews_count': 7,
      'publication_date': '10/7/2004',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 1519,
      'title': 'The Oresteia: Agamemnon  The Libation Bearers  The Eumenides',
      'authors': 'Aeschylus/Robert Fagles/William Bedell Stanford',
      'average_rating': 4.02,
      'isbn': '0140443339',
      'isbn13': 9780140443332,
      'language_code': 'eng',
      '  num_pages': 335,
      'ratings_count': 28726,
      'text_reviews_count': 591,
      'publication_date': '2/7/1984',
      'publisher': 'Penguin Classics'},
     {'bookID': 1521,
      'title': 'Oresteia',
      'authors': 'Aeschylus/Peter Meineck/Helene P. Foley',
      'average_rating': 4.02,
      'isbn': '0872203905',
      'isbn13': 9780872203907,
      'language_code': 'eng',
      '  num_pages': 224,
      'ratings_count': 303,
      'text_reviews_count': 21,
      'publication_date': '9/15/1998',
      'publisher': 'Hackett Publishing Company  Inc.'},
     {'bookID': 1523,
      'title': 'Prometheus Bound and Other Plays',
      'authors': 'Aeschylus/Philip Vellacott',
      'average_rating': 4.1,
      'isbn': '0140441123',
      'isbn13': 9780140441123,
      'language_code': 'eng',
      '  num_pages': 160,
      'ratings_count': 4303,
      'text_reviews_count': 62,
      'publication_date': '8/30/1961',
      'publisher': 'Penguin Books'},
     {'bookID': 1525,
      'title': 'The Oresteia',
      'authors': 'Aeschylus/Ted Hughes',
      'average_rating': 4.02,
      'isbn': '0374527059',
      'isbn13': 9780374527051,
      'language_code': 'en-US',
      '  num_pages': 208,
      'ratings_count': 215,
      'text_reviews_count': 25,
      'publication_date': '9/4/2004',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 1526,
      'title': 'Aeschylus  1: The Oresteia: Agamemnon/The Libation Bearers/The Eumenides',
      'authors': 'Aeschylus/David R. Slavitt/Smith Palmer Bovie',
      'average_rating': 4.02,
      'isbn': '081221627X',
      'isbn13': 9780812216271,
      'language_code': 'eng',
      '  num_pages': 178,
      'ratings_count': 12,
      'text_reviews_count': 3,
      'publication_date': '11/1/1997',
      'publisher': 'University of Pennsylvania Press'},
     {'bookID': 1527,
      'title': 'The Complete Greek Tragedies  Volume 1: Aeschylus',
      'authors': 'Aeschylus/Richmond Lattimore/David Grene',
      'average_rating': 4.1,
      'isbn': '0226307646',
      'isbn13': 9780226307640,
      'language_code': 'eng',
      '  num_pages': 358,
      'ratings_count': 74,
      'text_reviews_count': 7,
      'publication_date': '8/1/1992',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1529,
      'title': 'Aeschylus: The Oresteia (A Student Guide: Landmarks of World Literature)',
      'authors': 'Simon Goldhill',
      'average_rating': 4.03,
      'isbn': '0521539811',
      'isbn13': 9780521539814,
      'language_code': 'eng',
      '  num_pages': 95,
      'ratings_count': 31,
      'text_reviews_count': 3,
      'publication_date': '1/22/2004',
      'publisher': 'Cambridge University Press'},
     {'bookID': 1530,
      'title': "The Oresteia: Agamemnon  Choephoroe & Eumenides (Everyman's Library  No. 260)",
      'authors': 'Aeschylus/George Thomson/Richard Seaford',
      'average_rating': 4.02,
      'isbn': '1400041929',
      'isbn13': 9781400041923,
      'language_code': 'eng',
      '  num_pages': 127,
      'ratings_count': 63,
      'text_reviews_count': 8,
      'publication_date': '1/20/2004',
      'publisher': "Everyman's Library"},
     {'bookID': 1531,
      'title': 'Aeschylus 2: The Persians/Seven Against Thebes/The Suppliants/Prometheus Bound',
      'authors': 'Aeschylus/David R. Slavitt/Smith Palmer Bovie',
      'average_rating': 4.1,
      'isbn': '0812216717',
      'isbn13': 9780812216714,
      'language_code': 'en-GB',
      '  num_pages': 232,
      'ratings_count': 12,
      'text_reviews_count': 2,
      'publication_date': '1/1/1998',
      'publisher': 'University of Pennsylvania Press'},
     {'bookID': 1532,
      'title': 'The Oresteia Trilogy: Agamemnon/The Libation-Bearers/The Furies',
      'authors': 'Aeschylus/E.D.A. Morshead',
      'average_rating': 4.02,
      'isbn': '0486292428',
      'isbn13': 9780486292427,
      'language_code': 'eng',
      '  num_pages': 151,
      'ratings_count': 89,
      'text_reviews_count': 8,
      'publication_date': '9/24/1996',
      'publisher': 'Dover Publications'},
     {'bookID': 1533,
      'title': 'The Suppliant Maidens/The Persians/Seven against Thebes/Prometheus Bound',
      'authors': 'Aeschylus/E.D.A. Morshead',
      'average_rating': 4.1,
      'isbn': '1419150014',
      'isbn13': 9781419150012,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 1,
      'text_reviews_count': 0,
      'publication_date': '6/17/2004',
      'publisher': 'Kessinger Publishing'},
     {'bookID': 1536,
      'title': 'Sophocles II: Ajax/Women of Trachis/Electra/Philoctetes (Complete Greek Tragedies 4)',
      'authors': 'Sophocles/David Grene/Richmond Lattimore/John Moore/Michael Jameson',
      'average_rating': 4.14,
      'isbn': '0226307867',
      'isbn13': 9780226307862,
      'language_code': 'eng',
      '  num_pages': 254,
      'ratings_count': 5032,
      'text_reviews_count': 36,
      'publication_date': '5/15/1969',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1537,
      'title': 'The Oedipus Plays of Sophocles: Oedipus the King; Oedipus at Colonus; Antigone',
      'authors': 'Sophocles/Paul Roche',
      'average_rating': 3.97,
      'isbn': '0452011671',
      'isbn13': 9780452011670,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 553,
      'text_reviews_count': 46,
      'publication_date': '5/1/1996',
      'publisher': 'Plume'},
     {'bookID': 1538,
      'title': 'The Complete Plays',
      'authors': 'Sophocles/Paul Roche',
      'average_rating': 4.27,
      'isbn': '0451527844',
      'isbn13': 9780451527844,
      'language_code': 'eng',
      '  num_pages': 420,
      'ratings_count': 2883,
      'text_reviews_count': 40,
      'publication_date': '3/1/2001',
      'publisher': 'New American Library'},
     {'bookID': 1540,
      'title': 'The Oedipus Cycle: Oedipus Rex  Oedipus at Colonus  Antigone',
      'authors': 'Sophocles/Robert Fitzgerald/Dudley Fitts',
      'average_rating': 3.97,
      'isbn': '015602764X',
      'isbn13': 9780156027649,
      'language_code': 'eng',
      '  num_pages': 259,
      'ratings_count': 45589,
      'text_reviews_count': 726,
      'publication_date': '11/1/2002',
      'publisher': 'Mariner Books'},
     {'bookID': 1542,
      'title': 'The Three Theban Plays: Antigone  Oedipus the King  Oedipus at Colonus',
      'authors': 'Sophocles/Robert Fagles/Bernard Knox',
      'average_rating': 3.97,
      'isbn': '0140444254',
      'isbn13': 9780140444254,
      'language_code': 'eng',
      '  num_pages': 430,
      'ratings_count': 2979,
      'text_reviews_count': 288,
      'publication_date': '1/3/2000',
      'publisher': 'Penguin Books'},
     {'bookID': 1546,
      'title': 'Theban Plays',
      'authors': 'Sophocles/Peter Meineck/Paul Woodruff',
      'average_rating': 3.97,
      'isbn': '0872205851',
      'isbn13': 9780872205857,
      'language_code': 'en-US',
      '  num_pages': 304,
      'ratings_count': 109,
      'text_reviews_count': 7,
      'publication_date': '3/15/2003',
      'publisher': 'Hackett Publishing Company  Inc.'},
     {'bookID': 1547,
      'title': "The Theban Plays (Everyman's Library  #93)",
      'authors': 'Sophocles/David Grene/Charles Segal',
      'average_rating': 3.97,
      'isbn': '0679431322',
      'isbn13': 9780679431329,
      'language_code': 'en-US',
      '  num_pages': 223,
      'ratings_count': 52,
      'text_reviews_count': 3,
      'publication_date': '10/18/1994',
      'publisher': 'Alfred A. Knopf'},
     {'bookID': 1548,
      'title': 'Electra and Other Plays',
      'authors': 'Sophocles/E.F. Watling',
      'average_rating': 4.14,
      'isbn': '0140440283',
      'isbn13': 9780140440287,
      'language_code': 'eng',
      '  num_pages': 218,
      'ratings_count': 135,
      'text_reviews_count': 9,
      'publication_date': '4/30/1953',
      'publisher': 'Penguin'},
     {'bookID': 1549,
      'title': 'Antigone; Oedipus the Kingn; Electra',
      'authors': 'Sophocles/Edith Hall/H.D.F. Kitto',
      'average_rating': 3.94,
      'isbn': '0192835882',
      'isbn13': 9780192835888,
      'language_code': 'eng',
      '  num_pages': 178,
      'ratings_count': 13358,
      'text_reviews_count': 199,
      'publication_date': '9/17/1998',
      'publisher': 'Oxford University Press'},
     {'bookID': 1554,
      'title': 'Oedipus Rex  (The Theban Plays  #1)',
      'authors': 'Sophocles/J.E. Thomas',
      'average_rating': 3.7,
      'isbn': '1580495931',
      'isbn13': 9781580495936,
      'language_code': 'eng',
      '  num_pages': 75,
      'ratings_count': 141555,
      'text_reviews_count': 1776,
      'publication_date': '6/22/2006',
      'publisher': 'Prestwick House - (Literary Touchstone Classic)'},
     {'bookID': 1555,
      'title': 'The Oedipus Plays of Sophocles',
      'authors': 'Sophocles/Paul Roche',
      'average_rating': 3.97,
      'isbn': '0451621603',
      'isbn13': 9780451621603,
      'language_code': 'eng',
      '  num_pages': 390,
      'ratings_count': 8,
      'text_reviews_count': 1,
      'publication_date': '9/1/1958',
      'publisher': 'Signet Books (NY)'},
     {'bookID': 1558,
      'title': 'Oedipus Rex (Greek and Latin Classics)',
      'authors': 'Sophocles/Roger D. Dawe',
      'average_rating': 3.7,
      'isbn': '0521617359',
      'isbn13': 9780521617352,
      'language_code': 'grc',
      '  num_pages': 214,
      'ratings_count': 218,
      'text_reviews_count': 1,
      'publication_date': '8/1/2006',
      'publisher': 'Cambridge University Press'},
     {'bookID': 1559,
      'title': 'Oedipus the King',
      'authors': 'Sophocles/Bernard Knox/Cynthia Brantley Johnson',
      'average_rating': 3.7,
      'isbn': '1416500332',
      'isbn13': 9781416500339,
      'language_code': 'eng',
      '  num_pages': 144,
      'ratings_count': 740,
      'text_reviews_count': 57,
      'publication_date': '7/1/2005',
      'publisher': 'Simon  Schuster'},
     {'bookID': 1560,
      'title': 'Four Plays: The Clouds/The Birds/Lysistrata/The Frogs',
      'authors': 'Aristophanes/William Arrowsmith/Richmond Lattimore/Douglass Parker',
      'average_rating': 4.06,
      'isbn': '0452007178',
      'isbn13': 9780452007178,
      'language_code': 'eng',
      '  num_pages': 624,
      'ratings_count': 6086,
      'text_reviews_count': 79,
      'publication_date': '11/1/1984',
      'publisher': 'Plume'},
     {'bookID': 1561,
      'title': 'Three Plays by Aristophanes: Lysistrata/Women at the Thesmophoria/Assemblywomen',
      'authors': 'Aristophanes/Jeffrey Henderson',
      'average_rating': 3.94,
      'isbn': '0415907446',
      'isbn13': 9780415907446,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 96,
      'text_reviews_count': 8,
      'publication_date': '8/27/1996',
      'publisher': 'Routledge'},
     {'bookID': 1562,
      'title': 'The Complete Plays',
      'authors': 'Aristophanes/Moses Hadas',
      'average_rating': 4.21,
      'isbn': '0553213431',
      'isbn13': 9780553213430,
      'language_code': 'eng',
      '  num_pages': 577,
      'ratings_count': 1998,
      'text_reviews_count': 33,
      'publication_date': '3/1/1984',
      'publisher': 'Bantam Classics'},
     {'bookID': 1563,
      'title': 'Aristophanes 1: The Acharnians/Peace/Celebrating Ladies/Wealth',
      'authors': 'Aristophanes/David R. Slavitt',
      'average_rating': 3.83,
      'isbn': '0812234561',
      'isbn13': 9780812234565,
      'language_code': 'eng',
      '  num_pages': 336,
      'ratings_count': 4,
      'text_reviews_count': 0,
      'publication_date': '1/29/1998',
      'publisher': 'University of Pennsylvania Press'},
     {'bookID': 1566,
      'title': 'Clouds/Wasps/Birds (Aristophanes 1)',
      'authors': 'Aristophanes/Peter Meineck',
      'average_rating': 3.77,
      'isbn': '0872203611',
      'isbn13': 9780872203617,
      'language_code': 'eng',
      '  num_pages': 480,
      'ratings_count': 1,
      'text_reviews_count': 0,
      'publication_date': '9/15/1998',
      'publisher': 'Hackett Publishing Company  Inc.'},
     {'bookID': 1567,
      'title': 'Lysistrata and Other Plays',
      'authors': 'Aristophanes/Alan H. Sommerstein',
      'average_rating': 3.95,
      'isbn': '0140448144',
      'isbn13': 9780140448146,
      'language_code': 'en-US',
      '  num_pages': 241,
      'ratings_count': 3833,
      'text_reviews_count': 120,
      'publication_date': '1/30/2003',
      'publisher': 'Penguin Classics'},
     {'bookID': 1568,
      'title': 'Acharnians',
      'authors': 'Aristophanes/Jeffrey Henderson',
      'average_rating': 3.42,
      'isbn': '1585100870',
      'isbn13': 9781585100873,
      'language_code': 'eng',
      '  num_pages': 96,
      'ratings_count': 23,
      'text_reviews_count': 1,
      'publication_date': '5/1/2003',
      'publisher': 'Focus Publishing/R. Pullins Company'},
     {'bookID': 1571,
      'title': 'Clouds',
      'authors': 'Aristophanes/Kenneth James Dover',
      'average_rating': 3.75,
      'isbn': '0199120099',
      'isbn13': 9780199120093,
      'language_code': 'eng',
      '  num_pages': 254,
      'ratings_count': 13,
      'text_reviews_count': 2,
      'publication_date': '12/15/1969',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 1572,
      'title': 'Clouds/Wasps/Peace',
      'authors': 'Aristophanes/Jeffrey Henderson',
      'average_rating': 4.07,
      'isbn': '0674995376',
      'isbn13': 9780674995376,
      'language_code': 'grc',
      '  num_pages': 624,
      'ratings_count': 69,
      'text_reviews_count': 10,
      'publication_date': '12/15/1998',
      'publisher': 'Loeb Classical Library/Harvard University Press'},
     {'bookID': 1576,
      'title': 'Three Plays: The Wasps / The Poet and the Women / The Frogs',
      'authors': 'Aristophanes/David B. Barrett',
      'average_rating': 3.94,
      'isbn': '0140441522',
      'isbn13': 9780140441529,
      'language_code': 'eng',
      '  num_pages': 224,
      'ratings_count': 391,
      'text_reviews_count': 27,
      'publication_date': '2/28/1964',
      'publisher': 'Penguin Books'},
     {'bookID': 1577,
      'title': "Four Comedies: Lysistrata / The Frogs / The Birds / Ladies' Day",
      'authors': 'Aristophanes/Dudley Fitts',
      'average_rating': 4.03,
      'isbn': '0156027658',
      'isbn13': 9780156027656,
      'language_code': 'eng',
      '  num_pages': 400,
      'ratings_count': 14,
      'text_reviews_count': 2,
      'publication_date': '1/6/2003',
      'publisher': 'Harcourt'},
     {'bookID': 1579,
      'title': 'Frogs/Assemblywomen/Wealth (Loeb Classical Library 180)',
      'authors': 'Aristophanes/Jeffrey Henderson',
      'average_rating': 4.21,
      'isbn': '0674995961',
      'isbn13': 9780674995963,
      'language_code': 'grc',
      '  num_pages': 608,
      'ratings_count': 58,
      'text_reviews_count': 4,
      'publication_date': '5/1/2002',
      'publisher': 'Harvard University Press'},
     {'bookID': 1584,
      'title': "Cliffs Notes on Aristophanes' Lysistrata  The Birds  The Clouds  The Frogs",
      'authors': 'W. John Campbell',
      'average_rating': 2.8,
      'isbn': '0822007762',
      'isbn13': 49086007763,
      'language_code': 'eng',
      '  num_pages': 80,
      'ratings_count': 5,
      'text_reviews_count': 0,
      'publication_date': '12/29/1983',
      'publisher': 'Cliffs Notes'},
     {'bookID': 1585,
      'title': 'Aristophanes and Athens: An Introduction to the Plays',
      'authors': 'Douglas M. MacDowell',
      'average_rating': 4.07,
      'isbn': '0198721595',
      'isbn13': 9780198721598,
      'language_code': 'eng',
      '  num_pages': 376,
      'ratings_count': 14,
      'text_reviews_count': 3,
      'publication_date': '10/1/1995',
      'publisher': 'Oxford University Press'},
     {'bookID': 1586,
      'title': 'Lysistrata',
      'authors': 'Aristophanes/Douglass Parker',
      'average_rating': 3.85,
      'isbn': '0451616227',
      'isbn13': 9780451616227,
      'language_code': 'eng',
      '  num_pages': 98,
      'ratings_count': 19,
      'text_reviews_count': 2,
      'publication_date': '2/1/1970',
      'publisher': 'Signet'},
     {'bookID': 1590,
      'title': 'Peace',
      'authors': 'Aristophanes/S. Douglas Olson',
      'average_rating': 3.6,
      'isbn': '0198140819',
      'isbn13': 9780198140818,
      'language_code': 'eng',
      '  num_pages': 408,
      'ratings_count': 262,
      'text_reviews_count': 13,
      'publication_date': '2/25/1999',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 1591,
      'title': 'Lysistrata',
      'authors': 'Aristophanes/Sarah Ruden',
      'average_rating': 3.85,
      'isbn': '0872206033',
      'isbn13': 9780872206038,
      'language_code': 'eng',
      '  num_pages': 132,
      'ratings_count': 30604,
      'text_reviews_count': 552,
      'publication_date': '3/1/2003',
      'publisher': 'Hackett Publishing Company  Inc.'},
     {'bookID': 1592,
      'title': 'The Knights / Peace / The Birds / The Assembly Women / Wealth',
      'authors': 'Aristophanes/Alan H. Sommerstein/David B. Barrett/David Brett',
      'average_rating': 3.69,
      'isbn': '0140443320',
      'isbn13': 9780140443325,
      'language_code': 'en-US',
      '  num_pages': 335,
      'ratings_count': 42,
      'text_reviews_count': 1,
      'publication_date': '7/27/1978',
      'publisher': 'Penguin Classics'},
     {'bookID': 1595,
      'title': 'Genres in Dialogue: Plato and the Construct of Philosophy',
      'authors': 'Andrea Wilson Nightingale',
      'average_rating': 4.33,
      'isbn': '0521774330',
      'isbn13': 9780521774338,
      'language_code': 'en-GB',
      '  num_pages': 238,
      'ratings_count': 5,
      'text_reviews_count': 2,
      'publication_date': '4/13/2000',
      'publisher': 'Cambridge University Press'},
     {'bookID': 1618,
      'title': 'The Curious Incident of the Dog in the Night-Time',
      'authors': 'Mark Haddon',
      'average_rating': 3.88,
      'isbn': '1400032717',
      'isbn13': 9781400032716,
      'language_code': 'eng',
      '  num_pages': 226,
      'ratings_count': 1054308,
      'text_reviews_count': 35537,
      'publication_date': '5/18/2004',
      'publisher': 'Vintage'},
     {'bookID': 1620,
      'title': 'The Night Gardener',
      'authors': 'George Pelecanos',
      'average_rating': 3.64,
      'isbn': '0316156507',
      'isbn13': 9780316156509,
      'language_code': 'eng',
      '  num_pages': 372,
      'ratings_count': 4067,
      'text_reviews_count': 357,
      'publication_date': '8/8/2006',
      'publisher': 'Little Brown and Company'},
     {'bookID': 1625,
      'title': 'Twelfth Night',
      'authors': 'William Shakespeare',
      'average_rating': 3.98,
      'isbn': '0743482778',
      'isbn13': 9780743482776,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 138101,
      'text_reviews_count': 2513,
      'publication_date': '7/1/2004',
      'publisher': 'Simon Schuster'},
     {'bookID': 1627,
      'title': 'Brokeback Mountain',
      'authors': 'Annie Proulx',
      'average_rating': 3.94,
      'isbn': '0743271327',
      'isbn13': 9780743271325,
      'language_code': 'eng',
      '  num_pages': 55,
      'ratings_count': 24985,
      'text_reviews_count': 1751,
      'publication_date': '12/2/2005',
      'publisher': 'Scribner'},
     {'bookID': 1633,
      'title': 'Getting Things Done: The Art of Stress-Free Productivity',
      'authors': 'David    Allen',
      'average_rating': 3.99,
      'isbn': '0142000280',
      'isbn13': 9780142000281,
      'language_code': 'en-GB',
      '  num_pages': 267,
      'ratings_count': 105507,
      'text_reviews_count': 3838,
      'publication_date': '12/31/2002',
      'publisher': 'Penguin Books'},
     {'bookID': 1634,
      'title': 'Getting Things Done When You Are Not in Charge',
      'authors': 'Geoffrey M. Bellman',
      'average_rating': 3.46,
      'isbn': '1576751724',
      'isbn13': 9781576751725,
      'language_code': 'eng',
      '  num_pages': 176,
      'ratings_count': 75,
      'text_reviews_count': 12,
      'publication_date': '8/27/2001',
      'publisher': 'Berrett-Koehler Publishers'},
     {'bookID': 1642,
      'title': 'Formas breves',
      'authors': 'Ricardo Piglia',
      'average_rating': 4.17,
      'isbn': '843392463X',
      'isbn13': 9788433924636,
      'language_code': 'spa',
      '  num_pages': 144,
      'ratings_count': 240,
      'text_reviews_count': 30,
      'publication_date': '6/1/2001',
      'publisher': 'Anagrama'},
     {'bookID': 1643,
      'title': 'El ??ltimo lector',
      'authors': 'Ricardo Piglia',
      'average_rating': 4.14,
      'isbn': '8433968777',
      'isbn13': 9788433968777,
      'language_code': 'spa',
      '  num_pages': 209,
      'ratings_count': 331,
      'text_reviews_count': 24,
      'publication_date': '7/15/2009',
      'publisher': 'Anagrama'},
     {'bookID': 1645,
      'title': 'Money to Burn',
      'authors': 'Ricardo Piglia/Amanda Hopkinson',
      'average_rating': 3.76,
      'isbn': '1862076650',
      'isbn13': 9781862076655,
      'language_code': 'eng',
      '  num_pages': 209,
      'ratings_count': 69,
      'text_reviews_count': 12,
      'publication_date': '8/1/2004',
      'publisher': 'Granta UK'},
     {'bookID': 1646,
      'title': 'Respiraci??n artificial',
      'authors': 'Ricardo Piglia',
      'average_rating': 3.96,
      'isbn': '8433924710',
      'isbn13': 9788433924711,
      'language_code': 'spa',
      '  num_pages': 218,
      'ratings_count': 1279,
      'text_reviews_count': 77,
      'publication_date': '3/1/2008',
      'publisher': 'Anagrama'},
     {'bookID': 1654,
      'title': 'Plata quemada',
      'authors': 'Ricardo Piglia',
      'average_rating': 3.76,
      'isbn': '8433924621',
      'isbn13': 9788433924629,
      'language_code': 'spa',
      '  num_pages': 227,
      'ratings_count': 1098,
      'text_reviews_count': 65,
      'publication_date': '7/1/2005',
      'publisher': 'Anagrama'},
     {'bookID': 1658,
      'title': 'American Government: Continuity and Change  Alternate Edition',
      'authors': "Karen  O'Connor/Larry J. Sabato",
      'average_rating': 2.83,
      'isbn': '0321317106',
      'isbn13': 9780321317100,
      'language_code': 'eng',
      '  num_pages': 664,
      'ratings_count': 0,
      'text_reviews_count': 0,
      'publication_date': '3/11/2005',
      'publisher': 'Longman Publishing Group'},
     {'bookID': 1664,
      'title': 'Essentials of American and Texas Government: Continuity and Change',
      'authors': "Karen  O'Connor/Larry J. Sabato",
      'average_rating': 3.5,
      'isbn': '0321365208',
      'isbn13': 9780321365200,
      'language_code': 'eng',
      '  num_pages': 854,
      'ratings_count': 0,
      'text_reviews_count': 0,
      'publication_date': '7/29/2005',
      'publisher': 'Longman Publishing Group'},
     {'bookID': 1667,
      'title': 'El t??nel',
      'authors': 'Ernesto Sabato',
      'average_rating': 4.05,
      'isbn': '8432216429',
      'isbn13': 9788432216428,
      'language_code': 'spa',
      '  num_pages': 159,
      'ratings_count': 453,
      'text_reviews_count': 60,
      'publication_date': '7/1/2003',
      'publisher': 'Seix Barral'},
     {'bookID': 1681,
      'title': 'The Confessions (Works of Saint Augustine 1)',
      'authors': 'Augustine of Hippo/John E. Rotelle/Maria Boulding',
      'average_rating': 3.92,
      'isbn': '1565480848',
      'isbn13': 9781565480841,
      'language_code': 'eng',
      '  num_pages': 416,
      'ratings_count': 142,
      'text_reviews_count': 24,
      'publication_date': '12/1/2002',
      'publisher': 'New City Press'},
     {'bookID': 1684,
      'title': 'The City of God',
      'authors': 'Augustine of Hippo/Thomas Merton/Marcus Dods',
      'average_rating': 3.92,
      'isbn': '0679783199',
      'isbn13': 9780679783190,
      'language_code': 'eng',
      '  num_pages': 905,
      'ratings_count': 104,
      'text_reviews_count': 16,
      'publication_date': '9/12/2000',
      'publisher': 'Random House'},
     {'bookID': 1685,
      'title': 'The Enchiridion on Faith Hope and Love (Augustine Series 1)',
      'authors': 'Augustine of Hippo/Bruce Harbert/John E. Rotelle',
      'average_rating': 4.04,
      'isbn': '1565481240',
      'isbn13': 9781565481244,
      'language_code': 'eng',
      '  num_pages': 144,
      'ratings_count': 271,
      'text_reviews_count': 21,
      'publication_date': '10/1/1999',
      'publisher': 'New City Press'},
     {'bookID': 1686,
      'title': 'Augustine of Hippo: A Biography',
      'authors': 'Peter R.L. Brown',
      'average_rating': 4.27,
      'isbn': '0520227573',
      'isbn13': 9780520227576,
      'language_code': 'en-US',
      '  num_pages': 576,
      'ratings_count': 1643,
      'text_reviews_count': 97,
      'publication_date': '11/24/2000',
      'publisher': 'University of California Press'},
     {'bookID': 1693,
      'title': 'On Christian Doctrine',
      'authors': 'Augustine of Hippo/D.W. Robertson Jr.',
      'average_rating': 4.03,
      'isbn': '0024021504',
      'isbn13': 9780024021502,
      'language_code': 'eng',
      '  num_pages': 191,
      'ratings_count': 2335,
      'text_reviews_count': 67,
      'publication_date': '1/11/1958',
      'publisher': 'Library of Liberal Arts/Bobb-Merrill (Indianapolis  IN)'},
     {'bookID': 1698,
      'title': 'Confessions  Books 1-13',
      'authors': 'Augustine of Hippo/Peter R.L. Brown/Frank Sheed',
      'average_rating': 3.92,
      'isbn': '0872201864',
      'isbn13': 9780872201866,
      'language_code': 'eng',
      '  num_pages': 296,
      'ratings_count': 84,
      'text_reviews_count': 8,
      'publication_date': '1/1/1993',
      'publisher': 'Hackett Publ. Co Inc'},
     {'bookID': 1702,
      'title': 'Saint Augustine',
      'authors': 'Garry Wills',
      'average_rating': 3.55,
      'isbn': '0143035983',
      'isbn13': 9780143035985,
      'language_code': 'eng',
      '  num_pages': 176,
      'ratings_count': 259,
      'text_reviews_count': 30,
      'publication_date': '8/30/2005',
      'publisher': 'Penguin Books'},
     {'bookID': 1703,
      'title': 'Augustine: A Very Short Introduction',
      'authors': 'Henry Chadwick',
      'average_rating': 3.71,
      'isbn': '0192854526',
      'isbn13': 9780192854520,
      'language_code': 'eng',
      '  num_pages': 144,
      'ratings_count': 236,
      'text_reviews_count': 33,
      'publication_date': '6/7/2001',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 1707,
      'title': 'On Genesis/A Refutation of the Manichees/The Unfinished Literal Meaning of Genesis (Works of St Augustine 1)',
      'authors': 'Augustine of Hippo/Boniface Ramsey/Edmund Hill',
      'average_rating': 3.94,
      'isbn': '1565482018',
      'isbn13': 9781565482012,
      'language_code': 'eng',
      '  num_pages': 540,
      'ratings_count': 29,
      'text_reviews_count': 3,
      'publication_date': '5/1/2004',
      'publisher': 'New City Press'},
     {'bookID': 1709,
      'title': 'Kitchen Confidential: Adventures in the Culinary Underbelly',
      'authors': 'Anthony Bourdain',
      'average_rating': 4.07,
      'isbn': '0060934913',
      'isbn13': 9780060934910,
      'language_code': 'eng',
      '  num_pages': 302,
      'ratings_count': 2488,
      'text_reviews_count': 266,
      'publication_date': '5/1/2001',
      'publisher': 'Ecco Press'},
     {'bookID': 1710,
      'title': 'Confesiones de un chef',
      'authors': 'Anthony Bourdain',
      'average_rating': 4.07,
      'isbn': '8466308954',
      'isbn13': 9788466308953,
      'language_code': 'spa',
      '  num_pages': 478,
      'ratings_count': 11,
      'text_reviews_count': 0,
      'publication_date': '2/1/2003',
      'publisher': 'Santillana USA Publishing Company'},
     {'bookID': 1713,
      'title': 'The Metamorphoses of Ovid',
      'authors': 'Ovid/Allen Mandelbaum',
      'average_rating': 4.05,
      'isbn': '0156001268',
      'isbn13': 9780156001267,
      'language_code': 'eng',
      '  num_pages': 559,
      'ratings_count': 710,
      'text_reviews_count': 64,
      'publication_date': '4/15/1995',
      'publisher': 'Harcourt Brace'},
     {'bookID': 1715,
      'title': 'Metamorphoses',
      'authors': 'Ovid/David Raeburn/Denis Feeney',
      'average_rating': 4.05,
      'isbn': '014044789X',
      'isbn13': 9780140447897,
      'language_code': 'eng',
      '  num_pages': 723,
      'ratings_count': 48223,
      'text_reviews_count': 764,
      'publication_date': '8/3/2004',
      'publisher': 'Penguin'},
     {'bookID': 1718,
      'title': 'Metamorphoses',
      'authors': 'Ovid/Bernard Knox/Charles    Martin',
      'average_rating': 4.05,
      'isbn': '0393058107',
      'isbn13': 9780393058109,
      'language_code': 'eng',
      '  num_pages': 624,
      'ratings_count': 30,
      'text_reviews_count': 8,
      'publication_date': '11/17/2003',
      'publisher': 'W. W. Norton  Company'},
     {'bookID': 1720,
      'title': "Ovid's Metamorphoses: Books 1-5",
      'authors': 'Ovid/William Scovil Anderson',
      'average_rating': 4.27,
      'isbn': '0806128941',
      'isbn13': 9780806128948,
      'language_code': 'eng',
      '  num_pages': 584,
      'ratings_count': 229,
      'text_reviews_count': 16,
      'publication_date': '1/15/1998',
      'publisher': 'University of Oklahoma Press'},
     {'bookID': 1721,
      'title': 'Ovid???s Metamorphoses: Books 6-10',
      'authors': 'Ovid/William Scovil Anderson',
      'average_rating': 4.32,
      'isbn': '0806114568',
      'isbn13': 9780806114569,
      'language_code': 'eng',
      '  num_pages': 560,
      'ratings_count': 32,
      'text_reviews_count': 3,
      'publication_date': '1/15/1978',
      'publisher': 'University of Oklahoma Press'},
     {'bookID': 1722,
      'title': 'Latin Via Ovid: A First Course',
      'authors': 'Norma Goldman/Jacob E. Nyenhuis',
      'average_rating': 4.36,
      'isbn': '0814317324',
      'isbn13': 9780814317327,
      'language_code': 'en-US',
      '  num_pages': 524,
      'ratings_count': 78,
      'text_reviews_count': 8,
      'publication_date': '9/1/1982',
      'publisher': 'Wayne State University Press'},
     {'bookID': 1725,
      'title': 'The Art of Love and Other Poems',
      'authors': 'Ovid/J.H. Mozley/G.P. Goold',
      'average_rating': 4.02,
      'isbn': '0674992555',
      'isbn13': 9780674992559,
      'language_code': 'eng',
      '  num_pages': 400,
      'ratings_count': 98,
      'text_reviews_count': 5,
      'publication_date': '1/1/1929',
      'publisher': 'Harvard University Press'},
     {'bookID': 1728,
      'title': 'The Poems of Exile: Tristia and the Black Sea Letters',
      'authors': 'Ovid/Peter Green',
      'average_rating': 4.12,
      'isbn': '0520242602',
      'isbn13': 9780520242609,
      'language_code': 'eng',
      '  num_pages': 451,
      'ratings_count': 432,
      'text_reviews_count': 14,
      'publication_date': '1/18/2005',
      'publisher': 'University of California Press'},
     {'bookID': 1729,
      'title': 'Metamorphoses: Volume 2  Books IX-XV',
      'authors': 'Ovid/Frank Justus Miller',
      'average_rating': 4.52,
      'isbn': '0674990471',
      'isbn13': 9780674990470,
      'language_code': 'eng',
      '  num_pages': 499,
      'ratings_count': 61,
      'text_reviews_count': 4,
      'publication_date': '1/1/1985',
      'publisher': 'Harvard University Press'},
     {'bookID': 1730,
      'title': 'Metamorphoses: Volume I  Books I-VIII',
      'authors': 'Ovid/Frank Justus Miller',
      'average_rating': 4.42,
      'isbn': '0674990463',
      'isbn13': 9780674990463,
      'language_code': 'eng',
      '  num_pages': 496,
      'ratings_count': 813,
      'text_reviews_count': 14,
      'publication_date': '1/1/1977',
      'publisher': 'Harvard University Press'},
     {'bookID': 1731,
      'title': 'Practice! Practice!: A Latin Via Ovid Workbook',
      'authors': 'Norma Goldman/Michael  Rossi',
      'average_rating': 4.08,
      'isbn': '0814326110',
      'isbn13': 9780814326114,
      'language_code': 'eng',
      '  num_pages': 152,
      'ratings_count': 12,
      'text_reviews_count': 0,
      'publication_date': '7/1/1995',
      'publisher': 'Wayne State University Press'},
     {'bookID': 1744,
      'title': 'Tibullus: A Commentary',
      'authors': 'Michael C.J. Putnam',
      'average_rating': 3.71,
      'isbn': '0806115602',
      'isbn13': 9780806115603,
      'language_code': 'eng',
      '  num_pages': 222,
      'ratings_count': 7,
      'text_reviews_count': 1,
      'publication_date': '11/15/1979',
      'publisher': 'University of Oklahoma Press'},
     {'bookID': 1750,
      'title': "Dionysiac Poetics and Euripides' Bacchae",
      'authors': 'Charles Segal',
      'average_rating': 4.62,
      'isbn': '069101597X',
      'isbn13': 9780691015972,
      'language_code': 'eng',
      '  num_pages': 440,
      'ratings_count': 12,
      'text_reviews_count': 0,
      'publication_date': '11/16/1997',
      'publisher': 'Princeton University Press'},
     {'bookID': 1752,
      'title': 'Antigone',
      'authors': 'Sophocles/Reginald Gibbons/Charles Segal',
      'average_rating': 3.64,
      'isbn': '0195143108',
      'isbn13': 9780195143102,
      'language_code': 'eng',
      '  num_pages': 197,
      'ratings_count': 36,
      'text_reviews_count': 5,
      'publication_date': '9/1/2007',
      'publisher': 'Oxford University Press'},
     {'bookID': 1761,
      'title': 'Antigone',
      'authors': 'Sophocles/Reginald Gibbons/Charles Segal',
      'average_rating': 3.64,
      'isbn': '0195143736',
      'isbn13': 9780195143737,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 264,
      'text_reviews_count': 14,
      'publication_date': '6/5/2003',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 1771,
      'title': 'Object-Oriented Programming in C++',
      'authors': 'Richard Johnsonbaugh/Martin Kalin',
      'average_rating': 4.07,
      'isbn': '0130158852',
      'isbn13': 9780130158857,
      'language_code': 'eng',
      '  num_pages': 640,
      'ratings_count': 14,
      'text_reviews_count': 0,
      'publication_date': '8/13/1999',
      'publisher': 'Prentice Hall'},
     {'bookID': 1796,
      'title': 'The Iliad',
      'authors': 'Homer/Robert Fitzgerald',
      'average_rating': 3.86,
      'isbn': '1857150600',
      'isbn13': 9781857150605,
      'language_code': 'eng',
      '  num_pages': 594,
      'ratings_count': 30,
      'text_reviews_count': 2,
      'publication_date': '3/19/1992',
      'publisher': 'Everyman'},
     {'bookID': 1800,
      'title': 'Love  Sex & Tragedy: How the Ancient World Shapes Our Lives',
      'authors': 'Simon Goldhill',
      'average_rating': 3.79,
      'isbn': '0226301192',
      'isbn13': 9780226301198,
      'language_code': 'eng',
      '  num_pages': 345,
      'ratings_count': 122,
      'text_reviews_count': 16,
      'publication_date': '11/1/2005',
      'publisher': 'University of Chicago Press'},
     {'bookID': 1801,
      'title': 'Reading Greek Tragedy',
      'authors': 'Simon Goldhill',
      'average_rating': 4.12,
      'isbn': '0521315794',
      'isbn13': 9780521315791,
      'language_code': 'eng',
      '  num_pages': 302,
      'ratings_count': 32,
      'text_reviews_count': 3,
      'publication_date': '8/5/1986',
      'publisher': 'Cambridge University Press'},
     {'bookID': 1804,
      'title': 'Who Needs Greek? Contests in the Cultural History of Hellenism',
      'authors': 'Simon Goldhill',
      'average_rating': 3.4,
      'isbn': '0521011760',
      'isbn13': 9780521011761,
      'language_code': 'eng',
      '  num_pages': 334,
      'ratings_count': 10,
      'text_reviews_count': 1,
      'publication_date': '4/4/2002',
      'publisher': 'Cambridge University Press'},
     {'bookID': 1805,
      'title': "Foucault's Virginity: Ancient Erotic Fiction & the History of Sexuality (Stanford Memorial Lecture)",
      'authors': 'Simon Goldhill',
      'average_rating': 3.73,
      'isbn': '0521479347',
      'isbn13': 9780521479349,
      'language_code': 'eng',
      '  num_pages': 212,
      'ratings_count': 10,
      'text_reviews_count': 0,
      'publication_date': '1/26/1995',
      'publisher': 'Cambridge University Press'},
     {'bookID': 1814,
      'title': '2012: The Return of Quetzalcoatl',
      'authors': 'Daniel Pinchbeck',
      'average_rating': 3.42,
      'isbn': '1585424838',
      'isbn13': 9781585424832,
      'language_code': 'en-US',
      '  num_pages': 408,
      'ratings_count': 1416,
      'text_reviews_count': 217,
      'publication_date': '5/4/2006',
      'publisher': 'Tarcher'},
     {'bookID': 1815,
      'title': 'Breaking Open the Head: A Psychedelic Journey Into the Heart of Contemporary Shamanism',
      'authors': 'Daniel Pinchbeck/Lee Fukui',
      'average_rating': 4.06,
      'isbn': '0767907434',
      'isbn13': 9780767907439,
      'language_code': 'en-US',
      '  num_pages': 336,
      'ratings_count': 2799,
      'text_reviews_count': 166,
      'publication_date': '8/12/2003',
      'publisher': 'Three Rivers Press (CA)'},
     {'bookID': 1823,
      'title': 'Them: Adventures with Extremists',
      'authors': 'Jon Ronson',
      'average_rating': 3.95,
      'isbn': '0743233212',
      'isbn13': 9780743233217,
      'language_code': 'eng',
      '  num_pages': 336,
      'ratings_count': 11990,
      'text_reviews_count': 831,
      'publication_date': '1/7/2003',
      'publisher': 'Simon  Schuster'},
     {'bookID': 1824,
      'title': 'The Men Who Stare at Goats',
      'authors': 'Jon Ronson',
      'average_rating': 3.61,
      'isbn': '0743270606',
      'isbn13': 9780743270601,
      'language_code': 'eng',
      '  num_pages': 259,
      'ratings_count': 10679,
      'text_reviews_count': 899,
      'publication_date': '4/10/2006',
      'publisher': 'Simon  Schuster'},
     {'bookID': 1839,
      'title': 'Guns  Germs and Steel: The Fates of Human Societies',
      'authors': 'Jared Diamond',
      'average_rating': 4.03,
      'isbn': '0393061310',
      'isbn13': 9780393061314,
      'language_code': 'eng',
      '  num_pages': 518,
      'ratings_count': 4356,
      'text_reviews_count': 404,
      'publication_date': '7/11/2005',
      'publisher': 'W.W. Norton'},
     {'bookID': 1843,
      'title': "Caught Inside: A Surfer's Year on the California Coast",
      'authors': 'Daniel Duane',
      'average_rating': 3.87,
      'isbn': '0865475091',
      'isbn13': 9780865475090,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 633,
      'text_reviews_count': 60,
      'publication_date': '4/10/1997',
      'publisher': 'North Point Press'},
     {'bookID': 1845,
      'title': 'Into the Wild',
      'authors': 'Jon Krakauer',
      'average_rating': 3.98,
      'isbn': '0385486804',
      'isbn13': 9780385486804,
      'language_code': 'eng',
      '  num_pages': 207,
      'ratings_count': 800349,
      'text_reviews_count': 18198,
      'publication_date': '1/20/1997',
      'publisher': 'Anchor Books'},
     {'bookID': 1846,
      'title': "Wild at Heart: Discovering the Secret of a Man's Soul",
      'authors': 'John Eldredge',
      'average_rating': 3.92,
      'isbn': '0785268839',
      'isbn13': 9780785268833,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 55106,
      'text_reviews_count': 1503,
      'publication_date': '4/1/2001',
      'publisher': 'Thomas Nelson'},
     {'bookID': 1848,
      'title': 'Wild Swans: Three Daughters of China',
      'authors': 'Jung Chang',
      'average_rating': 4.26,
      'isbn': '0743246985',
      'isbn13': 9780743246989,
      'language_code': 'eng',
      '  num_pages': 562,
      'ratings_count': 73572,
      'text_reviews_count': 4280,
      'publication_date': '8/12/2003',
      'publisher': 'Simon  Schuster'},
     {'bookID': 1849,
      'title': 'Wild Fire (John Corey  #4)',
      'authors': 'Nelson DeMille',
      'average_rating': 4.01,
      'isbn': '044657967X',
      'isbn13': 9780446579674,
      'language_code': 'eng',
      '  num_pages': 519,
      'ratings_count': 20909,
      'text_reviews_count': 944,
      'publication_date': '11/6/2006',
      'publisher': 'Warner Books (NY)'},
     {'bookID': 1850,
      'title': 'Born to Be Wild',
      'authors': 'Catherine Coulter',
      'average_rating': 3.78,
      'isbn': '0515142395',
      'isbn13': 9780515142396,
      'language_code': 'eng',
      '  num_pages': 354,
      'ratings_count': 2456,
      'text_reviews_count': 115,
      'publication_date': '7/25/2006',
      'publisher': 'Jove'},
     {'bookID': 1852,
      'title': 'The Call of the Wild',
      'authors': 'Jack London/Avi',
      'average_rating': 3.86,
      'isbn': '0439227143',
      'isbn13': 9780439227148,
      'language_code': 'eng',
      '  num_pages': 172,
      'ratings_count': 274649,
      'text_reviews_count': 7203,
      'publication_date': '1/1/2001',
      'publisher': 'Scholastic'},
     {'bookID': 1853,
      'title': 'Wild About Books',
      'authors': 'Judy Sierra/Marc Brown',
      'average_rating': 4.17,
      'isbn': '037582538X',
      'isbn13': 9780375825385,
      'language_code': 'eng',
      '  num_pages': 40,
      'ratings_count': 4541,
      'text_reviews_count': 378,
      'publication_date': '8/10/2004',
      'publisher': 'Alfred A. Knopf Books for Young Readers'},
     {'bookID': 1856,
      'title': 'In Web Design for Libraries',
      'authors': 'Charles P. Rubenstein',
      'average_rating': 2.67,
      'isbn': '1591583667',
      'isbn13': 9781591583660,
      'language_code': 'eng',
      '  num_pages': 196,
      'ratings_count': 9,
      'text_reviews_count': 2,
      'publication_date': '12/1/2006',
      'publisher': 'Libraries Unlimited'},
     {'bookID': 1869,
      'title': 'Nickel and Dimed: On (Not) Getting by in America',
      'authors': 'Barbara Ehrenreich',
      'average_rating': 3.63,
      'isbn': '0805063897',
      'isbn13': 9780805063899,
      'language_code': 'eng',
      '  num_pages': 240,
      'ratings_count': 168362,
      'text_reviews_count': 5762,
      'publication_date': '5/1/2002',
      'publisher': 'Owl Books (Henry Holt)'},
     {'bookID': 1877,
      'title': 'The History of Sexuality 1: An Introduction',
      'authors': 'Michel Foucault/Robert Hurley',
      'average_rating': 4.04,
      'isbn': '0394417755',
      'isbn13': 9780394417752,
      'language_code': 'eng',
      '  num_pages': 168,
      'ratings_count': 15,
      'text_reviews_count': 3,
      'publication_date': '10/1/1978',
      'publisher': 'Pantheon Books (NY)'},
     {'bookID': 1879,
      'title': 'The History of Sexuality  Volume 1: The Will to Knowledge',
      'authors': 'Michel Foucault/Robert Hurley',
      'average_rating': 4.04,
      'isbn': '0140268685',
      'isbn13': 9780140268683,
      'language_code': 'eng',
      '  num_pages': 168,
      'ratings_count': 313,
      'text_reviews_count': 27,
      'publication_date': '10/29/1998',
      'publisher': 'Penguin'},
     {'bookID': 1883,
      'title': 'The History of Sexuality  Volume 2: The Use of Pleasure',
      'authors': 'Michel Foucault/Robert Hurley',
      'average_rating': 4.08,
      'isbn': '0140137343',
      'isbn13': 9780140137347,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 51,
      'text_reviews_count': 2,
      'publication_date': '7/30/1998',
      'publisher': 'Penguin'},
     {'bookID': 1887,
      'title': 'The Making of Pride and Prejudice',
      'authors': 'Sue Birtwistle/Sue Conklin/Susie Conklin',
      'average_rating': 4.45,
      'isbn': '014025157X',
      'isbn13': 9780140251579,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 4244,
      'text_reviews_count': 99,
      'publication_date': '9/7/1995',
      'publisher': 'Penguin Books Ltd'},
     {'bookID': 1888,
      'title': 'Pride and Prejudice',
      'authors': 'Jane Austen',
      'average_rating': 4.26,
      'isbn': '0192802380',
      'isbn13': 9780192802385,
      'language_code': 'eng',
      '  num_pages': 333,
      'ratings_count': 2399,
      'text_reviews_count': 253,
      'publication_date': '2/11/2004',
      'publisher': 'Oxford University Press'},
     {'bookID': 1889,
      'title': 'Pride & Prejudice',
      'authors': 'Jane Austen/Vivien Jones',
      'average_rating': 4.26,
      'isbn': '0143036238',
      'isbn13': 9780143036234,
      'language_code': 'eng',
      '  num_pages': 392,
      'ratings_count': 1821,
      'text_reviews_count': 210,
      'publication_date': '9/1/2005',
      'publisher': 'Penguin Books'},
     {'bookID': 1891,
      'title': 'Pride and Prejudice',
      'authors': 'Jane Austen/George Saintsbury/Hugh  Thomson',
      'average_rating': 4.26,
      'isbn': '0486440915',
      'isbn13': 9780486440910,
      'language_code': 'eng',
      '  num_pages': 476,
      'ratings_count': 1146,
      'text_reviews_count': 166,
      'publication_date': '5/5/2005',
      'publisher': 'Dover Publications'},
     {'bookID': 1893,
      'title': 'Pride and Prejudice',
      'authors': 'Jane Austen/Carol Howard',
      'average_rating': 4.26,
      'isbn': '1593083246',
      'isbn13': 9781593083243,
      'language_code': 'eng',
      '  num_pages': 392,
      'ratings_count': 1628,
      'text_reviews_count': 171,
      'publication_date': '9/20/2004',
      'publisher': 'Barnes  Noble Classics'},
     {'bookID': 1894,
      'title': 'Under the Banner of Heaven: A Story of Violent Faith',
      'authors': 'Jon Krakauer',
      'average_rating': 4.0,
      'isbn': '1400032806',
      'isbn13': 9781400032808,
      'language_code': 'eng',
      '  num_pages': 399,
      'ratings_count': 7481,
      'text_reviews_count': 1022,
      'publication_date': '7/10/2003',
      'publisher': 'Anchor Books'},
     {'bookID': 1896,
      'title': 'Iceland: Land of the Sagas',
      'authors': 'David  Roberts/Jon Krakauer',
      'average_rating': 3.71,
      'isbn': '0375752676',
      'isbn13': 9780375752674,
      'language_code': 'eng',
      '  num_pages': 160,
      'ratings_count': 330,
      'text_reviews_count': 40,
      'publication_date': '10/6/1998',
      'publisher': 'Villard'},
     {'bookID': 1898,
      'title': 'Into Thin Air: A Personal Account of the Mount Everest Disaster',
      'authors': 'Jon Krakauer',
      'average_rating': 4.17,
      'isbn': '0385494785',
      'isbn13': 9780385494786,
      'language_code': 'eng',
      '  num_pages': 368,
      'ratings_count': 351406,
      'text_reviews_count': 11701,
      'publication_date': '10/19/1999',
      'publisher': 'Anchor Books'},
     {'bookID': 1902,
      'title': 'In the Land of White Death: An Epic Story of Survival in the Siberian Arctic',
      'authors': 'Valerian Albanov/Jon Krakauer/David  Roberts/Alison Anderson/???????????????? ????????????????',
      'average_rating': 4.01,
      'isbn': '067978361X',
      'isbn13': 9780679783619,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 1910,
      'text_reviews_count': 136,
      'publication_date': '9/4/2001',
      'publisher': 'Modern Library'},
     {'bookID': 1911,
      'title': 'The World Is Flat: A Brief History of the Twenty-first Century',
      'authors': 'Thomas L. Friedman',
      'average_rating': 3.68,
      'isbn': '0374292795',
      'isbn13': 9780374292799,
      'language_code': 'eng',
      '  num_pages': 616,
      'ratings_count': 87570,
      'text_reviews_count': 2800,
      'publication_date': '4/18/2006',
      'publisher': 'Farrar  Straus and Giroux (NY)'},
     {'bookID': 1914,
      'title': 'La Tierra es plana: Breve historia del mundo globalizado del siglo XXI',
      'authors': 'Thomas L. Friedman',
      'average_rating': 3.68,
      'isbn': '8427032226',
      'isbn13': 9788427032224,
      'language_code': 'spa',
      '  num_pages': 495,
      'ratings_count': 38,
      'text_reviews_count': 0,
      'publication_date': '1/1/2006',
      'publisher': 'Planeta Publishing'},
     {'bookID': 1925,
      'title': 'The Avalanche Handbook',
      'authors': 'David McClung/Peter Schaerer',
      'average_rating': 4.07,
      'isbn': '0898868092',
      'isbn13': 9780898868098,
      'language_code': 'eng',
      '  num_pages': 342,
      'ratings_count': 43,
      'text_reviews_count': 1,
      'publication_date': '10/12/2006',
      'publisher': 'Mountaineers Books'},
     {'bookID': 1931,
      'title': 'Avalanche',
      'authors': 'Arthur J. Roth',
      'average_rating': 3.65,
      'isbn': '0590422677',
      'isbn13': 9780590422673,
      'language_code': 'eng',
      '  num_pages': 144,
      'ratings_count': 273,
      'text_reviews_count': 36,
      'publication_date': '1/1/1989',
      'publisher': 'Scholastic'},
     {'bookID': 1934,
      'title': 'Little Women',
      'authors': 'Louisa May Alcott',
      'average_rating': 4.07,
      'isbn': '0451529308',
      'isbn13': 9780451529305,
      'language_code': 'eng',
      '  num_pages': 449,
      'ratings_count': 1479727,
      'text_reviews_count': 18458,
      'publication_date': '4/6/2004',
      'publisher': 'Signet Classics'},
     {'bookID': 1935,
      'title': 'Little Women (Little Women  #1)',
      'authors': 'Louisa May Alcott/Scott McKowen',
      'average_rating': 4.07,
      'isbn': '1402714580',
      'isbn13': 9781402714580,
      'language_code': 'eng',
      '  num_pages': 536,
      'ratings_count': 1395,
      'text_reviews_count': 131,
      'publication_date': '10/1/2004',
      'publisher': 'Sterling'},
     {'bookID': 1936,
      'title': 'Little Women',
      'authors': 'Louisa May Alcott/Paula Danziger',
      'average_rating': 4.07,
      'isbn': '0439101360',
      'isbn13': 9780439101363,
      'language_code': 'eng',
      '  num_pages': 562,
      'ratings_count': 462,
      'text_reviews_count': 45,
      'publication_date': '1/1/2000',
      'publisher': 'Scholastic Paperbacks'},
     {'bookID': 1937,
      'title': 'Little Women',
      'authors': 'Louisa May Alcott/Jessie Willcox Smith/Frank T. Merrill',
      'average_rating': 4.07,
      'isbn': '0517221160',
      'isbn13': 9780517221167,
      'language_code': 'eng',
      '  num_pages': 389,
      'ratings_count': 166,
      'text_reviews_count': 9,
      'publication_date': '9/3/2002',
      'publisher': 'Gramercy Books'},
     {'bookID': 1946,
      'title': "Little Women  Little Men  Jo's Boys",
      'authors': 'Louisa May Alcott/Elaine Showalter',
      'average_rating': 4.33,
      'isbn': '1931082731',
      'isbn13': 9781931082730,
      'language_code': 'eng',
      '  num_pages': 1064,
      'ratings_count': 3124,
      'text_reviews_count': 87,
      'publication_date': '2/17/2005',
      'publisher': 'Library of America'},
     {'bookID': 1947,
      'title': 'Little Women',
      'authors': 'Louisa May Alcott',
      'average_rating': 4.07,
      'isbn': '1904633277',
      'isbn13': 9781904633273,
      'language_code': 'eng',
      '  num_pages': 327,
      'ratings_count': 83,
      'text_reviews_count': 9,
      'publication_date': '2/1/2004',
      'publisher': "Collector's Library"},
     {'bookID': 1955,
      'title': 'A Tale of Two Cities',
      'authors': 'Charles Dickens/Keith Cox/Cynthia Brantley Johnson',
      'average_rating': 3.84,
      'isbn': '0743487605',
      'isbn13': 9780743487603,
      'language_code': 'eng',
      '  num_pages': 496,
      'ratings_count': 131,
      'text_reviews_count': 28,
      'publication_date': '5/1/2004',
      'publisher': 'Simon  Schuster'},
     {'bookID': 1957,
      'title': 'A Tale of Two Cities',
      'authors': "Charles Dickens/Gillen D'Arcy Wood",
      'average_rating': 3.84,
      'isbn': '1593081383',
      'isbn13': 9781593081386,
      'language_code': 'eng',
      '  num_pages': 409,
      'ratings_count': 1343,
      'text_reviews_count': 183,
      'publication_date': '7/25/2004',
      'publisher': 'Barnes & Noble Classics'},
     {'bookID': 1958,
      'title': 'A Tale of Two Cities: Charles Dickens',
      'authors': 'SparkNotes',
      'average_rating': 4.0,
      'isbn': '158663352X',
      'isbn13': 9781586633523,
      'language_code': 'eng',
      '  num_pages': 96,
      'ratings_count': 10,
      'text_reviews_count': 1,
      'publication_date': '1/10/2002',
      'publisher': 'Spark Publishing'},
     {'bookID': 1959,
      'title': 'A Tale of Two Cities',
      'authors': "Charles Dickens/Gillen D'Arcy Wood",
      'average_rating': 3.84,
      'isbn': '1593080557',
      'isbn13': 9781593080556,
      'language_code': 'en-US',
      '  num_pages': 429,
      'ratings_count': 730,
      'text_reviews_count': 88,
      'publication_date': '12/1/2003',
      'publisher': 'Barnes  Noble Classics'},
     {'bookID': 1960,
      'title': 'A Tale of Two Cities',
      'authors': 'Charles Dickens/Simon Schama',
      'average_rating': 3.84,
      'isbn': '1857151437',
      'isbn13': 9781857151435,
      'language_code': 'eng',
      '  num_pages': 432,
      'ratings_count': 39,
      'text_reviews_count': 9,
      'publication_date': '3/18/1993',
      'publisher': "Everyman's Library"},
     {'bookID': 1972,
      'title': 'Den of Thieves',
      'authors': 'James B. Stewart',
      'average_rating': 4.16,
      'isbn': '067179227X',
      'isbn13': 9780671792275,
      'language_code': 'en-US',
      '  num_pages': 592,
      'ratings_count': 9718,
      'text_reviews_count': 216,
      'publication_date': '9/1/1992',
      'publisher': 'Simon  Schuster'},
     {'bookID': 1976,
      'title': 'Den of Thieves (Cat Royal  #3)',
      'authors': 'Julia Golding',
      'average_rating': 4.21,
      'isbn': '1405228180',
      'isbn13': 9781405228183,
      'language_code': 'eng',
      '  num_pages': 416,
      'ratings_count': 1432,
      'text_reviews_count': 61,
      'publication_date': '1/31/2007',
      'publisher': 'Egmont Books Ltd'},
     {'bookID': 1982,
      'title': 'Charles Dickens: Four Novels:  Great Expectations  Hard Times  A Christmas Carol  and A Tale of Two Cities',
      'authors': 'Charles Dickens',
      'average_rating': 4.3,
      'isbn': '0517093391',
      'isbn13': 9780517093399,
      'language_code': 'en-US',
      '  num_pages': 848,
      'ratings_count': 32,
      'text_reviews_count': 2,
      'publication_date': '10/2/1993',
      'publisher': 'Gramercy'},
     {'bookID': 1984,
      'title': 'Bleak House',
      'authors': 'Charles Dickens/Mary Gaitskill/Hablot Knight Browne',
      'average_rating': 4.01,
      'isbn': '0375760059',
      'isbn13': 9780375760051,
      'language_code': 'eng',
      '  num_pages': 887,
      'ratings_count': 1235,
      'text_reviews_count': 146,
      'publication_date': '7/9/2002',
      'publisher': 'Modern Library'},
     {'bookID': 1985,
      'title': 'David Copperfield',
      'authors': 'Charles Dickens/Gish Jen',
      'average_rating': 3.99,
      'isbn': '0451530047',
      'isbn13': 9780451530042,
      'language_code': 'eng',
      '  num_pages': 928,
      'ratings_count': 355,
      'text_reviews_count': 17,
      'publication_date': '2/7/2006',
      'publisher': 'Signet'},
     {'bookID': 1987,
      'title': 'What Jane Austen Ate and Charles Dickens Knew: From Fox Hunting to Whist???the Facts of Daily Life in 19th-Century England',
      'authors': 'Daniel Pool',
      'average_rating': 3.85,
      'isbn': '0671882368',
      'isbn13': 9780671882365,
      'language_code': 'en-US',
      '  num_pages': 416,
      'ratings_count': 4873,
      'text_reviews_count': 501,
      'publication_date': '4/21/1994',
      'publisher': 'Touchstone'},
     {'bookID': 1988,
      'title': 'Charles Dickens',
      'authors': 'Jane Smiley',
      'average_rating': 3.82,
      'isbn': '0670030775',
      'isbn13': 9780670030774,
      'language_code': 'eng',
      '  num_pages': 224,
      'ratings_count': 552,
      'text_reviews_count': 81,
      'publication_date': '5/13/2002',
      'publisher': 'Viking'},
     {'bookID': 1990,
      'title': 'Martin Chuzzlewit',
      'authors': 'Charles Dickens/Patricia Ingham/Hablot Knight Browne',
      'average_rating': 3.83,
      'isbn': '0140436146',
      'isbn13': 9780140436143,
      'language_code': 'eng',
      '  num_pages': 830,
      'ratings_count': 13212,
      'text_reviews_count': 394,
      'publication_date': '11/25/1999',
      'publisher': 'Penguin Classics'},
     {'bookID': 1991,
      'title': 'Why Is Sex Fun? The Evolution of Human Sexuality (Science Masters)',
      'authors': 'Jared Diamond',
      'average_rating': 3.71,
      'isbn': '0465031269',
      'isbn13': 9780465031269,
      'language_code': 'eng',
      '  num_pages': 176,
      'ratings_count': 4532,
      'text_reviews_count': 278,
      'publication_date': '9/25/1998',
      'publisher': 'Basic Books'},
     {'bookID': 1993,
      'title': 'The Third Chimpanzee: The Evolution & Future of the Human Animal',
      'authors': 'Jared Diamond',
      'average_rating': 4.06,
      'isbn': '0060183071',
      'isbn13': 9780060183073,
      'language_code': 'eng',
      '  num_pages': 407,
      'ratings_count': 59,
      'text_reviews_count': 1,
      'publication_date': '1/1/1992',
      'publisher': 'HarperCollins Publishers'},
     {'bookID': 1999,
      'title': 'J.K.Rowling',
      'authors': 'Colleen Sexton',
      'average_rating': 3.84,
      'isbn': '0822533898',
      'isbn13': 9780822533894,
      'language_code': 'eng',
      '  num_pages': 112,
      'ratings_count': 127,
      'text_reviews_count': 10,
      'publication_date': '9/1/2005',
      'publisher': 'Lerner Publications'},
     {'bookID': 2002,
      'title': 'Harry Potter Schoolbooks Box Set: Two Classic Books from the Library of Hogwarts School of Witchcraft and Wizardry',
      'authors': 'J.K. Rowling',
      'average_rating': 4.4,
      'isbn': '043932162X',
      'isbn13': 9780439321624,
      'language_code': 'eng',
      '  num_pages': 240,
      'ratings_count': 11515,
      'text_reviews_count': 139,
      'publication_date': '11/1/2001',
      'publisher': 'Arthur A. Levine'},
     {'bookID': 2004,
      'title': "J.K. Rowling's Harry Potter Novels: A Reader's Guide",
      'authors': 'Philip Nel',
      'average_rating': 3.58,
      'isbn': '0826452329',
      'isbn13': 9780826452320,
      'language_code': 'eng',
      '  num_pages': 96,
      'ratings_count': 78,
      'text_reviews_count': 9,
      'publication_date': '9/26/2001',
      'publisher': 'Bloomsbury Academic'},
     {'bookID': 2005,
      'title': 'Harry Potter and the Half-Blood Prince (Harry Potter  #6)',
      'authors': 'J.K. Rowling',
      'average_rating': 4.57,
      'isbn': '0747584664',
      'isbn13': 9780747584667,
      'language_code': 'eng',
      '  num_pages': 768,
      'ratings_count': 1213,
      'text_reviews_count': 78,
      'publication_date': '6/23/2006',
      'publisher': 'Bloomsbury Publishing'},
     {'bookID': 2010,
      'title': 'The Santaroga Barrier',
      'authors': 'Frank Herbert',
      'average_rating': 3.66,
      'isbn': '0765342510',
      'isbn13': 9780765342515,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 1625,
      'text_reviews_count': 85,
      'publication_date': '9/16/2002',
      'publisher': 'Tor Books'},
     {'bookID': 2011,
      'title': 'The Dosadi Experiment (ConSentiency Universe  #2)',
      'authors': 'Frank Herbert',
      'average_rating': 3.81,
      'isbn': '0765342537',
      'isbn13': 9780765342539,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 6146,
      'text_reviews_count': 150,
      'publication_date': '9/16/2002',
      'publisher': 'Tor Books'},
     {'bookID': 2015,
      'title': 'The Eyes of Heisenberg',
      'authors': 'Frank Herbert',
      'average_rating': 3.43,
      'isbn': '0765342529',
      'isbn13': 9780765342522,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 1485,
      'text_reviews_count': 76,
      'publication_date': '9/16/2002',
      'publisher': 'Tor Books'},
     {'bookID': 2019,
      'title': 'The Birds (Methuen Drama)',
      'authors': "Sean O'Brien",
      'average_rating': 2.67,
      'isbn': '0413772780',
      'isbn13': 9780413772787,
      'language_code': 'en-GB',
      '  num_pages': 96,
      'ratings_count': 3,
      'text_reviews_count': 1,
      'publication_date': '7/22/2002',
      'publisher': 'Bloomsbury Methuen Drama'},
     {'bookID': 2022,
      'title': 'The Frogs',
      'authors': 'Aristophanes/B.B. Rogers',
      'average_rating': 3.8,
      'isbn': '1420926713',
      'isbn13': 9781420926712,
      'language_code': 'en-US',
      '  num_pages': 88,
      'ratings_count': 3,
      'text_reviews_count': 1,
      'publication_date': '1/1/2005',
      'publisher': 'Digireads.com'},
     {'bookID': 2025,
      'title': 'Lysistrata',
      'authors': 'Aristophanes/Jeffrey Henderson',
      'average_rating': 3.85,
      'isbn': '0198144962',
      'isbn13': 9780198144960,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 76,
      'text_reviews_count': 6,
      'publication_date': '6/21/1990',
      'publisher': 'OUP Oxford'},
     {'bookID': 2026,
      'title': 'Myths of the Underworld Journey: Plato  Aristophanes  and the "Orphic" Gold Tablets',
      'authors': 'Radcliffe G. Edmonds III',
      'average_rating': 3.75,
      'isbn': '0521834341',
      'isbn13': 9780521834346,
      'language_code': 'eng',
      '  num_pages': 276,
      'ratings_count': 3,
      'text_reviews_count': 0,
      'publication_date': '11/18/2004',
      'publisher': 'Cambridge University Press'},
     {'bookID': 2028,
      'title': 'Assembly of Women (Literary Classics)',
      'authors': 'Aristophanes/Robert Mayhew',
      'average_rating': 3.77,
      'isbn': '1573921335',
      'isbn13': 9781573921336,
      'language_code': 'en-GB',
      '  num_pages': 124,
      'ratings_count': 56,
      'text_reviews_count': 4,
      'publication_date': '4/1/1997',
      'publisher': 'Prometheus Books'},
     {'bookID': 2034,
      'title': 'Comoediae 1: Acharenses/Equites/Nubes/Vespae/Pax/Aves',
      'authors': 'Aristophanes/F.W. Hall/W.M. Geldart',
      'average_rating': 5.0,
      'isbn': '0198145047',
      'isbn13': 9780198145042,
      'language_code': 'grc',
      '  num_pages': 364,
      'ratings_count': 0,
      'text_reviews_count': 0,
      'publication_date': '2/22/1922',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 2043,
      'title': 'Aristophanes and His Theatre of the Absurd',
      'authors': 'Paul Anthony Cartledge',
      'average_rating': 3.86,
      'isbn': '1853991147',
      'isbn13': 9781853991141,
      'language_code': 'eng',
      '  num_pages': 127,
      'ratings_count': 7,
      'text_reviews_count': 1,
      'publication_date': '6/1/1991',
      'publisher': 'Bristol Classical Press'},
     {'bookID': 2045,
      'title': 'Later Novels and Other Writings: The Lady in the Lake / The Little Sister / The Long Goodbye / Playback / Double Indemnity (screenplay) / Selected Essays and Letters',
      'authors': 'Raymond Chandler/Frank MacShane',
      'average_rating': 4.47,
      'isbn': '1883011086',
      'isbn13': 9781883011086,
      'language_code': 'eng',
      '  num_pages': 1076,
      'ratings_count': 1107,
      'text_reviews_count': 48,
      'publication_date': '10/1/1995',
      'publisher': 'Library of America'},
     {'bookID': 2046,
      'title': 'Stories and Early Novels: Pulp Stories / The Big Sleep / Farewell  My Lovely / The High Window',
      'authors': 'Raymond Chandler/Frank MacShane',
      'average_rating': 4.5,
      'isbn': '1883011078',
      'isbn13': 9781883011079,
      'language_code': 'eng',
      '  num_pages': 1199,
      'ratings_count': 1324,
      'text_reviews_count': 66,
      'publication_date': '10/1/1995',
      'publisher': 'Library of America'},
     {'bookID': 2048,
      'title': "The Lady in the Lake  The Little Sister  The Long Goodbye  Playback (Everyman's Library)",
      'authors': 'Raymond Chandler/Tom Hiney',
      'average_rating': 4.45,
      'isbn': '0375415025',
      'isbn13': 9780375415029,
      'language_code': 'eng',
      '  num_pages': 1016,
      'ratings_count': 241,
      'text_reviews_count': 11,
      'publication_date': '10/15/2002',
      'publisher': "Everyman's Library"},
     {'bookID': 2049,
      'title': 'The High Window (Philip Marlowe  #3)',
      'authors': 'Raymond Chandler',
      'average_rating': 4.08,
      'isbn': '0394758269',
      'isbn13': 9780394758268,
      'language_code': 'eng',
      '  num_pages': 265,
      'ratings_count': 13233,
      'text_reviews_count': 570,
      'publication_date': '8/12/1992',
      'publisher': 'Vintage Crime/Black Lizard'},
     {'bookID': 2051,
      'title': 'The Simple Art of Murder',
      'authors': 'Raymond Chandler',
      'average_rating': 4.16,
      'isbn': '0394757653',
      'isbn13': 9780394757650,
      'language_code': 'eng',
      '  num_pages': 384,
      'ratings_count': 4952,
      'text_reviews_count': 162,
      'publication_date': '9/12/1988',
      'publisher': 'Vintage Crime/Black Lizard'},
     {'bookID': 2052,
      'title': 'The Big Sleep (Philip Marlowe  #1)',
      'authors': 'Raymond Chandler',
      'average_rating': 4.01,
      'isbn': '0394758285',
      'isbn13': 9780394758282,
      'language_code': 'eng',
      '  num_pages': 231,
      'ratings_count': 103400,
      'text_reviews_count': 4076,
      'publication_date': '7/12/1988',
      'publisher': 'Vintage Crime'},
     {'bookID': 2054,
      'title': 'The Long Goodbye (Philip Marlowe  #6)',
      'authors': 'Raymond Chandler',
      'average_rating': 4.22,
      'isbn': '0394757688',
      'isbn13': 9780394757681,
      'language_code': 'eng',
      '  num_pages': 379,
      'ratings_count': 26389,
      'text_reviews_count': 1619,
      'publication_date': '8/12/1988',
      'publisher': 'Vintage Crime/Black Lizard'},
     {'bookID': 2056,
      'title': 'An Evening of Long Goodbyes',
      'authors': 'Paul Murray',
      'average_rating': 3.6,
      'isbn': '0812970403',
      'isbn13': 9780812970401,
      'language_code': 'eng',
      '  num_pages': 448,
      'ratings_count': 983,
      'text_reviews_count': 130,
      'publication_date': '9/13/2005',
      'publisher': 'Random House Trade Paperbacks'},
     {'bookID': 2057,
      'title': 'The Long Goodbye: Memories of My Father',
      'authors': 'Patti   Davis',
      'average_rating': 3.82,
      'isbn': '0452286875',
      'isbn13': 9780452286870,
      'language_code': 'eng',
      '  num_pages': 205,
      'ratings_count': 214,
      'text_reviews_count': 31,
      'publication_date': '10/1/2005',
      'publisher': 'Plume Books'},
     {'bookID': 2058,
      'title': 'Ghost In the Shell 2: Innocence: After the Long Goodbye',
      'authors': 'Masaki Yamada/Yuji Oniki/Carl Gustav Horn',
      'average_rating': 3.97,
      'isbn': '1421501562',
      'isbn13': 9781421501567,
      'language_code': 'eng',
      '  num_pages': 196,
      'ratings_count': 250,
      'text_reviews_count': 12,
      'publication_date': '10/11/2005',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 2059,
      'title': 'The Long Goodbye (Philip Marlowe  #6)',
      'authors': 'Raymond Chandler',
      'average_rating': 4.22,
      'isbn': '056352474X',
      'isbn13': 9780563524748,
      'language_code': 'eng',
      '  num_pages': 2,
      'ratings_count': 10,
      'text_reviews_count': 2,
      'publication_date': '9/20/2004',
      'publisher': 'BBC Worldwide'},
     {'bookID': 2067,
      'title': 'Breaking the Spell: Religion as a Natural Phenomenon',
      'authors': 'Daniel C. Dennett',
      'average_rating': 3.89,
      'isbn': '067003472X',
      'isbn13': 9780670034727,
      'language_code': 'eng',
      '  num_pages': 448,
      'ratings_count': 10135,
      'text_reviews_count': 330,
      'publication_date': '2/24/2006',
      'publisher': 'Viking Books'},
     {'bookID': 2068,
      'title': "Darwin's Dangerous Idea: Evolution and the Meanings of Life",
      'authors': 'Daniel C. Dennett',
      'average_rating': 4.04,
      'isbn': '068482471X',
      'isbn13': 9780684824710,
      'language_code': 'eng',
      '  num_pages': 588,
      'ratings_count': 13563,
      'text_reviews_count': 235,
      'publication_date': '6/12/1996',
      'publisher': 'Simon  Schuster'},
     {'bookID': 2071,
      'title': 'Freedom Evolves',
      'authors': 'Daniel C. Dennett',
      'average_rating': 3.83,
      'isbn': '0142003840',
      'isbn13': 9780142003848,
      'language_code': 'eng',
      '  num_pages': 368,
      'ratings_count': 2324,
      'text_reviews_count': 88,
      'publication_date': '1/27/2004',
      'publisher': 'Penguin'},
     {'bookID': 2072,
      'title': 'Brainstorms: Philosophical Essays on Mind and Psychology',
      'authors': 'Daniel C. Dennett',
      'average_rating': 3.95,
      'isbn': '0262540371',
      'isbn13': 9780262540377,
      'language_code': 'eng',
      '  num_pages': 424,
      'ratings_count': 573,
      'text_reviews_count': 11,
      'publication_date': '7/13/1981',
      'publisher': 'MIT Press'},
     {'bookID': 2074,
      'title': 'Kinds of Minds: Towards an Understanding of Consciousness',
      'authors': 'Daniel C. Dennett',
      'average_rating': 3.82,
      'isbn': '0465073514',
      'isbn13': 9780465073511,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 1555,
      'text_reviews_count': 63,
      'publication_date': '6/12/1997',
      'publisher': 'Basic Books'},
     {'bookID': 2077,
      'title': 'Leaps of Faith: Science  Miracles & the Search for Supernatural Consolation',
      'authors': 'Nicholas Humphrey/Daniel C. Dennett',
      'average_rating': 3.61,
      'isbn': '0387987207',
      'isbn13': 9780387987200,
      'language_code': 'en-US',
      '  num_pages': 244,
      'ratings_count': 21,
      'text_reviews_count': 3,
      'publication_date': '6/4/1999',
      'publisher': 'Copernicus Books'},
     {'bookID': 2078,
      'title': 'Elbow Room: The Varieties of Free Will Worth Wanting',
      'authors': 'Daniel C. Dennett',
      'average_rating': 3.92,
      'isbn': '0262540428',
      'isbn13': 9780262540421,
      'language_code': 'eng',
      '  num_pages': 212,
      'ratings_count': 515,
      'text_reviews_count': 37,
      'publication_date': '11/21/1984',
      'publisher': 'MIT Press'},
     {'bookID': 2081,
      'title': 'The Mind???s I: Fantasies and Reflections on Self and Soul',
      'authors': 'Douglas R. Hofstadter/Daniel C. Dennett',
      'average_rating': 4.14,
      'isbn': '0553345842',
      'isbn13': 9780553345841,
      'language_code': 'eng',
      '  num_pages': 512,
      'ratings_count': 4786,
      'text_reviews_count': 92,
      'publication_date': '4/1/1985',
      'publisher': 'Bantam Books'},
     {'bookID': 2093,
      'title': 'The Illustrated A Brief History of Time',
      'authors': 'Stephen Hawking',
      'average_rating': 4.17,
      'isbn': '0553103741',
      'isbn13': 9780553103748,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 817,
      'text_reviews_count': 63,
      'publication_date': '11/1/1996',
      'publisher': 'Bantam Books'},
     {'bookID': 2094,
      'title': 'A Briefer History of Time',
      'authors': 'Stephen Hawking/Leonard Mlodinow',
      'average_rating': 4.22,
      'isbn': '0553804367',
      'isbn13': 9780553804362,
      'language_code': 'eng',
      '  num_pages': 176,
      'ratings_count': 24035,
      'text_reviews_count': 828,
      'publication_date': '9/27/2005',
      'publisher': 'Bantam'},
     {'bookID': 2095,
      'title': 'The Universe in a Nutshell',
      'authors': 'Stephen Hawking',
      'average_rating': 4.15,
      'isbn': '055380202X',
      'isbn13': 9780553802023,
      'language_code': 'eng',
      '  num_pages': 216,
      'ratings_count': 29607,
      'text_reviews_count': 645,
      'publication_date': '11/6/2001',
      'publisher': 'Bantam'},
     {'bookID': 2096,
      'title': 'God Created the Integers: The Mathematical Breakthroughs That Changed History',
      'authors': 'Stephen Hawking',
      'average_rating': 4.07,
      'isbn': '0762419229',
      'isbn13': 9780762419227,
      'language_code': 'eng',
      '  num_pages': 1160,
      'ratings_count': 1682,
      'text_reviews_count': 51,
      'publication_date': '10/4/2005',
      'publisher': 'Running Press Book Publishers'},
     {'bookID': 2099,
      'title': "Stephen Hawking's Universe: The Cosmos Explained",
      'authors': 'David Filkin/Stephen Hawking',
      'average_rating': 4.29,
      'isbn': '0465081983',
      'isbn13': 9780465081981,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 1469,
      'text_reviews_count': 22,
      'publication_date': '10/9/1998',
      'publisher': 'Basic Books'},
     {'bookID': 2100,
      'title': 'The Future of Spacetime',
      'authors': 'Stephen Hawking/Kip S. Thorne/Igor Novikov/Timothy Ferris/Alan Lightman/Richard     Price',
      'average_rating': 3.94,
      'isbn': '039332446X',
      'isbn13': 9780393324464,
      'language_code': 'eng',
      '  num_pages': 224,
      'ratings_count': 257,
      'text_reviews_count': 10,
      'publication_date': '6/17/2003',
      'publisher': 'W. W. Norton  Company'},
     {'bookID': 2102,
      'title': "Stephen Hawking's Universe",
      'authors': 'John Boslough',
      'average_rating': 4.02,
      'isbn': '0380707632',
      'isbn13': 9780380707638,
      'language_code': 'eng',
      '  num_pages': 160,
      'ratings_count': 674,
      'text_reviews_count': 30,
      'publication_date': '6/1/1989',
      'publisher': 'Avon'},
     {'bookID': 2103,
      'title': 'The Nature of Space and Time',
      'authors': 'Stephen Hawking/Roger Penrose',
      'average_rating': 4.09,
      'isbn': '0691050848',
      'isbn13': 9780691050843,
      'language_code': 'eng',
      '  num_pages': 152,
      'ratings_count': 989,
      'text_reviews_count': 40,
      'publication_date': '10/8/2000',
      'publisher': 'Princeton University Press'},
     {'bookID': 2104,
      'title': 'The Physics of Star Trek',
      'authors': 'Lawrence M. Krauss/Stephen Hawking',
      'average_rating': 3.83,
      'isbn': '0060977108',
      'isbn13': 9780060977108,
      'language_code': 'eng',
      '  num_pages': 188,
      'ratings_count': 4774,
      'text_reviews_count': 178,
      'publication_date': '8/16/1996',
      'publisher': 'ReganBooks'},
     {'bookID': 2107,
      'title': 'Falconry & Hawking',
      'authors': 'Phillip Glasier',
      'average_rating': 4.31,
      'isbn': '0713484071',
      'isbn13': 9780713484076,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 51,
      'text_reviews_count': 5,
      'publication_date': '2/1/2006',
      'publisher': 'Batsford'},
     {'bookID': 2109,
      'title': 'The World Treasury of Physics  Astronomy & Mathematics from Albert Einstein to Stephen W. Hawking & from Annie Dillard to John Updike',
      'authors': 'Timothy Ferris',
      'average_rating': 4.13,
      'isbn': '0316281336',
      'isbn13': 9780316281331,
      'language_code': 'eng',
      '  num_pages': 859,
      'ratings_count': 371,
      'text_reviews_count': 12,
      'publication_date': '6/30/1993',
      'publisher': 'Back Bay Books'},
     {'bookID': 2112,
      'title': 'The Art of Nonfiction: A Guide for Writers and Readers',
      'authors': 'Ayn Rand/Robert Mayhew/Peter   Schwartz',
      'average_rating': 3.96,
      'isbn': '0452282314',
      'isbn13': 9780452282315,
      'language_code': 'en-US',
      '  num_pages': 192,
      'ratings_count': 429,
      'text_reviews_count': 39,
      'publication_date': '2/1/2001',
      'publisher': 'New American Library'},
     {'bookID': 2113,
      'title': 'The Journals of Ayn Rand',
      'authors': 'Ayn Rand/Leonard Peikoff/David Harriman',
      'average_rating': 3.94,
      'isbn': '0452278872',
      'isbn13': 9780452278875,
      'language_code': 'eng',
      '  num_pages': 752,
      'ratings_count': 317,
      'text_reviews_count': 14,
      'publication_date': '8/1/1999',
      'publisher': 'NAL'},
     {'bookID': 2122,
      'title': 'The Fountainhead',
      'authors': 'Ayn Rand/Leonard Peikoff',
      'average_rating': 3.87,
      'isbn': '0451191153',
      'isbn13': 9780451191151,
      'language_code': 'eng',
      '  num_pages': 704,
      'ratings_count': 271754,
      'text_reviews_count': 10063,
      'publication_date': '9/1/1996',
      'publisher': 'Signet Book'},
     {'bookID': 2123,
      'title': 'The 36-Hour Day: A Family Guide to Caring for Persons with Alzheimer Disease  Related Dementing Illnesses  and Memory Loss in Later Life',
      'authors': 'Nancy L. Mace/Peter V. Rabins',
      'average_rating': 4.24,
      'isbn': '0446618764',
      'isbn13': 9780446618762,
      'language_code': 'eng',
      '  num_pages': 624,
      'ratings_count': 69,
      'text_reviews_count': 6,
      'publication_date': '11/1/2006',
      'publisher': 'Grand Central Life & Style'},
     {'bookID': 2126,
      'title': 'The 3-Hour Diet: On the Go',
      'authors': 'Jorge Cruise',
      'average_rating': 3.1,
      'isbn': '0060793198',
      'isbn13': 9780060793197,
      'language_code': 'en-US',
      '  num_pages': 192,
      'ratings_count': 31,
      'text_reviews_count': 2,
      'publication_date': '10/18/2005',
      'publisher': 'William Morrow Paperbacks'},
     {'bookID': 2127,
      'title': "The Last Hours of Ancient Sunlight: The Fate of the World and What We Can Do Before It's Too Late",
      'authors': 'Thom Hartmann/Joseph Chilton Pearce/Neale Donald Walsch',
      'average_rating': 4.23,
      'isbn': '1400051576',
      'isbn13': 9781400051571,
      'language_code': 'en-US',
      '  num_pages': 400,
      'ratings_count': 1392,
      'text_reviews_count': 136,
      'publication_date': '4/27/2004',
      'publisher': 'Broadway Books'},
     {'bookID': 2136,
      'title': 'Specimen Days',
      'authors': 'Michael Cunningham',
      'average_rating': 3.58,
      'isbn': '0312425023',
      'isbn13': 9780312425029,
      'language_code': 'eng',
      '  num_pages': 336,
      'ratings_count': 4462,
      'text_reviews_count': 446,
      'publication_date': '4/18/2006',
      'publisher': 'Picador USA'},
     {'bookID': 2137,
      'title': 'A Home at the End of the World',
      'authors': 'Michael Cunningham',
      'average_rating': 3.91,
      'isbn': '0312424086',
      'isbn13': 9780312424084,
      'language_code': 'eng',
      '  num_pages': 342,
      'ratings_count': 14769,
      'text_reviews_count': 658,
      'publication_date': '7/1/2004',
      'publisher': 'Picador'},
     {'bookID': 2140,
      'title': 'Blink: The Power of Thinking Without Thinking',
      'authors': 'Malcolm Gladwell',
      'average_rating': 3.93,
      'isbn': '0316172324',
      'isbn13': 9780316172325,
      'language_code': 'en-US',
      '  num_pages': 277,
      'ratings_count': 4254,
      'text_reviews_count': 355,
      'publication_date': '1/11/2005',
      'publisher': 'Little  Brown and Company'},
     {'bookID': 2142,
      'title': 'Blink',
      'authors': 'Ted Dekker',
      'average_rating': 4.17,
      'isbn': '0849945119',
      'isbn13': 9780849945113,
      'language_code': 'eng',
      '  num_pages': 400,
      'ratings_count': 13334,
      'text_reviews_count': 502,
      'publication_date': '10/11/2004',
      'publisher': 'Thomas Nelson'},
     {'bookID': 2144,
      'title': 'Blink-182: Tales from Beneath Your Mom',
      'authors': 'Mark Hoppus/Anne Hoppus/Alex Gaskarth',
      'average_rating': 4.39,
      'isbn': '0743422074',
      'isbn13': 9780743422079,
      'language_code': 'eng',
      '  num_pages': 112,
      'ratings_count': 169,
      'text_reviews_count': 22,
      'publication_date': '10/2/2001',
      'publisher': 'MTV Books'},
     {'bookID': 2151,
      'title': 'The Complete Novels',
      'authors': 'Jane Austen/Hugh  Thomson',
      'average_rating': 4.55,
      'isbn': '0517147688',
      'isbn13': 9780517147689,
      'language_code': 'eng',
      '  num_pages': 1103,
      'ratings_count': 300,
      'text_reviews_count': 31,
      'publication_date': '9/3/1995',
      'publisher': 'Gramercy Books'},
     {'bookID': 2152,
      'title': 'The Jane Austen Book Club',
      'authors': 'Karen Joy Fowler',
      'average_rating': 3.08,
      'isbn': '0452286530',
      'isbn13': 9780452286535,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 57720,
      'text_reviews_count': 3535,
      'publication_date': '4/26/2005',
      'publisher': "G.P. Putnam's Sons"},
     {'bookID': 2153,
      'title': 'Jane Austen: The Complete Novels',
      'authors': 'Jane Austen',
      'average_rating': 4.55,
      'isbn': '0517118297',
      'isbn13': 9780517118290,
      'language_code': 'eng',
      '  num_pages': 1103,
      'ratings_count': 267,
      'text_reviews_count': 24,
      'publication_date': '6/1/1994',
      'publisher': 'Gramercy Books'},
     {'bookID': 2155,
      'title': "Jane Austen's Letters",
      'authors': 'Jane Austen/Deirdre Le Faye',
      'average_rating': 4.16,
      'isbn': '0192832972',
      'isbn13': 9780192832979,
      'language_code': 'eng',
      '  num_pages': 672,
      'ratings_count': 2278,
      'text_reviews_count': 69,
      'publication_date': '4/3/1997',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 2156,
      'title': 'Persuasion',
      'authors': 'Jane Austen/James Kinsley/Anna Massey/Richard S. Hartmetz/Maurgaux Motin/Deidre Shauna Lynch',
      'average_rating': 4.14,
      'isbn': '0192802631',
      'isbn13': 9780192802637,
      'language_code': 'eng',
      '  num_pages': 249,
      'ratings_count': 441462,
      'text_reviews_count': 11308,
      'publication_date': '3/18/2004',
      'publisher': 'Oxford University Press'},
     {'bookID': 2157,
      'title': 'Tea with Jane Austen',
      'authors': 'Kim Wilson/Tom Carpenter',
      'average_rating': 3.79,
      'isbn': '097212179X',
      'isbn13': 9780972121798,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 1442,
      'text_reviews_count': 108,
      'publication_date': '9/3/2004',
      'publisher': 'Jones Books'},
     {'bookID': 2166,
      'title': 'The Old Man and the Sea',
      'authors': 'Ernest Hemingway/Donald Sutherland',
      'average_rating': 3.77,
      'isbn': '0743564367',
      'isbn13': 9780743564366,
      'language_code': 'eng',
      '  num_pages': 3,
      'ratings_count': 393,
      'text_reviews_count': 77,
      'publication_date': '5/1/2006',
      'publisher': 'Simon  Schuster Audio'},
     {'bookID': 2167,
      'title': "Cliffs Notes on Hemingway's The Old Man and the Sea",
      'authors': 'Jeanne Sallade Criswell/Gary Carey',
      'average_rating': 2.83,
      'isbn': '0764586602',
      'isbn13': 9780764586606,
      'language_code': 'en-US',
      '  num_pages': 80,
      'ratings_count': 4,
      'text_reviews_count': 0,
      'publication_date': '12/5/2000',
      'publisher': 'Cliffs Notes'},
     {'bookID': 2176,
      'title': "Flaubert's Parrot",
      'authors': 'Julian Barnes',
      'average_rating': 3.66,
      'isbn': '0679731369',
      'isbn13': 9780679731368,
      'language_code': 'eng',
      '  num_pages': 190,
      'ratings_count': 9373,
      'text_reviews_count': 606,
      'publication_date': '11/27/1990',
      'publisher': 'Vintage'},
     {'bookID': 2178,
      'title': 'Flaubert in Egypt: A Sensibility on Tour',
      'authors': 'Gustave Flaubert/Francis Steegmuller',
      'average_rating': 3.62,
      'isbn': '0140435824',
      'isbn13': 9780140435825,
      'language_code': 'eng',
      '  num_pages': 230,
      'ratings_count': 378,
      'text_reviews_count': 31,
      'publication_date': '3/30/1996',
      'publisher': 'Penguin Books (Penguin Classics)'},
     {'bookID': 2179,
      'title': 'A Sentimental Education',
      'authors': 'Gustave Flaubert/Douglas Parm??e',
      'average_rating': 3.83,
      'isbn': '0192836226',
      'isbn13': 9780192836229,
      'language_code': 'eng',
      '  num_pages': 464,
      'ratings_count': 105,
      'text_reviews_count': 7,
      'publication_date': '5/18/2000',
      'publisher': 'Oxford University Press'},
     {'bookID': 2182,
      'title': 'Three Tales',
      'authors': 'Gustave Flaubert/Roger Whitehouse/Geoffrey Wall',
      'average_rating': 3.69,
      'isbn': '0140448004',
      'isbn13': 9780140448009,
      'language_code': 'eng',
      '  num_pages': 110,
      'ratings_count': 3190,
      'text_reviews_count': 150,
      'publication_date': '1/27/2005',
      'publisher': 'Penguin Classics'},
     {'bookID': 2183,
      'title': 'Sentimental Education',
      'authors': 'Gustave Flaubert/Robert Baldick/Geoffrey Wall',
      'average_rating': 3.83,
      'isbn': '0140447970',
      'isbn13': 9780140447972,
      'language_code': 'eng',
      '  num_pages': 460,
      'ratings_count': 13499,
      'text_reviews_count': 388,
      'publication_date': '2/5/2004',
      'publisher': 'Penguin Classics'},
     {'bookID': 2186,
      'title': 'The Family Idiot 5: Gustave Flaubert 1821-1857',
      'authors': 'Jean-Paul Sartre/Carol Cosman',
      'average_rating': 3.8,
      'isbn': '0226735192',
      'isbn13': 9780226735191,
      'language_code': 'en-US',
      '  num_pages': 632,
      'ratings_count': 5,
      'text_reviews_count': 1,
      'publication_date': '1/26/1994',
      'publisher': 'University of Chicago Press'},
     {'bookID': 2187,
      'title': 'Middlesex',
      'authors': 'Jeffrey Eugenides',
      'average_rating': 4.0,
      'isbn': '0312422156',
      'isbn13': 9780312422158,
      'language_code': 'eng',
      '  num_pages': 529,
      'ratings_count': 540349,
      'text_reviews_count': 19548,
      'publication_date': '9/16/2003',
      'publisher': 'Picador USA'},
     {'bookID': 2199,
      'title': 'Team of Rivals: The Political Genius of Abraham Lincoln',
      'authors': 'Doris Kearns Goodwin',
      'average_rating': 4.28,
      'isbn': '0743270754',
      'isbn13': 9780743270755,
      'language_code': 'eng',
      '  num_pages': 916,
      'ratings_count': 133840,
      'text_reviews_count': 6118,
      'publication_date': '9/26/2006',
      'publisher': 'Simon & Schuster'},
     {'bookID': 2203,
      'title': 'John Adams',
      'authors': 'David McCullough',
      'average_rating': 4.06,
      'isbn': '0743223136',
      'isbn13': 9780743223133,
      'language_code': 'eng',
      '  num_pages': 751,
      'ratings_count': 282649,
      'text_reviews_count': 5325,
      'publication_date': '5/22/2001',
      'publisher': 'Simon & Schuster Paperbacks'},
     {'bookID': 2204,
      'title': 'The John Adams Reader: Eseential Writings on an American Composer',
      'authors': 'Thomas May/John   Adams',
      'average_rating': 3.5,
      'isbn': '1574671324',
      'isbn13': 9781574671322,
      'language_code': 'eng',
      '  num_pages': 455,
      'ratings_count': 20,
      'text_reviews_count': 5,
      'publication_date': '6/1/2006',
      'publisher': 'Amadeus'},
     {'bookID': 2205,
      'title': 'The Letters of John and Abigail Adams',
      'authors': 'Abigail Adams/Frank Shuffelton',
      'average_rating': 4.14,
      'isbn': '0142437115',
      'isbn13': 9780142437117,
      'language_code': 'eng',
      '  num_pages': 512,
      'ratings_count': 275,
      'text_reviews_count': 28,
      'publication_date': '12/30/2003',
      'publisher': 'Penguin Classics'},
     {'bookID': 2209,
      'title': 'Passionate Sage: The Character and Legacy of John Adams',
      'authors': 'Joseph J. Ellis',
      'average_rating': 4.05,
      'isbn': '0393311333',
      'isbn13': 9780393311334,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 2622,
      'text_reviews_count': 78,
      'publication_date': '2/17/2001',
      'publisher': 'W. W. Norton  Company'},
     {'bookID': 2211,
      'title': 'The Portable John Adams',
      'authors': 'John  Adams/John Patrick Diggins',
      'average_rating': 4.17,
      'isbn': '0142437786',
      'isbn13': 9780142437780,
      'language_code': 'eng',
      '  num_pages': 533,
      'ratings_count': 57,
      'text_reviews_count': 0,
      'publication_date': '6/29/2004',
      'publisher': 'Penguin Books'},
     {'bookID': 2218,
      'title': 'Sex For Dummies',
      'authors': 'Ruth Westheimer',
      'average_rating': 3.65,
      'isbn': '076455302X',
      'isbn13': 9780764553028,
      'language_code': 'eng',
      '  num_pages': 432,
      'ratings_count': 10,
      'text_reviews_count': 0,
      'publication_date': '12/28/2000',
      'publisher': 'For Dummies'},
     {'bookID': 2219,
      'title': 'Baby Signing For Dummies',
      'authors': 'Jennifer Watson',
      'average_rating': 3.64,
      'isbn': '0471773867',
      'isbn13': 9780471773863,
      'language_code': 'eng',
      '  num_pages': 257,
      'ratings_count': 37,
      'text_reviews_count': 9,
      'publication_date': '10/1/2006',
      'publisher': 'John Wiley & Sons'},
     {'bookID': 2222,
      'title': 'The Feeling Good Handbook',
      'authors': 'David D. Burns',
      'average_rating': 4.0,
      'isbn': '0452281326',
      'isbn13': 9780452281325,
      'language_code': 'eng',
      '  num_pages': 729,
      'ratings_count': 4797,
      'text_reviews_count': 124,
      'publication_date': '10/28/1999',
      'publisher': 'Penguin'},
     {'bookID': 2226,
      'title': 'On Death and Dying',
      'authors': 'Elisabeth K??bler-Ross',
      'average_rating': 4.16,
      'isbn': '0684842238',
      'isbn13': 9780684842233,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 144,
      'text_reviews_count': 10,
      'publication_date': '7/2/1997',
      'publisher': 'Scribner'},
     {'bookID': 2227,
      'title': 'Questions and Answers on Death and Dying: A Companion Volume to On Death and Dying',
      'authors': 'Elisabeth K??bler-Ross',
      'average_rating': 4.07,
      'isbn': '0684839377',
      'isbn13': 9780684839370,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 197,
      'text_reviews_count': 7,
      'publication_date': '6/9/1997',
      'publisher': 'Scribner'},
     {'bookID': 2228,
      'title': 'The Last Dance: Encountering Death and Dying',
      'authors': 'Lynne Ann DeSpelder/Albert Lee Strickland',
      'average_rating': 3.77,
      'isbn': '0072920963',
      'isbn13': 9780072920963,
      'language_code': 'eng',
      '  num_pages': 664,
      'ratings_count': 123,
      'text_reviews_count': 13,
      'publication_date': '2/6/2004',
      'publisher': 'McGraw-Hill Humanities/Social Sciences/Languages'},
     {'bookID': 2236,
      'title': "Mahatma Gandhi and His Myths: Civil Disobedience  Nonviolence  and Satyagraha in the Real World (Plus Why It's Gandhi  Not Ghandi)",
      'authors': 'Mark Shepard',
      'average_rating': 3.62,
      'isbn': '0938497197',
      'isbn13': 9780938497196,
      'language_code': 'eng',
      '  num_pages': 46,
      'ratings_count': 55,
      'text_reviews_count': 7,
      'publication_date': '1/1/2002',
      'publisher': 'Simple Productions'},
     {'bookID': 2249,
      'title': 'The Seven Habits of Highly Effective People',
      'authors': 'Stephen R. Covey',
      'average_rating': 4.1,
      'isbn': '0671708635',
      'isbn13': 9780671708634,
      'language_code': 'eng',
      '  num_pages': 368,
      'ratings_count': 2505,
      'text_reviews_count': 233,
      'publication_date': '9/15/1990',
      'publisher': 'Free Press'},
     {'bookID': 2250,
      'title': 'The 7 Habits of Highly Effective People Personal Workbook',
      'authors': 'Stephen R. Covey',
      'average_rating': 4.24,
      'isbn': '0743250974',
      'isbn13': 9780743250979,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 1874,
      'text_reviews_count': 114,
      'publication_date': '1/6/2004',
      'publisher': 'Simon  Schuster'},
     {'bookID': 2253,
      'title': 'Daily Reflections For Highly Effective People: Living the 7 Habits of Highly Successful People Every Day',
      'authors': 'Stephen R. Covey',
      'average_rating': 3.9,
      'isbn': '0671887173',
      'isbn13': 9780671887179,
      'language_code': 'eng',
      '  num_pages': 384,
      'ratings_count': 336,
      'text_reviews_count': 26,
      'publication_date': '3/21/1994',
      'publisher': 'Simon  Schuster'},
     {'bookID': 2255,
      'title': 'Way of the Peaceful Warrior: A Book That Changes Lives',
      'authors': 'Dan Millman',
      'average_rating': 4.14,
      'isbn': '1932073205',
      'isbn13': 9781932073201,
      'language_code': 'en-US',
      '  num_pages': 240,
      'ratings_count': 39947,
      'text_reviews_count': 1622,
      'publication_date': '4/13/2006',
      'publisher': 'HJ Kramer'},
     {'bookID': 2257,
      'title': 'Secret of the Peaceful Warrior',
      'authors': 'Dan Millman/Robert D. San Souci/T. Taylor Bruce',
      'average_rating': 4.15,
      'isbn': '0915811235',
      'isbn13': 9780915811236,
      'language_code': 'en-US',
      '  num_pages': 32,
      'ratings_count': 156,
      'text_reviews_count': 13,
      'publication_date': '12/28/1992',
      'publisher': 'HJ Kramer'},
     {'bookID': 2265,
      'title': "It's Not about the Bike: My Journey Back to Life",
      'authors': 'Lance Armstrong/Sally Jenkins',
      'average_rating': 3.72,
      'isbn': '0425179613',
      'isbn13': 9780425179611,
      'language_code': 'eng',
      '  num_pages': 294,
      'ratings_count': 35050,
      'text_reviews_count': 1833,
      'publication_date': '9/1/2001',
      'publisher': 'Berkley Publishing Group'},
     {'bookID': 2267,
      'title': "23 Days in July: Inside the Tour de France and Lance Armstrong's Record-Breaking Victory",
      'authors': 'John Wilcockson/Graham   Watson',
      'average_rating': 3.67,
      'isbn': '0306814552',
      'isbn13': 9780306814556,
      'language_code': 'eng',
      '  num_pages': 344,
      'ratings_count': 360,
      'text_reviews_count': 26,
      'publication_date': '6/15/2005',
      'publisher': 'Da Capo Press'},
     {'bookID': 2279,
      'title': 'Truman',
      'authors': 'David McCullough',
      'average_rating': 4.12,
      'isbn': '0671869205',
      'isbn13': 9780671869205,
      'language_code': 'eng',
      '  num_pages': 1120,
      'ratings_count': 71764,
      'text_reviews_count': 1937,
      'publication_date': '6/14/1993',
      'publisher': 'Simon  Schuster'},
     {'bookID': 2281,
      'title': 'The Complete Stories of Truman Capote',
      'authors': 'Truman Capote/Reynolds Price',
      'average_rating': 4.2,
      'isbn': '140009691X',
      'isbn13': 9781400096916,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 3993,
      'text_reviews_count': 217,
      'publication_date': '9/13/2005',
      'publisher': 'Vintage'},
     {'bookID': 2282,
      'title': "Breakfast at Tiffany's: A Short Novel and Three Stories",
      'authors': 'Truman Capote',
      'average_rating': 3.89,
      'isbn': '067960085X',
      'isbn13': 9780679600855,
      'language_code': 'eng',
      '  num_pages': 162,
      'ratings_count': 5658,
      'text_reviews_count': 699,
      'publication_date': '1/13/1994',
      'publisher': 'Modern Library'},
     {'bookID': 2283,
      'title': 'Murder at The Washington Tribune (Capital Crimes  #21)',
      'authors': 'Margaret Truman',
      'average_rating': 3.58,
      'isbn': '0345478207',
      'isbn13': 9780345478207,
      'language_code': 'eng',
      '  num_pages': 384,
      'ratings_count': 585,
      'text_reviews_count': 78,
      'publication_date': '10/31/2006',
      'publisher': 'Ballantine Books'},
     {'bookID': 2285,
      'title': "Murder at Ford's Theatre (Capital Crimes  #19)",
      'authors': 'Margaret Truman',
      'average_rating': 3.74,
      'isbn': '0449007383',
      'isbn13': 9780449007389,
      'language_code': 'en-US',
      '  num_pages': 376,
      'ratings_count': 623,
      'text_reviews_count': 68,
      'publication_date': '9/30/2003',
      'publisher': 'Fawcett'},
     {'bookID': 2287,
      'title': 'Other Voices  Other Rooms',
      'authors': 'Truman Capote',
      'average_rating': 3.8,
      'isbn': '0679745645',
      'isbn13': 9780679745648,
      'language_code': 'eng',
      '  num_pages': 232,
      'ratings_count': 10635,
      'text_reviews_count': 656,
      'publication_date': '2/1/1994',
      'publisher': 'Vintage'},
     {'bookID': 2289,
      'title': 'In Cold Blood',
      'authors': 'Truman Capote/Scott Brick',
      'average_rating': 4.07,
      'isbn': '073933364X',
      'isbn13': 9780739333648,
      'language_code': 'eng',
      '  num_pages': 15,
      'ratings_count': 563,
      'text_reviews_count': 133,
      'publication_date': '1/3/2006',
      'publisher': 'Random House Audio'},
     {'bookID': 2296,
      'title': 'Emergence: The Connected Lives of Ants  Brains  Cities  and Software',
      'authors': 'Steven Johnson',
      'average_rating': 3.96,
      'isbn': '0684868768',
      'isbn13': 9780684868769,
      'language_code': 'en-US',
      '  num_pages': 288,
      'ratings_count': 2769,
      'text_reviews_count': 200,
      'publication_date': '9/10/2002',
      'publisher': 'Scribner'},
     {'bookID': 2299,
      'title': 'Emergence: Labeled Autistic',
      'authors': 'Temple Grandin/Margaret M. Scariano',
      'average_rating': 4.07,
      'isbn': '0446671827',
      'isbn13': 9780446671828,
      'language_code': 'en-GB',
      '  num_pages': 200,
      'ratings_count': 1827,
      'text_reviews_count': 154,
      'publication_date': '9/1/1996',
      'publisher': 'Grand Central Publishing'},
     {'bookID': 2304,
      'title': 'The Emergence of Life on Earth: A Historical and Scientific Overview',
      'authors': 'Iris Fry',
      'average_rating': 4.02,
      'isbn': '0813527406',
      'isbn13': 9780813527406,
      'language_code': 'eng',
      '  num_pages': 344,
      'ratings_count': 48,
      'text_reviews_count': 5,
      'publication_date': '2/1/2000',
      'publisher': 'Rutgers University Press'},
     {'bookID': 2305,
      'title': 'The Ghost Stories of Edith Wharton',
      'authors': 'Edith Wharton/Laszlo Kubinyi',
      'average_rating': 3.89,
      'isbn': '0684842572',
      'isbn13': 9780684842578,
      'language_code': 'eng',
      '  num_pages': 303,
      'ratings_count': 2842,
      'text_reviews_count': 182,
      'publication_date': '10/10/1997',
      'publisher': 'Scribner'},
     {'bookID': 2306,
      'title': 'The House of Mirth / The Reef / The Custom of the Country / The Age of Innocence',
      'authors': 'Edith Wharton/R.W.B. Lewis',
      'average_rating': 4.3,
      'isbn': '0940450313',
      'isbn13': 9780940450318,
      'language_code': 'eng',
      '  num_pages': 1328,
      'ratings_count': 446,
      'text_reviews_count': 29,
      'publication_date': '5/12/1986',
      'publisher': 'Library of America'},
     {'bookID': 2307,
      'title': 'Collected Stories  1911-1937',
      'authors': 'Edith Wharton/Maureen Howard',
      'average_rating': 4.25,
      'isbn': '1883011949',
      'isbn13': 9781883011949,
      'language_code': 'eng',
      '  num_pages': 848,
      'ratings_count': 55,
      'text_reviews_count': 9,
      'publication_date': '1/29/2001',
      'publisher': 'Library of America'},
     {'bookID': 2309,
      'title': 'Novellas and Other Writings: Madame de Treymes / Ethan Frome / Summer / Old New York / The Mother???s Recompense / A Backward Glance',
      'authors': 'Edith Wharton/Cynthia Griffin Wolff',
      'average_rating': 4.22,
      'isbn': '0940450534',
      'isbn13': 9780940450530,
      'language_code': 'eng',
      '  num_pages': 1137,
      'ratings_count': 67,
      'text_reviews_count': 9,
      'publication_date': '4/1/1990',
      'publisher': 'Library of America'},
     {'bookID': 2314,
      'title': 'The House of Mirth',
      'authors': 'Edith Wharton',
      'average_rating': 3.95,
      'isbn': '0486420493',
      'isbn13': 9780486420493,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 749,
      'text_reviews_count': 62,
      'publication_date': '8/6/2002',
      'publisher': 'Dover Publications'},
     {'bookID': 2315,
      'title': 'Below the Root',
      'authors': 'Zilpha Keatley Snyder/Alton Raible',
      'average_rating': 4.08,
      'isbn': '0689304579',
      'isbn13': 9780689304576,
      'language_code': 'eng',
      '  num_pages': 231,
      'ratings_count': 41,
      'text_reviews_count': 9,
      'publication_date': '1/1/1975',
      'publisher': 'Atheneum Books'},
     {'bookID': 2319,
      'title': 'The Witches of Worm',
      'authors': 'Zilpha Keatley Snyder',
      'average_rating': 3.69,
      'isbn': '0440802504',
      'isbn13': 9780440802501,
      'language_code': 'eng',
      '  num_pages': 183,
      'ratings_count': 40,
      'text_reviews_count': 12,
      'publication_date': '5/1/1991',
      'publisher': 'Dell Yearling'},
     {'bookID': 2322,
      'title': 'The Deeper Meaning of Liff',
      'authors': 'Douglas Adams/John Lloyd',
      'average_rating': 3.93,
      'isbn': '0307236013',
      'isbn13': 9780307236012,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 3986,
      'text_reviews_count': 85,
      'publication_date': '4/19/2005',
      'publisher': 'Three Rivers Press'},
     {'bookID': 2326,
      'title': "Dirk Gently's Holistic Detective Agency (Dirk Gently #1)",
      'authors': 'Douglas Adams',
      'average_rating': 3.98,
      'isbn': '1597770078',
      'isbn13': 9781597770071,
      'language_code': 'eng',
      '  num_pages': 6,
      'ratings_count': 58,
      'text_reviews_count': 15,
      'publication_date': '9/30/2005',
      'publisher': 'Phoenix Audio'},
     {'bookID': 2327,
      'title': 'The Letters of J.R.R. Tolkien',
      'authors': 'J.R.R. Tolkien/Humphrey Carpenter/Christopher Tolkien',
      'average_rating': 4.15,
      'isbn': '0618056998',
      'isbn13': 9780618056996,
      'language_code': 'eng',
      '  num_pages': 502,
      'ratings_count': 4689,
      'text_reviews_count': 171,
      'publication_date': '6/6/2000',
      'publisher': 'Mariner Books'},
     {'bookID': 2329,
      'title': 'The History of the Lord of the Rings (The History of Middle-earth #6-9)',
      'authors': 'J.R.R. Tolkien/Christopher Tolkien',
      'average_rating': 4.38,
      'isbn': '0618083553',
      'isbn13': 9780618083558,
      'language_code': 'en-US',
      '  num_pages': 1680,
      'ratings_count': 237,
      'text_reviews_count': 3,
      'publication_date': '9/1/2000',
      'publisher': 'Mariner Books'},
     {'bookID': 2330,
      'title': "The Languages of Tolkien's Middle-Earth",
      'authors': 'Ruth S. Noel/J.R.R. Tolkien',
      'average_rating': 3.98,
      'isbn': '0395291305',
      'isbn13': 9780395291306,
      'language_code': 'eng',
      '  num_pages': 207,
      'ratings_count': 4685,
      'text_reviews_count': 74,
      'publication_date': '5/28/1980',
      'publisher': 'Houghton Mifflin Company'},
     {'bookID': 2331,
      'title': 'The Lord of the Rings- 3 volumes set (The Lord of the Rings  #1-3)',
      'authors': 'J.R.R. Tolkien',
      'average_rating': 4.5,
      'isbn': '0618574999',
      'isbn13': 9780618574995,
      'language_code': 'en-US',
      '  num_pages': 1438,
      'ratings_count': 232,
      'text_reviews_count': 9,
      'publication_date': '6/1/2005',
      'publisher': 'Mariner Books'},
     {'bookID': 2333,
      'title': 'Farmer Giles of Ham',
      'authors': 'J.R.R. Tolkien/Christina Scull/Wayne G. Hammond',
      'average_rating': 3.85,
      'isbn': '0618009361',
      'isbn13': 9780618009367,
      'language_code': 'eng',
      '  num_pages': 127,
      'ratings_count': 5526,
      'text_reviews_count': 225,
      'publication_date': '11/15/1999',
      'publisher': 'Houghton Mifflin Harcourt'},
     {'bookID': 2336,
      'title': 'Tandia',
      'authors': 'Bryce Courtenay',
      'average_rating': 4.05,
      'isbn': '0140272925',
      'isbn13': 9780140272925,
      'language_code': 'eng',
      '  num_pages': 905,
      'ratings_count': 8461,
      'text_reviews_count': 369,
      'publication_date': '8/31/1998',
      'publisher': 'Penguin Books Australia Ltd.'},
     {'bookID': 2338,
      'title': "Matthew Flinders' Cat",
      'authors': 'Bryce Courtenay',
      'average_rating': 3.8,
      'isbn': '0670910619',
      'isbn13': 9780670910618,
      'language_code': 'eng',
      '  num_pages': 611,
      'ratings_count': 2737,
      'text_reviews_count': 161,
      'publication_date': '12/31/2002',
      'publisher': 'Viking'},
     {'bookID': 2343,
      'title': "Solomon's Song (The Potato Factory  #3)",
      'authors': 'Bryce Courtenay',
      'average_rating': 4.01,
      'isbn': '0140271570',
      'isbn13': 9780140271577,
      'language_code': 'eng',
      '  num_pages': 671,
      'ratings_count': 3920,
      'text_reviews_count': 132,
      'publication_date': '8/31/2001',
      'publisher': 'Penguin Books Australia Ltd.'},
     {'bookID': 2348,
      'title': 'An Introduction to Old Norse',
      'authors': 'E.V. Gordon/A.R. Taylor',
      'average_rating': 4.1,
      'isbn': '0198111843',
      'isbn13': 9780198111849,
      'language_code': 'eng',
      '  num_pages': 412,
      'ratings_count': 104,
      'text_reviews_count': 7,
      'publication_date': '7/23/1981',
      'publisher': 'Oxford University Press'},
     {'bookID': 2353,
      'title': 'Cold Counsel: Women in Old Norse Literature and Myth',
      'authors': 'Sarah M.  Anderson/Karen Swenson',
      'average_rating': 3.68,
      'isbn': '0815319665',
      'isbn13': 9780815319665,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 19,
      'text_reviews_count': 2,
      'publication_date': '12/21/2002',
      'publisher': 'Routledge'},
     {'bookID': 2367,
      'title': 'Brave Companions: Portraits in History',
      'authors': 'David McCullough',
      'average_rating': 3.98,
      'isbn': '0671792768',
      'isbn13': 9780671792763,
      'language_code': 'eng',
      '  num_pages': 240,
      'ratings_count': 3460,
      'text_reviews_count': 482,
      'publication_date': '11/1/1992',
      'publisher': 'Simon Schuster'},
     {'bookID': 2368,
      'title': 'Mornings on Horseback: The Story of an Extraordinary Family  a Vanished Way of Life  and the Unique Child Who Became Theodore Roosevelt',
      'authors': 'David McCullough',
      'average_rating': 4.12,
      'isbn': '0671447548',
      'isbn13': 9780671447540,
      'language_code': 'eng',
      '  num_pages': 445,
      'ratings_count': 23064,
      'text_reviews_count': 1191,
      'publication_date': '5/12/1982',
      'publisher': 'Simon  Schuster'},
     {'bookID': 2370,
      'title': 'John Adams',
      'authors': 'David McCullough',
      'average_rating': 4.06,
      'isbn': '0684813637',
      'isbn13': 9780684813639,
      'language_code': 'en-US',
      '  num_pages': 752,
      'ratings_count': 1852,
      'text_reviews_count': 285,
      'publication_date': '5/1/2001',
      'publisher': 'Simon & Schuster'},
     {'bookID': 2371,
      'title': 'The Johnstown Flood',
      'authors': 'David McCullough',
      'average_rating': 4.11,
      'isbn': '0844662925',
      'isbn13': 9780844662923,
      'language_code': 'eng',
      '  num_pages': 302,
      'ratings_count': 14739,
      'text_reviews_count': 1199,
      'publication_date': '1/1/1990',
      'publisher': 'Peter Smith Publisher'},
     {'bookID': 2372,
      'title': 'The Path Between the Seas: The Creation of the Panama Canal  1870-1914',
      'authors': 'David McCullough',
      'average_rating': 4.2,
      'isbn': '0743262131',
      'isbn13': 9780743262132,
      'language_code': 'eng',
      '  num_pages': 697,
      'ratings_count': 12178,
      'text_reviews_count': 1042,
      'publication_date': '6/1/2004',
      'publisher': 'Simon  Schuster'},
     {'bookID': 2373,
      'title': 'The Bone Collector (Lincoln Rhyme  #1)',
      'authors': 'Jeffery Deaver',
      'average_rating': 4.19,
      'isbn': '0451188454',
      'isbn13': 9780451188458,
      'language_code': 'eng',
      '  num_pages': 528,
      'ratings_count': 140014,
      'text_reviews_count': 1753,
      'publication_date': '4/1/1998',
      'publisher': 'Signet Book'},
     {'bookID': 2375,
      'title': "The Bone Collector's Son",
      'authors': 'Paul Yee',
      'average_rating': 3.27,
      'isbn': '0761452427',
      'isbn13': 9780761452423,
      'language_code': 'eng',
      '  num_pages': 137,
      'ratings_count': 117,
      'text_reviews_count': 19,
      'publication_date': '1/1/2004',
      'publisher': 'Two Lions'},
     {'bookID': 2378,
      'title': 'El Coleccionista De Huesos (Lincoln Rhyme  #1)',
      'authors': 'Jeffery Deaver',
      'average_rating': 4.19,
      'isbn': '8466305130',
      'isbn13': 9788466305136,
      'language_code': 'spa',
      '  num_pages': 640,
      'ratings_count': 26,
      'text_reviews_count': 2,
      'publication_date': '6/1/2003',
      'publisher': 'Punto de Lectura'},
     {'bookID': 2386,
      'title': 'Moby Dick',
      'authors': 'Herman Melville/William Hootkins',
      'average_rating': 3.5,
      'isbn': '9626343583',
      'isbn13': 9789626343586,
      'language_code': 'eng',
      '  num_pages': 25,
      'ratings_count': 67,
      'text_reviews_count': 17,
      'publication_date': '9/1/2005',
      'publisher': 'Naxos Audiobooks'},
     {'bookID': 2388,
      'title': 'Moby-Dick',
      'authors': 'Jan Needle/Patrick Benson/Herman Melville',
      'average_rating': 3.71,
      'isbn': '0763630187',
      'isbn13': 9780763630188,
      'language_code': 'eng',
      '  num_pages': 192,
      'ratings_count': 161,
      'text_reviews_count': 16,
      'publication_date': '9/12/2006',
      'publisher': 'Candlewick Press'},
     {'bookID': 2389,
      'title': 'Moby Dick',
      'authors': 'Herman Melville/William Hootkins',
      'average_rating': 3.5,
      'isbn': '0143058096',
      'isbn13': 9780143058090,
      'language_code': 'eng',
      '  num_pages': 6,
      'ratings_count': 8858,
      'text_reviews_count': 885,
      'publication_date': '6/16/2005',
      'publisher': 'Penguin Audio'},
     {'bookID': 2390,
      'title': 'Moby-Dick',
      'authors': 'Herman Melville/Carl F. Hovde',
      'average_rating': 3.5,
      'isbn': '1593080182',
      'isbn13': 9781593080181,
      'language_code': 'eng',
      '  num_pages': 707,
      'ratings_count': 1260,
      'text_reviews_count': 207,
      'publication_date': '4/1/2003',
      'publisher': 'Barnes  Noble Classics'},
     {'bookID': 2400,
      'title': "Herman Melville's Moby-Dick: A Routledge Study Guide and Sourcebook",
      'authors': 'Michael J. Davey/Duncan Wu',
      'average_rating': 3.61,
      'isbn': '0415247713',
      'isbn13': 9780415247719,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 50,
      'text_reviews_count': 7,
      'publication_date': '9/18/2003',
      'publisher': 'Routledge'},
     {'bookID': 2404,
      'title': 'Moby Dick: or The White Whale (Oxford Illustrated Classics)',
      'authors': 'Geraldine McCaughrean/Victor G. Ambrus/Herman Melville',
      'average_rating': 3.82,
      'isbn': '0192781537',
      'isbn13': 9780192781536,
      'language_code': 'eng',
      '  num_pages': 104,
      'ratings_count': 39,
      'text_reviews_count': 5,
      'publication_date': '4/16/1998',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 2407,
      'title': "Melville's Moby Dick: An American Nekyia (Studies in Jungian Psychology by Jungian Analysts)",
      'authors': 'Edward F. Edinger',
      'average_rating': 3.93,
      'isbn': '0919123708',
      'isbn13': 9780919123700,
      'language_code': 'eng',
      '  num_pages': 156,
      'ratings_count': 23,
      'text_reviews_count': 4,
      'publication_date': '4/30/2004',
      'publisher': 'Inner City Books'},
     {'bookID': 2409,
      'title': 'Moby Dick: Or  the White Whale (Oxford Illustrated Classics Series)',
      'authors': 'Geraldine McCaughrean/Victor G. Ambrus/Herman Melville',
      'average_rating': 3.82,
      'isbn': '019274156X',
      'isbn13': 9780192741561,
      'language_code': 'eng',
      '  num_pages': 102,
      'ratings_count': 6,
      'text_reviews_count': 0,
      'publication_date': '4/3/1997',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 2411,
      'title': 'Melville and the politics of identity: From *King Lear* to *Moby-Dick*',
      'authors': 'Julian Markels',
      'average_rating': 3.33,
      'isbn': '0252063023',
      'isbn13': 9780252063022,
      'language_code': 'eng',
      '  num_pages': 164,
      'ratings_count': 0,
      'text_reviews_count': 0,
      'publication_date': '7/1/1993',
      'publisher': 'University of Illinois Press'},
     {'bookID': 2412,
      'title': 'Unpainted to the Last: "Moby Dick" and Twentieth-century American Art',
      'authors': 'Elizabeth A. Schultz',
      'average_rating': 4.28,
      'isbn': '0700607420',
      'isbn13': 9780700607426,
      'language_code': 'eng',
      '  num_pages': 400,
      'ratings_count': 16,
      'text_reviews_count': 1,
      'publication_date': '10/20/1995',
      'publisher': 'University Press of Kansas'},
     {'bookID': 2423,
      'title': 'Double Tap (Paul Madriani  #8)',
      'authors': 'Steve Martini',
      'average_rating': 3.92,
      'isbn': '0515139734',
      'isbn13': 9780515139730,
      'language_code': 'en-US',
      '  num_pages': 401,
      'ratings_count': 2790,
      'text_reviews_count': 159,
      'publication_date': '12/27/2005',
      'publisher': 'Jove Books'},
     {'bookID': 2430,
      'title': 'The List',
      'authors': 'Steve Martini',
      'average_rating': 3.96,
      'isbn': '0515121495',
      'isbn13': 9780515121490,
      'language_code': 'eng',
      '  num_pages': 451,
      'ratings_count': 12534,
      'text_reviews_count': 141,
      'publication_date': '12/1/1997',
      'publisher': 'Jove'},
     {'bookID': 2442,
      'title': 'Witches Abroad (Discworld  #12; Witches #3)',
      'authors': 'Terry Pratchett',
      'average_rating': 4.22,
      'isbn': '0061020613',
      'isbn13': 9780061020612,
      'language_code': 'eng',
      '  num_pages': 374,
      'ratings_count': 58408,
      'text_reviews_count': 1272,
      'publication_date': '7/30/2002',
      'publisher': 'HarperTorch'},
     {'bookID': 2443,
      'title': 'The Innocents Abroad',
      'authors': 'Mark Twain/Grover Gardner',
      'average_rating': 3.86,
      'isbn': '0812967054',
      'isbn13': 9780812967050,
      'language_code': 'eng',
      '  num_pages': 560,
      'ratings_count': 8879,
      'text_reviews_count': 693,
      'publication_date': '2/11/2003',
      'publisher': 'Modern Library'},
     {'bookID': 2445,
      'title': 'Teaching English Abroad',
      'authors': 'Susan  Griffith',
      'average_rating': 3.57,
      'isbn': '1854583522',
      'isbn13': 9781854583529,
      'language_code': 'eng',
      '  num_pages': 576,
      'ratings_count': 38,
      'text_reviews_count': 6,
      'publication_date': '1/1/2007',
      'publisher': 'Vacation Work Publications'},
     {'bookID': 2452,
      'title': 'Theocritus: Select Poems: Select Poems',
      'authors': 'Theocritus/Kenneth James Dover',
      'average_rating': 3.0,
      'isbn': '0862921473',
      'isbn13': 9780862921477,
      'language_code': 'grc',
      '  num_pages': 395,
      'ratings_count': 1,
      'text_reviews_count': 1,
      'publication_date': '6/1/1991',
      'publisher': 'Bristol Classical Press'},
     {'bookID': 2473,
      'title': 'The Shield. Catalogue of Women. Other Fragments. (Hesiod II)',
      'authors': 'Hesiod/Glenn W. Most',
      'average_rating': 4.03,
      'isbn': '0674996232',
      'isbn13': 9780674996236,
      'language_code': 'eng',
      '  num_pages': 434,
      'ratings_count': 33,
      'text_reviews_count': 1,
      'publication_date': '3/1/2007',
      'publisher': 'Harvard University Press'},
     {'bookID': 2486,
      'title': "Death and the King's Horseman",
      'authors': 'Wole Soyinka/Simon Gikandi',
      'average_rating': 3.76,
      'isbn': '0393977617',
      'isbn13': 9780393977615,
      'language_code': 'en-US',
      '  num_pages': 254,
      'ratings_count': 259,
      'text_reviews_count': 30,
      'publication_date': '11/5/2002',
      'publisher': 'W. W. Norton & Company'},
     {'bookID': 2494,
      'title': 'The Time Machine',
      'authors': 'H.G. Wells/Patrick Parrinder/Steven McLean/Marina Warner',
      'average_rating': 3.89,
      'isbn': '0141439971',
      'isbn13': 9780141439976,
      'language_code': 'eng',
      '  num_pages': 104,
      'ratings_count': 3094,
      'text_reviews_count': 301,
      'publication_date': '3/31/2005',
      'publisher': 'Penguin Books Ltd'},
     {'bookID': 2495,
      'title': 'The Time Machine',
      'authors': 'H.G. Wells/Cynthia Brantley Johnson/Benjamin Beard',
      'average_rating': 3.89,
      'isbn': '0743487737',
      'isbn13': 9780743487733,
      'language_code': 'eng',
      '  num_pages': 150,
      'ratings_count': 372,
      'text_reviews_count': 36,
      'publication_date': '7/1/2004',
      'publisher': 'Simon  Schuster'},
     {'bookID': 2499,
      'title': "The Ultimate Time Machine: A Remote Viewer's Perception of Time & Predictions for the New Millennium",
      'authors': 'Joseph McMoneagle',
      'average_rating': 3.59,
      'isbn': '157174102X',
      'isbn13': 9781571741028,
      'language_code': 'en-GB',
      '  num_pages': 275,
      'ratings_count': 68,
      'text_reviews_count': 6,
      'publication_date': '10/1/1998',
      'publisher': 'Hampton Roads Publishing Company'},
     {'bookID': 2501,
      'title': 'The Time Machine',
      'authors': 'H.G. Wells/Melvin Burgess',
      'average_rating': 3.89,
      'isbn': '0439436540',
      'isbn13': 9780439436540,
      'language_code': 'eng',
      '  num_pages': 123,
      'ratings_count': 284,
      'text_reviews_count': 35,
      'publication_date': '3/1/2004',
      'publisher': 'Scholastic Paperbacks'},
     {'bookID': 2504,
      'title': 'The Complete Short Stories',
      'authors': 'H.G. Wells/John R. Hammond',
      'average_rating': 4.14,
      'isbn': '1842124021',
      'isbn13': 9781842124024,
      'language_code': 'eng',
      '  num_pages': 864,
      'ratings_count': 875,
      'text_reviews_count': 33,
      'publication_date': '5/1/2001',
      'publisher': 'Orion Publishing'},
     {'bookID': 2506,
      'title': 'Selected Stories',
      'authors': 'H.G. Wells/Ursula K. Le Guin',
      'average_rating': 3.93,
      'isbn': '0812970756',
      'isbn13': 9780812970753,
      'language_code': 'en-US',
      '  num_pages': 432,
      'ratings_count': 80,
      'text_reviews_count': 11,
      'publication_date': '7/13/2004',
      'publisher': 'Modern Library'},
     {'bookID': 2508,
      'title': 'Tono-Bungay',
      'authors': 'H.G. Wells/Edward Mendelson/Patrick Parrinder',
      'average_rating': 3.42,
      'isbn': '0141441119',
      'isbn13': 9780141441115,
      'language_code': 'eng',
      '  num_pages': 414,
      'ratings_count': 856,
      'text_reviews_count': 111,
      'publication_date': '6/28/2005',
      'publisher': 'Penguin Classics'},
     {'bookID': 2519,
      'title': "The Name of the Rose (Everyman's Library (Cloth))",
      'authors': 'Umberto Eco',
      'average_rating': 4.12,
      'isbn': '0307264890',
      'isbn13': 9780307264893,
      'language_code': 'en-US',
      '  num_pages': 560,
      'ratings_count': 1338,
      'text_reviews_count': 113,
      'publication_date': '9/26/2006',
      'publisher': "Everyman's Library"},
     {'bookID': 2520,
      'title': 'In the Name of Jesus: Reflections on Christian Leadership',
      'authors': 'Henri J.M. Nouwen',
      'average_rating': 4.34,
      'isbn': '0824512596',
      'isbn13': 9780824512590,
      'language_code': 'en-US',
      '  num_pages': 120,
      'ratings_count': 8228,
      'text_reviews_count': 410,
      'publication_date': '10/1/1992',
      'publisher': 'Crossroad'},
     {'bookID': 2521,
      'title': 'Blood Done Sign My Name: A True Story',
      'authors': 'Timothy B. Tyson',
      'average_rating': 4.15,
      'isbn': '1400083117',
      'isbn13': 9781400083114,
      'language_code': 'eng',
      '  num_pages': 368,
      'ratings_count': 2594,
      'text_reviews_count': 403,
      'publication_date': '5/3/2005',
      'publisher': 'Broadway Books'},
     {'bookID': 2526,
      'title': 'Blindness',
      'authors': 'Jos?? Saramago/Giovanni Pontiero',
      'average_rating': 4.11,
      'isbn': '0156007754',
      'isbn13': 9780156007757,
      'language_code': 'eng',
      '  num_pages': 326,
      'ratings_count': 107455,
      'text_reviews_count': 7778,
      'publication_date': '10/4/1999',
      'publisher': 'Mariner Books'},
     {'bookID': 2527,
      'title': 'The Gospel According to Jesus Christ',
      'authors': 'Jos?? Saramago/Giovanni Pontiero',
      'average_rating': 4.29,
      'isbn': '0156001411',
      'isbn13': 9780156001410,
      'language_code': 'eng',
      '  num_pages': 377,
      'ratings_count': 799,
      'text_reviews_count': 107,
      'publication_date': '9/28/1994',
      'publisher': 'Harcourt'},
     {'bookID': 2528,
      'title': 'All the Names',
      'authors': 'Jos?? Saramago/Margaret Jull Costa',
      'average_rating': 3.89,
      'isbn': '0156010593',
      'isbn13': 9780156010597,
      'language_code': 'eng',
      '  num_pages': 245,
      'ratings_count': 11016,
      'text_reviews_count': 734,
      'publication_date': '10/5/2001',
      'publisher': 'Mariner Books'},
     {'bookID': 2529,
      'title': 'The Tale of the Unknown Island',
      'authors': 'Jos?? Saramago/Peter S??s/Margaret Jull Costa',
      'average_rating': 3.89,
      'isbn': '0156013037',
      'isbn13': 9780156013031,
      'language_code': 'eng',
      '  num_pages': 64,
      'ratings_count': 3331,
      'text_reviews_count': 242,
      'publication_date': '10/5/2000',
      'publisher': 'Mariner Books'},
     {'bookID': 2530,
      'title': 'Baltasar and Blimunda',
      'authors': 'Jos?? Saramago/Giovanni Pontiero',
      'average_rating': 3.92,
      'isbn': '0156005204',
      'isbn13': 9780156005203,
      'language_code': 'eng',
      '  num_pages': 346,
      'ratings_count': 6184,
      'text_reviews_count': 284,
      'publication_date': '10/16/1998',
      'publisher': 'Mariner Books'},
     {'bookID': 2531,
      'title': 'The Cave',
      'authors': 'Jos?? Saramago/Margaret Jull Costa',
      'average_rating': 3.84,
      'isbn': '0156028794',
      'isbn13': 9780156028790,
      'language_code': 'eng',
      '  num_pages': 307,
      'ratings_count': 7649,
      'text_reviews_count': 548,
      'publication_date': '10/15/2003',
      'publisher': 'Mariner Books'},
     {'bookID': 2535,
      'title': 'The Stone Raft',
      'authors': 'Jos?? Saramago/Giovanni Pontiero',
      'average_rating': 3.8,
      'isbn': '0156004011',
      'isbn13': 9780156004015,
      'language_code': 'en-US',
      '  num_pages': 292,
      'ratings_count': 308,
      'text_reviews_count': 30,
      'publication_date': '6/14/1996',
      'publisher': 'Mariner Books'},
     {'bookID': 2536,
      'title': 'The Year of the Death of Ricardo Reis',
      'authors': 'Jos?? Saramago/Giovanni Pontiero',
      'average_rating': 4.02,
      'isbn': '1860465021',
      'isbn13': 9781860465024,
      'language_code': 'eng',
      '  num_pages': 384,
      'ratings_count': 3826,
      'text_reviews_count': 191,
      'publication_date': '9/17/1998',
      'publisher': 'Vintage Classics'},
     {'bookID': 2538,
      'title': 'El hombre duplicado',
      'authors': 'Jos?? Saramago/Pilar del R??o',
      'average_rating': 3.89,
      'isbn': '8466312803',
      'isbn13': 9788466312806,
      'language_code': 'spa',
      '  num_pages': 380,
      'ratings_count': 1295,
      'text_reviews_count': 106,
      'publication_date': '9/1/2004',
      'publisher': 'Punto de Lectura'},
     {'bookID': 2539,
      'title': 'Ensayo sobre la lucidez',
      'authors': 'Jos?? Saramago/Pilar del R??o',
      'average_rating': 3.8,
      'isbn': '8466314741',
      'isbn13': 9788466314749,
      'language_code': 'spa',
      '  num_pages': 461,
      'ratings_count': 1744,
      'text_reviews_count': 124,
      'publication_date': '1/1/2005',
      'publisher': 'Punto de Lectura'},
     {'bookID': 2541,
      'title': 'La caverna',
      'authors': 'Jos?? Saramago/Pilar del R??o',
      'average_rating': 3.84,
      'isbn': '846630679X',
      'isbn13': 9788466306799,
      'language_code': 'spa',
      '  num_pages': 441,
      'ratings_count': 842,
      'text_reviews_count': 69,
      'publication_date': '2/1/2003',
      'publisher': 'Punto de Lectura'},
     {'bookID': 2542,
      'title': 'The History of the Siege of Lisbon',
      'authors': 'Jos?? Saramago/Giovanni Pontiero',
      'average_rating': 3.81,
      'isbn': '0156006243',
      'isbn13': 9780156006248,
      'language_code': 'eng',
      '  num_pages': 314,
      'ratings_count': 331,
      'text_reviews_count': 62,
      'publication_date': '9/1/1998',
      'publisher': 'Mariner Books'},
     {'bookID': 2543,
      'title': 'Las intermitencias de la muerte',
      'authors': 'Jos?? Saramago/Pilar del R??o',
      'average_rating': 4.0,
      'isbn': '9587043642',
      'isbn13': 9789587043648,
      'language_code': 'spa',
      '  num_pages': 274,
      'ratings_count': 2862,
      'text_reviews_count': 306,
      'publication_date': '12/1/2005',
      'publisher': 'Alfaguara'},
     {'bookID': 2545,
      'title': 'The Treasured Writings of Kahlil Gibran',
      'authors': 'Kahlil Gibran',
      'average_rating': 4.42,
      'isbn': '089009389X',
      'isbn13': 9780890093894,
      'language_code': 'eng',
      '  num_pages': 902,
      'ratings_count': 1432,
      'text_reviews_count': 45,
      'publication_date': '10/6/2009',
      'publisher': 'Castle Books'},
     {'bookID': 2547,
      'title': 'The Prophet',
      'authors': 'Kahlil Gibran/?????????? ???????? ??????????/Jihad El',
      'average_rating': 4.23,
      'isbn': '000100039X',
      'isbn13': 9780001000391,
      'language_code': 'eng',
      '  num_pages': 127,
      'ratings_count': 184293,
      'text_reviews_count': 5418,
      'publication_date': '1/1/2010',
      'publisher': 'Rupa & Co'},
     {'bookID': 2549,
      'title': 'A Tear and a Smile',
      'authors': 'Kahlil Gibran/?????????? ???????? ??????????/H.M. Nahmad/Robert Hillyer',
      'average_rating': 4.03,
      'isbn': '0394448049',
      'isbn13': 9780394448046,
      'language_code': 'eng',
      '  num_pages': 228,
      'ratings_count': 2094,
      'text_reviews_count': 104,
      'publication_date': '6/27/1950',
      'publisher': 'Alfred A.Knopf'},
     {'bookID': 2551,
      'title': 'On the Road',
      'authors': 'Jack Kerouac',
      'average_rating': 3.63,
      'isbn': '0143036386',
      'isbn13': 9780143036388,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 488,
      'text_reviews_count': 39,
      'publication_date': '9/6/2005',
      'publisher': 'Penguin Books'},
     {'bookID': 2552,
      'title': 'On the Road',
      'authors': 'Jack Kerouac/Ann Charters',
      'average_rating': 3.63,
      'isbn': '0141182679',
      'isbn13': 9780141182674,
      'language_code': 'eng',
      '  num_pages': 281,
      'ratings_count': 5575,
      'text_reviews_count': 502,
      'publication_date': '2/24/2000',
      'publisher': 'Penguin Books'},
     {'bookID': 2557,
      'title': 'De Kooning: An American Master',
      'authors': 'Mark Stevens/Annalyn Swan',
      'average_rating': 4.11,
      'isbn': '0375711163',
      'isbn13': 9780375711169,
      'language_code': 'eng',
      '  num_pages': 732,
      'ratings_count': 2732,
      'text_reviews_count': 105,
      'publication_date': '4/4/2006',
      'publisher': 'Knopf Publishing Group'},
     {'bookID': 2560,
      'title': 'Willem de Kooning: Late Paintings',
      'authors': 'Julie Sylvester/David Sylvester',
      'average_rating': 5.0,
      'isbn': '382960226X',
      'isbn13': 9783829602266,
      'language_code': 'eng',
      '  num_pages': 83,
      'ratings_count': 1,
      'text_reviews_count': 0,
      'publication_date': '9/1/2006',
      'publisher': 'Schirmer Mosel'},
     {'bookID': 2567,
      'title': 'Ak??: The Years of Childhood',
      'authors': 'Wole Soyinka',
      'average_rating': 3.93,
      'isbn': '0679725407',
      'isbn13': 9780679725404,
      'language_code': 'eng',
      '  num_pages': 230,
      'ratings_count': 1284,
      'text_reviews_count': 90,
      'publication_date': '10/23/1989',
      'publisher': 'Vintage'},
     {'bookID': 2581,
      'title': 'Ready for Anything: 52 Productivity Principles for Getting Things Done',
      'authors': 'David    Allen',
      'average_rating': 3.85,
      'isbn': '0143034545',
      'isbn13': 9780143034544,
      'language_code': 'eng',
      '  num_pages': 165,
      'ratings_count': 3832,
      'text_reviews_count': 178,
      'publication_date': '12/28/2004',
      'publisher': 'Penguin Books'},
     {'bookID': 2584,
      'title': "The Facilitator's Book of Questions: Tools for Looking Together at Student and Teacher Work",
      'authors': 'David  Allen/Tina Blythe/Gene Thompson-Grove',
      'average_rating': 4.0,
      'isbn': '0807744689',
      'isbn13': 9780807744680,
      'language_code': 'eng',
      '  num_pages': 142,
      'ratings_count': 54,
      'text_reviews_count': 4,
      'publication_date': '4/29/2004',
      'publisher': 'Teachers College Press'},
     {'bookID': 2586,
      'title': 'Sun Tzu and the Art of Business: Six Strategic Principles for Managers',
      'authors': 'Sun Tzu/Mark McNeilly',
      'average_rating': 3.89,
      'isbn': '0195137892',
      'isbn13': 9780195137897,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 125,
      'text_reviews_count': 13,
      'publication_date': '4/1/2000',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 2595,
      'title': 'Marketing Warfare',
      'authors': 'Al Ries/Jack Trout',
      'average_rating': 4.11,
      'isbn': '0071460829',
      'isbn13': 9780071460828,
      'language_code': 'eng',
      '  num_pages': 216,
      'ratings_count': 942,
      'text_reviews_count': 59,
      'publication_date': '12/13/2005',
      'publisher': 'McGraw-Hill Education'},
     {'bookID': 2612,
      'title': 'The Tipping Point: How Little Things Can Make a Big Difference',
      'authors': 'Malcolm Gladwell',
      'average_rating': 3.97,
      'isbn': '0316346624',
      'isbn13': 9780316346627,
      'language_code': 'eng',
      '  num_pages': 301,
      'ratings_count': 633037,
      'text_reviews_count': 11898,
      'publication_date': '1/7/2002',
      'publisher': 'Back Bay Books'},
     {'bookID': 2613,
      'title': 'Unleashing the Ideavirus: Stop Marketing AT People! Turn Your Ideas into Epidemics by Helping Your Customers Do the Marketing thing for You.',
      'authors': 'Seth Godin/Malcolm Gladwell',
      'average_rating': 3.98,
      'isbn': '0786887176',
      'isbn13': 9780786887170,
      'language_code': 'en-US',
      '  num_pages': 234,
      'ratings_count': 4600,
      'text_reviews_count': 88,
      'publication_date': '10/10/2001',
      'publisher': 'Hachette Books'},
     {'bookID': 2615,
      'title': "The Innovator's Dilemma: The Revolutionary Book that Will Change the Way You Do Business",
      'authors': 'Clayton M. Christensen/L.J. Ganser',
      'average_rating': 3.99,
      'isbn': '0060521996',
      'isbn13': 9780060521998,
      'language_code': 'eng',
      '  num_pages': 286,
      'ratings_count': 32079,
      'text_reviews_count': 752,
      'publication_date': '1/7/2003',
      'publisher': 'Harper Paperbacks'},
     {'bookID': 2619,
      'title': 'Great Expectations',
      'authors': 'Charles Dickens/David Trotter/Charlotte Mitchell',
      'average_rating': 3.77,
      'isbn': '0141439564',
      'isbn13': 9780141439563,
      'language_code': 'eng',
      '  num_pages': 512,
      'ratings_count': 14228,
      'text_reviews_count': 668,
      'publication_date': '12/31/2002',
      'publisher': 'Penguin Books'},
     {'bookID': 2626,
      'title': 'Great Expectations: Authoritative Text  Backgrounds  Contexts  Criticism',
      'authors': 'Charles Dickens/Edgar Rosenberg',
      'average_rating': 3.77,
      'isbn': '0393960692',
      'isbn13': 9780393960693,
      'language_code': 'eng',
      '  num_pages': 776,
      'ratings_count': 573,
      'text_reviews_count': 38,
      'publication_date': '1/19/1999',
      'publisher': 'W.W. Norton & Company'},
     {'bookID': 2646,
      'title': 'Luther and Erasmus: Free Will and Salvation (Library of Christian Classics)',
      'authors': 'Erasmus/Martin Luther/Philip S. Watson/E. Gordon Rupp',
      'average_rating': 3.8,
      'isbn': '0664241581',
      'isbn13': 9780664241582,
      'language_code': 'eng',
      '  num_pages': 364,
      'ratings_count': 108,
      'text_reviews_count': 13,
      'publication_date': '1/1/1969',
      'publisher': 'Westminster John Knox Press'},
     {'bookID': 2654,
      'title': 'To Kill a Mockingbird',
      'authors': 'Harper Lee',
      'average_rating': 4.27,
      'isbn': '0060935464',
      'isbn13': 9780060935467,
      'language_code': 'eng',
      '  num_pages': 323,
      'ratings_count': 10524,
      'text_reviews_count': 898,
      'publication_date': '7/5/2005',
      'publisher': 'Harper Perennial Modern Classics'},
     {'bookID': 2655,
      'title': 'To Kill a Mockingbird',
      'authors': 'Harper Lee/Sissy Spacek',
      'average_rating': 4.27,
      'isbn': '0060888695',
      'isbn13': 9780060888695,
      'language_code': 'eng',
      '  num_pages': 11,
      'ratings_count': 697,
      'text_reviews_count': 180,
      'publication_date': '8/22/2006',
      'publisher': 'Caedmon'},
     {'bookID': 2661,
      'title': 'To Kill a Mockingbird',
      'authors': 'Harper Lee',
      'average_rating': 4.27,
      'isbn': '0061205699',
      'isbn13': 9780061205699,
      'language_code': 'en-US',
      '  num_pages': 323,
      'ratings_count': 271,
      'text_reviews_count': 34,
      'publication_date': '10/17/2006',
      'publisher': 'Harper'},
     {'bookID': 2673,
      'title': "The Wealthy Barber: Everyone's Common-Sense Guide to Becoming Financially Independent",
      'authors': 'David H. Chilton',
      'average_rating': 4.02,
      'isbn': '0761501665',
      'isbn13': 9780761501664,
      'language_code': 'eng',
      '  num_pages': 199,
      'ratings_count': 66,
      'text_reviews_count': 4,
      'publication_date': '9/20/1995',
      'publisher': 'Prima Lifestyles'},
     {'bookID': 2677,
      'title': 'A Modest Proposal and Other Satirical Works',
      'authors': 'Jonathan Swift',
      'average_rating': 4.05,
      'isbn': '0486287599',
      'isbn13': 9780486287591,
      'language_code': 'eng',
      '  num_pages': 64,
      'ratings_count': 13562,
      'text_reviews_count': 141,
      'publication_date': '2/2/1996',
      'publisher': 'Dover Publications'},
     {'bookID': 2678,
      'title': "Gulliver's Travels / A Modest Proposal",
      'authors': 'Jonathan Swift/Jesse Gale',
      'average_rating': 3.79,
      'isbn': '1416500391',
      'isbn13': 9781416500391,
      'language_code': 'eng',
      '  num_pages': 416,
      'ratings_count': 2161,
      'text_reviews_count': 50,
      'publication_date': '8/1/2005',
      'publisher': 'Simon  Schuster'},
     {'bookID': 2680,
      'title': 'Empire 2.0: A Modest Proposal for a United States of the West (Terra Nova)',
      'authors': 'Xavier de C./Xavier de C./Joseph Rowe',
      'average_rating': 4.67,
      'isbn': '1556434952',
      'isbn13': 9781556434952,
      'language_code': 'eng',
      '  num_pages': 144,
      'ratings_count': 3,
      'text_reviews_count': 0,
      'publication_date': '5/4/2004',
      'publisher': 'North Atlantic Books'},
     {'bookID': 2686,
      'title': 'The Bostonians',
      'authors': 'Henry James/R.D. Gooder',
      'average_rating': 3.59,
      'isbn': '0192834428',
      'isbn13': 9780192834423,
      'language_code': 'eng',
      '  num_pages': 504,
      'ratings_count': 85,
      'text_reviews_count': 12,
      'publication_date': '7/23/1998',
      'publisher': 'Oxford University Press'},
     {'bookID': 2687,
      'title': 'Novels 1896???1899: The Other House / The Spoils of Poynton / What Maisie Knew / The Awkward Age',
      'authors': 'Henry James/Myra Jehlen',
      'average_rating': 4.28,
      'isbn': '1931082308',
      'isbn13': 9781931082303,
      'language_code': 'eng',
      '  num_pages': 1035,
      'ratings_count': 25,
      'text_reviews_count': 4,
      'publication_date': '3/10/2003',
      'publisher': 'Library of America'},
     {'bookID': 2688,
      'title': 'Novels 1901???1902: The Sacred Fount / The Wings of the Dove',
      'authors': 'Henry James/Leo Bersani',
      'average_rating': 4.63,
      'isbn': '193108288X',
      'isbn13': 9781931082884,
      'language_code': 'eng',
      '  num_pages': 713,
      'ratings_count': 27,
      'text_reviews_count': 3,
      'publication_date': '2/2/2006',
      'publisher': 'Library of America'},
     {'bookID': 2692,
      'title': 'Complete Stories 1892???1898',
      'authors': 'Henry James/John Hollander/David Bromwich',
      'average_rating': 4.22,
      'isbn': '1883011094',
      'isbn13': 9781883011093,
      'language_code': 'eng',
      '  num_pages': 958,
      'ratings_count': 198,
      'text_reviews_count': 7,
      'publication_date': '1/1/1996',
      'publisher': 'Library of America'},
     {'bookID': 2696,
      'title': 'The Canterbury Tales',
      'authors': 'Geoffrey Chaucer/Nevill Coghill',
      'average_rating': 3.49,
      'isbn': '0140424385',
      'isbn13': 9780140424386,
      'language_code': 'eng',
      '  num_pages': 504,
      'ratings_count': 168559,
      'text_reviews_count': 2365,
      'publication_date': '1/30/2003',
      'publisher': 'Penguin Classics'},
     {'bookID': 2698,
      'title': 'The Canterbury Tales',
      'authors': 'Geoffrey Chaucer/David  Wright',
      'average_rating': 3.49,
      'isbn': '019283360X',
      'isbn13': 9780192833600,
      'language_code': 'eng',
      '  num_pages': 465,
      'ratings_count': 257,
      'text_reviews_count': 22,
      'publication_date': '7/9/1998',
      'publisher': 'Oxford University Press'},
     {'bookID': 2701,
      'title': 'The Canterbury Tales (original-spelling edition)',
      'authors': 'Geoffrey Chaucer/Jill Mann',
      'average_rating': 3.49,
      'isbn': '014042234X',
      'isbn13': 9780140422344,
      'language_code': 'enm',
      '  num_pages': 1254,
      'ratings_count': 792,
      'text_reviews_count': 59,
      'publication_date': '4/7/2005',
      'publisher': 'Penguin Classics'},
     {'bookID': 2702,
      'title': "Chaucer's Canterbury Tales (Selected): An Interlinear Translation",
      'authors': 'Geoffrey Chaucer/Vincent Foster Hopper',
      'average_rating': 3.8,
      'isbn': '0812000390',
      'isbn13': 9780812000399,
      'language_code': 'eng',
      '  num_pages': 530,
      'ratings_count': 73,
      'text_reviews_count': 5,
      'publication_date': '12/31/1977',
      'publisher': 'Barrons Educational Series'},
     {'bookID': 2705,
      'title': 'Oxford Guides to Chaucer: The Canterbury Tales',
      'authors': 'Helen  Cooper',
      'average_rating': 4.02,
      'isbn': '0198711557',
      'isbn13': 9780198711551,
      'language_code': 'eng',
      '  num_pages': 456,
      'ratings_count': 84,
      'text_reviews_count': 4,
      'publication_date': '5/23/1996',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 2706,
      'title': 'Love Visions',
      'authors': 'Geoffrey Chaucer/Brian Stone',
      'average_rating': 3.61,
      'isbn': '0140444084',
      'isbn13': 9780140444087,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 70,
      'text_reviews_count': 6,
      'publication_date': '5/26/1983',
      'publisher': 'Penguin Classics'},
     {'bookID': 2710,
      'title': "Chaucer's Canterbury Tales",
      'authors': 'Geoffrey Chaucer',
      'average_rating': 3.49,
      'isbn': '0671475029',
      'isbn13': 9780671475024,
      'language_code': 'eng',
      '  num_pages': 383,
      'ratings_count': 36,
      'text_reviews_count': 5,
      'publication_date': '1/28/1964',
      'publisher': 'Washington Square Press'},
     {'bookID': 2711,
      'title': 'The Riverside Chaucer',
      'authors': 'Geoffrey Chaucer/Larry Dean Benson/F.N. Robinson',
      'average_rating': 4.18,
      'isbn': '0395290317',
      'isbn13': 9780395290316,
      'language_code': 'enm',
      '  num_pages': 1327,
      'ratings_count': 7760,
      'text_reviews_count': 152,
      'publication_date': '12/12/1987',
      'publisher': 'Houghton Mifflin'},
     {'bookID': 2713,
      'title': 'The Portable Chaucer',
      'authors': 'Geoffrey Chaucer/Theodore Morrison',
      'average_rating': 3.86,
      'isbn': '0140150811',
      'isbn13': 9780140150810,
      'language_code': 'eng',
      '  num_pages': 611,
      'ratings_count': 70,
      'text_reviews_count': 8,
      'publication_date': '5/26/1977',
      'publisher': 'Penguin Books'},
     {'bookID': 2715,
      'title': 'Salt: A World History',
      'authors': 'Mark Kurlansky',
      'average_rating': 3.74,
      'isbn': '0142001619',
      'isbn13': 9780142001615,
      'language_code': 'eng',
      '  num_pages': 484,
      'ratings_count': 50335,
      'text_reviews_count': 3012,
      'publication_date': '1/28/2003',
      'publisher': 'Penguin Books'},
     {'bookID': 2718,
      'title': 'Salt in His Shoes: Michael Jordan in Pursuit of a Dream',
      'authors': 'Deloris Jordan/Kadir Nelson/Roslyn M. Jordan',
      'average_rating': 4.2,
      'isbn': '0689834195',
      'isbn13': 9780689834196,
      'language_code': 'eng',
      '  num_pages': 32,
      'ratings_count': 1178,
      'text_reviews_count': 173,
      'publication_date': '11/1/2003',
      'publisher': 'Simon  Schuster Books for Young Readers'},
     {'bookID': 2719,
      'title': 'The Book of Salt',
      'authors': 'Monique Truong',
      'average_rating': 3.52,
      'isbn': '0618446885',
      'isbn13': 9780618446889,
      'language_code': 'eng',
      '  num_pages': 261,
      'ratings_count': 4411,
      'text_reviews_count': 629,
      'publication_date': '6/15/2004',
      'publisher': 'Mariner Books'},
     {'bookID': 2722,
      'title': 'Cities of Salt (?????? ?????????? #1)',
      'authors': 'Abdul Rahman Munif/Peter Theroux',
      'average_rating': 4.13,
      'isbn': '039475526X',
      'isbn13': 9780394755267,
      'language_code': 'eng',
      '  num_pages': 627,
      'ratings_count': 856,
      'text_reviews_count': 105,
      'publication_date': '7/17/1989',
      'publisher': 'Vintage'},
     {'bookID': 2723,
      'title': 'The Years of Rice and Salt',
      'authors': 'Kim Stanley Robinson',
      'average_rating': 3.73,
      'isbn': '0553580078',
      'isbn13': 9780553580075,
      'language_code': 'eng',
      '  num_pages': 763,
      'ratings_count': 9344,
      'text_reviews_count': 995,
      'publication_date': '6/3/2003',
      'publisher': 'Bantam Books'},
     {'bookID': 2725,
      'title': 'Illuminations: Essays and Reflections',
      'authors': 'Walter Benjamin/Hannah Arendt/Harry Zohn/Leon Wieseltier',
      'average_rating': 4.29,
      'isbn': '0805202412',
      'isbn13': 9780805202410,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 9254,
      'text_reviews_count': 194,
      'publication_date': '1/13/1969',
      'publisher': 'Schocken'},
     {'bookID': 2727,
      'title': 'Saul Steinberg: Illuminations',
      'authors': 'Saul Steinberg/Joel Smith/Charles Simic',
      'average_rating': 4.51,
      'isbn': '0300115865',
      'isbn13': 9780300115864,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 39,
      'text_reviews_count': 5,
      'publication_date': '11/1/2006',
      'publisher': 'Yale University Press'},
     {'bookID': 2731,
      'title': 'Advanced Global Illumination',
      'authors': 'Philip Dutre',
      'average_rating': 4.5,
      'isbn': '1568813074',
      'isbn13': 9781568813073,
      'language_code': 'eng',
      '  num_pages': 366,
      'ratings_count': 17,
      'text_reviews_count': 2,
      'publication_date': '8/30/2006',
      'publisher': 'A K PETERS'},
     {'bookID': 2735,
      'title': 'Snow Falling On Cedars',
      'authors': 'David Guterson',
      'average_rating': 3.83,
      'isbn': '074754655X',
      'isbn13': 9780747546559,
      'language_code': 'eng',
      '  num_pages': 404,
      'ratings_count': 588,
      'text_reviews_count': 46,
      'publication_date': '10/21/1999',
      'publisher': 'Bloomsbury Publishing PLC'},
     {'bookID': 2743,
      'title': 'The Lost Boy (Dave Pelzer #2)',
      'authors': 'Dave Pelzer',
      'average_rating': 4.1,
      'isbn': '1558745157',
      'isbn13': 9781558745155,
      'language_code': 'eng',
      '  num_pages': 331,
      'ratings_count': 52028,
      'text_reviews_count': 2513,
      'publication_date': '8/1/1997',
      'publisher': 'Health Communications Inc'},
     {'bookID': 2745,
      'title': 'Real Boys: Rescuing Our Sons from the Myths of Boyhood',
      'authors': 'William S. Pollack/Mary Pipher',
      'average_rating': 3.83,
      'isbn': '0805061835',
      'isbn13': 9780805061833,
      'language_code': 'en-US',
      '  num_pages': 480,
      'ratings_count': 1397,
      'text_reviews_count': 128,
      'publication_date': '5/10/1999',
      'publisher': 'Owl Publishing Company'},
     {'bookID': 2749,
      'title': 'Microserfs',
      'authors': 'Douglas Coupland',
      'average_rating': 3.88,
      'isbn': '0007179812',
      'isbn13': 9780007179817,
      'language_code': 'eng',
      '  num_pages': 371,
      'ratings_count': 442,
      'text_reviews_count': 38,
      'publication_date': '1/1/2008',
      'publisher': 'Harper Perennial'},
     {'bookID': 2756,
      'title': 'New Media Language',
      'authors': 'Jean Aitchison/Diana M. Lewis',
      'average_rating': 3.0,
      'isbn': '0415283043',
      'isbn13': 9780415283045,
      'language_code': 'eng',
      '  num_pages': 209,
      'ratings_count': 2,
      'text_reviews_count': 0,
      'publication_date': '5/22/2003',
      'publisher': 'Routledge'},
     {'bookID': 2761,
      'title': 'The Denial of Death',
      'authors': 'Ernest Becker/Sam Keen/Daniel Goleman',
      'average_rating': 4.16,
      'isbn': '0684832402',
      'isbn13': 9780684832401,
      'language_code': 'eng',
      '  num_pages': 336,
      'ratings_count': 6599,
      'text_reviews_count': 635,
      'publication_date': '5/8/1997',
      'publisher': 'Free Press'},
     {'bookID': 2767,
      'title': "A People's History of the United States",
      'authors': 'Howard Zinn',
      'average_rating': 4.08,
      'isbn': '0060838655',
      'isbn13': 9780060838652,
      'language_code': 'eng',
      '  num_pages': 729,
      'ratings_count': 167321,
      'text_reviews_count': 4711,
      'publication_date': '8/2/2005',
      'publisher': 'Harper Perennial'},
     {'bookID': 2768,
      'title': "A People's History of the United States",
      'authors': 'Howard Zinn/Kathy Emery/Ellen Gordon Reeves',
      'average_rating': 4.08,
      'isbn': '1565848268',
      'isbn13': 9781565848269,
      'language_code': 'eng',
      '  num_pages': 619,
      'ratings_count': 39,
      'text_reviews_count': 3,
      'publication_date': '7/1/2003',
      'publisher': 'The New Press'},
     {'bookID': 2770,
      'title': "A People's History of the United States: The Civil War to the Present",
      'authors': 'Howard Zinn/Kathy Emery/Ellen Gordon Reeves',
      'average_rating': 4.0,
      'isbn': '1565847253',
      'isbn13': 9781565847255,
      'language_code': 'eng',
      '  num_pages': 496,
      'ratings_count': 22,
      'text_reviews_count': 0,
      'publication_date': '8/1/2003',
      'publisher': 'The New Press'},
     {'bookID': 2778,
      'title': 'Graphic Design: A Concise History (World of Art)',
      'authors': 'Richard Hollis',
      'average_rating': 4.0,
      'isbn': '0500203474',
      'isbn13': 9780500203477,
      'language_code': 'en-US',
      '  num_pages': 232,
      'ratings_count': 675,
      'text_reviews_count': 12,
      'publication_date': '5/17/2002',
      'publisher': 'Thames  Hudson'},
     {'bookID': 2781,
      'title': 'Immigrant Acts: On Asian American Cultural Politics',
      'authors': 'Lisa Lowe',
      'average_rating': 4.0,
      'isbn': '0822318644',
      'isbn13': 9780822318644,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 206,
      'text_reviews_count': 9,
      'publication_date': '10/21/1996',
      'publisher': 'Duke University Press Books'},
     {'bookID': 2785,
      'title': 'The Old Way of Seeing: How Architecture Lost Its Magic - And How to Get It Back',
      'authors': 'Jonathan Hale',
      'average_rating': 3.92,
      'isbn': '039574010X',
      'isbn13': 9780395740101,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 81,
      'text_reviews_count': 12,
      'publication_date': '9/1/1995',
      'publisher': 'Mariner Books'},
     {'bookID': 2794,
      'title': 'The Crying of Lot 49',
      'authors': 'Thomas Pynchon',
      'average_rating': 3.69,
      'isbn': '006091307X',
      'isbn13': 9780060913076,
      'language_code': 'eng',
      '  num_pages': 152,
      'ratings_count': 57011,
      'text_reviews_count': 3332,
      'publication_date': '10/17/2006',
      'publisher': 'Harper Perennial'},
     {'bookID': 2802,
      'title': "E=mc??: A Biography of the World's Most Famous Equation",
      'authors': 'David Bodanis',
      'average_rating': 4.09,
      'isbn': '0425181642',
      'isbn13': 9780425181645,
      'language_code': 'eng',
      '  num_pages': 337,
      'ratings_count': 6368,
      'text_reviews_count': 321,
      'publication_date': '10/1/2000',
      'publisher': 'Berkley Trade'},
     {'bookID': 2804,
      'title': 'Passionate Minds',
      'authors': 'David Bodanis',
      'average_rating': 4.1,
      'isbn': '0307237206',
      'isbn13': 9780307237200,
      'language_code': 'en-US',
      '  num_pages': 373,
      'ratings_count': 717,
      'text_reviews_count': 112,
      'publication_date': '10/10/2006',
      'publisher': 'Crown Publishing Group (NY)'},
     {'bookID': 2810,
      'title': "Christian Mythmakers: C.S. Lewis  Madeleine L'Engle  J.R.R. Tolkien  George MacDonald  G.K. Chesterton  Charles Williams  Dante Alighieri  John Bunyan  Walter Wangerin  Robert Siegel  and Hannah Hurnard",
      'authors': 'Rolland Hein/Clyde S. Kilby',
      'average_rating': 3.93,
      'isbn': '094089548X',
      'isbn13': 9780940895485,
      'language_code': 'eng',
      '  num_pages': 303,
      'ratings_count': 448,
      'text_reviews_count': 18,
      'publication_date': '12/1/2002',
      'publisher': 'Cornerstone Press Chicago'},
     {'bookID': 2811,
      'title': "A House Like a Lotus (O'Keefe Family  #3)",
      'authors': "Madeleine L'Engle",
      'average_rating': 3.76,
      'isbn': '0440936853',
      'isbn13': 9780440936855,
      'language_code': 'eng',
      '  num_pages': 307,
      'ratings_count': 3976,
      'text_reviews_count': 163,
      'publication_date': '11/1/1985',
      'publisher': 'Dell'},
     {'bookID': 2814,
      'title': 'The Rock That Is Higher: Story as Truth',
      'authors': "Madeleine L'Engle",
      'average_rating': 4.12,
      'isbn': '0877887268',
      'isbn13': 9780877887263,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 496,
      'text_reviews_count': 48,
      'publication_date': '3/19/2002',
      'publisher': 'Shaw Books'},
     {'bookID': 2815,
      'title': 'The Glorious Impossible',
      'authors': "Madeleine L'Engle/Giotto di Bondone",
      'average_rating': 4.25,
      'isbn': '0671686909',
      'isbn13': 9780671686901,
      'language_code': 'eng',
      '  num_pages': 64,
      'ratings_count': 367,
      'text_reviews_count': 38,
      'publication_date': '9/30/1990',
      'publisher': "Simon & Schuster Children's Publishing"},
     {'bookID': 2817,
      'title': 'A Full House: An Austin Family Christmas (Austin Family  #5.6)',
      'authors': "Madeleine L'Engle/Mary Chambers",
      'average_rating': 3.98,
      'isbn': '0877880204',
      'isbn13': 9780877880202,
      'language_code': 'eng',
      '  num_pages': 48,
      'ratings_count': 235,
      'text_reviews_count': 4,
      'publication_date': '3/7/2000',
      'publisher': 'Shaw'},
     {'bookID': 2819,
      'title': 'A Circle of Quiet (Crosswicks Journals #1)',
      'authors': "Madeleine L'Engle",
      'average_rating': 4.21,
      'isbn': '0062545035',
      'isbn13': 9780062545039,
      'language_code': 'en-CA',
      '  num_pages': 246,
      'ratings_count': 5236,
      'text_reviews_count': 506,
      'publication_date': '1/1/1984',
      'publisher': 'HarperOne'},
     {'bookID': 2820,
      'title': 'The Birth of Tragedy and Other Writings',
      'authors': 'Friedrich Nietzsche/Raymond Geuss/Ronald Speirs',
      'average_rating': 4.04,
      'isbn': '0521639875',
      'isbn13': 9780521639873,
      'language_code': 'eng',
      '  num_pages': 204,
      'ratings_count': 388,
      'text_reviews_count': 23,
      'publication_date': '4/22/1999',
      'publisher': 'Cambridge University Press'},
     {'bookID': 2821,
      'title': 'The Birth of Tragedy/The Genealogy of Morals',
      'authors': 'Friedrich Nietzsche/Francis Golffing',
      'average_rating': 4.01,
      'isbn': '0385092105',
      'isbn13': 9780385092104,
      'language_code': 'en-US',
      '  num_pages': 320,
      'ratings_count': 843,
      'text_reviews_count': 42,
      'publication_date': '5/7/1990',
      'publisher': 'Anchor'},
     {'bookID': 2822,
      'title': 'The Birth of Tragedy',
      'authors': 'Friedrich Nietzsche',
      'average_rating': 3.98,
      'isbn': '1419154079',
      'isbn13': 9781419154072,
      'language_code': 'eng',
      '  num_pages': 84,
      'ratings_count': 32,
      'text_reviews_count': 0,
      'publication_date': '6/17/2004',
      'publisher': 'Kessinger Publishing'},
     {'bookID': 2823,
      'title': 'The Birth of Tragedy',
      'authors': 'Friedrich Nietzsche/Michael Tanner/Shaun Whiteside',
      'average_rating': 3.98,
      'isbn': '0140433392',
      'isbn13': 9780140433395,
      'language_code': 'en-US',
      '  num_pages': 160,
      'ratings_count': 10147,
      'text_reviews_count': 301,
      'publication_date': '11/27/2003',
      'publisher': 'Penguin Classics'},
     {'bookID': 2826,
      'title': 'Birth Of A Tragedy: Kashmir 1947',
      'authors': 'Alastair Lamb',
      'average_rating': 4.0,
      'isbn': '0907129072',
      'isbn13': 9780907129073,
      'language_code': 'eng',
      '  num_pages': 179,
      'ratings_count': 9,
      'text_reviews_count': 2,
      'publication_date': '3/14/2008',
      'publisher': 'Roxford Books'},
     {'bookID': 2834,
      'title': "The Tragedy of Pudd'nhead Wilson/Those Extraordinary Twins",
      'authors': 'Mark Twain/David Lionel Smith/Sherley Anne Williams',
      'average_rating': 3.79,
      'isbn': '0195114159',
      'isbn13': 9780195114157,
      'language_code': 'eng',
      '  num_pages': 512,
      'ratings_count': 3664,
      'text_reviews_count': 58,
      'publication_date': '3/6/1997',
      'publisher': 'Oxford University Press  USA'},
     {'bookID': 2835,
      'title': "The Tragedy of Pudd'nhead Wilson",
      'authors': 'Mark Twain/Michael Prichard',
      'average_rating': 3.79,
      'isbn': '140015068X',
      'isbn13': 9781400150687,
      'language_code': 'eng',
      '  num_pages': 0,
      'ratings_count': 3,
      'text_reviews_count': 0,
      'publication_date': '1/1/2003',
      'publisher': 'Tantor Media'},
     {'bookID': 2836,
      'title': 'Bridge to Terabithia',
      'authors': 'Katherine Paterson/Donna Diamond',
      'average_rating': 4.0,
      'isbn': '0060734019',
      'isbn13': 9780060734015,
      'language_code': 'en-US',
      '  num_pages': 191,
      'ratings_count': 1811,
      'text_reviews_count': 152,
      'publication_date': '7/1/2008',
      'publisher': 'HarperTeen'},
     {'bookID': 2843,
      'title': 'Literature Circle Guide: Bridge to Terabithia: Everything You Need For Successful Literature Circles That Get Kids Thinking  Talking  Writing???and Loving Literature',
      'authors': 'Tara MacCarthy',
      'average_rating': 5.0,
      'isbn': '0439271711',
      'isbn13': 9780439271714,
      'language_code': 'eng',
      '  num_pages': 32,
      'ratings_count': 4,
      'text_reviews_count': 1,
      'publication_date': '1/1/2002',
      'publisher': 'Teaching Resources'},
     {'bookID': 2847,
      'title': 'Bread and Roses  Too',
      'authors': 'Katherine Paterson',
      'average_rating': 3.76,
      'isbn': '0618654798',
      'isbn13': 9780618654796,
      'language_code': 'eng',
      '  num_pages': 275,
      'ratings_count': 2018,
      'text_reviews_count': 294,
      'publication_date': '9/4/2006',
      'publisher': 'Clarion Books'},
     {'bookID': 2851,
      'title': 'The Invisible Child',
      'authors': 'Katherine Paterson',
      'average_rating': 4.27,
      'isbn': '0525464824',
      'isbn13': 9780525464822,
      'language_code': 'eng',
      '  num_pages': 266,
      'ratings_count': 99,
      'text_reviews_count': 27,
      'publication_date': '12/31/2001',
      'publisher': 'Dutton Juvenile'},
     {'bookID': 2855,
      'title': 'A Short History of Decay',
      'authors': 'Emil M. Cioran/Richard Howard',
      'average_rating': 4.25,
      'isbn': '1559704640',
      'isbn13': 9781559704649,
      'language_code': 'eng',
      '  num_pages': 186,
      'ratings_count': 1771,
      'text_reviews_count': 99,
      'publication_date': '9/15/1998',
      'publisher': 'Arcade Publishing'},
     {'bookID': 2860,
      'title': 'Scholar of Decay (Ravenloft  #14)',
      'authors': 'Tanya Huff',
      'average_rating': 3.46,
      'isbn': '078690206X',
      'isbn13': 9780786902064,
      'language_code': 'eng',
      '  num_pages': 313,
      'ratings_count': 38,
      'text_reviews_count': 1,
      'publication_date': '5/1/2000',
      'publisher': 'TSR'},
     {'bookID': 2864,
      'title': 'Girl with a Pearl Earring',
      'authors': 'Tracy Chevalier',
      'average_rating': 3.88,
      'isbn': '0452284937',
      'isbn13': 9780452284937,
      'language_code': 'eng',
      '  num_pages': 233,
      'ratings_count': 1162,
      'text_reviews_count': 127,
      'publication_date': '9/30/2003',
      'publisher': 'Plume Books'},
     {'bookID': 2868,
      'title': 'The Golden Tulip',
      'authors': 'Rosalind Laker',
      'average_rating': 3.94,
      'isbn': '0385415605',
      'isbn13': 9780385415606,
      'language_code': 'eng',
      '  num_pages': 585,
      'ratings_count': 29,
      'text_reviews_count': 4,
      'publication_date': '9/1/1991',
      'publisher': 'Doubleday'},
     {'bookID': 2871,
      'title': 'Burning Bright',
      'authors': 'Tracy Chevalier',
      'average_rating': 3.36,
      'isbn': '052594978X',
      'isbn13': 9780525949787,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 10919,
      'text_reviews_count': 1113,
      'publication_date': '3/20/2007',
      'publisher': 'Dutton'},
     {'bookID': 2872,
      'title': 'Falling Angels',
      'authors': 'Tracy Chevalier',
      'average_rating': 3.58,
      'isbn': '0452283205',
      'isbn13': 9780452283206,
      'language_code': 'eng',
      '  num_pages': 336,
      'ratings_count': 20321,
      'text_reviews_count': 1214,
      'publication_date': '9/24/2002',
      'publisher': 'Penguin Books'},
     {'bookID': 2873,
      'title': 'The Virgin Blue',
      'authors': 'Tracy Chevalier',
      'average_rating': 3.66,
      'isbn': '0452284449',
      'isbn13': 9780452284449,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 26029,
      'text_reviews_count': 1588,
      'publication_date': '6/24/2003',
      'publisher': 'Penguin Books'},
     {'bookID': 2875,
      'title': 'Wenn Engel fallen',
      'authors': 'Tracy Chevalier',
      'average_rating': 3.58,
      'isbn': '3471772537',
      'isbn13': 9783471772539,
      'language_code': 'ger',
      '  num_pages': 384,
      'ratings_count': 6,
      'text_reviews_count': 1,
      'publication_date': '2/1/2002',
      'publisher': 'List'},
     {'bookID': 2877,
      'title': 'Tom Hunter: Living in Hell and Other Stories',
      'authors': 'Tom Hunter/Tracy Chevalier/Colin Wiggins',
      'average_rating': 3.64,
      'isbn': '1857093313',
      'isbn13': 9781857093315,
      'language_code': 'en-GB',
      '  num_pages': 80,
      'ratings_count': 42,
      'text_reviews_count': 0,
      'publication_date': '3/8/2006',
      'publisher': 'National Gallery London'},
     {'bookID': 2879,
      'title': 'Bleach  Volume 15',
      'authors': 'Tite Kubo',
      'average_rating': 4.42,
      'isbn': '1421506130',
      'isbn13': 9781421506135,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 19945,
      'text_reviews_count': 76,
      'publication_date': '10/3/2006',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 2880,
      'title': 'Bleach  Volume 01',
      'authors': 'Tite Kubo',
      'average_rating': 4.22,
      'isbn': '1591164419',
      'isbn13': 9781591164418,
      'language_code': 'eng',
      '  num_pages': 200,
      'ratings_count': 140403,
      'text_reviews_count': 1063,
      'publication_date': '5/19/2004',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 2881,
      'title': 'Bleach  Volume 14',
      'authors': 'Tite Kubo',
      'average_rating': 4.38,
      'isbn': '1421506122',
      'isbn13': 9781421506128,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 10356,
      'text_reviews_count': 79,
      'publication_date': '8/1/2006',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 2882,
      'title': 'Bleach  Volume 11',
      'authors': 'Tite Kubo',
      'average_rating': 4.36,
      'isbn': '1421502712',
      'isbn13': 9781421502717,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 8773,
      'text_reviews_count': 84,
      'publication_date': '2/7/2006',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 2883,
      'title': 'Bleach  Volume 12',
      'authors': 'Tite Kubo',
      'average_rating': 4.36,
      'isbn': '1421504030',
      'isbn13': 9781421504032,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 8948,
      'text_reviews_count': 86,
      'publication_date': '4/4/2006',
      'publisher': 'VIZ Media LLC'},
     {'bookID': 2885,
      'title': 'DEATH NOTE ??????????????? 1',
      'authors': 'Tsugumi Ohba/Takeshi Obata/?????? ?????????/?????? ???',
      'average_rating': 4.43,
      'isbn': '4088736214',
      'isbn13': 9784088736211,
      'language_code': 'jpn',
      '  num_pages': 195,
      'ratings_count': 227,
      'text_reviews_count': 38,
      'publication_date': '4/2/2004',
      'publisher': '?????????'},
     {'bookID': 2886,
      'title': 'Death Note  Vol. 4: ?????? (Death Note  #4)',
      'authors': 'Tsugumi Ohba/Takeshi Obata',
      'average_rating': 4.39,
      'isbn': '4088736710',
      'isbn13': 9784088736716,
      'language_code': 'jpn',
      '  num_pages': 204,
      'ratings_count': 452,
      'text_reviews_count': 13,
      'publication_date': '11/11/2004',
      'publisher': 'Shueisha'},
     {'bookID': 2887,
      'title': 'Death Note  Vol. 3: ?????? (Death Note  #3)',
      'authors': 'Tsugumi Ohba/Takeshi Obata',
      'average_rating': 4.43,
      'isbn': '4088736524',
      'isbn13': 9784088736525,
      'language_code': 'jpn',
      '  num_pages': 194,
      'ratings_count': 400,
      'text_reviews_count': 11,
      'publication_date': '9/3/2004',
      'publisher': 'Shueisha'},
     {'bookID': 2893,
      'title': 'Love Artist (Harlequin Romance #2860)',
      'authors': 'Valerie Parv',
      'average_rating': 3.25,
      'isbn': '0373028601',
      'isbn13': 9780373028603,
      'language_code': 'eng',
      '  num_pages': 187,
      'ratings_count': 3,
      'text_reviews_count': 1,
      'publication_date': '7/24/1987',
      'publisher': 'Harlequin Romance'},
     {'bookID': 2895,
      'title': 'Perfume: The Story of a Murderer',
      'authors': 'Patrick S??skind/John E. Woods',
      'average_rating': 4.02,
      'isbn': '0307277763',
      'isbn13': 9780307277763,
      'language_code': 'eng',
      '  num_pages': 255,
      'ratings_count': 1124,
      'text_reviews_count': 191,
      'publication_date': '2/13/2001',
      'publisher': 'Vintage International'},
     {'bookID': 2896,
      'title': 'Das Parfum. Die Geschichte eines M??rders',
      'authors': 'Patrick S??skind',
      'average_rating': 4.02,
      'isbn': '3257228007',
      'isbn13': 9783257228007,
      'language_code': 'ger',
      '  num_pages': 321,
      'ratings_count': 9674,
      'text_reviews_count': 343,
      'publication_date': '6/1/1994',
      'publisher': 'Diogenes'},
     {'bookID': 2898,
      'title': 'Three Stories and a Reflection',
      'authors': 'Patrick S??skind',
      'average_rating': 3.57,
      'isbn': '0747534934',
      'isbn13': 9780747534938,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 24,
      'text_reviews_count': 3,
      'publication_date': '11/13/1997',
      'publisher': 'Bloomsbury Publishing PLC'},
     {'bookID': 2899,
      'title': 'The Pigeon',
      'authors': 'Patrick S??skind',
      'average_rating': 3.68,
      'isbn': '0140105832',
      'isbn13': 9780140105834,
      'language_code': 'eng',
      '  num_pages': 77,
      'ratings_count': 6254,
      'text_reviews_count': 423,
      'publication_date': '6/29/1989',
      'publisher': 'Penguin'},
     {'bookID': 2900,
      'title': 'The Story of Mr Sommer',
      'authors': 'Patrick S??skind/Jean-Jacques Semp??',
      'average_rating': 3.84,
      'isbn': '0747566755',
      'isbn13': 9780747566755,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 2061,
      'text_reviews_count': 104,
      'publication_date': '11/3/2003',
      'publisher': 'Not Avail'},
     {'bookID': 2906,
      'title': 'Bleach?????????????????? 1 [Bur??chi 1] (Bleach  #1)',
      'authors': 'Tite Kubo',
      'average_rating': 4.22,
      'isbn': '4088732138',
      'isbn13': 9784088732138,
      'language_code': 'jpn',
      '  num_pages': 189,
      'ratings_count': 41,
      'text_reviews_count': 3,
      'publication_date': '1/5/2002',
      'publisher': 'Shueisha'},
     {'bookID': 2907,
      'title': 'Bleach  Tome 1: The Death and the Strawberry',
      'authors': 'Tite Kubo',
      'average_rating': 4.22,
      'isbn': '2723442276',
      'isbn13': 9782723442275,
      'language_code': 'fre',
      '  num_pages': 192,
      'ratings_count': 54,
      'text_reviews_count': 4,
      'publication_date': '7/2/2003',
      'publisher': 'Gl??nat'},
     {'bookID': 2912,
      'title': 'Escape from Fire Mountain (World of Adventure  #3)',
      'authors': 'Gary Paulsen/Steve Chorney',
      'average_rating': 3.67,
      'isbn': '0440410258',
      'isbn13': 9780440410256,
      'language_code': 'eng',
      '  num_pages': 80,
      'ratings_count': 114,
      'text_reviews_count': 17,
      'publication_date': '1/1/1995',
      'publisher': 'Yearling'},
     {'bookID': 2917,
      'title': 'How Angel Peterson Got His Name',
      'authors': 'Gary Paulsen',
      'average_rating': 3.93,
      'isbn': '0440229359',
      'isbn13': 9780440229353,
      'language_code': 'eng',
      '  num_pages': 111,
      'ratings_count': 1177,
      'text_reviews_count': 218,
      'publication_date': '8/10/2004',
      'publisher': 'Yearling'},
     {'bookID': 2920,
      'title': "Tucket's Travels: Francis Tucket's Adventures In The West  1847-1849 (The Tucket Adventures  #1-5)",
      'authors': 'Gary Paulsen',
      'average_rating': 4.44,
      'isbn': '0440419670',
      'isbn13': 9780440419679,
      'language_code': 'en-US',
      '  num_pages': 560,
      'ratings_count': 557,
      'text_reviews_count': 46,
      'publication_date': '9/9/2003',
      'publisher': 'Yearling'},
     {'bookID': 2921,
      'title': 'Chicago Blues: The City and the Music',
      'authors': 'Mike  Rowe/Ronald Radano',
      'average_rating': 3.92,
      'isbn': '0306801450',
      'isbn13': 9780306801457,
      'language_code': 'eng',
      '  num_pages': 226,
      'ratings_count': 25,
      'text_reviews_count': 2,
      'publication_date': '8/22/1981',
      'publisher': 'Da Capo Press'},
     {'bookID': 2923,
      'title': 'Winterdance: The Fine Madness of Running the Iditarod',
      'authors': 'Gary Paulsen',
      'average_rating': 4.26,
      'isbn': '0156001454',
      'isbn13': 9780156001458,
      'language_code': 'eng',
      '  num_pages': 272,
      'ratings_count': 5437,
      'text_reviews_count': 830,
      'publication_date': '2/17/1995',
      'publisher': 'Mariner Books'},
     {'bookID': 2928,
      'title': "Brian's Winter",
      'authors': 'Gary Paulsen',
      'average_rating': 4.01,
      'isbn': '0385321988',
      'isbn13': 9780385321983,
      'language_code': 'en-US',
      '  num_pages': 133,
      'ratings_count': 76,
      'text_reviews_count': 12,
      'publication_date': '1/1/1996',
      'publisher': 'Delacorte Books for Young Readers'},
     {'bookID': 2932,
      'title': 'Robinson Crusoe (Robinson Crusoe #1)',
      'authors': 'Daniel Defoe/Virginia Woolf',
      'average_rating': 3.67,
      'isbn': '0375757325',
      'isbn13': 9780375757327,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 209122,
      'text_reviews_count': 4131,
      'publication_date': '6/12/2001',
      'publisher': 'Modern Library'},
     {'bookID': 2933,
      'title': 'Robinson Crusoe',
      'authors': 'Daniel Defoe/John J. Richetti',
      'average_rating': 3.67,
      'isbn': '0141439823',
      'isbn13': 9780141439822,
      'language_code': 'eng',
      '  num_pages': 286,
      'ratings_count': 1507,
      'text_reviews_count': 142,
      'publication_date': '3/27/2003',
      'publisher': 'Penguin Classics'},
     {'bookID': 2934,
      'title': 'Robinson Crusoe',
      'authors': 'Daniel Defoe/Michael Shinagel',
      'average_rating': 3.67,
      'isbn': '0393964523',
      'isbn13': 9780393964523,
      'language_code': 'en-US',
      '  num_pages': 436,
      'ratings_count': 585,
      'text_reviews_count': 63,
      'publication_date': '12/19/1994',
      'publisher': 'W.W. Norton & Company'},
     {'bookID': 2937,
      'title': 'Robinson Crusoe',
      'authors': 'Daniel Defoe/Avi',
      'average_rating': 3.67,
      'isbn': '0689844085',
      'isbn13': 9780689844089,
      'language_code': 'eng',
      '  num_pages': 482,
      'ratings_count': 204,
      'text_reviews_count': 32,
      'publication_date': '7/1/2001',
      'publisher': 'Aladdin'},
     {'bookID': 2940,
      'title': 'Robinson Crusoe',
      'authors': 'Daniel Defoe',
      'average_rating': 3.67,
      'isbn': '1587263882',
      'isbn13': 9781587263880,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 311,
      'text_reviews_count': 18,
      'publication_date': '7/14/2006',
      'publisher': 'Ann Arbor Media'},
     {'bookID': 2942,
      'title': 'A General History of the Pyrates',
      'authors': 'Daniel Defoe/Manuel Schonhorn/Charles   Johnson',
      'average_rating': 3.72,
      'isbn': '0486404889',
      'isbn13': 9780486404882,
      'language_code': 'eng',
      '  num_pages': 733,
      'ratings_count': 577,
      'text_reviews_count': 36,
      'publication_date': '1/26/1999',
      'publisher': 'Dover Publications'},
     {'bookID': 2949,
      'title': 'Huck Finn & Tom Sawyer among the Indians & Other Unfinished Stories (Mark Twain Library)',
      'authors': 'Mark Twain/Paul Baender/Dahlia Armon/Walter Blair',
      'average_rating': 3.85,
      'isbn': '0520238958',
      'isbn13': 9780520238954,
      'language_code': 'eng',
      '  num_pages': 389,
      'ratings_count': 5,
      'text_reviews_count': 0,
      'publication_date': '3/15/2003',
      'publisher': 'University of California Press'},
     {'bookID': 2952,
      'title': 'Huck Finn and Tom Sawyer Among the Indians',
      'authors': 'Mark Twain/Lee Nelson',
      'average_rating': 3.57,
      'isbn': '1555176801',
      'isbn13': 9781555176808,
      'language_code': 'eng',
      '  num_pages': 277,
      'ratings_count': 242,
      'text_reviews_count': 29,
      'publication_date': '4/22/2003',
      'publisher': 'Council Press'},
     {'bookID': 2953,
      'title': "Huck Finn/Pudd'nhead Wilson/No 44 Mysterious Stranger other Writings",
      'authors': 'Mark Twain/Guy Cardwell/Louis J. Budd',
      'average_rating': 4.06,
      'isbn': '1883011884',
      'isbn13': 9781883011888,
      'language_code': 'en-US',
      '  num_pages': 808,
      'ratings_count': 33,
      'text_reviews_count': 3,
      'publication_date': '8/1/2000',
      'publisher': 'Library of America'},
     {'bookID': 2956,
      'title': 'The Adventures of Huckleberry Finn (Adventures of Tom and Huck  #2)',
      'authors': 'Mark Twain/Guy Cardwell/John Seelye/Walter Trier',
      'average_rating': 3.82,
      'isbn': '0142437174',
      'isbn13': 9780142437179,
      'language_code': 'eng',
      '  num_pages': 327,
      'ratings_count': 1049912,
      'text_reviews_count': 11391,
      'publication_date': '12/31/2002',
      'publisher': 'Penguin Classics'},
     {'bookID': 2958,
      'title': 'Adventures of Huckleberry Finn',
      'authors': 'Mark Twain/E.W. Kemble',
      'average_rating': 3.82,
      'isbn': '0486443221',
      'isbn13': 9780486443225,
      'language_code': 'eng',
      '  num_pages': 368,
      'ratings_count': 144,
      'text_reviews_count': 17,
      'publication_date': '5/6/2005',
      'publisher': 'Dover Publications'},
     {'bookID': 2960,
      'title': 'Adventures of Huckleberry Finn',
      'authors': 'Mark Twain/George Saunders',
      'average_rating': 3.82,
      'isbn': '0375757376',
      'isbn13': 9780375757372,
      'language_code': 'eng',
      '  num_pages': 244,
      'ratings_count': 687,
      'text_reviews_count': 37,
      'publication_date': '8/14/2001',
      'publisher': 'The Modern Library'},
     {'bookID': 2962,
      'title': 'The Annotated Huckleberry Finn',
      'authors': 'Mark Twain/Michael Patrick Hearn/E.W. Kemble',
      'average_rating': 3.82,
      'isbn': '0393020398',
      'isbn13': 9780393020397,
      'language_code': 'eng',
      '  num_pages': 656,
      'ratings_count': 185,
      'text_reviews_count': 18,
      'publication_date': '10/17/2001',
      'publisher': 'W. W. Norton  Company'},
     {'bookID': 2965,
      'title': 'The Wit and Wisdom of Mark Twain',
      'authors': 'Mark Twain',
      'average_rating': 4.2,
      'isbn': '0486406644',
      'isbn13': 9780486406640,
      'language_code': 'eng',
      '  num_pages': 64,
      'ratings_count': 970,
      'text_reviews_count': 53,
      'publication_date': '12/23/1998',
      'publisher': 'Dover Publications'},
     {'bookID': 2967,
      'title': "Mark Twain's Helpful Hints for Good Living: A Handbook for the Damned Human Race",
      'authors': 'Mark Twain/Lin Salamo/Victor Fischer/Michael B. Frank',
      'average_rating': 3.86,
      'isbn': '0520242459',
      'isbn13': 9780520242456,
      'language_code': 'eng',
      '  num_pages': 221,
      'ratings_count': 513,
      'text_reviews_count': 71,
      'publication_date': '10/18/2004',
      'publisher': 'University of California Press'},
     {'bookID': 2968,
      'title': 'The Complete Short Stories of Mark Twain',
      'authors': 'Mark Twain/Charles Neider',
      'average_rating': 4.28,
      'isbn': '0553211951',
      'isbn13': 9780553211955,
      'language_code': 'eng',
      '  num_pages': 848,
      'ratings_count': 5710,
      'text_reviews_count': 142,
      'publication_date': '3/1/1984',
      'publisher': 'Bantam Classics'},
     {'bookID': 2971,
      'title': 'The Autobiography of Mark Twain',
      'authors': 'Mark Twain/Charles Neider',
      'average_rating': 4.05,
      'isbn': '0060955422',
      'isbn13': 9780060955427,
      'language_code': 'eng',
      '  num_pages': 508,
      'ratings_count': 2871,
      'text_reviews_count': 209,
      'publication_date': '11/28/2000',
      'publisher': 'Harper Perennial'},
     {'bookID': 2973,
      'title': 'Collected Tales  Sketches  Speeches  & Essays 1891???1910',
      'authors': 'Mark Twain/Louis J. Budd',
      'average_rating': 4.39,
      'isbn': '0940450739',
      'isbn13': 9780940450738,
      'language_code': 'eng',
      '  num_pages': 1050,
      'ratings_count': 207,
      'text_reviews_count': 10,
      'publication_date': '10/15/1992',
      'publisher': 'Library of America'},
     {'bookID': 2978,
      'title': 'Lost Horizon',
      'authors': 'James Hilton',
      'average_rating': 3.92,
      'isbn': '0060594527',
      'isbn13': 9780060594527,
      'language_code': 'eng',
      '  num_pages': 241,
      'ratings_count': 11892,
      'text_reviews_count': 955,
      'publication_date': '6/15/2004',
      'publisher': 'Harper Perennial'},
     {'bookID': 2988,
      'title': "Louisa May Alcott's Christmas Treasury",
      'authors': 'Louisa May Alcott/C. Michael Dudash/Stephen W. Hines',
      'average_rating': 3.96,
      'isbn': '1589199502',
      'isbn13': 9781589199507,
      'language_code': 'eng',
      '  num_pages': 282,
      'ratings_count': 715,
      'text_reviews_count': 44,
      'publication_date': '6/1/2002',
      'publisher': 'David C Cook'},
     {'bookID': 2997,
      'title': "My Secret Garden: Women's Sexual Fantasies",
      'authors': 'Nancy Friday',
      'average_rating': 3.68,
      'isbn': '0671019872',
      'isbn13': 9780671019877,
      'language_code': 'eng',
      '  num_pages': 361,
      'ratings_count': 1817,
      'text_reviews_count': 123,
      'publication_date': '10/28/2003',
      'publisher': 'Pocket Books'},
     {'bookID': 2998,
      'title': 'The Secret Garden',
      'authors': 'Frances Hodgson Burnett',
      'average_rating': 4.13,
      'isbn': '0517189607',
      'isbn13': 9780517189603,
      'language_code': 'eng',
      '  num_pages': 331,
      'ratings_count': 764134,
      'text_reviews_count': 11796,
      'publication_date': '9/1/1998',
      'publisher': "Children's Classics"},
     {'bookID': 3003,
      'title': 'The Secret Garden',
      'authors': 'Frances Hodgson Burnett/Sandra M. Gilbert',
      'average_rating': 4.13,
      'isbn': '0451528832',
      'isbn13': 9780451528834,
      'language_code': 'eng',
      '  num_pages': 281,
      'ratings_count': 1739,
      'text_reviews_count': 116,
      'publication_date': '7/1/2003',
      'publisher': 'Signet'},
     {'bookID': 3004,
      'title': 'The Secret Garden',
      'authors': 'Martha Hailey DuBose/Frances Hodgson Burnett/Lucy Corvino/Arthur Pober',
      'average_rating': 4.33,
      'isbn': '1402713193',
      'isbn13': 9781402713194,
      'language_code': 'eng',
      '  num_pages': 160,
      'ratings_count': 1653,
      'text_reviews_count': 76,
      'publication_date': '3/1/2005',
      'publisher': 'Sterling'},
     {'bookID': 3006,
      'title': 'The Secret Garden',
      'authors': 'Frances Hodgson Burnett/Alison Lurie',
      'average_rating': 4.13,
      'isbn': '0142437050',
      'isbn13': 9780142437056,
      'language_code': 'en-GB',
      '  num_pages': 288,
      'ratings_count': 517,
      'text_reviews_count': 13,
      'publication_date': '1/30/2003',
      'publisher': 'Penguin Classics'},
     {'bookID': 3008,
      'title': 'A Little Princess',
      'authors': 'Frances Hodgson Burnett/Nancy Bond',
      'average_rating': 4.2,
      'isbn': '0142437018',
      'isbn13': 9780142437018,
      'language_code': 'eng',
      '  num_pages': 242,
      'ratings_count': 238192,
      'text_reviews_count': 4392,
      'publication_date': '2/26/2002',
      'publisher': 'Penguin Books'},
     {'bookID': 3011,
      'title': 'Waiting for the Party: The Life of Frances Hodgson Burnett  1849-1924',
      'authors': 'Ann Thwaite',
      'average_rating': 3.8,
      'isbn': '0879237902',
      'isbn13': 9780879237905,
      'language_code': 'eng',
      '  num_pages': 274,
      'ratings_count': 23,
      'text_reviews_count': 7,
      'publication_date': '9/1/1994',
      'publisher': 'David R. Godine Publisher'},
     {'bookID': 3014,
      'title': "The Secret Garden Cookbook: Recipes Inspired by Frances Hodgson Burnett's The Secret Garden",
      'authors': 'Amy Cotler/Frances Hodgson Burnett/Prudence See',
      'average_rating': 4.3,
      'isbn': '0060277408',
      'isbn13': 9780060277406,
      'language_code': 'eng',
      '  num_pages': 128,
      'ratings_count': 150,
      'text_reviews_count': 23,
      'publication_date': '3/19/1999',
      'publisher': 'Festival'},
     {'bookID': 3023,
      'title': "Basic Economics: A Citizen's Guide to the Economy",
      'authors': 'Thomas Sowell',
      'average_rating': 4.32,
      'isbn': '0465081452',
      'isbn13': 9780465081455,
      'language_code': 'eng',
      '  num_pages': 448,
      'ratings_count': 5899,
      'text_reviews_count': 475,
      'publication_date': '12/24/2003',
      'publisher': 'Basic Books'},
     {'bookID': 3025,
      'title': 'Basic Economics: A Common Sense Guide to the Economy',
      'authors': 'Thomas Sowell',
      'average_rating': 4.32,
      'isbn': '0465002609',
      'isbn13': 9780465002603,
      'language_code': 'eng',
      '  num_pages': 627,
      'ratings_count': 328,
      'text_reviews_count': 43,
      'publication_date': '4/3/2007',
      'publisher': 'Basic Books (AZ)'},
     {'bookID': 3040,
      'title': 'Black Rednecks and White Liberals',
      'authors': 'Thomas Sowell',
      'average_rating': 4.38,
      'isbn': '1594030863',
      'isbn13': 9781594030864,
      'language_code': 'eng',
      '  num_pages': 372,
      'ratings_count': 2579,
      'text_reviews_count': 301,
      'publication_date': '6/1/2005',
      'publisher': 'Encounter Books'},
     {'bookID': 3041,
      'title': 'Applied Economics: Thinking Beyond Stage One',
      'authors': 'Thomas Sowell',
      'average_rating': 4.14,
      'isbn': '0465081436',
      'isbn13': 9780465081431,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 1546,
      'text_reviews_count': 122,
      'publication_date': '11/13/2003',
      'publisher': 'Basic Books'},
     {'bookID': 3042,
      'title': 'Knowledge And Decisions',
      'authors': 'Thomas Sowell',
      'average_rating': 4.39,
      'isbn': '0465037380',
      'isbn13': 9780465037384,
      'language_code': 'eng',
      '  num_pages': 422,
      'ratings_count': 766,
      'text_reviews_count': 47,
      'publication_date': '10/4/1996',
      'publisher': 'Basic Books'},
     {'bookID': 3047,
      'title': 'A Conflict of Visions: Ideological Origins of Political Struggles',
      'authors': 'Thomas Sowell',
      'average_rating': 4.31,
      'isbn': '0465081428',
      'isbn13': 9780465081424,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 1797,
      'text_reviews_count': 166,
      'publication_date': '1/3/2002',
      'publisher': 'Basic Books'},
     {'bookID': 3051,
      'title': 'Sir Gawain and the Green Knight',
      'authors': 'Selina Shirley Hastings/Juan Wijngaard',
      'average_rating': 3.91,
      'isbn': '0744520053',
      'isbn13': 9780744520057,
      'language_code': 'eng',
      '  num_pages': 29,
      'ratings_count': 65,
      'text_reviews_count': 9,
      'publication_date': '6/27/1991',
      'publisher': 'Walker Books Ltd'},
     {'bookID': 3053,
      'title': 'Alcoholics Anonymous',
      'authors': 'Alcoholics Anonymous',
      'average_rating': 4.45,
      'isbn': '0916856593',
      'isbn13': 9780916856595,
      'language_code': 'eng',
      '  num_pages': 250,
      'ratings_count': 22,
      'text_reviews_count': 0,
      'publication_date': '8/1/1993',
      'publisher': 'Alcoholics Anonymous World Services Inc'},
     {'bookID': 3055,
      'title': 'Alcoholics Anonymous',
      'authors': 'Alcoholics Anonymous',
      'average_rating': 4.45,
      'isbn': '1893007162',
      'isbn13': 9781893007161,
      'language_code': 'en-US',
      '  num_pages': 576,
      'ratings_count': 495,
      'text_reviews_count': 30,
      'publication_date': '2/10/2002',
      'publisher': 'AA World Services'},
     {'bookID': 3056,
      'title': 'The Twelve Steps & Twelve Traditions of Overeaters Anonymous',
      'authors': 'Overeaters Anonymous',
      'average_rating': 4.36,
      'isbn': '0960989862',
      'isbn13': 9780960989867,
      'language_code': 'en-US',
      '  num_pages': 221,
      'ratings_count': 213,
      'text_reviews_count': 10,
      'publication_date': '1/1/1993',
      'publisher': 'Overeaters Anonymous  Incorporated'},
     {'bookID': 3061,
      'title': 'The Natural Way to Draw',
      'authors': 'Kimon Nicolaides/Mamie Harmon',
      'average_rating': 3.9,
      'isbn': '0395530075',
      'isbn13': 9780395530078,
      'language_code': 'en-US',
      '  num_pages': 240,
      'ratings_count': 39369,
      'text_reviews_count': 80,
      'publication_date': '2/1/1990',
      'publisher': 'Mariner Books'},
     {'bookID': 3065,
      'title': 'Natural Health  Natural Medicine',
      'authors': 'Andrew Weil',
      'average_rating': 4.11,
      'isbn': '0618479031',
      'isbn13': 9780618479030,
      'language_code': 'en-US',
      '  num_pages': 448,
      'ratings_count': 580,
      'text_reviews_count': 41,
      'publication_date': '12/9/2004',
      'publisher': 'Mariner Books'},
     {'bookID': 3066,
      'title': 'The Fixer',
      'authors': 'Bernard Malamud/Jonathan Safran Foer',
      'average_rating': 3.96,
      'isbn': '0374529388',
      'isbn13': 9780374529383,
      'language_code': 'eng',
      '  num_pages': 335,
      'ratings_count': 8624,
      'text_reviews_count': 409,
      'publication_date': '5/5/2004',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 3067,
      'title': 'The Complete Stories',
      'authors': 'Bernard Malamud/Robert Giroux',
      'average_rating': 4.22,
      'isbn': '0374525757',
      'isbn13': 9780374525750,
      'language_code': 'en-US',
      '  num_pages': 656,
      'ratings_count': 712,
      'text_reviews_count': 51,
      'publication_date': '10/12/1998',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 3068,
      'title': 'The Assistant',
      'authors': 'Bernard Malamud/Jonathan Rosen',
      'average_rating': 3.89,
      'isbn': '0374504849',
      'isbn13': 9780374504847,
      'language_code': 'en-US',
      '  num_pages': 246,
      'ratings_count': 8073,
      'text_reviews_count': 319,
      'publication_date': '7/7/2003',
      'publisher': 'Farrar Straus and Giroux'},
     {'bookID': 3070,
      'title': 'Conversations with Bernard Malamud (Literary Conversations)',
      'authors': 'Lawrence M. Lasher',
      'average_rating': 4.0,
      'isbn': '0878054901',
      'isbn13': 9780878054909,
      'language_code': 'eng',
      '  num_pages': 184,
      'ratings_count': 4,
      'text_reviews_count': 0,
      'publication_date': '3/1/1991',
      'publisher': 'University Press of Mississippi'},
     {'bookID': 3072,
      'title': 'The Tenants',
      'authors': 'Bernard Malamud/Aleksandar Hemon',
      'average_rating': 3.65,
      'isbn': '0374521026',
      'isbn13': 9780374521028,
      'language_code': 'eng',
      '  num_pages': 248,
      'ratings_count': 662,
      'text_reviews_count': 50,
      'publication_date': '9/18/2003',
      'publisher': 'Farrar  Straus and Giroux'},
     {'bookID': 3075,
      'title': 'Enchanted April: Acting Edition',
      'authors': 'Matthew Barber/Elizabeth von Arnim',
      'average_rating': 3.61,
      'isbn': '0822219751',
      'isbn13': 9780822219750,
      'language_code': 'eng',
      '  num_pages': 73,
      'ratings_count': 67,
      'text_reviews_count': 6,
      'publication_date': '4/7/2004',
      'publisher': 'Dramatists Play Service'},
     {'bookID': 3084,
      'title': 'April  May und June',
      'authors': 'Elizabeth von Arnim',
      'average_rating': 3.88,
      'isbn': '345833422X',
      'isbn13': 9783458334224,
      'language_code': 'ger',
      '  num_pages': 88,
      'ratings_count': 0,
      'text_reviews_count': 0,
      'publication_date': '4/1/1995',
      'publisher': 'Insel  Frankfurt'},
     {'bookID': 3087,
      'title': 'A Room with a View',
      'authors': 'E.M. Forster',
      'average_rating': 3.91,
      'isbn': '1420925431',
      'isbn13': 9781420925432,
      'language_code': 'eng',
      '  num_pages': 119,
      'ratings_count': 128596,
      'text_reviews_count': 3422,
      'publication_date': '1/1/2005',
      'publisher': 'Digireads.com'},
     {'bookID': 3088,
      'title': 'A Room with a View / Howards End',
      'authors': 'E.M. Forster/Benjamin DeMott',
      'average_rating': 4.1,
      'isbn': '0451521412',
      'isbn13': 9780451521415,
      'language_code': 'eng',
      '  num_pages': 449,
      'ratings_count': 2450,
      'text_reviews_count': 113,
      'publication_date': '2/4/1986',
      'publisher': 'Signet'},
     {'bookID': 3100,
      'title': 'E.M. Forster: Critical Guidebook',
      'authors': 'Lionel Trilling/E.M. Forster',
      'average_rating': 3.51,
      'isbn': '0811202100',
      'isbn13': 9780811202107,
      'language_code': 'eng',
      '  num_pages': 208,
      'ratings_count': 6,
      'text_reviews_count': 0,
      'publication_date': '1/17/1971',
      'publisher': 'New Directions'},
     {'bookID': 3101,
      'title': 'The Longest Journey',
      'authors': 'E.M. Forster/Gilbert Adair/Elizabeth Heine',
      'average_rating': 3.48,
      'isbn': '0141441488',
      'isbn13': 9780141441481,
      'language_code': 'eng',
      '  num_pages': 396,
      'ratings_count': 1665,
      'text_reviews_count': 125,
      'publication_date': '7/27/2006',
      'publisher': 'Penguin Classics'},
     {'bookID': 3102,
      'title': 'Howards End',
      'authors': 'E.M. Forster',
      'average_rating': 3.96,
      'isbn': '0486424545',
      'isbn13': 9780486424545,
      'language_code': 'eng',
      '  num_pages': 246,
      'ratings_count': 54765,
      'text_reviews_count': 1437,
      'publication_date': '10/29/2002',
      'publisher': 'Dover Publications'},
     {'bookID': 3103,
      'title': 'Maurice',
      'authors': 'E.M. Forster',
      'average_rating': 4.03,
      'isbn': '0393310329',
      'isbn13': 9780393310320,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 21997,
      'text_reviews_count': 1005,
      'publication_date': '12/17/2005',
      'publisher': 'W. W. Norton  Company'},
     {'bookID': 3104,
      'title': 'E. M. Forster: A Life',
      'authors': 'P.N. Furbank',
      'average_rating': 4.14,
      'isbn': '0156286513',
      'isbn13': 9780156286510,
      'language_code': 'eng',
      '  num_pages': 648,
      'ratings_count': 141,
      'text_reviews_count': 11,
      'publication_date': '5/2/1994',
      'publisher': 'Mariner Books'},
     {'bookID': 3105,
      'title': 'Howards End',
      'authors': 'E.M. Forster',
      'average_rating': 3.96,
      'isbn': '0141183357',
      'isbn13': 9780141183350,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 368,
      'text_reviews_count': 26,
      'publication_date': '9/28/2000',
      'publisher': 'Penguin Books'},
     {'bookID': 3107,
      'title': 'The Sixteen Pleasures',
      'authors': 'Robert Hellenga',
      'average_rating': 3.59,
      'isbn': '0385314698',
      'isbn13': 9780385314695,
      'language_code': 'eng',
      '  num_pages': 384,
      'ratings_count': 2699,
      'text_reviews_count': 336,
      'publication_date': '5/1/1995',
      'publisher': 'Delta'},
     {'bookID': 3113,
      'title': 'Revolutionary Characters: What Made the Founders Different',
      'authors': 'Gordon S. Wood',
      'average_rating': 3.97,
      'isbn': '1594200939',
      'isbn13': 9781594200939,
      'language_code': 'eng',
      '  num_pages': 336,
      'ratings_count': 3259,
      'text_reviews_count': 187,
      'publication_date': '5/18/2006',
      'publisher': 'Penguin Press HC  The'},
     {'bookID': 3117,
      'title': 'The Rescue (Kidnapped  #3)',
      'authors': 'Gordon Korman',
      'average_rating': 4.11,
      'isbn': '0439847796',
      'isbn13': 9780439847797,
      'language_code': 'eng',
      '  num_pages': 140,
      'ratings_count': 1864,
      'text_reviews_count': 117,
      'publication_date': '9/1/2006',
      'publisher': 'Scholastic Books'},
     {'bookID': 3119,
      'title': 'Hunting the Hunter (On the Run  #6)',
      'authors': 'Gordon Korman',
      'average_rating': 4.21,
      'isbn': '0439651417',
      'isbn13': 9780439651417,
      'language_code': 'eng',
      '  num_pages': 151,
      'ratings_count': 1928,
      'text_reviews_count': 85,
      'publication_date': '2/1/2006',
      'publisher': 'Scholastic'},
     {'bookID': 3120,
      'title': 'Public Enemies (On The Run  #5)',
      'authors': 'Gordon Korman',
      'average_rating': 4.19,
      'isbn': '0439651409',
      'isbn13': 9780439651400,
      'language_code': 'eng',
      '  num_pages': 150,
      'ratings_count': 2050,
      'text_reviews_count': 76,
      'publication_date': '12/1/2005',
      'publisher': 'Scholastic'},
     {'bookID': 3130,
      'title': 'Runaway Bride',
      'authors': 'Deborah  Gordon',
      'average_rating': 4.25,
      'isbn': '0380777584',
      'isbn13': 9780380777587,
      'language_code': 'eng',
      '  num_pages': 390,
      'ratings_count': 8,
      'text_reviews_count': 0,
      'publication_date': '9/28/1994',
      'publisher': 'Avon'},
     {'bookID': 3142,
      'title': 'The Bridge over the Drina',
      'authors': 'Ivo Andri??/William H. McNeill',
      'average_rating': 4.33,
      'isbn': '1860460585',
      'isbn13': 9781860460586,
      'language_code': 'eng',
      '  num_pages': 314,
      'ratings_count': 254,
      'text_reviews_count': 35,
      'publication_date': '4/5/1995',
      'publisher': 'The Harvill Press'},
     {'bookID': 3144,
      'title': 'Drina Dances in Paris',
      'authors': 'Jean Estoril',
      'average_rating': 4.16,
      'isbn': '0750000333',
      'isbn13': 9780750000338,
      'language_code': 'eng',
      '  num_pages': 194,
      'ratings_count': 14,
      'text_reviews_count': 4,
      'publication_date': '4/1/1991',
      'publisher': 'Simon and Schuster'},
     {'bookID': 3145,
      'title': 'Drina Ballerina',
      'authors': 'Jean Estoril',
      'average_rating': 4.16,
      'isbn': '0750005947',
      'isbn13': 9780750005944,
      'language_code': 'eng',
      '  num_pages': 188,
      'ratings_count': 8,
      'text_reviews_count': 1,
      'publication_date': '1/17/1991',
      'publisher': 'Hodder'},
     {'bookID': 3147,
      'title': 'Le Pont sur la Drina',
      'authors': 'Ivo Andri??/Pascale Delpech',
      'average_rating': 4.33,
      'isbn': '225393321X',
      'isbn13': 9782253933212,
      'language_code': 'fre',
      '  num_pages': 384,
      'ratings_count': 69,
      'text_reviews_count': 10,
      'publication_date': '7/5/1999',
      'publisher': 'Livre de Poche'},
     {'bookID': 3152,
      'title': 'Drina Dances in Italy',
      'authors': 'Jean Estoril',
      'average_rating': 4.08,
      'isbn': '0750012633',
      'isbn13': 9780750012638,
      'language_code': 'eng',
      '  num_pages': 191,
      'ratings_count': 21,
      'text_reviews_count': 0,
      'publication_date': '8/31/1992',
      'publisher': 'Hodder'},
     {'bookID': 3155,
      'title': 'Drina Goes on Tour',
      'authors': 'Jean Estoril/Mabel Esther Allan',
      'average_rating': 4.26,
      'isbn': '0750002468',
      'isbn13': 9780750002462,
      'language_code': 'eng',
      '  num_pages': 188,
      'ratings_count': 112,
      'text_reviews_count': 7,
      'publication_date': '10/20/1991',
      'publisher': 'Simon and Schuster'},
     {'bookID': 3156,
      'title': 'Drina Dances in Madeira',
      'authors': 'Jean Estoril/Mabel Esther Allan',
      'average_rating': 4.09,
      'isbn': '0750002425',
      'isbn13': 9780750002424,
      'language_code': 'eng',
      '  num_pages': 164,
      'ratings_count': 139,
      'text_reviews_count': 6,
      'publication_date': '2/6/1991',
      'publisher': 'Simon and Schuster'},
     {'bookID': 3167,
      'title': 'Phaedrus/Apology/Crito/Symposium',
      'authors': 'Plato/Benjamin Jowett',
      'average_rating': 3.0,
      'isbn': '1420926845',
      'isbn13': 9781420926842,
      'language_code': 'en-US',
      '  num_pages': 144,
      'ratings_count': 19,
      'text_reviews_count': 0,
      'publication_date': '1/1/2006',
      'publisher': 'Digireads.com'},
     {'bookID': 3207,
      'title': 'The Dialogues of Plato  Volume 1: Euthyphro  Apology  Crito  Meno  Gorgias  Menexenus',
      'authors': 'Plato/Reginald E. Allen',
      'average_rating': 4.17,
      'isbn': '0300044887',
      'isbn13': 9780300044881,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 114,
      'text_reviews_count': 11,
      'publication_date': '9/10/1989',
      'publisher': 'Yale University Press'},
     {'bookID': 3231,
      'title': 'Gorgias/Timaeus',
      'authors': 'Plato/Benjamin Jowett',
      'average_rating': 3.74,
      'isbn': '0486427595',
      'isbn13': 9780486427591,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 34,
      'text_reviews_count': 5,
      'publication_date': '7/15/2003',
      'publisher': 'Dover Publications'},
     {'bookID': 3232,
      'title': 'Minor Works: On Colours/On Things Heard/Physiognomics/On Plants/On Marvellous Things Heard/Mechanical Problems/On Indivisible Lines/The...Gorgias',
      'authors': 'Aristotle/W.S. Hett',
      'average_rating': 4.57,
      'isbn': '0674993381',
      'isbn13': 9780674993389,
      'language_code': 'grc',
      '  num_pages': 528,
      'ratings_count': 14,
      'text_reviews_count': 0,
      'publication_date': '6/28/1963',
      'publisher': 'Loeb Classical Library 307'},
     {'bookID': 3248,
      'title': 'Aristophanes I: Clouds/Wasps/Birds',
      'authors': 'Aristophanes/Peter Meineck/Ian C. Storey',
      'average_rating': 3.77,
      'isbn': '0872203603',
      'isbn13': 9780872203600,
      'language_code': 'eng',
      '  num_pages': 480,
      'ratings_count': 100,
      'text_reviews_count': 9,
      'publication_date': '9/1/1998',
      'publisher': 'Hackett Publishing Company  Inc. (USA)'},
     {'bookID': 3254,
      'title': 'The Trojan Women',
      'authors': 'Euripides/Gilbert Murray',
      'average_rating': 3.89,
      'isbn': '1420927329',
      'isbn13': 9781420927320,
      'language_code': 'eng',
      '  num_pages': 80,
      'ratings_count': 4577,
      'text_reviews_count': 126,
      'publication_date': '1/1/2006',
      'publisher': 'Digireads.com'},
     {'bookID': 3258,
      'title': 'Greek Tragedies  Volume 2',
      'authors': 'David Grene/Richmond Lattimore/Aeschylus/Sophocles/Euripides',
      'average_rating': 4.29,
      'isbn': '0226307751',
      'isbn13': 9780226307756,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 327,
      'text_reviews_count': 12,
      'publication_date': '2/15/1960',
      'publisher': 'University Of Chicago Press'},
     {'bookID': 3273,
      'title': "Moloka'i (Moloka'i #1)",
      'authors': 'Alan Brennert',
      'average_rating': 4.17,
      'isbn': '0312304358',
      'isbn13': 9780312304355,
      'language_code': 'eng',
      '  num_pages': 405,
      'ratings_count': 91395,
      'text_reviews_count': 8192,
      'publication_date': '10/4/2004',
      'publisher': "St. Martin's Griffin"},
     {'bookID': 3280,
      'title': 'Teaching with the Brain in Mind',
      'authors': 'Eric Jensen',
      'average_rating': 4.11,
      'isbn': '1416600302',
      'isbn13': 9781416600305,
      'language_code': 'eng',
      '  num_pages': 186,
      'ratings_count': 592,
      'text_reviews_count': 49,
      'publication_date': '6/15/2005',
      'publisher': 'Association for Supervision & Curriculum Development'},
     {'bookID': 3283,
      'title': 'Introducing Mind and Brain (Introducing...)',
      'authors': 'Angus Gellatly/Oscar Z??rate/Richard Appignanesi',
      'average_rating': 3.54,
      'isbn': '1840466383',
      'isbn13': 9781840466386,
      'language_code': 'en-GB',
      '  num_pages': 176,
      'ratings_count': 26,
      'text_reviews_count': 1,
      'publication_date': '5/10/2001',
      'publisher': 'Totem Books'},
     {'bookID': 3290,
      'title': 'Eva Luna',
      'authors': 'Isabel Allende/Margaret Sayers Peden',
      'average_rating': 3.97,
      'isbn': '0553383825',
      'isbn13': 9780553383829,
      'language_code': 'eng',
      '  num_pages': 320,
      'ratings_count': 430,
      'text_reviews_count': 23,
      'publication_date': '8/30/2005',
      'publisher': 'Dial Press'},
     {'bookID': 3291,
      'title': 'The Stories of Eva Luna',
      'authors': 'Isabel Allende',
      'average_rating': 3.97,
      'isbn': '0743217187',
      'isbn13': 9780743217187,
      'language_code': 'eng',
      '  num_pages': 352,
      'ratings_count': 12839,
      'text_reviews_count': 375,
      'publication_date': '11/13/2001',
      'publisher': 'Scribner'},
     {'bookID': 3293,
      'title': 'Diez Cuentos de Eva Luna Con Guia de Comprension y Repaso de Gramatica',
      'authors': 'Isabel Allende/Richard D. Woods/Kenneth M. Taggart',
      'average_rating': 3.97,
      'isbn': '007001356X',
      'isbn13': 9780070013568,
      'language_code': 'eng',
      '  num_pages': 256,
      'ratings_count': 10,
      'text_reviews_count': 1,
      'publication_date': '12/1/1994',
      'publisher': 'McGraw-Hill Humanities/Social Sciences/Languages'},
     {'bookID': 3298,
      'title': 'El bosque de los pigmeos',
      'authors': 'Isabel Allende',
      'average_rating': 3.77,
      'isbn': '0060816198',
      'isbn13': 9780060816193,
      'language_code': 'spa',
      '  num_pages': 304,
      'ratings_count': 1099,
      'text_reviews_count': 46,
      'publication_date': '9/6/2005',
      'publisher': 'HarperCollins Espanol'},
     {'bookID': 3300,
      'title': 'In??s of My Soul',
      'authors': 'Isabel Allende/Margaret Sayers Peden',
      'average_rating': 3.93,
      'isbn': '0061161535',
      'isbn13': 9780061161537,
      'language_code': 'eng',
      '  num_pages': 321,
      'ratings_count': 15345,
      'text_reviews_count': 1075,
      'publication_date': '11/7/2006',
      'publisher': 'Harper'},
     {'bookID': 3301,
      'title': 'La casa de los esp??ritus',
      'authors': 'Isabel Allende',
      'average_rating': 4.23,
      'isbn': '0060951303',
      'isbn13': 9780060951306,
      'language_code': 'spa',
      '  num_pages': 454,
      'ratings_count': 608,
      'text_reviews_count': 38,
      'publication_date': '9/18/2001',
      'publisher': 'HarperCollins Espanol'},
     {'bookID': 3302,
      'title': 'El plan infinito',
      'authors': 'Isabel Allende',
      'average_rating': 3.72,
      'isbn': '0060951273',
      'isbn13': 9780060951276,
      'language_code': 'spa',
      '  num_pages': 336,
      'ratings_count': 514,
      'text_reviews_count': 33,
      'publication_date': '5/14/2002',
      'publisher': 'Harper Perennial'},
     {'bookID': 3303,
      'title': 'El reino del drag??n de oro',
      'authors': 'Isabel Allende',
      'average_rating': 3.84,
      'isbn': '0060591714',
      'isbn13': 9780060591717,
      'language_code': 'spa',
      '  num_pages': 432,
      'ratings_count': 1189,
      'text_reviews_count': 51,
      'publication_date': '9/7/2004',
      'publisher': 'HarperCollins Espanol'},
     {'bookID': 3304,
      'title': 'City of the Beasts (Eagle and Jaguar  #1)',
      'authors': 'Isabel Allende/Margaret Sayers Peden',
      'average_rating': 3.71,
      'isbn': '0060535032',
      'isbn13': 9780060535032,
      'language_code': 'eng',
      '  num_pages': 408,
      'ratings_count': 17962,
      'text_reviews_count': 778,
      'publication_date': '4/27/2004',
      'publisher': 'Rayo'},
     {'bookID': 3311,
      'title': 'Self',
      'authors': 'Yann Martel',
      'average_rating': 3.43,
      'isbn': '0571219764',
      'isbn13': 9780571219766,
      'language_code': 'eng',
      '  num_pages': 331,
      'ratings_count': 2359,
      'text_reviews_count': 146,
      'publication_date': '4/7/2003',
      'publisher': 'Faber  Faber'},
     {'bookID': 3316,
      'title': 'Die Br??cke ??ber die Drina',
      'authors': 'Ivo Andri??/Ernst E. Jonas',
      'average_rating': 4.33,
      'isbn': '3518399608',
      'isbn13': 9783518399606,
      'language_code': 'ger',
      '  num_pages': 407,
      'ratings_count': 9,
      'text_reviews_count': 0,
      'publication_date': '3/1/2003',
      'publisher': 'Suhrkamp'},
     {'bookID': 3325,
      'title': 'Drina Dances in Switzerland',
      'authors': 'Jean Estoril/Jenny Sanders',
      'average_rating': 4.02,
      'isbn': '0750002441',
      'isbn13': 9780750002448,
      'language_code': 'eng',
      '  num_pages': 188,
      'ratings_count': 13,
      'text_reviews_count': 1,
      'publication_date': '8/23/1993',
      'publisher': "Hodder Children's Books"},
     {'bookID': 3340,
      'title': 'The Story of Salt',
      'authors': 'Mark Kurlansky/S.D. Schindler',
      'average_rating': 4.08,
      'isbn': '0399239987',
      'isbn13': 9780399239984,
      'language_code': 'eng',
      '  num_pages': 48,
      'ratings_count': 382,
      'text_reviews_count': 85,
      'publication_date': '9/7/2006',
      'publisher': "G.P. Putnam's Sons Books for Young Readers"},
     {'bookID': 3341,
      'title': 'Nonviolence: Twenty-Five Lessons from the History of a Dangerous Idea',
      'authors': 'Mark Kurlansky/Dalai Lama XIV',
      'average_rating': 4.0,
      'isbn': '0679643354',
      'isbn13': 9780679643357,
      'language_code': 'eng',
      '  num_pages': 203,
      'ratings_count': 768,
      'text_reviews_count': 96,
      'publication_date': '9/12/2006',
      'publisher': 'Modern Library'},
     {'bookID': 3343,
      'title': 'Boogaloo on 2nd Avenue',
      'authors': 'Mark Kurlansky',
      'average_rating': 3.17,
      'isbn': '0345448197',
      'isbn13': 9780345448194,
      'language_code': 'eng',
      '  num_pages': 319,
      'ratings_count': 191,
      'text_reviews_count': 26,
      'publication_date': '2/28/2006',
      'publisher': 'Random House Trade'},
     {'bookID': 3344,
      'title': 'Cod: A Biography of the Fish That Changed the World',
      'authors': 'Mark Kurlansky',
      'average_rating': 3.91,
      'isbn': '0140275010',
      'isbn13': 9780140275018,
      'language_code': 'eng',
      '  num_pages': 294,
      'ratings_count': 970,
      'text_reviews_count': 104,
      'publication_date': '7/1/1998',
      'publisher': 'Penguin Books'},
     {'bookID': 3345,
      'title': '1968: The Year That Rocked the World',
      'authors': 'Mark Kurlansky',
      'average_rating': 3.78,
      'isbn': '0345455827',
      'isbn13': 9780345455826,
      'language_code': 'eng',
      '  num_pages': 480,
      'ratings_count': 2046,
      'text_reviews_count': 248,
      'publication_date': '1/11/2005',
      'publisher': 'Random House Trade Paperbacks'},
     {'bookID': 3346,
      'title': "A Chosen Few: The Resurrection of European Jewry (Reader's Circle)",
      'authors': 'Mark Kurlansky',
      'average_rating': 3.87,
      'isbn': '0345448146',
      'isbn13': 9780345448149,
      'language_code': 'eng',
      '  num_pages': 456,
      'ratings_count': 51,
      'text_reviews_count': 2,
      'publication_date': '3/26/2002',
      'publisher': 'Ballantine Books'},
     {'bookID': 3347,
      'title': 'The Basque History of the World: The Story of a Nation',
      'authors': 'Mark Kurlansky',
      'average_rating': 3.85,
      'isbn': '0140298517',
      'isbn13': 9780140298512,
      'language_code': 'eng',
      '  num_pages': 400,
      'ratings_count': 3457,
      'text_reviews_count': 329,
      'publication_date': '2/1/2001',
      'publisher': 'Penguin Books'},
     {'bookID': 3348,
      'title': "The Cod's Tale",
      'authors': 'Mark Kurlansky/S.D. Schindler',
      'average_rating': 3.91,
      'isbn': '0399234764',
      'isbn13': 9780399234767,
      'language_code': 'eng',
      '  num_pages': 48,
      'ratings_count': 127,
      'text_reviews_count': 25,
      'publication_date': '9/10/2001',
      'publisher': "G.P. Putnam's Sons Books for Young Readers"},
     {'bookID': 3351,
      'title': 'Open City 6: The Only Woman He Ever Left',
      'authors': 'Open City Magazine/James Purdy/Daniel Pinchbeck/Michael Cunningham/Deborah Garrison/Rem Koolhaas/Rick Moody/Strawberry Saroyan/Debra Garrison',
      'average_rating': 0.0,
      'isbn': '189044717X',
      'isbn13': 9781890447175,
      'language_code': 'eng',
      '  num_pages': 200,
      'ratings_count': 0,
      'text_reviews_count': 0,
      'publication_date': '10/13/2000',
      'publisher': 'Grove Press  Open City Books'},
     {'bookID': 3357,
      'title': 'Harry Potter Y La Piedra Filosofal (Harry Potter  #1)',
      'authors': 'J.K. Rowling',
      'average_rating': 4.47,
      'isbn': '0613359607',
      'isbn13': 9780613359603,
      'language_code': 'spa',
      '  num_pages': 254,
      'ratings_count': 142,
      'text_reviews_count': 12,
      'publication_date': '3/6/2001',
      'publisher': 'Turtleback Books'},
     {'bookID': 3359,
      'title': 'Angle of Repose',
      'authors': 'Wallace Stegner/Jackson J. Benson',
      'average_rating': 4.27,
      'isbn': '0141185473',
      'isbn13': 9780141185477,
      'language_code': 'eng',
      '  num_pages': 557,
      'ratings_count': 856,
      'text_reviews_count': 146,
      'publication_date': '12/1/2000',
      'publisher': 'Penguin Classics'},
     {'bookID': 3368,
      'title': "Don't Make Me Think: A Common Sense Approach to Web Usability",
      'authors': 'Steve Krug',
      'average_rating': 4.25,
      'isbn': '0321344758',
      'isbn13': 9780321344755,
      'language_code': 'en-US',
      '  num_pages': 201,
      'ratings_count': 7736,
      'text_reviews_count': 641,
      'publication_date': '8/28/2005',
      'publisher': 'New Riders Publishing'},
     {'bookID': 3384,
      'title': 'Girlfriend in a Coma',
      'authors': 'Douglas Coupland',
      'average_rating': 3.62,
      'isbn': '0060987324',
      'isbn13': 9780060987329,
      'language_code': 'eng',
      '  num_pages': 288,
      'ratings_count': 15798,
      'text_reviews_count': 612,
      'publication_date': '3/1/1999',
      'publisher': 'ReganBooks'},
     {'bookID': 3388,
      'title': "Corelli's Mandolin",
      'authors': 'Louis de Berni??res',
      'average_rating': 3.98,
      'isbn': '067976397X',
      'isbn13': 9780679763970,
      'language_code': 'eng',
      '  num_pages': 437,
      'ratings_count': 62954,
      'text_reviews_count': 1791,
      'publication_date': '8/29/1995',
      'publisher': 'Vintage'},
     {'bookID': 3402,
      'title': 'Kiffe Kiffe Tomorrow',
      'authors': 'Fa??za Gu??ne/Sarah    Adams',
      'average_rating': 3.4,
      'isbn': '0156030489',
      'isbn13': 9780156030489,
      'language_code': 'eng',
      '  num_pages': 179,
      'ratings_count': 1084,
      'text_reviews_count': 131,
      'publication_date': '7/3/2006',
      'publisher': 'Mariner Books'},
     {'bookID': 3403,
      'title': "Our Kind of People: Inside America's Black Upper Class",
      'authors': 'Lawrence Otis Graham',
      'average_rating': 3.72,
      'isbn': '0060984384',
      'isbn13': 9780060984380,
      'language_code': 'en-US',
      '  num_pages': 406,
      'ratings_count': 1170,
      'text_reviews_count': 117,
      'publication_date': '12/22/1999',
      'publisher': 'Harper Perennial'},
     {'bookID': 3404,
      'title': "The Senator and the Socialite: The True Story of America's First Black Dynasty",
      'authors': 'Lawrence Otis Graham',
      'average_rating': 3.95,
      'isbn': '0060184124',
      'isbn13': 9780060184124,
      'language_code': 'eng',
      '  num_pages': 480,
      'ratings_count': 138,
      'text_reviews_count': 29,
      'publication_date': '6/27/2006',
      'publisher': 'Harper'},
     {'bookID': 3409,
      'title': 'Temptations',
      'authors': 'Otis Williams/Patricia Romanowski',
      'average_rating': 4.19,
      'isbn': '0815412185',
      'isbn13': 9780815412182,
      'language_code': 'eng',
      '  num_pages': 304,
      'ratings_count': 99,
      'text_reviews_count': 16,
      'publication_date': '6/25/2002',
      'publisher': 'Cooper Square Press'},
     {'bookID': 3413,
      'title': 'The Thorn Birds',
      'authors': 'Colleen McCullough',
      'average_rating': 4.23,
      'isbn': '0060837551',
      'isbn13': 9780060837556,
      'language_code': 'eng',
      '  num_pages': 673,
      'ratings_count': 533,
      'text_reviews_count': 66,
      'publication_date': '9/6/2005',
      'publisher': 'Avon Books'},
     {'bookID': 3416,
      'title': 'Caesar (Masters of Rome  #5)',
      'authors': 'Colleen McCullough',
      'average_rating': 4.37,
      'isbn': '0060510854',
      'isbn13': 9780060510855,
      'language_code': 'eng',
      '  num_pages': 928,
      'ratings_count': 5991,
      'text_reviews_count': 120,
      'publication_date': '1/28/2003',
      'publisher': 'Avon'},
     {'bookID': 3417,
      'title': "Caesar's Women (Masters of Rome  #4)",
      'authors': 'Colleen McCullough',
      'average_rating': 4.25,
      'isbn': '0380710846',
      'isbn13': 9780380710843,
      'language_code': 'eng',
      '  num_pages': 943,
      'ratings_count': 5423,
      'text_reviews_count': 157,
      'publication_date': '2/1/1997',
      'publisher': 'Avon'},
     ...]




```python
data2 = greek_roman_clean_for_combine_df.to_dict(orient = 'records')
data2
```




    [{'Unnamed: 0': 0,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 1,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 2,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 3,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 4,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 5,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 6,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 7,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 8,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 9,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 10,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 11,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 12,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 13,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 14,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 15,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 16,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 17,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 18,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 19,
      'ISBN-10': '41392649',
      'ISBN-13': '9780141392646',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 04/17/2018 '},
     {'Unnamed: 0': 20,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 21,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 22,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 23,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 24,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 25,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 26,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 27,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 28,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 29,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 30,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 31,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 32,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 33,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 34,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 35,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 36,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 37,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 38,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 39,
      'ISBN-10': '691156573',
      'ISBN-13': '9780691156576',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 01/22/2013 '},
     {'Unnamed: 0': 40,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 41,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 42,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 43,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 44,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 45,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 46,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 47,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 48,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 49,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 50,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 51,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 52,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 53,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 54,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 55,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 56,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 57,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 58,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 59,
      'ISBN-10': '942299175',
      'ISBN-13': '9780942299175',
      'Publisher': '                          Publisher: Zone Books ',
      'Publish Date': '                                Publish Date: 10/17/1990 '},
     {'Unnamed: 0': 60,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 61,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 62,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 63,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 64,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 65,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 66,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 67,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 68,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 69,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 70,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 71,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 72,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 73,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 74,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 75,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 76,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 77,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 78,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 79,
      'ISBN-10': '40442103',
      'ISBN-13': '9780140442106',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 07/30/1969 '},
     {'Unnamed: 0': 80,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 81,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 82,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 83,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 84,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 85,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 86,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 87,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 88,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 89,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 90,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 91,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 92,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 93,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 94,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 95,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 96,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 97,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 98,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 99,
      'ISBN-10': '40441360',
      'ISBN-13': '9780140441369',
      'Publisher': '                          Publisher: Penguin Group ',
      'Publish Date': '                                Publish Date: 05/30/1964 '},
     {'Unnamed: 0': 100,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 101,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 102,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 103,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 104,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 105,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 106,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 107,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 108,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 109,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 110,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 111,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 112,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 113,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 114,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 115,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 116,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 117,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 118,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '},
     {'Unnamed: 0': 119,
      'ISBN-10': '691150265',
      'ISBN-13': '9780691150260',
      'Publisher': '                          Publisher: Princeton University Press ',
      'Publish Date': '                                Publish Date: 03/27/2011 '}]




```python
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
```

    ETL Complete
    


```python

```


```python

```
