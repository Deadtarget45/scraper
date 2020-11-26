import scrapy
#links = response.xpath('//h3/a[starts-with(@href, "collection")]/@href').getall() 
#titulo = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
#cuerpo = response.xpath('//div[@class="field-item even"]/p[3]/text()').get()


class CiaSpider(scrapy.Spider):

    name = 'cia'
    
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI':'cia_scraper.json',
        'FEED_FORMAT_ENCODING': 'utf-8'
    }

    start_urls = ['https://www.cia.gov/library/readingroom/historical-collections']


    def parse(self, response):
        links_declassified = response.xpath('//h3/a[starts-with(@href, "collection")]/@href').getall()

        for link in links_declassified:
           yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        cuerpo = response.xpath('//div[@class="field-item even"]/p[3]/text()').get()

        yield {
            'link':link,
            'title': title,
            'body':cuerpo
        }

        

