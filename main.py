import pprint

import requests
import re,bs4

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}
url="https://www.zhihu.com/explore"
res= requests.get(url, headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
a=soup.select('a')
for a1 in a:
    print(a1.getText())
