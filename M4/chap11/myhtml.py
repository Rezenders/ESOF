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


pElemes = exampleSoup.select('p')
print ('\npelems 0 ------')
print (len(pElemes))
print (str(pElemes[0]))
print (pElemes[0].getText())
print ('\npelems 1------')
#~ print (str(pElemes[1]))
print (pElemes[1].getText())
print ('\npelems 2------')
#~ print (str(pElemes[2]))
print (pElemes[2].getText())

spanElem = exampleSoup.select('span')[0]
print (str(spanElem))
print (spanElem.get('id'))
print (spanElem.get('coco')==None)
print (spanElem.attrs)

