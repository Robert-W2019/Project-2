# Project-2 - ETL

##● **E**xtract: your original data sources and how the data was formatted (CSV, JSON, pgAdmin 4, etc).

Extract is where I spent most of the project's time.

I started with the goal to scrap book data from a website to compare it to the goodreads csv found here: 
[Kaggle](https://www.kaggle.com/jealousleopard/goodreadsbooks)

Since I have not had much experience with scraping data I wanted to practice with a site designed for it, so I used the Books to Scrape sandbox found here:
[Books2Scrape]( https://books.toscrape.com/index.html)
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
	table_of_tables.append(table_on_page)
        df = pd.read_html(str(table))[0]
        print(df)
               
             
        
browser.quit()    
               
             
        
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
    2  Price (excl. tax)                   £51.77
    3  Price (incl. tax)                   £51.77
    4                Tax                    £0.00
    5       Availability  In stock (22 available)
    6  Number of reviews                        0
    ----------
    Tipping the Velvet
                       0                        1
    0                UPC         90fa61229261140a
    1       Product Type                    Books
    2  Price (excl. tax)                   £53.74
    3  Price (incl. tax)                   £53.74
    4                Tax                    £0.00
    5       Availability  In stock (20 available)
    6  Number of reviews                        0

Now that I had a proof of concept with a more forgiving site I moved on to using a public site not designed for scraping. I tried a few different sites, but ultimately used the City Lights Booksellers & Publishers website’s (bookstore in San Francisco) Greek & Roman classic book section found here:
[Books2Scrape]( https://citylights.com/greek-roman/)









##● **T**ransform: what data cleaning or transformation was required.
I initially to used Splinter, BeautifulSoup, and Pandas to put the practice site data into a DataFrame then a CSV.

Once I had the data scraped from City Lights Booksellers & Publishers I cleaned, put it into a dataframe, and saved it as a CSV using the same or similar steps as the practice site data transforming process.


I then attempted to combine the two datasets (Kaggle CSV and City Lights CSV); however, it appears that the books did not have any overlap

Although my goal was to combine and compare the two via ISBN it did not work out so I moved onto the Loading portion.


##● **L**oad: the final database, tables/collections, and why this was chosen.

For loading I put all of the data into MongoDB, screenshots below:

