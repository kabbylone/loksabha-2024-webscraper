import scrapy

class MainElection(scrapy.Spider):
    name = 'main-election'
    start_urls = ['https://results.eci.gov.in/PcResultGenJune2024/index.htm']

    
    def parse(self, response):
        for row in response.xpath('//*[@class="table"]//tbody//tr'):
            yield {
                'Party' : row.xpath('td[1]//text()').extract_first().strip(),
                'Won' : row.xpath('td[2]//a//text()').extract_first().strip(),
                'Leading' : row.xpath('td[3]//text()').extract_first().strip(),
                'Total' : row.xpath('td[4]//text()').extract_first().strip(),
            }