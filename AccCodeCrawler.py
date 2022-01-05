import pyppeteer
import asyncio
import bs4
import time


async def antiAntiCrawler(page):
    await page.setUserAgent('Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36')
    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator, \
    { webdriver:{ get: () => false } }) }')


async def getHtml(url):
    browser = await pyppeteer.launch(headless=False, executablePath="C:\\Users\\liangqiao\\Desktop\\chrlauncher-win64"
                                                                    "-dev-official\\bin\\chrome.exe",
                                     userdataDir="tmp")
    page = await browser.newPage()
    await antiAntiCrawler(page)
    await page.goto(url)
    l = await page.querySelectorAll(".problem-id")
    page1 = await browser.newPage()
    await antiAntiCrawler(page)
    return l


async def getAccCode(url):
    browser = await pyppeteer.launch(headless=False, executablePath="C:\\Users\\liangqiao\\Desktop\\chrlauncher-win64"
                                                                    "-dev-official\\bin\\chrome.exe",
                                     userdataDir="tmp", args=[f'--window-size={width},{height}'])
    page = await browser.newPage()
    await antiAntiCrawler(page)
    await page.setViewport({'width': width, 'height': height})
    await page.goto(url)
    await page.waitForNavigation()
    page1 = await browser.newPage()
    await antiAntiCrawler(page1)
    await page1.setViewport({'width': width, 'height': height})
    await page1.goto(url02)
    elements = await page1.querySelectorAll(".problem-id")
    page2 = await browser.newPage()
    await antiAntiCrawler(page2)
    await page2.setViewport({'width': width, 'height': height})
    for element in elements[1:]:
        obj = await element.getProperty("innerText")
        text = await obj.jsonValue()
        url2 = page1.url+text
        await page2.goto(url2)
        element1 = await page2.querySelector("#pageTitle > h2")
        obj = await element1.getProperty("innerText")
        title = await obj.jsonValue()
        element1 = await page2.querySelector(".result-right")
        await element1.click()
        await page2.waitForNavigation()
        element1 = await page2.querySelector("pre")
        obj = await element1.getProperty("innerText")
        text = await obj.jsonValue()
        print(title)
        print(text)
        print("--------------------------------------------------")
        # time.sleep(2)
    await asyncio.sleep(100)
    await browser.close()



width, height = 1800, 1000
url = "http://openjudge.cn/auth/login/"
url01 = "http://cxsjsxmooc.openjudge.cn/2021pyfall/"
url02 = "http://cxsjsxmooc.openjudge.cn/2021t1fall/"

m = asyncio.ensure_future(getAccCode(url))
asyncio.get_event_loop().run_until_complete(m)
# print(m.result())
# soup = bs4.BeautifulSoup(m.result(), "html.parser")
# diva = soup.find_all("a")
# print(diva)

# soup = bs4.BeautifulSoup(m.result(), "html.parser")
# for x in soup.find_all("td"):
#     print(x.text)
