#使用urllib获取seclimax首页源码
import urllib.request

import pandas as pd

#(1)定义一个url
#url = 'https://20.climaxfun.pw/forum.php'
url = 'https://20.climaxfun.pw/forum-68-1.html'
#url = 'https://20.climaxfun.pw/'
#url = 'http://www.baidu.com'


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}


request = urllib.request.Request(url=url, headers=headers)

#(2)模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

#(3)获取响应中的页面源码
#read返回是二进制数据
#二进制-->字符串 解码 decode()
content = response.read().decode('utf-8')

#(4)打印内容
print(content)

from lxml import etree
#from lxml import html

#解析网址 ，获取网页内容

#tree = etree.fromstring(content)
tree = etree.HTML(content)
#tree = html.fromstring(content)

list = tree.xpath('//a[@class="s xst"]')

data = {'Name': ['河北彩伽', '三上悠亜', '吉高寧々'],
        'Number': ['SONE-001', 'SONE-002', 'FSDSS-001'],
        'Content': ['SONE-308 美脚下半身が大絶頂するまで[媚薬?巨根]ピストンを欲しがるデカチンキメセク大好き脚長スケベお姉さん 楓ふうあ', '姉がメンズエステのバイトを始めたんだが、僕の体で際どいマッサージの練習をしてきてヤバい！ 黒島玲衣', 'AV制作アシスタントに密着 パワハラ上司やセクハラ男優の無茶振りにも健気に働く女性AD 吉高寧々']}

append_data = {'Name': '苍井空', 'Number': 'SONE-888', 'Content': '3'}

# 创建 DataFrame 对象
df = pd.DataFrame(data)

for i in list:
    append_data['Content'] = i.text
    append_df = pd.DataFrame([append_data])
    df = pd.concat([df, append_df], ignore_index=True)
    #print(i.text)

# 写入 excel 至指定位置（若文件已存在，则覆盖）
FILE_PATH = r'./搞定数据哈哈.xlsx'
df.to_excel(FILE_PATH)

