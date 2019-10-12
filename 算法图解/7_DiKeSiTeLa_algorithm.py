# encoding: utf-8
"""
@author: Mengrui
@contact: 1025888636@qq.com
@time: 2019/10/12 9:55
@file: 7_DiKeSiTeLa_algorithm.py
@desc: 狄克斯特拉算法
"""

# 创建散列表存储邻居和开销
graph = {}
graph["start"]={}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# 存储节点的开销


