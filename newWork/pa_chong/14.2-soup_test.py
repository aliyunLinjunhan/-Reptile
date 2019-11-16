from bs4 import BeautifulSoup

soup = BeautifulSoup(open('renrenwang1.html', encoding='utf8'), 'lxml')
# print(type(soup))
# print(soup.head)
# print(soup.head.string)
# print(soup.head.get_text())
print(soup.head.text)
print(soup.find_all(['a', 'img']))