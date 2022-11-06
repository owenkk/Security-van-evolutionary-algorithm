#!/usr/bin/python3
# coding: utf8

import pandas as pd
import random


df=pd.read_table('BankProblem.txt', sep=':', header=None)
# print(df)
#

# print(df[2:3])
key_list = []
for a in df[0]:
    key_list.append(a.strip())
# print(key_list)
# print(len(key_list))
# #
value_list = []
for b in df[1]:
    value_list.append(str(b))
# print(value_list)
# print(value_list[1])
# print(len(value_list))
# dict = {}
sum_dict = {}
sum_list = []
# van_dict = {}
# van_dict[key_list[0]] = value_list[0]
# sum_list.append(van_dict)
i = 1
while i < 301:
    # print(i)
    # print(key_list[i])
    # print(value_list[i])
    bag_dict = {}
    value_dict = {}
    value_dict[key_list[i+1]] = value_list[i+1]
    value_dict[key_list[i+2]] = value_list[i+2]
    bag_dict[key_list[i]] = value_dict
    # print(bag_dict)
    sum_list.append(bag_dict)
    i = i + 3

# print(sum_list)
# 生成最终读取列表
# print(len(sum_list))




# capacity = 0
sum_capacity = 0
bag_list = []
while sum_capacity < 285:

# random int
    random_int = random.randint(0, 99)
    print(random_int)
    capacity = sum_list[random_int]

# print(capacity)
    key = 'bag ' + str(random_int+1)
    # print(key)
    # print(type(key))
    # print(capacity[key]["weight"])
    bag_list.append(key)

    weight = capacity[key]["weight"]

    sum_capacity = sum_capacity + float(weight)
    if sum_capacity > 285:
        sum_capacity = sum_capacity - float(weight)
        del(bag_list[-1])
        break


print(sum_capacity)

print(bag_list)
