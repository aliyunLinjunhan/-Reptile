import requests
import urllib

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36',
    'Cookie': 'tgw_l7_route=a37704a413efa26cf3f23813004f1'
              'a3b; _zap=eb71d42f-6553-40cd-bcb9-69946faa'
              'fe8a; _xsrf=RNDcHfvfWqqbWUhaiieyOosV9UthceX'
              '5; d_c0="ALAlveTvPQ-PTp9G5DWOJV2Wrof-AtzmXb'
              'A=|1554634565"; capsion_ticket="2|1:0|10:15'
              '54634653|14:capsion_ticket|44:OTMxZjE3Mzg2M'
              'DhiNDczMGJjMTIyZTdhMDhjYWQwN2M=|275f2e0cb90'
              '39522cadecf489abe2602d000ec36a09661b704bfbd'
              'd77fb4013a"; z_c0="2|1:0|10:1554634665|4:z_'
              'c0|92:Mi4xaDFOZ0JnQUFBQUFBc0NXOTVPODlEeVlBQ'
              'UFCZ0FsVk5xU1dYWFFBX3lSTjdwN3JvZ2ZyV1BYWDhl'
              'ZWhaeUxDSGhR|7642cc7013109888861de09cf8b3ea'
              '5c434143f626c93625ec26f80b913328c8"; unlock'
              '_ticket="AHCCTcoungwmAAAAYAJVTbHeqVyBmU59SRI'
              'LiguP7qWsaOMQ8w42HQ=="; q_c1=739ebf665d454bd'
              'fbdb2b6623bd62e38|1554634679000|155463467900'
              '0; __gads=ID=27f02d11ec5d42a8:T=1554634693:S'
              '=ALNI_MZJHKprs3g_BJJ6pMbibqUlU2Jzeg; __utma='
              '51854390.1888928663.1554634706.1554634706.15'
              '54634706.1; __utmb=51854390.0.10.1554634706;'
              ' __utmc=51854390; __utmz=51854390.1554634706'
              '.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmc'
              'md=referral|utmcct=/; __utmv=51854390.100--|'
              '2=registration_date=20171102=1^3=entry_date='
              '20171102=1; tst=h'

}

headers2 = {
    'User-Agent': "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
}
url = "https://www.zhihu.com/hot"
tieba_url = 'http://tieba.baidu.com/hottopic/browse/topicList?res_type=1&red_tag=q0865325379'

response = requests.get(url, headers=headers)
tieba_r = requests.get(tieba_url, headers=headers2)
# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)
with open('tieba.html', 'wb') as fp:
    fp.write(tieba_r.content)
