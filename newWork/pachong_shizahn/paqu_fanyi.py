import requests
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
}

formdata = {
    'kw': 'computer'
}

r = requests.post(url, headers=headers, params = formdata)
r.encoding = 'utf-8'
print(r.json())