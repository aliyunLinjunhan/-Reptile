# -*- coding: utf-8 -*-
import re
import pymysql.cursors

pattern_title = re.compile('诗文名称: (.*?)点赞量')
pattren_good = re.compile('点赞量: ([0-9]+)')
pattren_content = re.compile('诗文内容: (.*?), 诗文作者')
pattren_zaxiang = re.compile('诗文译文和注释: (.*?)}')
pattren_autor = re.compile('诗文作者: (.*?)诗文译文和注释')

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

a = set()
i = 1
n = 1
for str in open(r'C:\Users\Administrator\PycharmProjects\newWork\paqu_gushiwen\siwen_message.txt', 'r',
                encoding='UTF-8'):
    if i == 5151:
        i = i + 1
        continue
    else:
        i = i + 1

    # str = "{'诗文名称': '鹿柴', '点赞量': '2502', '诗文朝代': '唐代', '诗文内容': ['\n空山不见人，但闻人语响。', '返景入深林，复照青苔上。\n'], '诗文作者': '王维', '诗文译文和注释': ['幽静的山谷里看不见人，只能听到那说话的声音。', '落日的影晕映入了深林，又照在青苔上景色宜人。', '鹿柴（zhài）：“柴”同“寨“，栅栏。此为地名。', '但：只。闻：听见。', '返景：夕阳返照的光。“景”古时同“影”。', '照：照耀(着)。', '幽静的山谷里看不见人，只听得说话的人语声响。', '落日的影晕映入了深林，又照在幽暗处的青苔上。', '鹿柴（zhài）：', '辋川别墅之一（在今陕西省蓝田县西南）。柴：通“寨”、“砦”，用树木围成的栅栏。', '但：只。', '返景（yǐng）：同“返影”，太阳将落时通过云彩反射的阳光。', '复：又。', '\u3000\u3000第一句“空山不见人”，先正面描写空山的杳无人迹。王维特别喜欢用“空山”这个词语，但在不同的诗里，它所表现的境界却有区别。“空山新雨后，天气晚来秋”（《山居秋暝》），侧重于表现雨后秋山的空明洁净；“人闲桂花落，夜静春山空”（《鸟鸣涧》），侧重于表现夜间春山的宁静幽美；而“空山不见人”，则侧重于表现山的空寂清泠。由于杳无人迹，这并不真空的山在诗人的感觉中显得空廓虚无，宛如太古之境。“不见人”，把“空山”的意蕴具体化了。', '\u3000\u3000如果只读第一句，读者可能会觉得它比较平常，但在“空山不见人”之后紧接“但闻人语响”，却境界顿出。“但闻”二字颇可玩味。通常情况下，寂静的空山尽管“不见\n', '\u3000\u3000这首诗描绘的是鹿柴附近的空山深林在傍晚时分的幽静景色。诗的绝妙处在于以动衬静，以局部衬全局，清新自然，毫不做作。落笔先写空山寂绝人迹，接着以但闻一转，引出人语响来。空谷传音，愈见其空；人语过后，愈添空寂。最后又写几点夕阳余晖的映照，愈加触发人幽暗的感觉。', '\u3000\u3000大凡写山水，总离不开具体景物，或摹状嶙峋怪石，或描绘参天古木，或渲染飞瀑悬泉，其着眼点在于景物之奇。“空山不见人，但闻人语响。”我们走进深山密林都有这样的经验：山中分明杳无人迹，却突然听到有人说话的声音，前后左右环视寻觅，又见不到一丝人影。诗的前两句，写的就是这种情境。能听到话语，人应在不远之处，然而竟不得见，可\n', '\u3000\u3000鹿柴是', '在辋川别业的胜景之一。唐天宝年间，王维在终南山下购置辋川别业。辋川有胜景二十处，王维和他的好友', '逐处作', '，编为《辋川集》，这首诗是其中的第五首。']}"
    # str = "{'诗文名称': '行宫', '点赞量': '729', '诗文朝代': '唐代', '诗文内容': ['\n寥落古行宫，宫花寂寞红。', '白头宫女在，闲坐说玄宗。\n'], '诗文作者': '元稹', '诗文译文和注释': ['曾经富丽堂皇的古行宫已是一片荒凉冷落，宫中艳丽的花儿在寂寞寥落中开放。', '幸存的几个满头白发的宫女，闲坐无事只能谈论着玄宗轶事。', '寥（liáo）落：寂寞冷落。', '行宫：皇帝在京城之外的宫殿。这里指当时东都洛阳的皇帝行宫上阳宫。', '宫花：行宫里的花。', '白头宫女：据', '《上阳白发人》，一些宫女天宝末年被“潜配”到上阳宫，在这冷宫里一闭四十多年，成了白发宫人。', '说：谈论。', '玄宗：指唐玄宗。', '\u3000\u3000元稹的这首《行宫》是一首抒发盛衰之感的诗，这首短小精悍的五绝具有深邃的意境，富有隽永的诗味，倾诉了宫女无穷的哀怨之情，寄托了诗人深沉的盛衰之感。', '\u3000\u3000诗人先写环境。首句中“寥落”已点出行宫的空虚冷落，又着一“古”字，更显其破旧之象。这样的环境本身就暗示着昔盛今衰的变迁。而后以“宫花寂寞红”续接，此处可见运思缜密。娇艳红花与古旧行宫相映衬，更见行宫“寥落”，加强了时移世迁的盛衰之感。两句景语，令人心无旁鹜，只有沉沉的感伤。', '\u3000\u3000后两句由景及人，写宫女，“白头”与第二句中的红花相映衬。宫中花开如旧，而当年花容月貌的宫女已变成了白发老妇。物是人非，此间包含着\n', '\u3000\u3000', '生活在中唐年代，正值唐朝经历过安史之乱不久，国力衰退。该', '就是以小见大地点明了唐朝衰败的重要原因。']}"
    ret = re.sub(r"', '", '', str)
    ret = re.sub(r"'", '', ret)
    ret = re.sub(r"\[", '', ret)
    ret = re.sub(r"]", '', ret)
    ret = re.sub(r"\\n", '', ret)
    ret = re.sub(r"\\u3000", '', ret)
    ret = re.sub(r"/", '', ret)
    print(ret)
    title = pattern_title.findall(ret)[0]
    good = pattren_good.findall(ret)[0]
    content = pattren_content.findall(ret)[0]
    zaxiang = pattren_zaxiang.findall(ret)[0]
    autor = pattren_autor.findall(ret)[0]
    print(title + ' ' + autor + ' ' + content)
    title_zuihou = title + ' ' + autor + ' ' + content
    print(good)
    print(type(good))
    print(zaxiang)
    if title_zuihou not in a:
        a.add(title_zuihou)
        # 执行sql语句
        try:
            with connection.cursor() as cursor:
                # 执行sql语句，插入记录
                sql = "INSERT INTO gushiwen2 (id, title_content, good_amount, explains, keywords) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(sql, (n, title_zuihou, good, zaxiang, ''))
                n = n + 1
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            pass
    else:
        continue

connection.close()
