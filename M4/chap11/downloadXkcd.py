import webbrowser, sys, pyperclip, requests, bs4

xkcdhome = 'http://xkcd.com/'

xkcd = requests.get(xkcdhome)

try:
	xkcd.raise_for_status()
except Exception as exc:
	print ('Ocorreu um erro: %s' %(exc))

xkcdSoup = bs4.BeautifulSoup(xkcd.text,"lxml")
xkcdElem = xkcdSoup.select('#comic img')

#ta dando erro pq tem // antes do url da imagem
image = requests.get(xkcdElem[0].get('src'))

try:
	image.raise_for_status()
except Exception as exc:
	print ('Ocorreu um erro: %s' %(exc))

imageFile = open('Comic 1.png','wb')
for chunk in imageFile.iter_content(100000):
	imageFile.write(chunk)

imageFile.close()

