import sys, urllib,json
import urllib.request
import urllib.parse
import base64


url = 'http://apis.baidu.com/apistore/idlocr/ocr'

data = {}
data['fromdevice'] = "pc"
data['clientip'] = "121.8.210.40"
data['detecttype'] = "LocateRecognize"
data['languagetype'] = "CHN_ENG"
data['imagetype'] = "1"

# 读取图片
file = open('0.jpg', 'rb')
image = file.read()
file.close()

data['image'] = base64.b64encode(image)
decoded_data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data=decoded_data)

req.add_header("Content-Type", "application/x-www-form-urlencoded")
req.add_header("npQm5T7oh7jicQeT92YvmIYR", "GsGgl8ev8iwDoRbEz5BAvRpkbmMe256k")

resp = urllib.request.urlopen(req)
content = resp.read()
if (content):
    print(content)