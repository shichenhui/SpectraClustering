import time, sys, os
import gc
import multiprocessing
from multiprocessing import Pool
from astropy import units as u      # 用于单位转换的包
from astropy.coordinates import SkyCoord
import numpy as np
import pandas as pd

# count = 1
# rows = 0
# data = pd.read_csv(file)
# data.shape


# 赤经赤纬转银经银纬，这里只需要银纬
def choose_coord(a, b):
    skycood = SkyCoord(ra=a*u.degree,dec=b*u.degree,frame='icrs')
    g = skycood.galactic
    w = g.b.deg
    return w

# 进程函数，将处理后的数据append到共享列表中
def worker(data_all, df,n):
    #global data_concat
    print('process ',n)
    df_temp = df
    df_temp['b'] = df_temp.apply(lambda x: choose_coord(x["ra_obs"], x["dec_obs"]), axis=1)
    df_temp = df_temp[df_temp['b']>45]
    data_all.append(df_temp)
    print('process ',n,'finish')

if __name__=='__main__':
    chunk_size = 1000000

    file = r'../dr8_v1.1_LRS_wd.csv'
    file_all = r'../dr8_v1.1_LRS_catalogue.csv'

    # 多进程共享列表的写法，普通列表无法共享
    data_concat = multiprocessing.Manager().list()
    po = Pool(35)
    n = 0
    for df in pd.read_csv(file_all, chunksize=10000):
        n += 1
        po.apply_async(worker, (data_concat, df, n,))

    po.close()  # 关闭进程池，关闭后po不再接收新的请求
    po.join()   # 进程阻塞，子进程全部结束再继续主进程

    r = pd.concat(data_concat)
    r.to_csv('../dr8_gb_greater_45.csv')

    print("info:\n", r.info())
    print('describe\n',r.describe())
    print('shape\n',r.shape)
    print('data_concat\n',len(data_concat))
