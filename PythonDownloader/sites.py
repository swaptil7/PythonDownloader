from html.parser import HTMLParser
import requests
import sys

parent_url = "https://www.tutorialspoint.com/"

class ViewSites(HTMLParser):

	def geturl(self,url):
		if(url.find("https") == 0 or url.find("http") == 0):
			r = requests.get(url)
		else:
			r = requests.get("https://"+url)
		self.feed(r.text)

	def handle_starttag(self,tag,attr):
		if(tag=="a"):
			(href,link)=attr[0]
			link=parent_url + link
			self.links.append(link)
			link = ""

	def __init__(self,url):
		HTMLParser.__init__(self)
		self.links = []             #Target urls
		self.geturl(url)
		#print(self.links[0])

	def handle_lis(self,a):
		return a[1]

	def getjson(self):
		return data
		

# def main():
# 	obj = ViewSites(sys.argv[1])
# 	print(links)
# main()