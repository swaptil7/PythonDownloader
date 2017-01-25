import SimpleDownloader
import sites

url = "https://www.tutorialspoint.com/java/java_networking.htm"

obj1 = sites.ViewSites(url)

# print(obj1.links)

for i in obj1.links:
	obj = SimpleDownloader.Downloader(i,location="Downloaded/",filetype=".htm")