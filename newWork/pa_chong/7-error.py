'''
URLError/HTTPError
    这两个类都在 urllib.error 里面
    NameError TypeError FileNotFound    异常
    异常处理结构：
        try-except

    URLError :
        (1) 没有网
        (2) 服务器连接失败
        (3) 找不到指定的服务器
    HTTPError:
        是URLError的子类
        【注】俩个同时捕获时，需要先捕获URLError
'''