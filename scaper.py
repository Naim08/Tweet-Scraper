import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import math
import random

def constantTimer(min, max):
	return math.floor(random.randint(min,max)) + min
#change directory accordingly. Also make sure the right driver is being used
browser = webdriver.PhantomJS('/Users/Naim/Desktop/finanicalprogramming/scrapetweets/phantomjs-2.1.1-macosx/bin/phantomjs')
query = u'remicade'
base_url = u'https://twitter.com/search?f=tweets&vertical=news&q='+ query +'&src=typd'
url = base_url + query

browser.get(url)

body = browser.find_element_by_tag_name('body')

lastHeight = browser.execute_script("return document.body.scrollHeight")

for _ in range(3):
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	timer = constantTimer(1,3)
	print timer
	time.sleep(timer)
	newHeight = browser.execute_script("return document.body.scrollHeight")
	print newHeight
	if newHeight == lastHeight:
		break
	lastHeight = newHeight

tweets = browser.find_elements_by_class_name('tweet-text')

for tweet in tweets:
	print(tweet.text)

browser.quit()