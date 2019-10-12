# encoding: utf-8
"""
@author: Mengrui
@contact: 1025888636@qq.com
@time: 2019/10/10 15:47
@file: 4_quick_sort.py
@desc: 分而治之的思想，代表之一是快速排序
"""

def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <=pivot]
        greater = [i for i in arr[1:] if i >pivot]
        return quick_sort(less)+[pivot] + quick_sort(greater)

print(quick_sort([10,5,2,1,4,3]))

