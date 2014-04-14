#coding=UTF-8

import urllib2
import urllib
import cookielib
import re
def findrand(html):
	pattern = re.compile(r'rand=\d+')
	match = pattern.search(html)
	return match.group().replace('rand=','')
def findpasswd(html):
	pattern = re.compile(r'password_\d+')
	match = pattern.search(html)
	return match.group()
def findvk(html):
	pattern = re.compile(r'name\=\"vk\" value=\"(\w)+')
	match = pattern.search(html)
	print match.group()
	return match.group().replace('name="vk" value="','')
class Weibo:
	def __init__(self):
		self.loginUrl = 'http://login.weibo.cn/login/'
		self.cookie = cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie)) # Login
		self.loginHttpHead = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'UTF-8,*;q=0.5',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36', 
			'Content-Type': 'application/x-www-form-urlencoded',
			'Connection': 'keep-alive',
			'HOST': 'login.weibo.cn',
			'Origin':  'http://login.weibo.cn',
			'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F%3Fs2w%3Dlogin&backTitle=%CE%A2%B2%A9&vt=4'}
	def Login(self,account,password):
		login_request = urllib2.Request(self.loginUrl, '', self.loginHttpHead )
		html = self.opener.open(login_request).read()
		randStr = findrand(html)
		passwordStr = findpasswd(html)
		vkStr = findvk(html)
		print randStr
		print passwordStr
		print vkStr
		postdata = urllib.urlencode({'mobile': account,  
									 passwordStr: password,  
									 'remember': 'on',  
									 'backURL': 'http://weibo.cn/',  
									 'backTitle': '新浪微博',  
									 'vk': vkStr,  
									 'submit': '登录',  
									 'encoding': 'utf-8'})  
		loginUrl2 = 'http://login.weibo.cn/login/?rand='+randStr+'&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%D0%C2%C0%CB%CE%A2%B2%A9&vt=4&revalid=2&ns=1'
		login_request = urllib2.Request(loginUrl2, postdata, self.loginHttpHead )
		html = self.opener.open(login_request,postdata).read()
		# print html.decode('UTF-8')
		# httpHead2 = {
					# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					# 'Accept-Charset': 'UTF-8,*;q=0.5',
					# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36', 
					# 'Content-Type': 'application/x-www-form-urlencoded',
					# 'Connection': 'keep-alive'}
		# login_request = urllib2.Request('http://weibo.cn/buaichiyu',urllib.urlencode({}),httpHead2 )
		# html = self.opener.open(login_request).read()
		# print html
		# file = open('weibo.html','w')
		# file.write(html)
		
	def Fetch(self,url):
		httpHead2 = {
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Charset': 'UTF-8,*;q=0.5',
				'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36', 
				'Content-Type': 'application/x-www-form-urlencoded',
				'Connection': 'keep-alive'}
		login_request = urllib2.Request(url,urllib.urlencode({}),httpHead2 )
		html = self.opener.open(login_request).read()
		return html

