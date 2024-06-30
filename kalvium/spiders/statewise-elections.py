import scrapy

class MainElectionSpider(scrapy.Spider):
    name = 'statewise-elections'

    start_urls = [
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U01.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U02.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U03.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U05.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U06.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U07.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U08.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-U09.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S01.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S02.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S03.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S04.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S05.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S06.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S07.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S08.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S10.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S11.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S12.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S13.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S14.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S15.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S16.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S17.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S18.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S19.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S20.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S21.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S22.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S23.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S24.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S25.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S26.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S27.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S28.htm',
        'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S29.htm'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        state = response.css('div.page-title strong::text').get().strip()
        for row in response.xpath('//*[@class="table"]//tbody//tr'):
            yield {
                'State': state,
                'Party': row.xpath('td[1]//text()').extract_first().strip(),
                'Won': row.xpath('td[2]//a//text()').extract_first().strip(),
                'Leading': row.xpath('td[3]//text()').extract_first().strip(),
                'Total': row.xpath('td[4]//text()').extract_first().strip(),
            }
