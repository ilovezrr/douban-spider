"""Douban Top 250 crawler."""
import time
import random
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import re

BASE_URL = "https://movie.douban.com/top250"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}
OUT_DIR = Path("data")
OUT_DIR.mkdir(exist_ok=True)


def fetch_page(start: int) -> str:
    r = requests.get(BASE_URL, params={"start": start},
                     headers=HEADERS, timeout=10)
    r.raise_for_status()
    r.encoding = "utf-8"
    return r.text


def parse_page(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    results = []
    for item in soup.select("div.item"):
        p = item.select_one(".bd p")          # 每个电影条目里的 <p> 标签
        results.append({
            "rank": int(item.select_one("em").text),
            "title": item.select_one("span.title").text.strip(),
            "rating": float(item.select_one("span.rating_num").text),
            "quote": (item.select_one("span.inq").text
                      if item.select_one("span.inq") else ""),
            # "director": p.get_text(" ", strip=True).split("导演：")[1].split("主演：")[0].strip(),
            "year": re.search(r"\d{4}", p.get_text(" ", strip=True)).group()
        })
                
            # TODO: year / director / votes 自己补

    return results


def main():
    all_movies = []
    for start in range(0, 250, 25):
        print(f"→ 抓第 {start // 25 + 1} 页 ...")
        html = fetch_page(start)
        all_movies.extend(parse_page(html))
        time.sleep(random.uniform(1.0, 2.0))

    df = pd.DataFrame(all_movies)
    df.to_csv(OUT_DIR / "movies.csv", index=False, encoding="utf-8-sig")
    df.to_json(OUT_DIR / "movies.json", orient="records",
               force_ascii=False, indent=2)
    print(f"✅ 完成,共 {len(df)} 部,已写入 data/")


if __name__ == "__main__":
    main()