# encoding: utf-8
import sys

import requests, json
from requests.adapters import HTTPAdapter

reload(sys)
sys.setdefaultencoding('utf-8')


def getZnFromApi(en):
    """
    翻译接口调用
    :param en:
    :return:
    """
    print en
    url = 'http://localhost:1262/trans'
    data = json.dumps({"src": en, "domain": "metadata"})
    s = requests.Session()
    r = s.post(url, data)
    ss = json.loads(r.text, encoding="utf-8")
    fr = ss['exception']
    rs = ss['result']
    print("from %s result %s" % (fr, rs))
    s.close()
    if fr:
        return rs
    else:
        return en

