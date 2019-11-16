import json
import re
import pymysql.cursors


f = open(r"C:\Users\Administrator\Desktop\mysql_data\gushiwen.json", 'r', encoding="utf8")

dic = json.load(f)
print(dic["title_content"])
# # print(type(dic["RECORDS"]))
# # print(len(dic["RECORDS"]))
# index = 0
# # 写一个匹配阅读量和时间的正则
# pattren = re.compile('(.*?2019) (.*)([\u4e00-\u9fa5])')
# pattren2 = re.compile('(.*?)([a-zA-z]+://[^\s]*)')
#
#
# def parse_readAmount_time(readAmount_time):
#     """
#     用来解析提取时间和阅读量
#     :param readAmount_time:
#     :return: 时间和阅读量
#     """
#     it = pattren.findall(readAmount_time)
#     # print(it)
#     amount = float(it[0][1])
#     if it[0][2] == "万":
#         amount = amount * 10000
#     else:
#         amount = amount * 100000000
#     # print(int(amount))
#     time_now = it[0][0]
#     # print(time_now)
#     return int(amount), str(time_now)
#
# def parse_url_content(content):
#     # print(content)
#     it = pattren2.findall(content)
#     # print(it)
#     return str(it[0][0]), str(it[0][1])
'''
if __name__ == "__main__":
    # 配置连接信息
    config = {
        'host': '203.195.244.169',
        'port': 3306,
        'user': 'root',
        'password': 'Wissen123**',
        'db': 'gushi',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    # 创建连接
    connection = pymysql.connect(**config)

    while(index < 1437):
        dic_t = dic["RECORDS"][index]
        # print(dic_t)
        amount, time_now = parse_readAmount_time(dic_t['time_readAmount'])
        title = dic_t['title']
        content, url = parse_url_content(dic_t['content'])
        print(amount)
        print(time_now)
        print(title)
        print(content)
        print(url)
        # 执行sql语句
        try:
            with connection.cursor() as cursor:
                delSql = "DELETE FROM Hotspot WHERE title = %s"
                sql = "INSERT INTO Hotspot (title, amount, daytime, content, url, keywords) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(delSql, (title))
                cursor.execute(sql, (title, amount, time_now, content, url, ''))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            pass

        index = index + 1

    connection.close()
'''





