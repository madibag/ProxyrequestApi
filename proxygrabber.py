#the request part

from requests_html import HTMLSession
#import script
import time



def make_request(url):
	session = HTMLSession()
	r = session.get(url)
	r.html.render()
	co = (r.html)
	return co


'''
url = input('Paste the url Here: ')
make_request(url)
'''
