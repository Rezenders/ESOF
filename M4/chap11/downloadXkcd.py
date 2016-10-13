import webbrowser, sys, pyperclip, requests, bs4

xkcdurl = 'http://xkcd.com/'
i =1
while(True):
	print (i)
	xkcd = requests.get(xkcdurl)

	try:
		xkcd.raise_for_status()
	except Exception as exc:
		print ('Ocorreu um erro: %s' %(exc))

	xkcdSoup = bs4.BeautifulSoup(xkcd.text,"lxml")
	xkcdElem = xkcdSoup.select('#comic img')

	if xkcdElem == []:
		print('Could not find comic image.')
	else:
		image = requests.get('http:' + xkcdElem[0].get('src'))

		try:
			image.raise_for_status()
		except Exception as exc:
			print ('Ocorreu um erro: %s' %(exc))

		imageFile = open('img/Comic'+str(i)+ '.png','wb')

		for chunk in image.iter_content(100000):
			imageFile.write(chunk)

		imageFile.close()

	prevLink = xkcdSoup.select('a[rel="prev"] ')[0]
	xkcdurl = 'http://xkcd.com' + prevLink.get('href')
	i = i +1
	if(prevLink.get('href')=='#'):
		break
	

	
