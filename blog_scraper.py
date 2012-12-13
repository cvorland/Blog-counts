from BeautifulSoup import BeautifulSoup
import mechanize
import time
import re
from xlrd import open_workbook 
from xlwt import easyxf

pagenum = 1
url = "http://www.bloghomepage.com"
browser = mechanize.Browser()
page = browser.open(url)
postcount = 0
totalwordcount = 0
totalrefcount = 0
stop = "false"

while "false" in stop:
    time.sleep(0)
    soup = BeautifulSoup(page)
    link = soup.find("span", {"class":"next"})
    if "Older" in str(link):
        pagenum += 1
        print pagenum
        stop = "false"
    else:
        stop = "true"
    for table in soup.findAll('h1', {'class':'title'}):
        links = table.findAll('a')
        if "href" in str(links):
            #print links
            separatelinks = re.search("(?P<url>http?://[^\>\"\s]+)", str(links)).group("url")
            print separatelinks
            site = browser.open(str(separatelinks)).read()
            soup = BeautifulSoup(site)
            content = soup.find("div", {"class":"content entry-content"})
            fp = open('C:/filename.html', 'w')
            fp.write(str(content))
            fp.close()

            f = open('C:/filename.html', 'r')
            readit = f.read()
            f.close()

            onlytext = ''.join(BeautifulSoup(readit).findAll(text=True))
            #print onlytext
            fp2 = open('C:/filename.html', 'w')
            fp2.write(str(onlytext.encode('ascii','ignore')))
            fp2.close()

            words = re.findall('\w+', open('C:/filename.html').read().lower())
            wordcount = len(words)
            print wordcount
            totalwordcount += wordcount
            print totalwordcount

            refcount = 0
            for Z3988 in soup.findAll('span', {'class':'Z3988'}):
                refcount += 1
            print refcount
            totalrefcount += refcount
            print totalrefcount
            
            postcount += 1
            print postcount

            #time.sleep(1) If you don't want to hit the server too fast
            
        else:
            print "not a link"
            url = "http://www.bloghomepage.com/page/"+str(pagenum)
            page = browser.open(url)
