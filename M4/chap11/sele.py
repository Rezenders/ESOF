from selenium import webdriver

browser = webdriver.Firefox()
print (type(browser))

browser.get('http://inventwithpython.com')
