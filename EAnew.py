#!/usr/bin/python3
# coding: utf8

import numpy as np
import random
import pandas as pd


def pandas_txt(name, num):
    df = pd.read_table(name, sep=':', header=None)
    key_list = []
    for a in df[0]:
        key_list.append(a.strip())
    value_list = []
    for b in df[1]:
        value_list.append(str(b))
    data = []
    i = 1
    while i < num:
        bag_dict = {}
        value_dict = {}
        value_dict[key_list[i + 1]] = value_list[i + 1]
        value_dict[key_list[i + 2]] = value_list[i + 2]
        bag_dict[key_list[i]] = value_dict
        data.append(bag_dict)
        i = i + 3
    return data


# Initialize the population, popsize is the population size, n chromosome length
def init(times):
    p_initial_data_list = []
    p_bag_initial_data_list = []

    p_bag_initial_data_dict = {}

    i = 0
    while i < times:

        # 生成含有100个0的列表
        bag_initial_list = [0] * 100
        # print(bag_initial_list)
        # print(len(bag_initial_list))

        # 选取bag的数量范围
        bag_num_score = [45, 55]

        # 随机选取bag的数量范围的一个值
        bag_num_random_int = random.randint(bag_num_score[0], bag_num_score[1])
        # print(bag_num_random_int)

        # 生成需要选取的bag的标号num
        select_sign_list = random.sample(range(0, 99), bag_num_random_int)
        # print(select_sign_list)
        # print(len(select_sign_list))

        # 生成bag_list, 格式：[[bag1, bag28], [bag94,bag6]]
        bag_select_sign_list = []
        for each_select_sign in select_sign_list:
            bag_select_sign_list.append('bag ' + str(each_select_sign + 1))

        # print(bag_select_sign_list)
        p_bag_initial_data_list.append(bag_select_sign_list)

        # 循环更替初始bag__initial_list
        for each_sign in select_sign_list:
            bag_initial_list[each_sign] = 1

        # print(bag__initial_list)

        # 将生成方案汇总到总表里
        p_initial_data_list.append(bag_initial_list)

        p_bag_initial_data_dict['p ' + str(i + 1)] = bag_select_sign_list

        i += 1
    return p_initial_data_list, p_bag_initial_data_list, p_bag_initial_data_dict


def get_bag_params(sum_list, bag_list):
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


def get_p_father(times ,value_list):
    father = random.randint(0, times - 1)
    mother = random.randint(0, times - 1)

    if value_list[father] >= value_list[mother]:
        return all_sign_list[father]
    else:
        return all_sign_list[mother]


name = 'docs/BankProblem.txt'
data = pandas_txt(name, 301)

times = 10
all_sign_list, p_bag_initial_data_list, p_bag_initial_data_dict = init(times)


p_num =2
mutation_num =1
cycles_times = 1000
i = 0
while i < cycles_times:

    value_list = []
    weight_list = []
    for each_p in all_sign_list:
        bag_name_list = []
        for m in each_p:
            if m ==1 :
                bag_name_list.append('bag ' + str(each_p.index(m)+1))
            else:
                pass

        sum_weight, sum_value = get_bag_params(data, bag_name_list)
        weight_list.append(sum_weight)
        value_list.append(sum_value)

    # total_weight, total_value = get_bag_info(sum_list, p_initial_population_list)
    print(value_list)

    a = get_p_father(times ,value_list)
    b = get_p_father(times ,value_list)
    print(a)

    cross_num = random.randint(1, len(a)-1)
    a_list_left = a[0:cross_num]
    a_list_right = a[cross_num:len(a)-1]

    # b
    b_list_left = b[0:cross_num]
    b_list_right = b[cross_num:len(b)-1]

    c = a_list_left + b_list_right
    d = b_list_left + a_list_right

    choose_mutation_list = random.sample(range(0, len(c)), mutation_num)

    # c 进行mutation 成 e
    for each_c_mutation in choose_mutation_list:
        if c[each_c_mutation] == 1:
            c[each_c_mutation] = 0
        else:
            c[each_c_mutation] = 1

    e = c

    for each_d_mutation in choose_mutation_list:
        if d[each_d_mutation] == 1:
            d[each_d_mutation] = 0
        else:
            d[each_d_mutation] = 1

    f = d

    bag_name_list = []
    for m in e:
        if m == 1:
            bag_name_list.append('bag ' + str(e.index(m) + 1))
        else:
            pass

    sum_weight, sum_value = get_bag_params(data, bag_name_list)
    if sum_weight <= 285:
        if sum_value > min(value_list):
            index = value_list.index(min(value_list))
            all_sign_list[index] = all_sign_list
        else:
            pass
    else:
        pass

    new_value = []
    new_weight = []
    for each_new_p in all_sign_list:
        bag_name_list = []
        for m in each_new_p:
            if m == 1:
                bag_name_list.append('bag ' + str(each_new_p.index(m) + 1))
            else:
                pass
        new_each_weight, new_each_value = get_bag_params(data, bag_name_list)
        new_weight.append(new_each_weight)
        new_value.append(new_each_value)
    print(new_value)
    print('最大价值为：' + str(max(new_value)))
    print(i)
    i += 1







