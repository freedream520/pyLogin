from Zhengfang import *
zhengfang = Zhengfang()
zhengfang.Login('3100203102','')
html = zhengfang.Fetch('http://jiaowu1.fjut.edu.cn/xs_main.aspx?xh=3100203102')
file = open('zhengfang.html','w')
file.write(html)
