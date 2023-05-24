import sys, time, os
import yaml
import numpy as np
import pandas as pd
from astropy.io import fits
from Utils import *

def cat_fits_filename(info,fits_path='/home/shichenhui/code/data/spectra_gb_greater_45',):
    # spec-55877-B7708_sp06-051.fits.gz
    filename = 'spec-' + str(info['lmjd']) + '-' + str(info['planid']) + '_sp' + parse_s(str(info['spid']), 2) + '-' + \
               parse_s(str(info['fiberid']), 3) + '.fits.gz'
    filename = os.path.join(fits_path,filename)
    #print(filename)
    if os.path.exists(filename):
        return filename
    else:
        return None

def parse_s(s, length):
    l = len(s)
    return '0'*(length-l) + s
def chose_snr(snr, info):
    if snr == '>30':
        if info['snrg'] > 30 and info['snri']> 30:
            return cat_fits_filename(info)
        else:
            return None
    elif snr == '10-30':
        if 10 < info['snrg'] < 30 or 10 < info['snri'] < 30:
            return cat_fits_filename(info)
        else:
            return None
    elif snr == '<10':
        if info['snrg'] < 10 and info['snri'] < 10:
            return cat_fits_filename(info)
        else:
            return None
    elif snr == '>10':
        if info['snrg'] > 10 and info['snri'] > 10:
            return cat_fits_filename(info)
        else:
            return None
    elif snr == 'all':
        return cat_fits_filename(info)
    else:
        print('snr input error\n')
        sys.exit()


def construct(config):

    classes = config['classes'].keys()
    classes_data = {}  # 存放每一类的数据
    classes_data_num = {}  # 每类添加了多少条数据了
    classes_label = {}  # 每类的类标签，0,1,2，3...
    for e, i in enumerate(classes):
        classes_data[i] = []
        classes_data_num[i] = 0
        classes_label[i] = e
    num_all = sum(config['classes'].values())
    for index, row in star_table.iterrows():
        if index%500==0:
            print(index)
            print(classes_data_num)
        snr_yn = chose_snr(config['snr'], row)  # 判断是否符合信噪比要求
        #filename_i =
        # print(snr_yn)
        if snr_yn != None:
            filename_i = snr_yn  # 判断是否符合信噪比要求
            #print(filename_i)
            class_i = row['subclass'][0]  # 当前光谱的类别
            #print(class_i,classes)
            if row['class']=='STAR' and class_i in classes:  # 如果当前光谱是所需光谱
                if classes_data_num[class_i] < config['classes'][class_i]:  # 如果数量小于所需数量
                    # 判断需要原始光谱还是线指数
                    if config['data_type'] == 'spectra':
                        sp_i = read_fits(filename_i)
                    elif config['data_type'] == 'line_index':
                        sp_i = read_line_index(filename_i)
                    sp_i = np.append(sp_i, classes_label[class_i])  # 在数据最后加上标签列
                    # print(sp_i.shape)
                    classes_data[class_i].append(sp_i)
                    classes_data_num[class_i] += 1
        if sum(classes_data_num.values()) == num_all:
            f_save = open(config['save_filename'], 'w')
            for k, v in classes_data.items():
                np.savetxt(f_save, np.array(v), fmt='%.4f', delimiter=',')
            f_save.close()
            print('finish choose')
            break
        else:
            pass

    pass

def construct_sgq(config):

    classes = config['classes'].keys()
    classes_data = {}  # 存放每一类的数据
    classes_data_num = {}  # 每类添加了多少条数据了
    classes_label = {}  # 每类的类标签，0,1,2，3...
    for e, i in enumerate(classes):
        classes_data[i] = []
        classes_data_num[i] = 0
        classes_label[i] = e
    num_all = sum(config['classes'].values())
    for index, row in star_table.iterrows():
        if index%500==0:
            print(index)
            print(classes_data_num)

        if row['class']=='STAR':
            snr_yn = chose_snr(config['snr'], row)  # 判断是否符合信噪比要求
        elif  row['class']=='QSO' or row['class']=='GALAXY':
            snr_yn = chose_snr('all', row)
        else:
            snr_yn = None
        #filename_i =
        # print(snr_yn)
        if snr_yn != None:
            filename_i = snr_yn
            #print(filename_i)
            class_i = row['class']  # 当前光谱的类别
            #print(class_i,classes)
            if class_i in classes:  # 如果当前光谱是所需光谱
                if classes_data_num[class_i] < config['classes'][class_i]:  # 如果数量小于所需数量
                    # 判断需要原始光谱还是线指数
                    if config['data_type'] == 'spectra':
                        sp_i = read_fits(filename_i)
                    elif config['data_type'] == 'line_index':
                        sp_i = read_line_index(filename_i)
                    sp_i = np.append(sp_i, classes_label[class_i])  # 在数据最后加上标签列
                    # print(sp_i.shape)
                    classes_data[class_i].append(sp_i)
                    classes_data_num[class_i] += 1
        if sum(classes_data_num.values()) == num_all:
            f_save = open(config['save_filename'], 'w')
            for k, v in classes_data.items():
                np.savetxt(f_save, np.array(v), fmt='%.4f', delimiter=',')
            f_save.close()
            print('finish choose')
            break
        else:
            pass

    pass
def construct_sgq_remove_reshift(config):

    classes = config['classes'].keys()
    classes_data = {}  # 存放每一类的数据
    classes_data_num = {}  # 每类添加了多少条数据了
    classes_label = {}  # 每类的类标签，0,1,2，3...
    for e, i in enumerate(classes):
        classes_data[i] = []
        classes_data_num[i] = 0
        classes_label[i] = e
    num_all = sum(config['classes'].values())
    for index, row in star_table.iterrows():
        if index%500==0:
            print(index)
            print(classes_data_num)

        if row['class']=='STAR' and 0<row['z']<0.3 and row['z']!=-9999:
            snr_yn = chose_snr('>10', row)  # 判断是否符合信噪比要求
        elif row['class']=='GALAXY' and 0<row['z']<0.3 and row['z']!=-9999:
            snr_yn = chose_snr('all', row)
        elif row['class']=='QSO' and row['z']!=-9999 and 0<row['z']<0.3:
            snr_yn = chose_snr('all', row)
        else:
            snr_yn = None
        #filename_i =
        # print(snr_yn)
        if snr_yn != None:
            filename_i = snr_yn
            #print(filename_i)
            class_i = row['class']  # 当前光谱的类别
            #print(class_i,classes)
            if class_i in classes:  # 如果当前光谱是所需光谱
                if classes_data_num[class_i] < config['classes'][class_i]:  # 如果数量小于所需数量
                    # 判断需要原始光谱还是线指数
                    if config['data_type'] == 'spectra':
                        sp_i = read_fits_remove_redshift(filename_i)

                    elif config['data_type'] == 'line_index':
                        sp_i = read_line_index(filename_i)
                    if sp_i is not None:
                        if len(sp_i) != 2580:
                            print(len(sp_i))
                            sys.exit()
                        sp_i = np.append(sp_i, classes_label[class_i])  # 在数据最后加上标签列
                        # print(sp_i.shape)
                        classes_data[class_i].append(sp_i)
                        classes_data_num[class_i] += 1
        if sum(classes_data_num.values()) == num_all:
            f_save = open(config['save_filename'], 'w')
            for k, v in classes_data.items():
                np.savetxt(f_save, np.array(v), fmt='%.4f', delimiter=',')
            f_save.close()
            print('finish choose')
            break
        else:
            pass

    pass

if __name__ == '__main__':
    t1 = time.time()
    star_table = pd.read_csv('/home/shichenhui/code/data/dr8_gb_greater_45.csv')
    t2 = time.time()
    print(t2 - t1)
    with open('config.yml', encoding='utf-8') as file_config:
        data_config = yaml.load(file_config, Loader=yaml.FullLoader)  # 读取yaml文件

    # construct(data_config['Diff_Size_1'])
    # construct(data_config['Diff_Size_2'])
    # construct(data_config['Diff_Size_3'])
    # construct(data_config['Diff_SNR_h'])
    # construct(data_config['Diff_SNR_m'])
    # construct(data_config['Diff_SNR_l'])
    #construct_sgq_remove_reshift(data_config['SGQ_remove_shift'])
    # construct(data_config['Diff_Feature_LineIndex'])
    # construct(data_config['Diff_Feature_1Dspectra'])
    #construct(data_config['Diff_Size_4'])
    #construct(data_config['NormalSpectraStar'])
    #construct_sgq(data_config['NormalSpectraGQ'])
    construct_sgq(data_config['SGQ_10000'])
