import os
import time
import requests
from bs4 import BeautifulSoup


def main(blver):
    while True:
        os.system("cls")
        keyword = input("请输入要搜索的关键词：")
        page = input("请输入要查找的页数：")

        try:
            page_num = int(page)
            if page_num <= 0:
                print("请输入正整数！")
                continue
        except ValueError:
            print("请输入正整数！")
            continue

        url = f"https://www.so.com/s?q={keyword}&pn={page_num - 1}"

        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        result_divs = soup.find_all('div', class_='result')

        if not result_divs:
            print("没有找到相关内容！")
            continue

        for div in result_divs:
            title = div.find('h3').get_text().strip()
            summary = div.find('p').get_text().strip()
            link = div.find('a').get('href')

            print(title)
            print(summary)
            print(link)

        time.sleep(1)

main("test 1")