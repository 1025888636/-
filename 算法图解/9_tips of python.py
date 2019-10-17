# encoding: utf-8
"""
@author: Mengrui
@contact: 1025888636@qq.com
@time: 2019/10/17 14:19
@file: 9_tips of python.py
@desc: 30s学会一个python小技巧
"""

# 3. List：bifurcate
# 功能实现：将列表值分组。如果在filter的元素是True，那么对应的元素属于第一个组；否则属于第二个组。
# 解读：使用列表推导式和enumerate()基于filter元素到各组。
def bifurcate(lst, filter):
  return [
    [x for i,x in enumerate(lst) if filter[i] == True],
    [x for i,x in enumerate(lst) if filter[i] == False]
  ]

# l =bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# print(l)

# 4. List：difference
# 功能实现：返回两个iterables间的差异。
# 解读：创建b的集合，使用a的列表推导式保留不在_b中的元素。

def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]


# m = difference([1, 2, 3], [1, 2, 4])
# print(m)

# 5. List：flatten
# 功能实现：一次性的整合列表。
# 解读：使用嵌套的列表提取子列表的每个值。

def flatten(lst):
    print([x for x in lst])
    return [x for y in lst for x in y]

# l = flatten([[1,2,3,4],[5,6,7,8]]) # [1, 2, 3, 4, 5, 6, 7, 8]
# print(l)


# 6. Math：digitize
# 功能实现：将一个数分解转换为个位数字。
# 解读：将n字符化后使用map()函数结合int完成转化

def digitize(n):
  print(map(int, str(n)))
  return list(map(int, str(n)))
#举例：

# print(digitize(123)) # [1, 2, 3]

# 7. List：shuffle
# 功能实现：将列表元素顺序随机打乱。
# 解读：使用Fisher-Yates算法重新排序列表元素。

from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst


#举例：
foo = [1,2,3,4,5,6,7,8]
print(shuffle(foo)) # [2,3,1] , foo = [1,2,3]


# 9. String：byte_size
# 功能实现：返回字符串的字节数。
# 解读：使用string.encode('utf-8')解码给定字符串，返回长度。

def byte_size(string):
  return len(string.encode('utf-8'))


# 举例：
byte_size('😀') # 4
byte_size('Hello World') # 11



# 10. Math：gcd
# 功能实现：计算几个数的最大公因数。
# 解读：使用reduce()和math.gcd在给定列表上实现。

from functools import reduce
import math

def gcd(numbers):
  return reduce(math.gcd, numbers)


# 举例：
gcd([8,36,28]) # 4