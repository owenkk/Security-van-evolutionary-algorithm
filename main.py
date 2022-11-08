#!/usr/bin/python3
# coding: utf8

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


def set_p_num(sum_list, p_times, van_capacity):
    p_data_dict = {}
    i = 0
    while i < p_times:
        # capacity = 0
        sum_capacity = 0
        bag_list = []
        random_int_list = []
        while sum_capacity < van_capacity:
            # random int
            random_int = random.randint(0, 99)
            # print(random_int)
            #需要去重
            if random_int in random_int_list:
                random_int = random.randint(0, 99)
            else:
                random_int_list.append(random_int)

            capacity = sum_list[random_int]
            # print(capacity)
            key = 'bag ' + str(random_int + 1)
            # print(key)
            # print(type(key))
            # print(capacity[key]["weight"])
            bag_list.append(key)
            weight = capacity[key]["weight"]
            sum_capacity = sum_capacity + float(weight)
            if sum_capacity > 285:
                sum_capacity = sum_capacity - float(weight)
                del (bag_list[-1])
                break
        # print(sum_capacity)
        # print(bag_list)
        # print(random_int_list)
        p_data_dict['p' + str(i + 1)] = bag_list
        # print(i)
        i += 1

    return p_data_dict


def get_p_father(p_father_num):
    # p_father_num = 2
    random_int = random.sample(range(1, p_times+1), p_father_num)
    print(random_int)
    p_father_dict = {}
    p_father_list = []
    for i in random_int:
        # print(i)
        p_father_dict['p' + str(i)] = p_data['p' + str(i)]
        p_father_list.append(p_data['p' + str(i)])

    # print(p_father_dict)

    return p_father_dict, p_father_list


def get_bag_params(bag_list):
    bag_capacity_sum = 0
    bag_value_sum = 0
    print(bag_list)
    for each_bag in bag_list:
        each_bag_split = each_bag.split(' ')
        each_bag_num = each_bag_split[1]
        bag_params = sum_list[int(each_bag_num)-1]
        # 这个遇到一个bug，，会有bag 0 的出现
        # 这个遇到一个bug，，会有bag 0 的出现
        # 这个遇到一个bug，，会有bag 0 的出现
        try:
            each_bag_capacity = bag_params[each_bag]['weight']
        except KeyError:
            print('KeyError: bag 0')

        # 这个遇到一个bug，，会有bag 0 的出现
        # 这个遇到一个bug，，会有bag 0 的出现
        # 这个遇到一个bug，，会有bag 0 的出现
        bag_capacity_sum = float(bag_capacity_sum) + float(each_bag_capacity)

        # 这个遇到一个bug，，会有bag 0 的出现
        bag_value = bag_params[each_bag]['value']
        # 这个遇到一个bug，，会有bag 0 的出现

        bag_value_sum = bag_value_sum + float(bag_value)
    # print(bag_capacity_sum)
    # print(bag_value_sum)

    return bag_capacity_sum, bag_value_sum


# 用于读取文本数据
text_name = 'docs/BankProblem.txt'
text_num = 301
sum_list = read_data(text_name, text_num)


# print(sum_list)
'''
格式：[{'bag 1': {'weight': '9.4', 'value': '57.0'}}, {'bag 2': {'weight': '7.4', 'value': '94.0'}},
'''


# 获取随机p
p_times = 3
van_capacity = 285
p_data = set_p_num(sum_list, p_times, van_capacity)
# print(p_data)
'''
# 格式
{'p1': ['bag 11', 'bag 57', 'bag 73', 'bag 56', 'bag 15', 'bag 76', 'bag 13', 'bag 65', 'bag 84', 'bag 38', 'bag 76', 'bag 39', 'bag 100', 'bag 53', 'bag 28', 'bag 38', 'bag 98', 'bag 36', 'bag 62', 'bag 36', 'bag 51', 'bag 77', 'bag 54', 'bag 74', 'bag 37', 'bag 97', 'bag 29', 'bag 32', 'bag 10', 'bag 3', 'bag 91', 'bag 75', 'bag 23', 'bag 66', 'bag 47', 'bag 68', 'bag 35', 'bag 83', 'bag 92', 'bag 94', 'bag 88', 'bag 45', 'bag 39', 'bag 18', 'bag 70'], 'p2': ['bag 75', 'bag 84', 'bag 32'
'''

# 随机抽取两个父母 a 和 b
p_father_num = 2
p_father_dict_res, p_father_list = get_p_father(p_father_num)
# print(p_father_dict_res)


# 计算p的capacity and value
p_sumvalue_dict = {}
for each_p in p_data:
    # print(each_p)
    each_p_baglist = p_data[each_p]
    each_p_capacity_sum, each_p_value_sum = get_bag_params(each_p_baglist)
    p_sumvalue_dict[each_p] = each_p_value_sum

# print(p_sumvalue_dict)

p_sum_value_dict_sort = sorted(p_sumvalue_dict.items(), key=lambda x: x[1])
# print(p_sum_value_dict_sort)


'''
终止标准，循环体
'''
termination_times = 10

cycles_times = 0
while cycles_times < termination_times:
    # 从列表随机抽取多个元素
    a_list = p_father_list[0]
    # print(a_list)
    # print(len(a_list))
    a_choice_part = sample(a_list, 5)
    # print(a_choice_part)

    b_list = p_father_list[1]
    # print(b_list)
    b_choice_part = sample(b_list, 5)
    # print(b_choice_part)

    # crossover c and d: remove
    for i in a_choice_part:
        # print(i)
        a_list.remove(i)

    # print(a_list)
    # print(len(a_list))
    for o in b_choice_part:
        # print(i)
        b_list.remove(o)
    # print(b_list)

    for m in b_choice_part:
        a_list.append(m)
    # print(a_list)
    c_list = a_list

    for n in a_choice_part:
        b_list.append(n)
    # print(b_list)
    d_list = b_list

    # c and d 运行变异生成e
    random_mutation_int_list = []
    while len(random_mutation_int_list) < 5:
        random_mutation_int = random.randint(0, 99)
        key = 'bag ' + str(random_mutation_int + 1)
        # print(key)
        if key in c_list:
            random_mutation_int = random.randint(0, 99)
        else:
            random_mutation_int_list.append(random_mutation_int)

    # print(random_mutation_int_list)

    e_remove_list = sample(c_list, 5)
    for b in e_remove_list:
        c_list.remove(b)
    for v in random_mutation_int_list:
        key = 'bag ' + str(v)
        c_list.append(key)

    e_list = c_list
    # print(e_list)

    # c and d 运行变异生成f
    random_mutation_int_list = []
    while len(random_mutation_int_list) < 5:
        random_mutation_int = random.randint(0, 99)
        key = 'bag ' + str(random_mutation_int + 1)
        # print(key)
        if key in d_list:
            random_mutation_int = random.randint(0, 99)
        else:
            random_mutation_int_list.append(random_mutation_int)

    # print(random_mutation_int_list)

    f_remove_list = sample(d_list, 5)
    for c in f_remove_list:
        d_list.remove(c)
    for x in random_mutation_int_list:
        key = 'bag ' + str(x)
        d_list.append(key)

    f_list = d_list
    # print(f_list)

    # 评估 e and f 的可行性

    # 评估e
    e_capacity_sum, e_value_sum = get_bag_params(e_list)

    # 评估f
    f_capacity_sum, f_value_sum = get_bag_params(f_list)

    '''
    # 计算p的capacity and value
    p_sumvalue_dict = {}
    for each_p in p_data:
        # print(each_p)
        each_p_baglist = p_data[each_p]
        each_p_capacity_sum, each_p_value_sum = get_bag_params(each_p_baglist)
        p_sumvalue_dict[each_p] = each_p_value_sum

    # print(p_sumvalue_dict)

    p_sum_value_dict_sort = sorted(p_sumvalue_dict.items(), key=lambda x: x[1])
    # print(p_sum_value_dict_sort)
    '''

    # print(type(p_sum_value_dict_sort[0][1]))
    # 替换
    # final_p_sum_value_dict_sort = []
    # print(e_capacity_sum)
    # print(e_value_sum)
    if e_capacity_sum > 285:
        # print(2)
        final_p_sum_value_dict_sort = p_sum_value_dict_sort
    else:
        # print(3)
        if e_capacity_sum > int(p_sum_value_dict_sort[0][1]):
            # 替换
            # print(1)
            p_data[str(p_sum_value_dict_sort[0][0])] = e_list
        else:
            # print(4)
            pass

    # print(p_sum_value_dict_sort)

    # f 运行最弱替换

    if f_capacity_sum > 285:
        # print(2)
        p_sum_value_dict_sort = p_sum_value_dict_sort
    else:
        # print(3)
        if f_capacity_sum > int(p_sum_value_dict_sort[0][1]):
            # 替换
            # print(1)
            p_data[str(p_sum_value_dict_sort[0][0])] = f_list
        else:
            # print(4)
            pass

    # print(p_sum_value_dict_sort)

    print(cycles_times)
    cycles_times += 1


print(p_sum_value_dict_sort)











