import scrapy

class IndeedSpider(scrapy.Spider):
	name = 'indeed_spider'
	start_urls = ['https://www.indeed.com/jobs?q&l=Sonoma%2C%20CA&radius=5&fromage=1&sort=date&vjk=c8b436b8016fad08']
	links = []

	def parse(self, response,):
		links = []
		TITLE_SELECTOR = '.title'
		for title in response.css(TITLE_SELECTOR):

			LINK_SELECTOR = 'a ::attr(href)'
			links.append('https://www.indeed.comcls'+ title.css(LINK_SELECTOR).extract_first())

		NEXT_PAGE_SELECTOR = '.pagination-list a ::attr(href)'
		next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		if next_page:
			scrapy.Request(response.urljoin(next_page), callback=self.parse)
		print('\n\n')

		print("LENGTH " + str(len(links)))
		for l in links:
			print(l + '\n\n')
		print('\n\n')
