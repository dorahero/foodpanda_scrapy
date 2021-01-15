from foodpanda.items import FoodpandaItem
import scrapy
import time
from datetime import datetime

class FoodPandaSpider(scrapy.Spider):
    name:str = "foodpanda"
    NowDateTime = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")         
    headers={
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "cookie": "__cfduid=dc79d779dadcd31e4c3bee4beda649aa21600414766; hl=zh; AppVersion=cd681f5; ld_key=60.250.28.225; _pxvid=1871354f-f982-11ea-874d-0242ac120004; _px3=2010e56d57aea08019808a3d6a1f138e8ff077ff3d0423f5a191fbf4b2a52cd4:RIhQhtKtdWdKeM2bq1MaokyIXIcxIAheZ0aqQUTQHzkI93R0+5mFP7KPfOYRf1a7xcQbTuj/kfX+O2ePaOLSBg==:1000:FqDsJ92+f+u3zAcdbORoEFJ0sbyw3w/NOKxNU9LxXGdGOftmtLcBuBCTYZToMwEY8mWuYNrTeHj42q6HkQqJYlPCJDZqbQqY2Ioif/YcQfOJwDNzCSGmu+itLS3AOsllN06CPaVOfQed0yGX3luZDU4Xmtn5eeMJawYwdTd3TvM=",
        "dps-session-id": "undefined",
        "pragma": "no-cache",
        "referer": "https://www.foodpanda.com.tw/restaurant/u2xh/big-als-burgers",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "x-pd-language-id": "6",
        "x-requested-with": "XMLHttpRequest",
    }      
    def start_requests(self):        
        for id in range(3000,111111):
            url = 'https://www.foodpanda.com.tw/api/v1/vendors/'+str(id)+'?include=menus%2Cmenu_categories&order_time=' + self.NowDateTime +'+0800&language_id=6&opening_type=delivery'  
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):           
        api1_data = response.json()        
        item = FoodpandaItem()
        item['data'] = api1_data
        yield item