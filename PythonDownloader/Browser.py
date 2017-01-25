import requests 	
import sys
import os
import errno
from urllib.parse import urlparse
from urllib.parse import parse_qs
import shutil

class Downloader():

	counter = 0
	duplicates = {}

	def __init__(self,url,**kwargs):
		#######Required args########
		self.attrlist = ["filetype","location"]		
		self.url = url
		self.parsed_url = urlparse(self.url)
		self.content = ""
		self.filename = ""
		self.location = ""
		self.filetype = ""
		self.parameters = ""
		self.parameters_dic = {}
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

		if(self.parsed_url.scheme == ''):
			self.url = "http://" + self.url
			self.parsed_url = urlparse(self.url)

		if not(self.parsed_url.query == ''):
			self.parameters = self.parsed_url.query

	def extract_filename(self):
		filename = self.parsed_url.path.split("/")
		self.filename=filename[len(filename)-1]

	def download(self):

		if(self.filetype == ""):
			if(self.parameters == ""):
				r = requests.get(self.url,stream=True)
			else:
				r = requests.get(self.url,parse_qs(self.parameters),stream=True)

			self.content = r.content
			print(str(Downloader.counter)+")"+"downloading...:"+self.filename+" "+self.location)
			self.storeit()

			Downloader.counter+=1
			return r.status_code

		if(self.filetype in self.filename):

			if(self.parameters == ""):
				r = requests.get(self.url)
			else:
				r = requests.get(self.url,parse_qs(self.parameters))	

			self.content = r.content
			print(str(Downloader.counter)+")"+"downloading...:"+self.filename+" "+self.location)
			self.storeit()

			Downloader.counter+=1
			return r.status_code

	def storeit(self):

			try:
				with open(self.location+self.filename,"x+b") as f:
					f.write(self.content)
				print(successful)

			except OSError as e:
				if(e.errno == errno.EEXIST):
					print("file exists")

		# else:
		# 	count = 0
		# 	self.rename_rec(self.filename,count)

	# def rename_rec(self,fname,count):
	# 	fname = "copy_" + str(count) "." + fname
	# 	fname.replace(fname.split(".")[0],)
 
	# 	if not(os.path.isfile(bytes(self.location+fname,encoding="utf-8"))):
	# 		with open(self.location+fname,"x+b") as f:
	# 			f.write(self.content)

	# 	else:
	# 		count+=1
	# 		self.rename_rec(fname,count)

def main():
	url = sys.argv[1]
	obj = Downloader(url,location="Browser_Files/")
	#shutil.rmtree("Browser_Files")

main()
