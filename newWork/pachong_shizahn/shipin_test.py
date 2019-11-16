import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}

url = 'http://v3-default.ixigua.com/822c7345ec9d47b46a1c679dbcceffc2/5ca8eb06/video/m/220e12a763ce20d418791a62d633c74d9521161739820000b4be414c6d9f/?rc=M200OnE0NHg4azMzaDczM0ApQHRAbzc4NDs4MzUzMzYzMzMzNDVvQGgzdSlAZjN1KWRzcmd5a3VyZ3lybHh3Zjc2QDA2L2hzZWVhaV8tLV4tL3NzLW8jbyMxLjUtNC0tLi0vLjQxNi06I28jOmEtcSM6YHZpXGJmK2BeYmYrXnFsOiMzLl4%3D&vfrom=xgplayer'
r = requests.get(url, headers=headers)

with open('jiepai.mp4', 'wb') as fp:
    fp.write(r.content)
