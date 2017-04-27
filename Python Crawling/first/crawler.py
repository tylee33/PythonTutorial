import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter


maximum_tries = 2
seed_url = "http://virtual-labs.ac.in/index.php/"
links_crawled = []
links_tocrawl = [seed_url]
links_broken = []
links_unvalid = ["javascript", "png", "jpeg", "jpg", "gif", "deb", "exe", "facebook", "linkedin", "ieee", "twitter.com"]
not_valid_url = 0

crawled_unvalid_links = []

session = requests.Session()
session.mount('http://', HTTPAdapter(max_retries=maximum_tries))



def getLink(page):
	href_index = page.find( '<a href=' )
	
	if href_index != -1:
		start_quote = page.find('"', href_index + 1)
		end_quote = page.find('"', start_quote + 1)
		url = page[start_quote + 1:end_quote]
		return url, end_quote
	else:
		return -1, -1

for url in links_tocrawl:
	print "Crawling URL", url
	
	# If link is broken then try for maximum number of times, and throw an exception. And move to next url is links_tocrawl list
	try:
		req = requests.get(url)
	except requests.exceptions.ConnectionError, e:
		links_broken.append(url)
		print "Maximum retires exceeded for", url
		links_tocrawl.pop(0)
		continue
	except requests.exceptions.TooManyRedirects, e:
		print "Too many redirects therefore continuing to next link"
		continue

	page = str(BeautifulSoup(req.content))
	link, end_quote = getLink(page)
	while link!=-1:		
		page = page[end_quote:]
		for non in links_unvalid:
			if non in link:
				not_valid_url = 1
				break
		if (not_valid_url == 1):
			not_valid_url = 0
			pass
		#if ("javascript" in link or "jpg" in link or "png" in link or "jpeg" in link):
		#	pass
		else:
			if ('http://' not in link and 'https://' not in link):
				link = url + link

			link = link.strip(' /') + '/'
			if link in links_tocrawl or link in links_crawled:
				pass
			else:
				links_tocrawl.append(link)
		link, end_quote = getLink(page)
	links_crawled.append(url)
	links_tocrawl.pop(0)
	#print "Tocrawl", len(links_tocrawl)
	#print "Crawled", len(links_crawled)

f1 = open('virtualtocrawl', 'w')
f2 = open('virtualcrawled', 'w')

for link in links_tocrawl:
	f1.write(link)
	f1.write('\n')

for link in links_crawled:
	f2.write(link)
	f2.write('\n')


f1.close()
f2.close()
#print "Tocrawl", links_tocrawl
#print "Crawled", links_crawled
#print "Broken link", links_broken
#print "Crawled unvalid links", crawled_unvalid_links
