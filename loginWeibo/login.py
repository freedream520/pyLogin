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
	
loginUrl = 'http://login.weibo.cn/login/'
baidu = 'http://www.baidu.com'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'

student_cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(student_cookie)) # Login
#html = opener.open(loginUrl).read()
#print html
#findrand(html)

password=''
data=''
httpHead = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'UTF-8,*;q=0.5',
			'User-Agent': USER_AGENT, 
			'Content-Type': 'application/x-www-form-urlencoded',
			'Connection': 'keep-alive',
			'HOST': 'login.weibo.cn',
			'Origin':  'http://login.weibo.cn',
			'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F%3Fs2w%3Dlogin&backTitle=%CE%A2%B2%A9&vt=4'}
login_request = urllib2.Request(loginUrl, data,httpHead )
html = opener.open(login_request).read()
randStr = findrand(html)
passwordStr = findpasswd(html)
vkStr = findvk(html)
print randStr
print passwordStr
print vkStr
postdata = urllib.urlencode({'mobile': '547010823@qq.com',  
							 passwordStr: '',  
							 'remember': 'on',  
							 'backURL': 'http://weibo.cn/',  
							 'backTitle': '新浪微博',  
							 'vk': vkStr,  
							 'submit': '登录',  
							 'encoding': 'utf-8'})  
loginUrl = 'http://login.weibo.cn/login/?rand='+randStr+'&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%D0%C2%C0%CB%CE%A2%B2%A9&vt=4&revalid=2&ns=1'
login_request = urllib2.Request(loginUrl, postdata,httpHead )
html = opener.open(login_request,postdata).read()
print html.decode('UTF-8')
httpHead2 = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'UTF-8,*;q=0.5',
			'User-Agent': USER_AGENT, 
			'Content-Type': 'application/x-www-form-urlencoded',
			'Connection': 'keep-alive'}
#opener.open(login_request, data)
login_request = urllib2.Request('http://weibo.cn/buaichiyu',urllib.urlencode({}),httpHead2 )
html = opener.open(login_request).read()
print html
file = open('weibo.html','w')
file.write(html)
