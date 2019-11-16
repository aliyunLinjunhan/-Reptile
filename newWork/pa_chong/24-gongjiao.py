import requests
from lxml import etree

final_list=[]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36'
}

def final_parse(content):
	tree = etree.HTML(content)
	# 获取线路名称
	route_name = tree.xpath('//div[@class="bus_i_t1"]/h1/text()')[0]
	# 获取公车运行时间
	route_time = tree.xpath('//div[@class="bus_i_content"]/p[1]/text()')[0]
	# 获取票价信息
	route_money = tree.xpath('//div[@class="bus_i_content"]/p[2]/text()')[0]
	# 获取网站最后更新时间
	route_fianltime = tree.xpath('//div[@class="bus_i_content"]/p[4]/text()')[0]
	# 获取上行总站数
	total_stationsa = tree.xpath('//span[@class="bus_line_no"]/text()')[0]
	total_stationsa = total_stationsa.replace('\xa0', '')
	# 获取上行站名
	stations_namea = tree.xpath('//div[@class="bus_line_site "][1]/div/div/a/text()')
	try:
		# 获取下行总站数
		total_stationsb = tree.xpath('//span[@class="bus_line_no"]/text()')[1]
		total_stationsb = total_stationsb.replace('\xa0', '')
		# 获取下行站名
		stations_nameb = tree.xpath('//div[@class="bus_line_site "][2]/div/div/a/text()')
	except Exception as e:
		total_stationsb = '0'
		stations_nameb = ''

	message_dict = {
		'线路名称': route_name,
		'公车运行时间': route_time,
		'票价信息': route_money,
		'网站最后更新时间': route_fianltime,
		'上行总站数': total_stationsa,
		'上行站名': stations_namea,
		'下行总站数': total_stationsb,
		'下行站名': stations_nameb,
	}
	final_list.append(message_dict)



def first_parse(content):
	tree = etree.HTML(content)
	# 获取公交车号
	num_list = tree.xpath('//div[@class="bus_kt_r1"]/a/@href')
	# 获取公交车字母开头号
	zimu_list = tree.xpath('//div[@class="bus_kt_r2"]/a/@href')
	return num_list + zimu_list


def seconed_parse(content):
	tree = etree.HTML(content)
	# 获取线路名称
	routes_name = tree.xpath('//div[@id="con_site_1"]/a/text()')
	# 获取各线路网站
	routes_url = tree.xpath('//div[@id="con_site_1"]/a/@href')
	# print(route_url, route_name)
	i = 0
	# print(routes_name)
	# print(routes_url)
	for it in routes_url:
		print('开始爬取{0}'.format(routes_name[i]))
		url = 'https://guangzhou.8684.cn' + it
		final_content = requests.get(url=url, headers=headers)
		final_parse(final_content.text)
		print('结束爬取{0}'.format(routes_name[i]))
		i = i + 1



def main():
	url = 'https://guangzhou.8684.cn/'
	# 获取第一页网页内容
	first_content = requests.get(url=url, headers=headers)
	# print(first_content.text)
	# 对第一页的内容进行解析
	first_list = first_parse(first_content.text)
	# print(first_list)
	# 分别访问各线路
	for it in first_list:
		url_second = 'https://guangzhou.8684.cn' + it
		seconed_content = requests.get(url=url_second, headers=headers)
		# 对各个线路进行解析
		seconed_parse(seconed_content.text)
	# print(final_list)
	with open(r'gongjiao_guangzhou.txt', 'w', encoding="utf8") as fp:
		fp.write(str(final_list) + '\n\n\n\n')



if __name__ == '__main__':
	main()
