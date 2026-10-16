import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

r = requests.get(url, headers=headers, timeout=10)
r.raise_for_status()
r.encoding = "utf-8"

soup = BeautifulSoup(r.text, "lxml")

# 页面里每部电影都包在 <div class="item"> 里
items = soup.select("div.item")
print(f"本页共找到 {len(items)} 部电影\n")

for item in items[:5]:   # 先只打印前 5 部看效果
    rank    = item.select_one("em").text
    title   = item.select_one("span.title").text
    rating  = item.select_one("span.rating_num").text
    quote_el = item.select_one("span.inq")
    quote   = quote_el.text if quote_el else "(无简介)"
    
    print(f"#{rank:>3}  {title:<20}  ⭐ {rating}   —  {quote}")