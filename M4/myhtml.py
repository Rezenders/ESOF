import requests, bs4
print ('------------------------------------')

#~ res = requests.get('http://nostarch.com')

#~ try:
	#~ res.raise_for_status()
	
#~ except Exception as exc:
	#~ print('There was a problem: %s' % (exc))
	
#~ noStarchSoup = bs4.BeautifulSoup(res.text,"lxml")
#~ print (type(noStarchSoup))

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile,"lxml"	)
print (type(exampleSoup))

elems = exampleSoup.select('#author')
print (type(elems))
print (len(elems))
print (type(elems[0]))
print (elems[0].getText())
print (str(elems[0]))
print (elems[0].attrs)
