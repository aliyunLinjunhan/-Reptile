'''
bs4��
    BeautifulSoup
    ��Ҫ��pipԴ����Ϊ����Դ������Դ������Դ������Դ�ȵ�
    windows:
        ��1�����ļ���Դ������
        ��2���ڵ�ַ���������� %appdata%
        ��3�����������½�һ���ļ��� pip
        ��4����pip�ļ��������½�һ���ļ����� pip.ini
            ���������£�
            [global]
            timeout = 6000
            index-url=https://mirrors.aliyun.com/pypi/simple/
            trusted-host=mirrors.aliyun.com
    linux:
        (1) cd ~
        (2) mkdir ~/.pip
        (3) vi ~/.pip/pip.conf
        (4) �༭����һ��

    ��Ҫ��װ��pip install bs4
        bs4��ʹ��ʱ��Ҫ��װһ���� pip install lxml

    ��ʹ�ã�
        ˵����ѡ������jquery
        from bs4 import BeautifulSoup
        ʹ�÷�ʽ�����Խ�һ��html�ĵ���ת��Ϊָ������Ȼ��ͨ������ķ�����������ȥ����ָ��������
        ��1��ת�������ļ���
            soup = BeautifulSoup(open('�����ļ�'), 'lxml')
        (2) ת�������ļ���
            soup = BeautifulSoup('�ַ������ͻ����ֽ�����','lxml')
    (1) ���ݱ�ǩ������
        soup.a
    (2) ��ȡ����
        soup.a['href']  ��ȡ��������
        soup.a.attrs  ��ȡ�������Ժ�ֵ������һ���ֵ�
    (3) ��ȡ����
        soup.head.string: ���ܻ�ȡ������ǩ���ı�
        soup.head.get_text():
        soup.head.text�����������Ի�ȡ�ı�����
    (4) find
        soup.find('a') �ҵ���һ������Ҫ��ı�ǩ
        soup.find('a', title='qin') ������������Title����ɸѡ

        ֻ���ҵ���һ������Ҫ��ı�ǩ
    (5)find_all
        soup.find_all('a'): �ҳ����еĺ���a��ǩ
        soup.find_all(['a', 'img']) ����һ���б����Խ��б�������ı�ǩ���ҳ���
    (6)select
        ����ѡ����ѡ��ָ��������

        ������ѡ��������ǩѡ��������ѡ������idѡ���������ѡ�������㼶ѡ������α��ѡ����������ѡ����
        a
        .dudu
        #lala
        a, .dudu, #lala, .meme
        div .dudu #lala .meme   ����ö༶
        div>p>a>.lala   ֻ��������һ��
        input[name='lala']

        select ѡ����������Զ���б���Ҫͨ���±���ȡ����Ȼ���ȡ���Ժͽڵ㣬�÷���Ҳ����ͨ����ͨ������ã��ҵ�������������������Ҫ������нڵ�
'''