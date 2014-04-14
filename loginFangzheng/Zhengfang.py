#coding=UTF-8

import urllib2
import urllib
import cookielib

class Zhengfang:
	def __init__(self):
		self.loginUrl = 'http://jiaowu1.fjut.edu.cn/default2.aspx'
		self.cookie = cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie)) # Login
		self.loginHttpHead = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'UTF-8,*;q=0.5',
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0', 
			'Content-Type': 'application/x-www-form-urlencoded',
			'Connection': 'keep-alive',
			'HOST': 'jiaowu1.fjut.edu.cn',
			'Referer': 'http://jiaowu1.fjut.edu.cn/default2.aspx'}
	def Login(self,account,password):
		checkCodeImg = self.opener.open('http://jiaowu1.fjut.edu.cn/CheckCode.aspx').read()
		checkcodefile = open('checkcode.jpg','wb')
		checkcodefile.write(checkCodeImg)
		checkcodefile.close()
		checkCode = raw_input('input code:')
		postdata = urllib.urlencode({'__VIEWSTATE':'dDwyODE2NTM0OTg7Oz69ub+LCDf8lWoGiSlCT4WB8War1g==',  
									 'txtUserName': '3100203102',  
									 'TextBox2':'Lbb060115',  
									 'txtSecretCode': checkCode,  
									 'RadioButtonList1': '学生',  
									 'Button1':'',  
									 'lbLanguage':'', 
									 'hidPdrs':'',
									 'hidsc':''})  
		loginUrl2 = 'http://jiaowu1.fjut.edu.cn/default2.aspx'
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

