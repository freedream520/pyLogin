#coding=UTF-8
'''
chrome - developer - network - default2.aspx:  
  
  
  
  
Request Headersview source  
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8  
Accept-Encoding:gzip,deflate,sdch  
Accept-Language:zh-CN,zh;q=0.8  
Connection:keep-alive  
Content-Length:168 #不用  
Content-Type:application/x-www-form-urlencoded  
Cookie:ASP.NET_SessionId=ieyqyl55xo0qhbmrft0tby45#不用  
Host:jiaowu1.fjut.edu.cn  
Origin:http://jiaowu1.fjut.edu.cn  
Referer:http://jiaowu1.fjut.edu.cn/  
User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36  
Form Dataview parsed  
__VIEWSTATE=dDwtMTg3MTM5OTI5MTs7Pu5xIryuEtxI6h%2Bwy2%2F%2BGZCwQadM&TextBox1=***&TextBox2=***&TextBox3=***&RadioButtonList1=%D1%A7%C9%FA&Button1=&lbLanguage=<

'''
import urllib2
import cookielib
VIEWSTATE = ''#可为空
_xh = '3100203102'
_pw = '**'
loginUrl = 'http://jiaowu2.fjut.edu.cn/default2.aspx'
checkCodeUrl = "http://jiaowu2.fjut.edu.cn/CheckCode.aspx"
checkCodeFile = 'checkCode.jpg'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
photoUrl = 'http://jiaowu2.fjut.edu.cn/readimagexs.aspx?xh=%s'% _xh
photo = _xh +'.jpg' 
student_cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(student_cookie)) # Login
checkCodeImg = opener.open(checkCodeUrl).read()
fp = open(checkCodeFile, 'wb')
fp.write(checkCodeImg)
fp.close()
checkCode = raw_input('input code:')
data = '__VIEWSTATE='+VIEWSTATE+'&TextBox1='+_xh+'&TextBox2='+_pw+'&TextBox3='+checkCode+'&ddl_js=%D1%A7%C9%FA&Button1=+%B5%C7+%C2%BC+'
login_request = urllib2.Request(loginUrl, data, {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'UTF-8,*;q=0.5',
                    'User-Agent': USER_AGENT, 
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Connection': 'keep-alive',
                    'HOST': 'jiaowu2.fjut.edu.cn',
                    'Origin':  'http://jiaowu2.fjut.edu.cn',
                    'Referer': 'http://jiaowu2.fjut.edu.cn/default2.aspx'})
opener.open(login_request, data)
photoBin = opener.open(photoUrl).read()
fp = open(photo, 'wb')
fp.write(photoBin)
fp.close()
