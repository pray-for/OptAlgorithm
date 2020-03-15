import networkx as nx
import os
import pickle
import numpy as np
from networkx.algorithms import community
import community
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import Louvain

'''
脑网络分模块函数，并绘图，结果存到PDF
1.原始二值矩阵脑网络
3.用Louvain算法分模块
'''
def Partition_F(name1, xxx, k):
    # name1 = 'E:\\脑电python3\\分区块数据\\'
    name2 = 'data%d.pdf' % (k)
    name = name1 + name2
    with PdfPages(name) as pdf:
        data = np.nonzero(xxx)
        row = data[0]
        col = data[1]
        di = zip(row, col)
        list_di = list(di)
        G = nx.Graph()
        G.add_edges_from(list_di)
        # print("list_di---", list_di)
        # print("type(list_di[0])---", type(list_di[0]))
        # print("type(list_di[0][0])---", type(list_di[0][0]))

        # 将节点写入txt文件
        for l1 in list_di:
            # print("l1---", l1)
            # print("l2---", l2)
            num1 = int(l1[0])
            num2 = int(l1[1])
            # list_num = [num1, num2]
            # print(list_num)
            fp = open("E:\\脑电python3\\ceshi\\node.txt", "a+")
            fp.writelines(str(num1)+" "+str(num2)+" "+"1" + "\n")
            # fp.writelines(str(list_num) + "\n")
        fp.close()

        # 画圆
        x1 = y1 = np.arange(-1, 15, 0.1)
        x1, y1 = np.meshgrid(x1, y1)
        plt.contour(x1, y1, (x1 - 7) ** 2 + (y1 - 7) ** 2, [49])
        plt.axis('scaled')
        # plt.show()

        # 统计节点的度
        list_degree = G.degree()
        print("节点的度：", list_degree)
        d1 = list_degree[0]
        print(d1)

        # 画网络图
        pos = [(5.5, 13.5), (5, 13), (4.5, 11.5), (3, 12.5), (2, 9.5),
               (5.5, 9.5), (3, 7), (0, 7), (2, 5), (5.5, 5),
               (4.5, 2.5), (3, 2), (5, 1.5), (6, 0.5), (7, 0),
               (7, 3), (8.5, 13.5), (9, 13), (7, 11), (9.5, 11.5),
               (11, 12.5), (12, 9.5), (8.5, 9.5), (7, 7), (11, 7),
               (14, 7), (12, 5), (8.5, 5), (9.5, 2.5), (11, 2),
               (9, 1.5), (8, 0.5)]
        nx.draw_networkx(G, pos, cmap=plt.cm.Blues, with_labels=True)
        plt.title('Page1')
        pdf.savefig()  # saves the current figure into a pdf page
        plt.close()

        # 实现网络划分（计算Q）
        # 画圆
        x1 = y1 = np.arange(-1, 15, 0.1)
        x1, y1 = np.meshgrid(x1, y1)
        plt.contour(x1, y1, (x1 - 7) ** 2 + (y1 - 7) ** 2, [49])
        plt.axis('scaled')
        # 分类
        # part = community.best_partition(G)
        # print("part-----", part)
        # mod = community.modularity(part, G)
        # print("mod-----", mod)
        # values = [part.get(node) for node in G.nodes()]
        # print("values-----", values)
        # nx.draw_networkx(G, pos, node_color=values, with_labels=True)
        # # plt.savefig('E:\\脑电python3\\分区块数据\\bbb.jpg')
        # # plt.show()
        # plt.title('Page2')
        # pdf.savefig()  # saves the current figure into a pdf page
        # plt.close()
        # values = []
        mod, values = FastUnfolding()
        nx.draw_networkx(G, pos, node_color=values, with_labels=True)
        plt.title('Page2')
        pdf.savefig()  # saves the current figure into a pdf page
        plt.close()
        # print("mod-----------", mod)
        # print("values-----------", values)

        # 过程
        x1 = y1 = np.arange(-1, 15, 0.1)
        x1, y1 = np.meshgrid(x1, y1)
        plt.contour(x1, y1, (x1 - 7) ** 2 + (y1 - 7) ** 2, [49])
        plt.axis('scaled')

        values2 = [0, 0, 0, 0, 1, 2, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 2, 3, 3, 3, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5]
        nx.draw_networkx(G, pos, node_color=values2, with_labels=True)
        plt.title('Page3')
        pdf.savefig()  # saves the current figure into a pdf page
        plt.close()


        return mod

def FastUnfolding():
    vector_dict, edge_dict = Louvain.loadData("E:\\脑电python3\\ceshi\\node.txt")
    mod, values = Louvain.fast_unfolding(vector_dict, edge_dict)
    return mod, values






