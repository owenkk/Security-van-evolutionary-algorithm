#!/usr/bin/python3
# coding: utf8

import pandas as pd
import random
def get_bag_params(bag_list):
    bag_capacity_sum = 0
    bag_value_sum = 0
    # print(bag_list)
    for each_bag in bag_list:
        each_bag_split = each_bag.split(' ')
        each_bag_num = each_bag_split[1]
        bag_params = sum_list[int(each_bag_num) - 1]
        each_bag_capacity = bag_params[each_bag]['weight']
        bag_capacity_sum = float(bag_capacity_sum) + float(each_bag_capacity)
        bag_value = bag_params[each_bag]['value']
        bag_value_sum = bag_value_sum + float(bag_value)

    return bag_capacity_sum, bag_value_sum

df=pd.read_table('../docs/BankProblem.txt', sep=':', header=None)
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
#
# fit_num_list = []
# a = 1
# for i in sum_list:
#     fit = i['bag ' + str(a)]
#     fir_num =  float(fit['value']) / float(fit['weight'])
#     fit_num_list.append(fir_num)
#     a += 1
#
# print(fit_num_list)
#
d = {'name': 'kk'}
key = list(d)[0]
print(key)

# print(fit_num_list)
#
#
# # capacity = 0
# sum_capacity = 0
# bag_list = []
# while sum_capacity < 285:
#
# # random int
#     random_int = random.randint(0, 99)
#     print(random_int)
#     capacity = sum_list[random_int]
#
# # print(capacity)
#     key = 'bag ' + str(random_int+1)
#     # print(key)
#     # print(type(key))
#     # print(capacity[key]["weight"])
#     bag_list.append(key)
#
#     weight = capacity[key]["weight"]
#
#     sum_capacity = sum_capacity + float(weight)
#     if sum_capacity > 285:
#         sum_capacity = sum_capacity - float(weight)
#         del(bag_list[-1])
#         break
#
#
# print(sum_capacity)
#
# print(bag_list)
