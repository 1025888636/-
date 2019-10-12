# # 求1-100以内的和
# sum = 0
# n = 100
# counter = 1
# while  counter <= n:
# 	sum = sum + counter
# 	counter += 1
# print('1到%d以内的数相加之和为: %d' % (n,sum))
#
# var = 1
# while var == 1:  # 表达式永远为 true
# 	num = int(input("输入一个数字  :"))
# 	print("你输入的数字是: ", num)
#
# print("Good bye!")

# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")

for letter in 'Runoob':
	if letter == 'b':
		break
	print('当前字母为：', letter)

for zimu in 'Runoob':
	if zimu == 'o':
		continue
	print('当前zimu为：', zimu)



var = 10  # 第二个实例
while var > 0:
	print('当期变量值为 :', var)
	var = var - 1
	if var == 5:
		break

print("Good bye!")

var = 10  # 第四个实例
while var > 0:
	print('当期变量值为 :', var)
	var = var - 1
	if var == 5:
		continue
	print('当期变量值为 :', var)

print("Good bye!")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')