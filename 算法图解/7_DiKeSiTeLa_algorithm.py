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
# 设定无穷大
infinity = float("inf")

# 整体开销如下
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 还需要一个存储父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 最后，你需要一个数组，用于记录处理过的节点，因为对于同一个节点，你不用处理多次。
processed = []


# 寻找开销最低的节点
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 具体处理
# 在未处理的节点中找出开销最小的点
node = find_lowest_cost_node(costs)
# while循环在所有节点被处理过后结束
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # 遍历当前节点的所有邻居
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # 若经当前节点前往该邻居更近
        if costs[n] > new_cost:
            # 曾更新该邻居的开销
            costs[n] = new_cost
            # 同时将该邻居的父节点设置为当前节点
            parents[n] = node
            processed.append(node) #将当前节点标记为处理过
            node = find_lowest_cost_node(costs) #找出接下来要处理的节点，并循环


