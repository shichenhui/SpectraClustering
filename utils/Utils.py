import sys, os, time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy.io import fits




def read_line_index(fits_path):
    """
    计算一条光谱的线指数
    :param flux: 光谱的流量向量
    :param wave: 光谱的波长向量
    :return: 线指数, np.array类型
    """
    elements = [(4143.375, 4178.375, 4081.375, 4118.875, 4245.375, 4285.375),
                (4143.375, 4178.375, 4085.125, 4097.625, 4245.375, 4285.375),
                (4223.500, 4236.000, 4212.250, 4221.000, 4242.250, 4252.250),
                (4282.625, 4317.625, 4267.625, 4283.875, 4320.125, 4333.375),
                (4370.375, 4421.625, 4360.375, 4371.625, 4444.125, 4456.625),
                (4453.375, 4475.875, 4447.125, 4455.875, 4478.375, 4493.375),
                (4515.500, 4560.500, 4505.500, 4515.500, 4561.750, 4580.500),
                (4635.250, 4721.500, 4612.750, 4631.500, 4744.000, 4757.750),
                (4848.875, 4877.625, 4828.875, 4848.875, 4877.625, 4892.625),
                (4979.000, 5055.250, 4947.750, 4979.000, 5055.250, 5066.500),
                (5070.375, 5135.375, 4896.375, 4958.875, 5302.375, 5367.375),
                (5155.375, 5197.875, 4896.375, 4958.875, 5302.375, 5367.375),
                (5161.375, 5193.875, 5143.875, 5162.625, 5192.625, 5207.625),
                (5247.375, 5287.375, 5234.875, 5249.875, 5287.375, 5319.875),
                (5314.125, 5354.125, 5306.625, 5317.875, 5355.375, 5365.375),
                (5390.250, 5417.750, 5379.000, 5390.250, 5417.750, 5427.750),
                (5698.375, 5722.125, 5674.625, 5698.375, 5724.625, 5738.375),
                (5778.375, 5798.375, 5767.125, 5777.125, 5799.625, 5813.375),
                (5878.625, 5911.125, 5862.375, 5877.375, 5923.875, 5949.875),
                (5938.875, 5995.875, 5818.375, 5850.875, 6040.375, 6105.375),
                (6191.375, 6273.875, 6068.375, 6143.375, 6374.375, 6416.875), ]

    fits_file = fits.open(fits_path)
    hdu = fits_file[0]
    flux = hdu.data[0]

    coeff0 = hdu.header['COEFF0']

    wave = np.linspace(start=coeff0,stop=coeff0+0.0001*len(flux),num=len(flux),endpoint=False)
    wave = 10**wave
    fits_file.close()
    line_index = []

    for n, i in enumerate(elements):
        # print(num)
        # 求每一个元素的线指数
        # 找出中心波段、蓝端、红端的波段和流量
        center_band, center_flux = wave[(wave >= i[0]) & (wave <= i[1])], flux[(wave >= i[0]) & (wave <= i[1])]
        left_band, left_flux = wave[(wave >= i[2]) & (wave <= i[3])], flux[(wave >= i[2]) & (wave <= i[3])]
        right_band, right_flux = wave[(wave >= i[4]) & (wave <= i[5])], flux[(wave >= i[4]) & (wave <= i[5])]

        # 计算连续谱直线,通过两个点画直线
        y_left = np.trapz(left_flux, left_band) / (left_band[-1] - left_band[0])
        y_right = np.trapz(right_flux, right_band) / (right_band[-1] - right_band[0])
        x_left = np.mean(left_band)
        x_right = np.mean(right_band)
        # y = kx + b
        k = (y_right - y_left) / (x_right - x_left)
        b = y_right - k * x_right

        if n in (0, 1, 10, 11, 19, 20):
            # 对部分元素，计算Mag星等，当做线指数值
            #                 Fc = k * center_band + b  # 连续谱流量
            #                 Mag = -2.5*np.log2((1 / (center_band[-1]-center_band[1])) * np.trapz(center_flux/Fc, center_band))
            #                 line_index.append(Mag)
            pass

        else:
            # 对部分元素，计算equivalent width等效带宽，当做线指数值
            Fc = k * center_band + b  # 连续谱流量
            EW = np.trapz((1 - center_flux / Fc), center_band)

            line_index.append(EW)

            ################# 画出中心波段、线指数，看看效果
    #                 plt.plot(center_band, center_flux/10)
    #                 plt.plot(left_band, left_flux/10)
    #                 plt.plot(right_band, right_flux/10)
    #                 plt.scatter(((center_band[0]+center_band[-1])/2,center_band[0],center_band[-1]), (line_index[-1],y_left/10,y_right/10))
    #                 plt.show()
    # 转换成np.array，并消除空值和无限值
    line_index = np.array(line_index)
    line_index[np.isnan(line_index)] = 0
    line_index[np.isinf(line_index)] = 0

    return line_index



def read_fits(fits_path):
    fits_file = fits.open(fits_path)
    hdu = fits_file[0]
    data = hdu.data[0]

    coeff0 = hdu.header['COEFF0']

    start = round(np.log10(4000), 4)
    connect1 = round(np.log10(5700), 4)
    connect2 = round(np.log10(5900), 4)
    end = round(np.log10(8510), 4)

    start_index = int((start - coeff0) / 0.0001)
    connect1_index = int((connect1 - coeff0) / 0.0001)
    connect2_index = int((connect2 - coeff0) / 0.0001)
    end_index = int((end - coeff0) / 0.0001)

    flux = np.concatenate((data[start_index: connect1_index], data[connect2_index: end_index]), axis=0)

    fits_file.close()
    # print(flux.shape)

    # if flux.shape[0] != 3121:
    #     raise ValueError

    return flux[:3121]

def read_fits_remove_redshift(fits_path):
    # 读取恒星和星系去红移之后3800-6960波长，共2628维，红移最大是0.3
    fits_file = fits.open(fits_path)
    hdu = fits_file[0]
    data = hdu.data[0]
    z = hdu.header['z']
    coeff0 = hdu.header['COEFF0']
    if coeff0>3.5843:
        return None
    star_wave = 3840
    end_wave = 6960  # 本来是6960，多10个防止短了，最后去2628个使它对齐
    start = round(np.log10(star_wave*(1+z)), 4)
    end = round(np.log10(end_wave*(1+z)), 4)

    #print(start, coeff0, start - coeff0,z)
    start_index = int((start - coeff0) / 0.0001)
    end_index = int((end - coeff0) / 0.0001)

    flux = data[start_index: end_index]
    # if len(flux)==0:
    #     print(fits_path)
    #     print(coeff0,z,start_index,end_index,start,end,data,len(data))
    #     sys.exit()
    fits_file.close()
    # print(flux.shape)

    # if flux.shape[0] != 3121:
    #     raise ValueError

    return flux[:2580]

def read_fits_QSO(fits_path):
    fits_file = fits.open(fits_path)
    hdu = fits_file[0]
    data = hdu.data[0]

    coeff0 = hdu.header['COEFF0']
    if coeff0>3.5843:
        return None
    start = round(np.log10(3840), 4)

    end = round(np.log10(6960), 4)

    start_index = int((start - coeff0) / 0.0001)
    end_index = int((end - coeff0) / 0.0001)

    flux = data[start_index: end_index]

    fits_file.close()
    # print(flux.shape)

    # if flux.shape[0] != 3121:
    #     raise ValueError

    return flux[:2580]
