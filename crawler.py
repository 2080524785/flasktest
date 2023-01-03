import json
import time

from urllib.parse import quote

import requests as requests


def crawler_page(key, pages):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
    }

    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=12029402755642622111&ipn=rj&ct=201326592&is=&fp=result&fr=&word={}&cg=wallpaper&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={}&1647499896405=".format(
        quote(key.encode('utf-8')), quote(key.encode('utf-8')), str(30 * pages))

    r = requests.get(url=url, headers=headers).text
    r1 = r.replace('\\', '\\\\')
    r2 = r.replace('，', ',')
    jsoninfo = json.loads(r2, strict=False)

    pic_sum_num = jsoninfo['displayNum']
    pic_ls = []
    for i in range(30):
        pic = {'url': jsoninfo['data'][i]['thumbURL'],
               'title': jsoninfo['data'][i]['fromPageTitleEnc']}
        pic_ls.append(pic)

    return pic_ls, pic_sum_num


def crawler_more(key):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
    }

    pic_url_ls = []
    # 默认最大为300张，10×30
    for pages in range(1, 11):
        url = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=12029402755642622111&ipn=rj&ct=201326592&is=&fp=result&fr=&word={}&cg=wallpaper&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={}&1647499896405=".format(
            quote(key.encode('utf-8')), quote(key.encode('utf-8')), str(30 * pages))

        r = requests.get(url=url, headers=headers).text
        r1 = r.replace('\\', '\\\\')
        r2 = r.replace('，', ',')
        jsoninfo = json.loads(r2, strict=False)

        for i in range(30):
            pic_url_ls.append(jsoninfo['data'][i]['thumbURL'])
    return pic_url_ls
