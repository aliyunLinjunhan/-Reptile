import urllib.parse
import urllib.request

'''
url只能由特定的字符组成，字母，数字，下划线
如果出现其他的，比如 $ 空格 中文等就要对其进行编码

    
'''

url = 'https://i.meizitu.net/2013/06/2013061932375wdkimqcyej.jpg'

# ret_url = urllib.parse.quote(url)
# urllib.request.urlretrieve(ret_url, 'chun2.jpg')
#
# print(ret_url)

data={
    "name" : "林俊涵",
    "sex"  : "nan",
    "age"  : 20 ,

}
ret_url = urllib.parse.urlencode(data)
ret_url = url.__add__(ret_url)
print(ret_url)