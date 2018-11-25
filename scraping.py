from bs4 import BeautifulSoup
from urllib.request import urlopen

def getWord(word):

    html = urlopen("http://www.usachan.co.jp/usachan/price/r/")
    data = html.read()
    html = data.decode('utf-8')

    # HTMLを解析
    soup = BeautifulSoup(html,'html.parser')

    # 解析したHTMLから任意の部分のみを抽出
    links = soup.find_all("tr")

    # 該当記事カウント変数と結果格納リスト
    count = 0
    result = ""
    list = []
    for a in links:
        col = a.find_all("td")
        if len(col) < 2:
            continue
        if a.text.find(word) > -1:
            item = a.find("th")
            list.append(item.text)
            list.append(col[0].text)

    if len(list) > 0:
        result = '\n'.join(list) + '\nだっぴょん'
    else:
        result = 'アイテムが見つからなかったぴょん'

    return result