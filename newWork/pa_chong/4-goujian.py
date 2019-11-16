import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'http://www.baidu.com/'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                   ' Chrome/69.0.3497.100 Safari/537.36',
}

ret_url = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(ret_url)

print(response)
