# 难点：找接口
# https://20.climaxfun.pw/forum-68-1.html
# https://20.climaxfun.pw/forum-68-2.html
# https://20.climaxfun.pw/forum-68-3.html

# 下载豆瓣电影前十页的数据
# （1）请求对象的定制
# （2）获取响应的数据
# （3）下载数据
import urllib.parse
import urllib.request
import pandas as pd

#from lib2to3.fixes.fix_input import context


def get_url(page):
    # url1 = 'https://20.climaxfun.pw/forum-68-'
    # page = str(page)
    # url2 = '.html'
    # url = url1+page+url2
    base_url = 'https://20.climaxfun.pw/forum-68-'
    tail_url = '.html'
    page = str(page)
    return base_url + page + tail_url

def create_request(page):

    url = get_url(page)
    # print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_content(request):
    # 模拟浏览器向服务器发送请求
    response = urllib.request.urlopen(request)
    # 获取响应中的页面源码
    # read返回是二进制数据
    # 二进制-->字符串 解码 decode()
    content = response.read().decode('utf_8')
    print(content)
    return content

from lxml import etree

def get_AV_data(content):
    # 解析网址 ，获取网页内容
    tree = etree.HTML(content)
    list = tree.xpath('//a[@class="s xst"]')
    data = {'Name': ['苍井空'],
            'Number': ['ONSD—783'],
            'Content': ['ONSD—783 そら—蒼井そら写真集']}

    append_data = {'Name': '苍井空', 'Number': 'SONE-888', 'Content': '3'}

    # 创建 DataFrame 对象
    df = pd.DataFrame(data)

    for i in list:
        append_data['Content'] = i.text
        append_df = pd.DataFrame([append_data])
        df = pd.concat([df, append_df], ignore_index=True)
        # print(i.text)
    return df

def write_excel_list(df, page):
    # 写入 excel 至指定位置（若文件已存在，则覆盖）
    base_path = r'./excel/AVLIST_'
    tail_path = '.xlsx'
    page = str(page)
    FILE_PATH = base_path + page + tail_path
    df.to_excel(FILE_PATH)

# 程序入口
if __name__ == '__main__':
    #start_page = int(input('请输入起始页码：'))
    #end_page = int(input('请输入终止页码：'))

    request = create_request(2)
    content = get_content(request)
    df = get_AV_data(content)
    write_excel_list(df, 2)



