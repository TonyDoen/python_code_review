from scrapy.spider import Spider
from scrapy import FormRequest 
from scrapy import Request 
from scrapy.selector import Selector
import time

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = [ "ntiaoji.kaoyan.com" ]
    start_urls = [
        #"http://ntiaoji.kaoyan.com/tjadm/1.html",
        "http://ntiaoji.kaoyan.com/tjadm/login"
    ]
    headers = {
    "Host": "ntiaoji.kaoyan.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "http://ntiaoji.kaoyan.com/tjadm/2.html",
    "Cookie": "Hm_lvt_d49310205bb84832b8827fd95bdfe1af=1456586298; _ga=GA1.2.388822438.1456586299; Hm_lpvt_d49310205bb84832b8827fd95bdfe1af=1456594275; _gat=1",
    "Connection": "keep-alive"
    }

    def parse(self, response) :
#        test_urls = [
#        "http://ntiaoji.kaoyan.com/tjadm/1.html",
#        "http://ntiaoji.kaoyan.com/tjadm/2.html",
#        "http://ntiaoji.kaoyan.com/tjadm/3.html",
#        "http://ntiaoji.kaoyan.com/tjadm/4.html",
#        "http://ntiaoji.kaoyan.com/tjadm/5.html",
#        "http://ntiaoji.kaoyan.com/tjadm/6.html",
#        "http://ntiaoji.kaoyan.com/tjadm/7.html"
#	]
#
#	for url in test_urls :
#	    print url
#	    time.sleep(2)
#	    self.headers['Referer'] = url
#            yield FormRequest.from_response(response,
#	        headers = self.headers,
#	        formdata = {
#	        'username' : 'kytj1',
#	        'password' : '6ujBJ4XQyLeGmJmB'
#	        },
#	        callback = self.download_page,
#	        dont_filter = True
#	    )
        return FormRequest.from_response(response,
	    headers = self.headers,
	    formdata = {
	        'username' : 'kytj1',
	        'password' : '6ujBJ4XQyLeGmJmB'
	    },
	    callback = self.after_login,
	    dont_filter = True
        )

    def after_login(self, response) :
        test_urls = [
        "http://ntiaoji.kaoyan.com/tjadm/1.html",
        "http://ntiaoji.kaoyan.com/tjadm/2.html"
        ]
	for num in range(2,2300) :
	    test_urls.append("http://ntiaoji.kaoyan.com/tjadm/" + str(num) + ".html")
	else :
	    print test_urls
	    time.sleep(0.2)

        for url in test_urls :
	    self.headers['Referer'] = url
            yield Request(url = url,
	    headers = self.headers,
	    method = "GET",
	    callback = self.convert_page
	    )

    def convert_page(self, response) :
        sel = Selector(response)
	#res = sel.xpath("//table[@class='tiaoji-tab']/tr/td/text()").extract()
	res = sel.xpath("//table[@class='tiaoji-tab']/tr").extract()
        #print res
        filename = response.url.split("/")[-2]+response.url.split("/")[-1]
	with open(filename, 'wb') as f :
	    for content in res :
	        f.write(content.encode('utf-8'))
	    f.close()

    def download_page(self, response) :
        filename = response.url.split("/")[-2]+response.url.split("/")[-1]
        print self.headers['Referer'],response.url
	open(filename, 'wb').write(response.body)
