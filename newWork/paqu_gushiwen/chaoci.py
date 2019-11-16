import requests
import re
import time

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}

i = 0
for line in open("pictures_url.txt"):
    print(line)
    pattren = re.compile('"url":"(.*?)"')
    url = pattren.findall(line)[0]
    content = requests.get(url, headers=header).content
    print(url)
    name = str(r'caoci2/' + str(i) + '.jpg')
    with open(name, 'wb') as fp:
        fp.write(content)
    time.sleep(1.2)
    i = i + 1






