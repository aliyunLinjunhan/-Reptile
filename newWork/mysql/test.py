# import pymysql
# #
# # # 打开数据库连接
# # db = pymysql.connect("203.195.244.169", "root", "Wissen123**", "gushi")
# #
# # # 使用cursor()方法获取操作游标
# # cursor = db.cursor()
# #
# # # SQL 插入语句
# # sql = "INSERT INTO redian(title, time_readAmount, content, key_words)" \
# #       "VALUES('视觉中国版权风波', 'Fri Apr 12 11:51:35 2019 3416万', '据“网信天津”通报，经查，视觉中国在其发布的多张图片中刊发敏感有害信息标注，4月11日，天津市网信办依法约谈网站负责人，责令该网站全面彻底整改，从严处理相关责任人，全面清查历史存量信息。视觉中国负责人表示，整改期间暂时关闭网站。 \u200b\u200b\u200b\u200bhttps://s.weibo.com/weibo?q=%23%E8%A7%86%E8%A7%89%E4%B8%AD%E5%9B%BD%E7%89%88%E6%9D%83%E9%A3%8E%E6%B3%A2%23', '');"
# #
# # try:
# #     # 执行sql语句
# #     cursor.execute(sql)
# #     # 提交到数据库执行
# #     db.commit()
# # except:
# #     # 如果发生错误则回滚
# #     db.rollback()
# #     print("写入失败！！")
# #
# # # 关闭数据库连接
# # db.close()

import pymysql.cursors

# 连接配置信息
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


# 执行sql语句
try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = "INSERT INTO redian (title, time_readAmount, content, key_words) VALUES ('视觉中国版权风波', 'Fri Apr 12 11:51:35 2019 3416万', '据“网信天津”通报，经查，视觉中国在其发布的多张图片中刊发敏感有害信息标注，4月11日，天津市网信办依法约谈网站负责人，责令该网站全面彻底整改，从严处理相关责任人，全面清查历史存量信息。视觉中国负责人表示，整改期间暂时关闭网站。 \u200b\u200b\u200b\u200bhttps://s.weibo.com/weibo?q=%23%E8%A7%86%E8%A7%89%E4%B8%AD%E5%9B%BD%E7%89%88%E6%9D%83%E9%A3%8E%E6%B3%A2%23', '')"
        cursor.execute(sql)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

finally:
    connection.close()
