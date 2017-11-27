# encoding: utf-8
import time

import json
import requests


def getZnFromApi(url, en, num_retries=3):
    """
    调用翻译接口
    :param url:
    :param en:
    :param num_retries:
    :return:
    """
    data = json.dumps({"src": en, "domain": "metadata"})
    try:
        s = requests.Session()
        r = s.post(url, data)
        r.raise_for_status()
        ss = json.loads(r.text, encoding="utf-8")
    except requests.HTTPError as e:
        if num_retries > 0:
            # 如果不是200就重试，每次递减重试次数
            return getZnFromApi(url, en, num_retries - 1)
    except requests.exceptions.ConnectionError as e:
        return
    if ss['exception']:
        return ss['result']
    else:
        return en


if __name__ == '__main__':
    print getZnFromApi('http://47.94.148.72:1262/trans','test')
