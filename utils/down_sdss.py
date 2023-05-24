import requests
from concurrent.futures import ThreadPoolExecutor
import time, os
import gzip
proxies = {
  "http": "http://192.168.1.107:10809",
  "https": "http://192.168.1.107:10809",
}

def download_spectra(s):
    url = s[0]
    spec_id = s[1]
    #time.sleep(0.1)
    n = 0

    req = requests.get(url, headers=header,proxies=proxies)
    # print(req.headers)
    # 获取文件名，文件名在响应的头部
    file_name = download_dir + '/' + req.headers['Content-disposition'].split('=')[-1]
    # print(req.headers)
    # 下载gz文件
    f1 = open(file_name, 'wb')
    f1.write(req.content)
    f1.close()
    file_table.append(spec_id+','+file_name+'\n')


            #print(e,url,'retry',n)

def parse_num(s, length):
    l = len(s)
    return '0'*(length-l) + s

if __name__ == '__main__':

    header = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",

    }

    # 下载文件夹，不存在则创建
    download_dir = '../spectra_bl_greater_45_both_sdss'
    # 光谱url列表
    url_list_file = '../spectra_table_both_sdss.csv'

    #pool = ThreadPoolExecutor(20)

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    f_list = open(url_list_file, 'r')
    f_list.readline()  # 读取没用的第一行
    file_table = []
    for e, i in enumerate(f_list.readlines()):
        i = i.strip()
        # print(i)
        # i = i.split('F27eb78f7a0')[0] + 'F27eb78f7a0'
        i = i.split(',')
        url = 'https://dr16.sdss.org/optical/spectrum/view/data/format=fits/spec=lite?plateid={0}&mjd={1}&fiberid={2}'\
            .format(i[4],i[5],i[6])
        #print(url)
        #print(i)
        #time.sleep(1)
        # spec-0271-51883-0601.fits
        filename = download_dir+'/'+'spec-%s-%s-%s.fits'%(parse_num(i[4],4), parse_num(i[5],5), parse_num(i[6],4))
        if os.path.exists(filename):
            print(e,'exist')
        else:
            try:
                download_spectra([url,i[3]])
                print(e,'down finish')
            except:
                print(e, 'download error')
        #pool.submit(download_spectra, [url,i[3]])
        #time.sleep(0.1)

            #print(len(pool))
        #download_spectra(i)
    #pool.shutdown(wait = True)
    f_table = open('table_sdss.csv','a')
    for i in file_table:
        f_table.write(i)
    f_table.close()
