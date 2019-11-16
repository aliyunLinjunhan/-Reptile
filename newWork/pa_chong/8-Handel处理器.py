'''
Handler 处理器、自定义Opener
    urlopen()   给一个url，发送请求，获取响应。
    Request()   定制请求头，创建请求对象
    高级功能：使用代理，cookie

    基本用法：见1代码


代理
    代理：及帮忙做的中介
        正向代理：代理客户端获取数据
        反向代理：代理服务端提供数据
    配置：
        浏览器配置
            右边三点==》 设置==》 高级==》代理 ==》局域网设置 ==》 为LAN使用代理==》 输入ip和端口号即可
        代码配置
        handler = urllib.request.ProxyHandler({'http': '114.215.95.188:3128'})
        //通过代理地址来创建handler
        后面使用


'''
# 1、Handler的基本用法
'''
import urllib.request
import urllib.parse

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}

# 创建一个handler
handler = urllib.request.HTTPHandler()
# 通过handler创建一个opener
# opener是一个对象，可以利用opener直接发送请求
opener = urllib.request.build_opener(handler)

# 构建请求对象
request = urllib.request.Request(url, headers=headers)
# 发送请求
response = opener.open(request)

print(response.read().decode())
'''
# 2、代理高级用法
'''
import urllib.request
import urllib.parse

# 通过代理的IP地址创建handler
handler = urllib.request.ProxyHandler({'http': '114.215.95.188:3128'})
# 常见opener
opener = urllib.request.build_opener(handler)

url = 'https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0xcdbe4c330001a013&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_' \
      'enter=1&oq=%25E8%258A%25B1%25E5%2588%25BA%25E4%25BB%25A3%25E7%2590%2586%25E9%25AA%258C%25E8%25AF%2581&input' \
      'T=1238&rsv_t=8eb6BXF148ag8vmsaZ3CuOANm3QvA42z7GawNIHYwu0GaXuOB531V20rNme0okakZFsw&rsv_pq=d23d080500020f17&rsv_sug3=' \
      '28&rsv_sug1=22&rsv_sug7=100&rsv_sug2=0&rsv_sug4=1238'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
}
request = urllib.request.Request(url, headers=headers)
response = opener.open(request)

print(response.read().decode())
with open('ip.html', 'w') as fp:
    fp.write(response.read().decode())
'''
# 3、