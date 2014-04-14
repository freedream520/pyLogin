from Weibo import *
weibo = Weibo()
weibo.Login('547010823@qq.com','')
html = weibo.Fetch('http://weibo.cn/buaichiyu')
file = open('weibo.html','w')
file.write(html)
