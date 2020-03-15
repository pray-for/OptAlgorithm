import os
import pickle
import Partition1
import operator
import xlwt
import numpy as np
from sklearn import preprocessing

'''
对32个阈值下的矩阵，分区块，并计算Q
将每个阈值下的Q保存，为绘图用
'''

pathname1 = "E:\\脑电python3\\选择阈值\\"
pathname3 = "E:\\脑电python3\\选择阈值2\\"

name = ['s01', 's02', 's05', 's12', 's13', 's22', 's25', 's29', 's32']
threshold = ['0.2', '0.225', '0.25', '0.275', '0.3', '0.325', '0.35', '0.375',
            '0.4', '0.425', '0.45', '0.475', '0.5', '0.525', '0.55', '0.575',
            '0.6', '0.625', '0.65', '0.675', '0.7', '0.725', '0.75', '0.775',
             '0.8', '0.825', '0.85', '0.875', '0.9', '0.925', '0.95', '0.975']
threshold_num = [0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375,
                0.4, 0.425, 0.45, 0.475, 0.5, 0.525, 0.55, 0.575,
                0.6, 0.625, 0.65, 0.675, 0.7, 0.725, 0.75, 0.775,
                0.8, 0.825, 0.85, 0.875, 0.9, 0.925, 0.95, 0.975]

for i in range(0, 9):
    pathname2 = name[i] + '\\'
    pathname12 = pathname1 + pathname2
    pathname4 = pathname3 + pathname2
    if not os.path.exists(pathname4):
        os.mkdir(pathname4)
    pathname2_p = pathname12 + "Positive\\"
    pathname2_n = pathname12 + "Negative\\"
    pathname5_p = pathname4 + "Positive\\"
    pathname5_n = pathname4 + "Negative\\"
    if not os.path.exists(pathname5_p):
        os.mkdir(pathname5_p)
    if not os.path.exists(pathname5_n):
        os.mkdir(pathname5_n)
    k = 0
    k = k + 1
    m = 0
    n = 64  # 32个阈值，n为阈值个数*2
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("sheet")
    for j in range(0, 2):
        pathname6 = "s0%d-%d\\" % ((k), (j + 1))
        pathname6_p = pathname5_p + pathname6
        pathname6_n = pathname5_n + pathname6
        if not os.path.exists(pathname6_p):
            os.mkdir(pathname6_p)
        if not os.path.exists(pathname6_n):
            os.mkdir(pathname6_n)

        for q in range(0, 32):  # 32个阈值
            filename1 = name[i] + "-%d\\" % (j + 1)
            filename2 = name[i] + "-%d" % (j + 1) + "-" + threshold[q] + ".dat"
            filename3_p = pathname2_p + filename1 + filename2
            filename3_n = pathname2_n + filename1 + filename2
            print(filename3_p)
            print(filename3_n)
            s1 = open(filename3_p, "rb")  # Positive
            x1 = pickle.load(s1, encoding="latin1")
            s2 = open(filename3_n, "rb")  # Negative
            x2 = pickle.load(s2, encoding="latin1")

            pathname22 = "s0%d-%d" % ((k), (j + 1)) + "-" + threshold[q] + "\\"
            savepath1 = pathname6_p + pathname22
            savepath2 = pathname6_n + pathname22
            if not os.path.exists(savepath1):
                os.mkdir(savepath1)
            if not os.path.exists(savepath2):
                os.mkdir(savepath2)

            data1_1 = x1['data1']
            data1_2 = x1['data2']
            data1_3 = x1['data3']
            data1_4 = x1['data4']
            labels1 = x1['labels']

            data2_1 = x2['data1']
            data2_2 = x2['data2']
            data2_3 = x2['data3']
            data2_4 = x2['data4']
            labels2 = x2['labels']

            mod1_1 = Partition1.Partition_F(savepath1, data1_1, 1)
            mod1_2 = Partition1.Partition_F(savepath1, data1_2, 2)
            mod1_3 = Partition1.Partition_F(savepath1, data1_3, 3)
            mod1_4 = Partition1.Partition_F(savepath1, data1_4, 4)

            mod2_1 = Partition1.Partition_F(savepath2, data2_1, 1)
            mod2_2 = Partition1.Partition_F(savepath2, data2_2, 2)
            mod2_3 = Partition1.Partition_F(savepath2, data2_3, 3)
            mod2_4 = Partition1.Partition_F(savepath2, data2_4, 4)

            mods_p = [mod1_1, mod1_2, mod1_3, mod1_4]
            mods_n = [mod2_1, mod2_2, mod2_3, mod2_4]
            max_index_p, max_number_p = max(enumerate(mods_p), key=operator.itemgetter(1))
            max_index_n, max_number_n = max(enumerate(mods_n), key=operator.itemgetter(1))

            pathname_exl = pathname4 + "text.xlsx"
            # workbook = xlwt.Workbook()
            # worksheet = workbook.add_sheet("sheet")
            # for m in range(0, 14):
            #     worksheet.write(m, 0, "Positive")
            #     worksheet.write(m, 1, threshold_num[q])
            #     worksheet.write(m, 2, max_number_p)
            # for m in range(14, 28):
            #     worksheet.write(m, 0, "Negative")
            #     worksheet.write(m, 1, threshold_num[q])
            #     worksheet.write(m, 2, max_number_n)
            # workbook.save(pathname_exl)
            # for m in range(0, 14):
            worksheet.write(m, 0, "Positive")
            worksheet.write(m, 1, threshold_num[q])
            worksheet.write(m, 2, max_number_p)
            # for m in range(14, 28):
            worksheet.write(n, 0, "Negative")
            worksheet.write(n, 1, threshold_num[q])
            worksheet.write(n, 2, max_number_n)
            workbook.save(pathname_exl)
            m = m + 1
            n = n + 1