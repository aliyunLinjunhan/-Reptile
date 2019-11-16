'''
bs4：
    BeautifulSoup
    需要将pip源设置为国内源，阿里源，豆瓣源，网易源等等
    windows:
        （1）打开文件资源管理器
        （2）在地址栏上面输入 %appdata%
        （3）在这里面新建一个文件夹 pip
        （4）在pip文件夹里面新建一个文件叫做 pip.ini
            ，内容如下：
            [global]
            timeout = 6000
            index-url=https://mirrors.aliyun.com/pypi/simple/
            trusted-host=mirrors.aliyun.com
    linux:
        (1) cd ~
        (2) mkdir ~/.pip
        (3) vi ~/.pip/pip.conf
        (4) 编辑内容一样

    需要安装：pip install bs4
        bs4在使用时需要安装一个库 pip install lxml

    简单使用：
        说明：选择器，jquery
        from bs4 import BeautifulSoup
        使用方式：可以将一个html文档，转化为指定对象，然后通过对象的方法或者属性去查找指定的内容
        （1）转化本地文件：
            soup = BeautifulSoup(open('本地文件'), 'lxml')
        (2) 转化网络文件：
            soup = BeautifulSoup('字符串类型或者字节类型','lxml')
    (1) 根据标签名查找
        soup.a
    (2) 获取属性
        soup.a['href']  获取单个属性
        soup.a.attrs  获取所有属性和值，返回一个字典
    (3) 获取内容
        soup.head.string: 不能获取包含标签的文本
        soup.head.get_text():
        soup.head.text以上俩个可以获取文本内容
    (4) find
        soup.find('a') 找到第一个符合要求的标签
        soup.find('a', title='qin') 可以利用属性Title进行筛选

        只能找到第一个满足要求的标签
    (5)find_all
        soup.find_all('a'): 找出所有的含有a标签
        soup.find_all(['a', 'img']) 传递一个列表，可以将列表的所含的标签都找出来
    (6)select
        根据选择器选择指定的内容

        常见的选择器：标签选择器，类选择器，id选择器，组合选择器，层级选择器，伪类选择器，属性选择器
        a
        .dudu
        #lala
        a, .dudu, #lala, .meme
        div .dudu #lala .meme   下面好多级
        div>p>a>.lala   只能是下面一级
        input[name='lala']

        select 选择器返回永远是列表，需要通过下标提取对象，然后获取属性和节点，该方法也可以通过普通对象调用，找到都是这个对象下面符合要求的所有节点
'''