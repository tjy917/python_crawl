#  https://morvanzhou.github.io/tutorials/data-manipulation/scraping/4-02-asyncio/

# Code1不是异步的 明显的体现是job是按照顺序执行的， 即Job1 完成后 Job2再拉起
# import time


# def job(t):
#     print('Start job ', t)
#     time.sleep(t)               # wait for "t" seconds
#     print('Job ', t, ' takes ', t, ' s')


# def main():
#     [job(t) for t in range(1, 3)]


# t1 = time.time()
# main()
# print("NO async total time : ", time.time() - t1)



# Code2异步机制，会在await 时切换到背的job，异步消耗的时间=等待最长的job的消耗时间
# import asyncio
# import time


# async def job(t):                   # async 形式的功能
#     print('Start job ', t)
#     await asyncio.sleep(t)          # 等待 "t" 秒, 期间切换其他任务
#     print('Job ', t, ' takes ', t, ' s')


# async def main(loop):                       # async 形式的功能
#     tasks = [
#     loop.create_task(job(t)) for t in range(1, 3)
#     ]                                       # 创建任务, 但是不执行
#     await asyncio.wait(tasks)               # 执行并等待所有任务完成

# t1 = time.time()
# loop = asyncio.get_event_loop()             # 建立 loop
# loop.run_until_complete(main(loop))         # 执行 loop
# loop.close()                                # 关闭 loop
# print("Async total time : ", time.time() - t1)


# Code3 普通的Requets模块爬网页

# import requests
# import time

# URL = 'https://morvanzhou.github.io/'


# def normal():
#     for i in range(2):
#         r = requests.get(URL)
#         url = r.url
#         print(url)

# t1 = time.time()
# normal()
# print("Normal total time:", time.time()-t1)


# Code4 aiohttp 模块使用，可以将requests替换成异步类型
# import aiohttp
# import time
# import asyncio

# URL = 'https://morvanzhou.github.io/'

# async def job(session):
#     response = await session.get(URL)       # 等待并切换
#     return str(response.url)


# async def main(loop):
#     async with aiohttp.ClientSession() as session:      # 官网推荐建立 Session 的形式
#         tasks = [loop.create_task(job(session)) for _ in range(2)]
#         finished, unfinished = await asyncio.wait(tasks)
#         all_results = [r.result() for r in finished]    # 获取所有结果
#         print(all_results)

# t1 = time.time()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(loop))
# loop.close()

# Code 5 Final Code 使用asyncio 和aiohttp

import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup
from urllib.request import urljoin
import re
import multiprocessing as mp

base_url = "https://morvanzhou.github.io/"
# base_url = "http://127.0.0.1:4000/"

# DON'T OVER CRAWL THE WEBSITE OR YOU MAY NEVER VISIT AGAIN
if base_url != "http://127.0.0.1:4000/":
    restricted_crawl = True
else:
    restricted_crawl = False

seen = set()
unseen = set([base_url])


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])
    url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url


async def crawl(url, session):
    r = await session.get(url)
    html = await r.text()
    await asyncio.sleep(0.1)        # slightly delay for downloading
    return html


async def main(loop):
    pool = mp.Pool(2)               # slightly affected
    async with aiohttp.ClientSession() as session:
        count = 1
        while len(unseen) != 0:
            if restricted_crawl and len(seen) > 20:
                break
            tasks = [loop.create_task(crawl(url, session)) for url in unseen]
            finished, unfinished = await asyncio.wait(tasks)
            htmls = [f.result() for f in finished]

            parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
            results = [j.get() for j in parse_jobs]

            seen.update(unseen)
            unseen.clear()
            for title, page_urls, url in results:
                print(count, title, url)
                unseen.update(page_urls - seen)
                count += 1

if __name__ == "__main__":
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
    print("Async total time: ", time.time() - t1)