import scrapy


class VideoSpider(scrapy.Spider):
    name = "bilibili"

    def start_requests(self):
        urls = [
            'https://www.bilibili.com/video/av13517141?from=search&seid=17251022428640802502',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)