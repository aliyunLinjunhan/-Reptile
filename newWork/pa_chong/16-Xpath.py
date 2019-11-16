'''
xpath:
    pip install lxml
    什么是xpath?
        xml是用来存储和传输数据的
        和html的不同点：
            （1） html用来显示数据，xml是用来传输数据的
            （2） html标签是固定的，xml标签是自定义的
            xpath用来在xml中查找指定元素，它是一种路径表达式

            常用的路径表达式：
            // ： 不考虑位置的查找
            ./ :  从当前节点往下查找
            @ ： 选取属性
    安装xpath插件：
        将xpath插件拖动到谷歌浏览器的扩展程序中，具体可以查看百度云中的插件资源
        启动和关闭插件：
            ctrl+shift+x
        属性定位：
            //input[id='kw']
            //input[@class='bg s_btn']
        层级索引：
        索引定位：
            //div[@id="head"]/div/div[2]/a[@class="toindex"]
            [注]索引从1开始
            //div[@id="head"]//a[@class="toindex"]
        逻辑运算：
            //input[@class="s_ipt" and @name="wd"]
        模糊匹配：
            contains:
                //input[contains(@class, "s_i")]
                所有的input，有class属性，并且属性中带有s_i的节点
            starts-with
                //input[starts-with(@class, "s")]
                所有的input，有class属性，并且属性以‘s’开头
        取文本：
            //div[@id="u1"]/a[5]/text()   获取节点内容
            //div[@id="u1"]//text()
            获取节点里面不带标签的所有内容
        取属性：
            //div[@id="u1"]/a[5]/@href

        代码中使用xpath
            from lxml import etree
            两种方式使用： 将html文档变成一个对象，然后调用对象的方法取查找它
            （1) 本地文件：
                tree = etree.parse(文件名)
            （2）网络文件：
                tree = etree.HTML(网页字符串) 

            调用 tree.xpath("")

            让标签中的内容全部拼接起来返回：
            ret = tree.xpath('//div[@class="song"]')
            string = ret[0].xapth('string(.)')
            print(string.replace('\n','').replace('\t',''))
'''
