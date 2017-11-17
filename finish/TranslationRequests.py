import requests, json


def getZnFromApi(en):
    url = 'http://47.94.148.72:1262/trans'
    data = json.dumps({"src": en, "domain": "metadata"})
    r = requests.post(url, data)
    ss = json.loads(r.text, encoding="utf-8")
    if ss['exception']:
        return en
    else:
        return ss['result']
