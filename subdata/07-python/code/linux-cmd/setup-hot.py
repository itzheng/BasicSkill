import requests
from bs4 import BeautifulSoup
import json
from time import sleep
import os
# 需要转成md
import html2text

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
               'Referer':'https://wangchujiang.com/linux-command/hot.html',
                'sec-ch-ua':'"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"'
                }

# 获取所有的命令列表
def getAllCmd():
    url = 'https://wangchujiang.com/linux-command/js/dt.js?v=1626403178815'
    #Referer: https://wangchujiang.com/linux-command/hot.html
    #sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
    #sec-ch-ua-mobile: ?0
    print (headers)
    r = requests.get(url,headers=headers)
    print('code : ',r.status_code)
    text = r.text
    print ('text len : ',len(text))
    #得到js文件 var linux_commands=[{"n":"a......"}]
    index = text.index('[')
    json_text = text[index:len(text)]
    #print(json_text)
    linux_commands = json.loads(json_text)
    #  "n": "ed", "p": "/ed", "d": "单行纯文本编辑器"
    print ('linux_commands len ',len(linux_commands))
    return linux_commands

#保存到哪个目录
dir = 'hot-cmds'
# 获取单个命令的信息，将保持到 命令.md文件
def getCmdInfoMd(cmd):
    url = 'https://wangchujiang.com/linux-command/c/{0}.html'.format(cmd)
    print(url)
    r = requests.get(url,headers=headers)
    print('code : ',r.status_code)
    html = r.text
    print ('text len : ',len(html))
    bfSoup = BeautifulSoup(html,features="html.parser")
    body = bfSoup.find_all('div', class_ = 'markdown-body')
    t_bf =BeautifulSoup(str(body[0]),features="html.parser")
    #<span class="edit_btn">
    t_bf.span.clear()
    #print(t_bf)
    # 创建 cmds 目录
    if not os.path.exists(dir):
        os.makedirs(dir)
    fo = open('{1}//{0}.md'.format(cmd,dir), "a+",encoding="utf-8")
    # 获取 html 源码，github 不能显示 html，还是要想办法做出 md ,开源是伟大的 html2text
    html_text = t_bf.prettify()
    #fo.write(html_text)
    md_text = html2text.html2text(html_text)
    fo.write(md_text)        
    #保存数据
    fo.flush()
    fo.close()

import progress
#开始执行
def run():
    linux_commands = getAllCmd()
    #每条数据都要保存到 md
    fo = open('hot-cmds.md', "a+",encoding="utf-8")
    start_index = progress.get_progress()
    for cmd in linux_commands[start_index:]:
        #print(cmd['n']+' '+cmd['p']+' '+cmd['d'])
        # ed  - 单行纯文本编辑器
        #睡眠1秒，这服务器经常卡死
        sleep(1)
        getCmdInfoMd(cmd['n'])
        fo.write('* [{0} - {1}]({2}//{0}.md)'.format(cmd['n'],cmd['d'],dir))
        fo.write('\n')
        fo.flush()
        start_index +=1
        progress.save_progress(start_index)
        
    #保存数据
    fo.close()    

# 调用执行代码
run()
