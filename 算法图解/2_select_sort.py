# encoding: utf-8
"""
@author: Mengrui
@contact: 1025888636@qq.com
@time: 2019/9/6 18:04
@file: 2_select_sort.py
@desc: 选择排序：先构造找最小值(也可以直接用min函数)
"""

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if smallest > arr[i]:
            smallest_index = i
    return smallest_index

def select_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr

L = [5,7,4,8,6,9,11]
print(select_sort(L))