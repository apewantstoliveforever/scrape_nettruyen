import requests
from bs4 import BeautifulSoup
import csv
import time

field = ["title", "chapternumber", "eyes", "comment", "heart", 'colour']
filename ="t.csv"
csvfile = open(filename, "w", encoding='utf-8')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(field)

def crawldata(pagenumber):
    site = f'http://www.nettruyengo.com/tim-truyen?status=-1&sort=10&page={pagenumber}'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(site, headers= hdr)
    soup = BeautifulSoup(page.content, "html.parser")
    time.sleep(0.5)
    while not soup.find(class_="error-404 not-found"):
        center = soup.find(id = 'ctl00_divCenter')
        items = center.find_all(class_= 'item')
        print(pagenumber, len(items))
        len(items)
        allmanga = []
        for item in items:
            names = item.find_all('figcaption')
            for name in names:
                title = name.find('a', class_="jtip").get_text()
                link = name.find('a', class_="jtip").get('href')
                pagegettag = requests.get(link, headers = hdr)
                content1 = BeautifulSoup(pagegettag.content, 'html.parser')
                kind = content1.find(class_="kind row")
                kind1 = kind.find_all('a')
                kindtext = ''
                m = 0
                for i in kind1:
                    if i.get_text() == "Truyện Màu":
                        m = 1
                        pass
                    else:
                        kindtext+= "," + i.get_text()
            chapters = item.find_all(class_="chapter clearfix")
            chapter = chapters[0].find('a').get_text()
            chapternumber = chapter.split(" ")[1]

            statics = item.find_all('div', class_="view clearfix")
            for static in statics:

                numbers = static.find('i', class_="fa fa-eye")
                numbers = static.get_text().strip('\n')
                numbers2 = numbers.split('\n')
                numbers1 = numbers2[0].split(' ')
                eyes = numbers1[1]
                comment = numbers1[3]
                heart = numbers1[5]
            allmanga.append([title, chapternumber, eyes, comment, heart, kindtext, m])

            print(title, chapternumber, eyes, comment, heart, kindtext, m)

        csvwriter.writerows(allmanga)
        pagenumber += 1
        site = f'http://www.nettruyengo.com/tim-truyen?status=-1&sort=10&page={pagenumber}'
        page = requests.get(site, headers=hdr)
        soup = BeautifulSoup(page.content, "html.parser")

        #comment = item.select("span", class_="fa fa-comment")
        #commentnumber = comment.get_text()

        #heart = item.select("span", class_="fa fa-heart")
        #heartnumber = heart.get_text()
    print(pagenumber)

crawldata(1)


