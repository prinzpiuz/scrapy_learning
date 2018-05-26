import scrapy


class QuotesSpider(scrapy.Spider):
    name = "espn"
    start_urls = [
   'http://www.espncricinfo.com/india/content/player/36084.html'
   ]

    def parse(self, response):
        for player in response.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[1]'):
            yield {
                'name': player.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[1]/div/h1/text()').extract_first(),
                'country': player.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[1]/div/h3/b/text()').extract_first(),
                'fullname': player.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[1]/p[1]/span/text()').extract_first(),
                'born':player.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[1]/p[2]/span/text()').extract_first(),
                'current_age':player.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[1]/p[3]/span/text()').extract_first(),
                'major_teams':player.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[1]/p[4]/text()').extract_first(),
                'playing_role ':player.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[1]/p[5]/span/text()').extract_first(),
                'batting_style':player.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[1]/p[6]/span/text()').extract_first(),
                'bowling_style':player.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[1]/p[7]/span/text()').extract_first(),
                'image':player.xpath('//*[@id="ciHomeContentlhs"]/div[4]/div[2]/div[2]/img/text()').extract_first(),
                'geo_details':''
            }

