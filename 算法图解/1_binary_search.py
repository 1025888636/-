# encoding: utf-8
"""
@author: Mengrui
@contact: 1025888636@qq.com
@time: 2019/9/6 14:34
@file: 1_binary_search.py
@desc: 《算法图解》第一章“算法简介”
"""

# def binary_search(target,arr):
#     low = arr[0]
#     hight = arr[-1]
#     mid = (low+hight)/2
#     if arr[mid] < target:
#         low=mid+1
#     elif arr[mid] > target:
#         hight = mid -1
#     else :
#         arr[mid] = target
#     return  s
# shit！！！low和high是位置。。。不是值


def binary_search(arr,target):
    low = 0
    hight = len(arr)-1
    # mid = (low + hight) // 2 放在此处是不对的，会使while陷入死循环
    while low <= hight:
        mid = (low + hight) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            hight = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,6,8]
print(binary_search(my_list,3))
