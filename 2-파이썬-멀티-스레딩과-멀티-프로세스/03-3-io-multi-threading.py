# https://docs.python.org/3.7/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com", "https://apple.com"] * 50

    #스레드의 최대 개수
    executor = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        # result = [fetcher(session, url) for url in urls]
        # print(result)
        params = [(session, url) for url in urls]

        #map 메소드는 실행시킬 함수와 파라미터를 넣으면 됨
        results = list(executor.map(fetcher, params))
        print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)  # 2.5
