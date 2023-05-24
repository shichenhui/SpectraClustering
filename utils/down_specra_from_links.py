import requests
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import time, os
import gzip


def download_spectra(file_table, url, num):
    #time.sleep(0.1)
    n = 0
    while 1:
        try:
            req = requests.get(url, headers=header, timeout=3)
            # print(req.headers)
            # 获取文件名，文件名在响应的头部
            file_name = download_dir + '/' + req.headers['Content-disposition'].split('=')[-1]
            # print(req.headers)
            # 下载gz文件
            f1 = open(file_name, 'wb')
            f1.write(req.content)
            f1.close()
            file_table.append(url.split('/')[-1]+','+file_name+'\n')
            if num%100==0:
                print('finish',num)
            break
        except Exception as e:  # 防止一次下载失败
            n+=1
            if n>=4:
                print('try:',n,url)
                break
            #print(e,url,'retry',n)

if __name__ == '__main__':

    header = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5",
        'cache-control': "no-cache",
        'connection': "keep-alive",
        'cookie': "_ga=GA1.2.1388735913.1637028545; UM_distinctid=17fac8bfc4b7f5-0a31707368fdc1-5617185b-100200-17fac8bfc4c576; has_js=1; _pk_testcookie.23.ae04=1; lamost_user=63b1797f6e39418785dd2ad200d260b5; lamost-session=.eJwljkFqBDEMBP_icw6SLdnS3vOCPGCwLYmEhCzMTCAQ8vf1sE2fCrrov7TF7sd7ukX_OvwlbR-WbmlSxW7QPCjzlTpo1VygtjmqKcqcBjkHgFTB1tCBInKDsMlzzQtMEkNzI21iYiwWHbiiwMiVlIGUULuGlhzYejBB0yK9p3Xk5_D9-abljIvMu_l2-u-50Otb9Qsde2zn_dO_F5MSgy45a5ihu2MMZSP20mHZWUQQIP0_AGe3RTQ.YotXHw.woGSjF9boBp0Omz4kqjAiXkBWYc; _pk_ref.23.ae04=%5B%22%22%2C%22%22%2C1653302155%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_id.23.ae04=2edb4c4fb7ecd3a8.1632891325.24.1653306623.1653302155.",
        'host': "www.lamost.org",
        'referer': "http//www.lamost.org/dr8/v1.1/search",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",
        'postman-token': "b73e75be-7f8c-1699-7bd3-013a42033366"
    }

    # 下载文件夹，不存在则创建
    download_dir = '../spectra_gb_greater_45'
    # 光谱url列表
    url_list_file = '../coord_greater_45.csv'

    pool = multiprocessing.Pool(20)

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    f_list = open(url_list_file, 'r')
    f_list.readline()  # 读取没用的第一行
    file_table = multiprocessing.Manager().list()
    for e, i in enumerate(f_list.readlines()[::-1][500000:1000000]):
        i = i.strip()
        # print(i)
        # i = i.split('F27eb78f7a0')[0] + 'F27eb78f7a0'
        i = i.split(',')[1]
        i = 'http://www.lamost.org/dr8/v1.1/spectrum/fits/'+i
        #print(i)
        #time.sleep(1)
        pool.apply_async(download_spectra, (file_table, i, e))
        #time.sleep(0.1)
        if e%100==0:
            print(e)
            #print(len(pool))
        #download_spectra(i)
    #pool.shutdown(wait = True)
    pool.close()  # 关闭进程池，关闭后po不再接收新的请求
    pool.join()   # 进程阻塞，子进程全部结束再继续主进程
    f_table = open('table_obsid_filename.csv','a')

    print('finish download, save table ...')
    for i in file_table:
        f_table.write(i)
    f_table.close()
