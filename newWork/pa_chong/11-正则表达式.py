'''
正则表达式的解析：
    作用：用来匹配一类具有相同规则字符串
    规则：
        单字符：
        .: 除换行以外所有的字符
        []: [aoe] [a-w] 匹配集合中任意一个字符
        \d: 数字 [0-9]
        \D: 非数字
        \w: 数字、字母、下划线、中文
        \W：非\w
        \s：所有的空白字符
        \S: 非空白

        数量修饰：
        * : 任意多次    >=0
        + : 至少一次    >=1
        ? : 可有可无    0次或者1次
        {m} : 固定m次
        {m,} : 至少m次
        {m,n} ： m-n次

        边界：
        \b \B
        $ : 以..结尾
        ^ ：以..开始

        分组：
        () : 视为一个整体
        () \1 \2 : 子模式  （见1代码示例）

        贪婪模式：
        .*? , .+?
        具体差别示例见代码2
        re.I : 忽略大小写
        re.M : 多行匹配
        re.S : 单行匹配

        match: 从开头开始找
        search:从任意位置开始找
        findall:

        # 正则的替换
        re.sub(正则表达式, 替换内容, 字符串)
        可以用一个函数作为参数
'''
# 1、子模式
'''
import re

string = '<p><div><span>猪八戒</span></div></p>'
pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')

ret = pattern.search(string)
print(ret)
'''
# 2、贪婪模式

import re
'''
string = '<div>猪八戒</div></div></div>'
pattern = re.compile(r'<\w+>.*</\w+>')
pattern2 = re.compile(r'<\w+>.*?</\w+>')

ret = pattern.search(string)
ret2 = pattern2.search(string)
print(ret)
print(ret2)
'''
# 3、正则替换

import re

string = 'you are my dsds'

pattern = re.compile(r'dsds')
# ret = re.sub(r'dsds', 'a', string)
# 用a在string中替换dsds
ret = pattern.sub('aaa', string)
# 用aaa在string替换pattern中的内容

print(ret)


# # 4、正则函数替换
# import re
#
# def fn(a):
#     ret = int(a.group())
#     return str(ret - 10)
#
# string = '178是最受欢迎的身高'
#
# pattern = re.compile(r'\d+')
# ret = pattern.sub(fn, string)

# print(ret)


