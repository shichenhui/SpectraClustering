import numpy as np
import matplotlib.pyplot as plt


class LineIndex:
    def __init__(self):
        self.elements = [(4143.375, 4178.375, 4081.375, 4118.875, 4245.375, 4285.375),
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
                            (6191.375, 6273.875, 6068.375, 6143.375, 6374.375, 6416.875),]

    def calc(self, flux, wave):
        """
        计算一条光谱的线指数
        :param flux: 光谱的流量向量
        :param wave: 光谱的波长向量
        :return: 线指数
        """
        line_index = []

        for num, i in enumerate(self.elements):
            print(num)
            # 求每一个元素的线指数
            # 找出中心波段、蓝端、红端的波段和流量
            center_band, center_flux = wave[(wave >= i[0]) & (wave <= i[1])], flux[(wave >= i[0]) & (wave <= i[1])]
            left_band, left_flux = wave[(wave >= i[2]) & (wave <= i[3])], flux[(wave >= i[2]) & (wave <= i[3])]
            right_band, right_flux = wave[(wave >= i[4]) & (wave <= i[5])], flux[(wave >= i[4]) & (wave <= i[5])]

            # 计算连续谱直线,通过两个点画直线
            y_left = np.trapz(left_flux, left_band)
            y_right = np.trapz(right_flux, right_band)
            x_left = np.mean(left_band)
            x_right = np.mean(right_band)
            # y = kx + b
            k = (y_right - y_left) / (x_right - x_left)
            b = y_right - k*y_right

            if num in (0,1,10,11,19,20):
                # 对部分元素，计算Mag星等，当做线指数值
                Fc = k * center_band + b  # 连续谱流量
                Mag = -2.5*np.log2((1 / (center_band[-1]-center_band[1])) * np.trapz(center_flux/Fc, center_band))
                line_index.append(Mag)

            else:
                # 对部分元素，计算equivalent width等效带宽，当做线指数值
                Fc = k*center_band + b   # 连续谱流量
                EW = np.trapz((1-center_flux/Fc), center_band)

                line_index.append(EW)

        # 转换成np.array，并消除控制和无限值
        line_index = np.array(line_index)
        line_index[np.isnan(line_index)] = 0
        line_index[np.isinf(line_index)] = 0

        return line_index

    def calc_and_plot(self,flux, wave):
        # 计算线指数，并画图看看效果，与self.calc() 函数传进传出相同
        line_index = self.calc(flux, wave)

        center_wave = []
        for i in self.elements:
            center_wave.append((i[0]+i[1]) / 2)
        plt.plot(wave, flux)
        plt.scatter(center_wave, line_index)
        plt.show()

        return line_index


if __name__ == '__main__':
    from astropy.io import fits

    data = fits.open(r'C:\Users\panda\Desktop\spec-56591-EG012606S021203F01_sp08-138.fits')
    a = data[0]
    wave = a.data[2]  # 第3行是波长
    flux = a.data[0]  # 第1行是光谱
    model = LineIndex()
    line_index = model.calc_and_plot(flux, wave)