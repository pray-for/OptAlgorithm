import os
import pickle
import test3
import numpy as np
from sklearn import preprocessing

'''
分区块，绘图，保存PDF
对筛选后的数据进行实验
'''

pathname1 = "E:\\脑电python3\\二值矩阵\\s01\\Positive\\s01-1.dat"
savepath1 = "E:\\脑电python3\\ceshi\\"
# pathname3 = "E:\\脑电python3\\分区块数据\\"

# name = ['s01', 's02', 's05', 's12', 's13', 's22', 's25', 's29', 's32']


s1 = open(pathname1, "rb")        # Positive
x1 = pickle.load(s1, encoding="latin1")


data1_1 = x1['data1']
# data1_2 = x1['data2']
# data1_3 = x1['data3']
# data1_4 = x1['data4']
labels1 = x1['labels']

test3.Partition_F(savepath1, data1_1, 1)
# test3.Partition_F(savepath1, data1_2, 2)
# test3.Partition_F(savepath1, data1_3, 3)
# test3.Partition_F(savepath1, data1_4, 4)



