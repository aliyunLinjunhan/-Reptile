import requests

# 创建一个会话用于记录cookie信息
s = requests.Session()

headers = {
    'User-Agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    'Cookie': 'adfbid=0; adfbid2=0; sts_deviceid=169f23f42785aa-0ddd4a8144f7ce-1333063-2073600-169f23f'
              '42794da; sts_sg=1; sts_sid=169f23f427c4a6-0c120124277b5d-1333063-2073600-169f23f427d6e9;'
              ' sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fa'
              'drc.php%3Ft%3D06KL00c00fZmx9C0TLu60KqiAsjT6J9T00000r2_AdC00000VSsHd6.THLyktAJ0A3qnWDsnjcY'
              'rHFxnHIxpA7EgLKM0ZnqmHm3nARkmHDsnjKbmHnvrfKd5HnvwHw7wWwanRcYfWf3PjmsrDcLnD77Pjm1P19jPWR30'
              'ADqI1YhUyPGujY1nWczPWcdrj6vFMKzUvwGujYkP6K-5y9YIZK1rBtEILILQMGCmyqspy38mvqV5LPGujYknWDknH'
              'n3njnhIgwVgLPEIgFWuHdBmy-bIgKWTZChIgwVgvd-uA-dUHdWTZf0mLFW5HRvnH6s%26tpl%3Dtpl_11535_1877'
              '8_14772%26l%3D1511763170%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2'
              '525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9'
              '%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText'
              '%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%'
              '2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7'
              '%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525B'
              'D%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525'
              'E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%252'
              '5BC%252581%2526xp%253Did(%252522m3222625886_canvas%252522)%25252FDIV%25255B1%25255D%25252FD'
              'IV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255'
              'D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D241%26w'
              'd%3D%25E6%2599%25BA%25E8%2581%2594%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3D210'
              '02492_17_hao_pg%26oq%3D%2525E4%2525BA%2525BA%2525E4%2525BA%2525BA%2525E7%2525BD%252591%26i'
              'nputT%3D2937; sajssdk_2015_cross_new_user=1; jobRiskWarning=true; urlfrom=121114583; urlfro'
              'm2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; dywea=95841923.34537961305514510'
              '00.1554547434.1554547434.1554547434.1; dywec=95841923; dywez=95841923.1554547434.1.1.dywecs'
              'r=baidu|dyweccn=(organic)|dywecmd=organic; __utma=269921210.1106658778.1554547435.155454743'
              '5.1554547435.1; __utmc=269921210; __utmz=269921210.1554547435.1.1.utmcsr=baidu|utmccn=(orga'
              'nic)|utmcmd=organic; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1554547435; JsNewlogin=21354252'
              '38; JSloginnamecookie=15521093428; JSShowname=%3FJun%3F; at=6825775320564239894217b22649545'
              '0; Token=6825775320564239894217b226495450; rt=fb6f41cfc47b4dc4b87b96743efc1da2; JSpUserInfo'
              '=36672168546b5c75407754714f6547715d6353655969596b4e713b653f7758774065566750685b6b5a7541775c'
              '714465437157635f6553693e6b3b714a654e772f7704650d675a68526b2e753c7758711a654671506352655a695'
              'a6b45714e654277517743655b672568586b5d7542774b711465187108635c653b693f6b487146654a7724772565'
              '5e675668446b5d75517754714f654d715163536553692a6b39714a6540775e77246522675868236b27754077547'
              '14f6547715d6353655969596b43714c65247731774c6552675e683a6b22754c7755714c651; uiioit=3d79306c'
              '4d735365556446640932546841745870426457645f77263176645579446c4b732; acw_tc=276082381554547452'
              '8262054ef40af451c3f2ec2e27100dc58bb7a3f1d454; ZP-ENV-FLAG=gray; ZP_OLD_FLAG=false; sensorsda'
              'ta2015jssdkcross=%7B%22distinct_id%22%3A%22711808412%22%2C%22%24device_id%22%3A%22169f23f428'
              'f7bc-0fd4855c379c3b-1333063-2073600-169f23f4290602%22%2C%22props%22%3A%7B%22%24latest_traffi'
              'c_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24late'
              'st_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%'
              '22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%B'
              'C%22%2C%22%24latest_utm_source%22%3A%22baiduPC%22%2C%22%24latest_utm_medium%22%3A%22CPC%22%2'
              'C%22%24latest_utm_campaign%22%3A%22pp%22%2C%22%24latest_utm_content%22%3A%22gz%22%2C%22%24lat'
              'est_utm_term%22%3A%2219301243%22%7D%2C%22first_id%22%3A%22169f23f428f7bc-0fd4855c379c3b-133306'
              '3-2073600-169f23f4290602%22%7D; referrerUrl=https%3A//i.zhaopin.com/; LastCity=%E5%B9%BF%E5%B7'
              '%9E; LastCity%5Fid=763; dyweb=95841923.4.10.1554547434; __utmb=269921210.4.10.1554547435; stay'
              'TimeCookie=1554548645860; sts_evtseq=10; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1554548654'

}

get_url = 'https://i.zhaopin.com/resume'
dataform = {
    'callback': 'jQuery1121017508455117080035_1554547433936',
    'validateId': 'cbcfd2de67b34c7990617ece64dc8737',
    'type': '20',
    'geetest_challenge': 'bb28b1863b1b96b952bb5c83e464112e',
    'geetest_validate': '49281a3240a4b0d8761e91525fad9e6e',
    'geetest_seccode': '49281a3240a4b0d8761e91525fad9e6e|jordan',
    'passportName': '15521093428',
    'passportPwd': '72564016ljh',
    'rememberMe': '1',
    'refer': '121114583',
    'clientType': 'n',
    'businessSystem': '1',
    '_': '1554547433938',

}
r = s.get(get_url, headers=headers)

with open('zhilian.html', 'wb') as fp:
    fp.write(r.content)
