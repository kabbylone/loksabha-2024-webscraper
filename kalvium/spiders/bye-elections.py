import scrapy

class MainElection(scrapy.Spider):
    name = 'bye-elections'
    start_urls = ['https://results.eci.gov.in/AcResultByeJune2024/index.htm']

    
    def parse(self, response):
        for card in response.css('div.box-content'):
            yield {
                'Constituency' : card.css('h3::text').extract_first().strip(),
                'State' : card.css('h4::text').extract_first().strip(),
                'Candidate Name' : card.css('h5::text').extract_first().strip(),
                'Party' : card.css('h6::text').extract_first().strip(),
            }