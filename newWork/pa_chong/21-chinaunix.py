import urllib.request
import urllib.parse

url = 'http://account.chinaunix.net/login/login'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36'
}

formdata = {
	'username':'15521093428',
	'password':'72564016ljh0906',
	'geetest_challenge':'0c899d229c260c22dff5d49da9b436c2',
	'geetest_validate':'eae2aca2fa7c9052e6547ceda9928ccc',
	'geetest_seccode':'eae2aca2fa7c9052e6547ceda9928ccc%7Cjordan',
	'_token':'KSOrZ8sot2Blzln8ZemWr1KWz5I9RYxTm0ebDDdO',
	'_t':'1549547460711',
}

formdata = urllib.parse.urlencode(formdata).encode()
request = urllib.request.Request(url = url, headers=headers)

response = urllib.request.urlopen(request, data = formdata)
print(response.read().decode())
