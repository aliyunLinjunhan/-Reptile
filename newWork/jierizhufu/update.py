import pymysql

if __name__ == "__main__":
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

    # 创建游标，查询获得的数据以 字典（dict） 形式返回
    cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
    try:
        # 修改表(test)表中ID 为1 的value 为 10
        cursor.execute('update gushi set value = "%s" where id = 1')
        connection.commit()
    except Exception as e:
        print("失败")
    cursor.close()

    connection.close()


