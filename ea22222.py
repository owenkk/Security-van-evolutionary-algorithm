#!/usr/bin/python3
# coding: utf8

import time

import pandas as pd
import random
from random import sample


def read_data(text_name_input, text_num_input):
    df = pd.read_table(text_name_input, sep=':', header=None)
    key_list = []
    for a in df[0]:
        key_list.append(a.strip())
    value_list = []
    for b in df[1]:
        value_list.append(str(b))
    sum_dict = {}
    sum_list = []
    i = 1
    while i < text_num_input:
        bag_dict = {}
        value_dict = {}
        value_dict[key_list[i + 1]] = value_list[i + 1]
        value_dict[key_list[i + 2]] = value_list[i + 2]
        bag_dict[key_list[i]] = value_dict
        sum_list.append(bag_dict)
        i = i + 3
    return sum_list


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


def get_p_father(p_father_num):
    final_p_father_dict = {}
    final_p_father_list = []
    final_p_father_sign_list = []

    choice_times = 0

    while choice_times < p_father_num:
        random_int = random.sample(range(0, p_times), p_father_num)
        # print(random_int)
        p_father_initial_data_list = []
        p_father_bag_initial_data_list = []

        for each_random_int in random_int:
            # print(each_random_int)
            p_father_initial_data_list.append(p_initial_data_list[each_random_int])
            p_father_bag_initial_data_list.append(p_bag_initial_data_list[each_random_int])

        # 将随机选取的2个p按照大小顺序排序
        p_father_sum_value_dict = {}
        p_father_sum_value_i = 1
        for each_father_p in p_father_bag_initial_data_list:
            each_p_father_capacity_sum, each_p_father_value_sum = get_bag_params(each_father_p)
            p_father_sum_value_dict['p ' + str(p_father_sum_value_i)] = each_p_father_value_sum
            p_father_sum_value_i += 1

        p_father_sum_value_dict_sort = sorted(p_father_sum_value_dict.items(), key=lambda x: x[1])
        # print(p_father_sum_value_dict_sort)
        # print(p_father_bag_initial_data_list)

        # 选取较大值存放总father表
        p_father_sum_value_dict_sort_num = int(p_father_sum_value_dict_sort[1][0].split(' ')[1]) - 1
        final_p_father_dict[p_father_sum_value_dict_sort[1][0]] = p_father_bag_initial_data_list[p_father_sum_value_dict_sort_num]
        # print(final_p_father_dict)
        final_p_father_list.append(p_father_bag_initial_data_list[p_father_sum_value_dict_sort_num])
        final_p_father_sign_list.append(p_initial_data_list[p_father_sum_value_dict_sort_num])

        choice_times += 1

    return final_p_father_dict, final_p_father_list, final_p_father_sign_list




'''
text_name: 需要读取的文件的地址path
text_num：需要读取的文件的行数
sum_list：文件读取后，存放的列表
sum_list格式：[{'bag 1': {'weight': '9.4', 'value': '57.0'}}, {'bag 2': {'weight': '7.4', 'value': '94.0'}},
'''
text_name = 'docs/BankProblem.txt'
text_num = 301
sum_list = read_data(text_name, text_num)
# print(sum_list)

'''
p_times = 2
len_list = 100

sum_random_list = []
sum_random_bag_list = []

i = 0

while i < p_times:

    random_list = []
    while len(random_list) < 100:
        random_list.append(random.randint(0, 1))

    print(random_list)
    print(len(random_list))
    sum_random_list.append(random_list)

    random_bag_list = []
    index_num = 1
    for each_bag in random_list:
        if each_bag == 1:
            random_bag_list.append('bag ' + str(index_num))
        else:
            pass
        index_num += 1
    print(random_bag_list)
    print(len(random_bag_list))

    i += 1
'''

p_times = 50
p_initial_data_list = []
p_bag_initial_data_list = []

p_bag_initial_data_dict = {}

i = 0
while i < p_times:



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
        bag_select_sign_list.append('bag ' + str(each_select_sign+1))

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

# print(p_initial_data_list)
# print(len(p_initial_data_list))

# print(p_bag_initial_data_list)
# print(len(p_bag_initial_data_list))

# print(p_bag_initial_data_dict)

# 计算p_data的value值
p_sum_value_dict = {}
for each_p_list in p_bag_initial_data_dict:
    # print(each_p_list)
    # print(each_p_bag_list)
    each_p_bag_list = p_bag_initial_data_dict[each_p_list]
    each_p_capacity_sum, each_p_value_sum = get_bag_params(each_p_bag_list)
    p_sum_value_dict[each_p_list] = each_p_value_sum

# print(p_sum_value_dict)
p_sum_value_dict_sort = sorted(p_sum_value_dict.items(), key=lambda x: x[1])
print(p_sum_value_dict_sort)
time.sleep(5)

termination_times = 10000

cross_num = 10
mutation_num = 5
p_father_num = 2
p_father_dict_res, p_father_list, p_father_sign_list = get_p_father(p_father_num)

cycles_times = 0
while cycles_times < termination_times:
    print('进行第' + str(cycles_times))

    total_value = []
    total_weight = []
    weight = 0
    value = 0
    for p in p_initial_data_list:
        for i in range(len(p)):
            if p[i] == 1:
                bag_params = sum_list[int(i)]
                bag_weight = bag_params['bag ' + str(i + 1)]['weight']
                bag_value = bag_params['bag ' + str(i + 1)]['value']
                weight = weight + float(bag_weight)
                value = value + int(bag_value)


    # print(p_father_dict_res)
    # print(p_father_list)
    # print(p_father_sign_list)

    a_list = p_father_sign_list[0]
    b_list = p_father_sign_list[1]

    random_a_int = random.randint(0, 99)

    a_list_left = a_list[0:random_a_int]
    a_list_right = a_list[random_a_int:len(a_list) - 1]

    # b
    b_list_left = b_list[0:random_a_int]
    b_list_right = b_list[random_a_int:len(a_list) - 1]

    c_list = a_list_left + b_list_right
    d_list = b_list_left + a_list_right
    # print(c_list)


    # 进行变异得到e and f
    c_mutation_list = random.sample(range(0, len(c_list) - 1), mutation_num)

    # c 进行mutation 成 e
    for each_c_mutation in c_mutation_list:
        if c_list[each_c_mutation] == 0:
            c_list[each_c_mutation] = 1
        else:
            c_list[each_c_mutation] = 0

    # mutation 得到e
    e_list = c_list
    # print(e_list)


    # d进行变异
    d_mutation_list = random.sample(range(0, len(d_list) - 1), mutation_num)
    # d 进行mutation 成 f
    for each_d_mutation in d_mutation_list:
        if d_list[each_d_mutation] == 0:
            d_list[each_d_mutation] = 1
        else:
            d_list[each_d_mutation] = 0

    f_list = d_list

    bag_list = [x for x, y in list(enumerate(e_list)) if y == 1]
    bag_num_list = []
    for each_num in bag_list:
        bag_num_list.append('bag ' + str(int(each_num) + 1))

    # print(bag_num_list)
    bag_capacity_sum, bag_value_sum = get_bag_params(bag_num_list)
    # print(bag_capacity_sum)
    # print(bag_value_sum)

    if bag_capacity_sum <= 285:
        if bag_value_sum > p_sum_value_dict_sort[len(p_sum_value_dict_sort)-1][1]:
            p_bag_initial_data_dict[list(p_father_dict_res)[0]] = bag_num_list
            # print(1)
        else:

            pass
    else:
        pass

    bag_list = [x for x, y in list(enumerate(f_list)) if y == 1]
    bag_num_list = []
    for each_num in bag_list:
        bag_num_list.append('bag ' + str(int(each_num) + 1))

    # print(bag_num_list)
    bag_capacity_sum, bag_value_sum = get_bag_params(bag_num_list)
    # print(bag_capacity_sum)
    # print(bag_value_sum)

    # 计算p_data的value值
    p_sum_value_dict = {}
    for each_p_list in p_bag_initial_data_dict:
        # print(each_p_list)
        # print(each_p_bag_list)
        each_p_bag_list = p_bag_initial_data_dict[each_p_list]
        each_p_capacity_sum, each_p_value_sum = get_bag_params(each_p_bag_list)
        p_sum_value_dict[each_p_list] = each_p_value_sum

    # print(p_sum_value_dict)
    p_sum_value_dict_sort = sorted(p_sum_value_dict.items(), key=lambda x: x[1])
    # print(p_sum_value_dict_sort)

    if bag_capacity_sum <= 285:
        if bag_value_sum > p_sum_value_dict_sort[len(p_sum_value_dict_sort)-1][1]:
            p_bag_initial_data_dict[list(p_father_dict_res)[0]] = bag_num_list

            # print(1)
        else:

            pass
    else:
        pass


    cycles_times += 1


# print(p_bag_initial_data_dict)

# 计算p_data的value值
p_sum_value_dict = {}
for each_p_list in p_bag_initial_data_dict:
    # print(each_p_list)
    # print(each_p_bag_list)
    each_p_bag_list = p_bag_initial_data_dict[each_p_list]
    each_p_capacity_sum, each_p_value_sum = get_bag_params(each_p_bag_list)
    print(each_p_capacity_sum)
    if each_p_capacity_sum <= 285:

        p_sum_value_dict[each_p_list] = each_p_value_sum


p_sum_value_dict_sort = sorted(p_sum_value_dict.items(), key=lambda x: x[1])
print(p_sum_value_dict_sort)
