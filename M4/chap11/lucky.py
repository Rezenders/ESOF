import webbrowser, sys, pyperclip, requests, bs4

if len(sys.argv)>1:
	address =' '.join(sys.argv[1:])	
else:
	address = pyperclip.paste()
googleprefix = 'https://www.google.com/search?q='
google = requests.get(googleprefix + address)

try:
	google.raise_for_status()
except Exception as exc:
	print ('There was a problem: %s' %(exc))
	
googleSoup = bs4.BeautifulSoup(google.text,"lxml")

googleElem = googleSoup.select('h3.r a')

#~ webbrowser.open( googleprefix + address)
numTab = min(5, len(googleElem))
for num in range(numTab):
	webbrowser.open('https://www.google.com' +googleElem[num].get('href'))
