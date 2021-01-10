#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import json
import requests
import re
import sys
import os
import getopt


# def decrypt(crypt_text):
#     with open('private.pem', 'rb') as privatefile:
#         p = privatefile.read()
#     privkey = rsa.PrivateKey.load_pkcs1(p)
#     # 注意，这里如果结果是bytes类型，就需要进行decode()转化为str
#     lase_text = rsa.decrypt(bytes.fromhex(crypt_text), privkey).decode()
#     return lase_text


def getAccount(argv):
    username = ''
    password = ''
    try:
        opts, args = getopt.getopt(
            argv, 'u:p:', ['username=', 'password='])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, val in opts:
        if(opt in ('-u', '--username')):
            username = val
        elif(opt in ('-p', '--password')):
            password = val
    return(username, password)


username, password = getAccount(sys.argv[1:])
if os.path.exists("NOSUBMIT"):
    exit()


data = {}

with open("./data.json", "r") as fd:
    data = json.load(fd)

conn = requests.Session()

# Login
# github action set up these arguments
result = conn.post('https://xxcapp.xidian.edu.cn/uc/wap/login/check',
                   data={'username': username, 'password': password})
if result.status_code != 200:
    print('认证失败')
    exit()

# Get previous info submitted
result = conn.get('https://xxcapp.xidian.edu.cn/ncov/wap/default/index')
if result.status_code != 200:
    print('获取页面失败')
    exit()

# if os.path.exists("last_get.html"):
#     os.rename("last_get.html", "last_get.html.1")
with open("last_get.html", "w") as fd:
    fd.write(result.text)

# TODO: diff those two files to determine whether submission form has been updated, then delay the submission when necessary
# get info and deserialize to a python object  from the last_get.html
predef = json.loads(re.search('var def = ({.*});', result.text).group(1))
if "dump_geo" in sys.argv:
    print(predef['geo_api_info'])
    exit()

try:
    del predef['_u']
    del predef['_p']
    del predef['jrdqtlqk']
    del predef['jrdqjcqk']
except:
    print("sensitive info doesn`t exit")
    pass
predef.update(data)

result = conn.post(
    'https://xxcapp.xidian.edu.cn/ncov/wap/default/save', data=predef)
print("疫情通提交结果："+result.text)

# 晨午检
data = {}
with open("data_3chk.json", "r") as fd:
    data = json.load(fd)
result = conn.post(
    'https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save', data=data)
print("晨午晚检提交结果"+result.text)
