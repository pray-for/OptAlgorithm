import igraph
import networkx as nx

# filename1 = "D:\\文件\\研究生\\参考论文\\dolphins\\dolphins.gml"
filename2 = "D:\\文件\\研究生\\参考论文\\论文数据集\\football\\football.gml"
# g1 = igraph.Graph.Read_GML(filename1)
# print(g1)
print("-----------------")
g2 = igraph.Graph.Read_GML(filename2)
print(g2)

# 抽取gml中的数据
# networkx可以直接通过函数从gml文件中读出数据
# def read_gml(data):
#     print("***")
#     H = nx.read_gml(data)
#     print(H)
#     # print(H.edges())
#
# print('---------------gml------------------')
# read_gml("D:\\文件\\研究生\\参考论文\\1cb356a81163bac2e0930d491357946e\\karate.gml")


