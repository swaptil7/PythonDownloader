import requests 	
import sys
import os
import errno

class Downloader():

	counter = 0
	duplicates = {}

	def __init__(self,url,**kwargs):
		#######Required args########
		self.attrlist = ["filetype","location"]		
		self.url = url
		self.content = ""
		self.filename = ""
		self.location = ""
		self.filetype = ""
		########OPTIONAL############
		for i in kwargs:
			if not(i in self.attrlist):
				print("Invalid Argument:"+i)

		if("filetype" in kwargs):
			self.filetype = kwargs["filetype"]

		if("location" in kwargs):
			self.location = kwargs["location"]

		self.design_url()
		self.extract_filename()
		self.download()

	def design_url(self):
		if not("http" in self.url or "https" in self.url):
			self.url = "http://" + self.url

	def extract_filename(self):
		filename = self.url.split("/")
		self.filename=filename[len(filename)-1].split("?")[0]

	def download(self):
		if(self.filetype == ""):
			r = requests.get(self.url)
			self.content = r.content
			self.storeit()

		if(self.filetype in self.filename):
			r = requests.get(self.url)
			self.content = r.content
			self.storeit()

		print(str(Downloader.counter)+")"+"downloading...:"+self.filename+" "+self.location)

		Downloader.counter+=1

	def storeit(self):
		try:
			with open(self.location+self.filename,"x+b") as f:
				f.write(self.content)
		except OSError as e:
			if(e.errno == errno.EEXIST):
				if(self.filename in Downloader.duplicates):
					Downloader.duplicates[self.filename]+=1
					copy=Downloader.duplicates[self.filename]
					with open(self.location+self.filename.rstrip(self.filetype)+"_"+str(copy)+self.filetype,"x+b") as f:
						f.write(self.content)
				else:
					Downloader.duplicates[self.filename] = 0
					with open(self.location+self.filename.rstrip(self.filetype)+"_"+str(0)+self.filetype,"x+b") as f:
						f.write(self.content)

def main():
	url = sys.argv[1]
	obj = Downloader(url,location="Downloaded/")

main()