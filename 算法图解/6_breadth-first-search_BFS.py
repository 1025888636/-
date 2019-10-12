# encoding: utf-8
"""
@author: Mengrui
@contact: 1025888636@qq.com
@time: 2019/10/11 16:42
@file: 6_breadth-first-search_BFS.py
@desc: 广度优先搜索
"""

from collections import deque
import pysnooper
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# search_queue = deque()
# search_queue += graph["you"]

def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    print("0",search_queue)
    searched = [] #这个数组用于记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        print("person is ",person)
        if person not in searched:  # 仅当这个人没检查过时才检查
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                print("search_queue=",search_queue)
                searched.append(person)  #将这个人标记为检查过
                print("searched=",searched)
                print("********************************")
    return False


search("you")