from bs4 import BeautifulSoup
import requests
from requests import RequestException
import re
from hashlib import md5


def get_page_index():
    url = "https://www.zhihu.com/question/22918070"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except RequestException:
        print("请求错误")
        pass

def parse_page_index(html):
    soup = BeautifulSoup(html,"html.parser")
    print(html)
    links = soup.find_all('img', "origin_image zh-lightbox-thumb", src=re.compile(r'.jpg$'))
    download_image(links)


def download_image(links):
    for link in links:
        image_url = link.attrs["src"]
        try:
            response = requests.get(image_url)
            print("正在下载",image_url)
            if response.status_code == 200:
                save_image(response.content)
        except RequestException:
            print("请求错误")
            pass

def save_image(content):
    path = "G:/zhihu/image"
    file_path = '{0}/{1}.{2}'.format(path, md5(content).hexdigest(), "jpg")
    print(file_path)
    with open(file_path,"wb") as f:
        f.write(content)
        f.close()


def main():
    html = get_page_index()
    parse_page_index(html)


if __name__ == '__main__':
    main()