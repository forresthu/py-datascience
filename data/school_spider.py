import scrapy
from scrapy.crawler import CrawlerProcess


class RankItem(scrapy.Item):
    current_rank = scrapy.Field()
    last_5_years_rank = scrapy.Field()
    school_name = scrapy.Field()
    school_rank_detail_link = scrapy.Field()
    current_rating = scrapy.Field()
    last_5_years_rating = scrapy.Field()


class SchoolSpider(scrapy.Spider):
    name = "GTA School Extract"
    start_urls = ["http://ontario.compareschoolrankings.org/elementary/SchoolsByRankLocationName.aspx"]

    def parse(self, response):
        self.logger.info(response)
        print(response)
        for rating_table in response.xpath("//table[@class='rating']"):
            print(rating_table)
            schools = []
            for row in rating_table.xpath('.//table/tbody/tr'):
                school = RankItem()
                i = 0
                for col in row.xpath(".//td/text()"):
                    self.logger.log(col.extract_first())


process = CrawlerProcess({
    'USER_AGENT': 'Mozilia/4.0'
})

# aspnetForm > table:nth-child(7) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)

process.crawl(SchoolSpider)
process.start()
