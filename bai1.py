import requests
from bs4 import BeautifulSoup
import json
import os
import re

def scrape_vnexpress_politics():
    url = "https://vnexpress.net/thoi-su/chinh-tri"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    folder_name = "data"
    os.makedirs(folder_name, exist_ok=True)

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # ✅ FIX selector
    articles = soup.select('h3.title-news a, h2.title-news a')

    print(f"Tìm thấy {len(articles)} bài")

    for index, link_tag in enumerate(articles):
        article_url = link_tag['href']

        try:
            detail_res = requests.get(article_url, headers=headers)
            detail_soup = BeautifulSoup(detail_res.content, 'html.parser')

            title = detail_soup.select_one('h1.title-detail')
            title = title.get_text(strip=True) if title else "No title"

            date = detail_soup.select_one('span.date')
            date = date.get_text(strip=True) if date else "No date"

            content_div = detail_soup.select_one('article.fck_detail')
            if content_div:
                paragraphs = content_div.find_all('p')
                content = "\n".join(p.get_text(strip=True) for p in paragraphs)
            else:
                content = "No content"

            data = {
                "Title": title,
                "Date": date,
                "Content": content
            }

            file_name = re.sub(r'[\\/*?:"<>|]', "", title)[:50] + f"_{index}.json"
            file_path = os.path.join(folder_name, file_name)

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            print("Đã lưu:", file_name)

        except Exception as e:
            print("Lỗi:", e)

    print("Done!")

if __name__ == "__main__":
    scrape_vnexpress_politics()