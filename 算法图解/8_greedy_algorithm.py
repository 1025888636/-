# encoding: utf-8
"""
@author: Mengrui
@contact: 1025888636@qq.com
@time: 2019/10/14 15:59
@file: 8_greedy_algorithm.py
@desc: 贪心算法
"""

#  传入一个数组，它被转换为集合
states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])  # 表示要覆盖的州

# 用散列表表示可供选择的广播台清单
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 需要一个集合来存储最终选择的广播台
final_stations = set()


while states_needed:
    # 正确的解可能有多个。你需要遍历所有的广播台，从中选择覆盖了最多的未覆盖州的广播台。将这个广播台存储在best_station中。
    best_stations = None
    # states_covered是一个集合，包含该广播台覆盖的所有未覆盖的州。
    states_covered = set()
    for station, states in stations.items():
        print(station, "——", states)
        covered = states_needed & states
        print("0_covered is", covered)
        print("states_covered is ",states_covered)
        if len(covered) > len(states_covered):
            best_station = station
            print("1_best_station is",best_station)
            states_covered = covered
            print("2_states_covered is",states_covered)
    states_needed -= states_covered
    print("3_states_needed",states_needed)
    final_stations.add(best_station)
    print("4_final_stations",final_stations)
    print("**************************")
print(final_stations)
