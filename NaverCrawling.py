from bs4 import BeautifulSoup
import requests
# from naver import get_data
# naver = get_data()

if __name__ == "__main__":

    search = input("네이버 뉴스에 검색할 키워드를 입력하세요:")
    page = int(input("크롤링할 페이지를 입력해주세요. ex)1(숫자만 입력:"))
    # print("크롤링할 페이지:", page, "페이지")

    class coco:
        def __init__(self):
            self.print = "크롤링할 페이지:", page, "페이지"
        
        def greeting(self):
            print(self.print)

    james = coco()
    james.greeting()

    page_num = 0

    if page == 1:
        page_num = 1
    elif page == 0:
        page_num=1
    else:
        page_num = page+9*(page-1)

    url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page_num)
    print("생성url:", url)

    # ConnectionError방지
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75" }
    #html불러오기
    original_html = requests.get(url, headers=headers)
    html = BeautifulSoup(original_html.text, "html.parser")

    # 검색 결과
    articles = html.select("div.group_news > ul.list_news > li div.news_area > a")
    print(articles)

    # 검색된 기사의 갯수
    print(len(articles), "개의 기사가 검샘됨")    

    # 뉴스기사 제목 가져오기
    news_title = []
    for i in articles:
        news_title.append(i.attrs['title'])
    news_title

    # 뉴스기사 URL 가져오기
    news_url = []
    for i in articles:
        news_url.append(i.attrs['href'])
    news_url

    # 뉴스기사 내용
    # contents = []
    # for i in news_url:
    #     news = requests.get(i)
    #     news_html = BeautifulSoup(news.text, "hrml.parser")
    #     contents.append(news_html.find_all('p'))
    # contents








