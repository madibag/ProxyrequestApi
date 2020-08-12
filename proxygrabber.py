#the request part

from requests_html import HTMLSession
import script
import random
import json
import time

pr_url = json.loads('proxy.json')

def make_request(url):
	session = HTMLSession()
	leng = len(pr_url['data'])
	rand = random.randint(0, leng)
	proxy = pr_url['data'][rand]
	r = session.get(url, proxies={'http' : proxy , 'https' : proxy})
	r.html.render()
	co = (r.html)
	return co


'''
url = input('Paste the url Here: ')
make_request(url)
'''