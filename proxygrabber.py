#the request part

from requests_html import HTMLSession
#import script
import random
import json
import time



def make_request(url):
	re = open('proxy.json', 'r').read()
	pr_url = json.loads(re)
	#
	
	session = HTMLSession()
	leng = len(pr_url['data'])
	rand = random.randint(1, leng)
	proxy = pr_url['data'][rand]
	r = session.get(url)
	r.html.render()
	co = (r.html)
	return co


'''
url = input('Paste the url Here: ')
make_request(url)
'''
