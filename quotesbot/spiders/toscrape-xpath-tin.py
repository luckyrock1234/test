# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath-tin'
    urlTemplate='https://www.tinxsys.com/TinxsysInternetWeb/dealerControllerServlet?searchBy=TIN&tinNumber='
    tinNumber = '06512826303'
    start_urls = [
        urlTemplate+tinNumber,
    ]

    def parse(self, response):
    	temp = response.xpath('//div/table/tr[0]/td[0]/div/text()').extract_first()
    	
    	if temp.startswith("Dealer Not Found for the entered TIN"):
    		print 'Dealer Not Found for the entered TIN --> '+tinNumber
    	else:
	    	yield {
				'tin': response.xpath('//div/table/tr[1]/td[1]/div/text()').extract_first(),
				'dealerName': response.xpath('//div/table/tr[2]/td[1]/div/text()').extract_first(),
				'dealerAddress': response.xpath('//div/table/tr[3]/td[1]/div/text()').extract_first()
			}
    		
    	next_page_url = urlTemplate+(tinNumber+1)
    	
		if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))