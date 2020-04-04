"""
巴哈姆特場外休憩區爬蟲練習
2020.04.03
Elian
"""
import requests
# 載入BeautifulSoup套件, 若沒有的話可以先: pip install beautifulsoup4
from bs4 import BeautifulSoup
import pandas as pd
class Cralwer():
    def crawler():
        url = 'https://forum.gamer.com.tw/B.php?bsn=60076'
        # 透過request套件抓下這個網址的資料
        requ = requests.get(url)
        # 初步檢視抓到的資料結構
        web_content = requ.text
        #print(web_content)

        # 以 Beautiful Soup 解析 HTML 程式碼 :
        soup = BeautifulSoup(web_content, 'lxml')

        # 找出所有class為"b-list__main__title"的a elements
        titleElements = soup.find_all('a', class_="b-list__main__title")
        #print(titleElements)
        title = [e.text for e in titleElements]
        #print(title)

        # 找出所有class為"b-list__main__title"的p elements
        titleElements = soup.find_all('p', class_="b-list__main__title")
        #print(titleElements)
        title = [e.text for e in titleElements]
        #print(title)

        #找出所有class為"b-list__brief"的p elements
        briefElements = soup.find_all('p', class_="b-list__brief")
        #print(briefElements)
        brief = [e.text for e in briefElements]
        #print(brief)

        # 找出所有target為"b-list__brief"的a elements
        blankElements = soup.find_all('a', target="_blank")
        #print(blankElements)
        blank = [e.text for e in blankElements]
        #print(blank)

        # 找出所有target為"b-list__brief"的a elements
        timeElements = soup.find_all('a',title="觀看最新回覆文章")
        #print(timeElements)
        time = [e.text for e in timeElements]
        #print(time)

        #print數量
        print('文章數量:',len(title), len(brief), len(time))

        for ti, br, bl in zip(title, brief, time):
            print(ti,br,bl)

        bahamut_dict = {"title": title,
                        "brief": brief,
        }

    crawler()
#save to excel
"""
excelWriter = pd.ExcelWriter("bahamut.xlsx")   # 儲存路徑
bahamut_df = pd.DataFrame(bahamut_dict)
bahamut_df.to_excel(excelWriter, "Reply")        # Sheet name
excelWriter.save()
"""