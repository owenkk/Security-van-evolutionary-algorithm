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
            # 需要去重
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


def set_p_bag_num(sum_list, p_times, bag_num_score):
    bag_num_score = [50, 85]
    p_data_dict = {}
    i = 0
    while i < p_times:
        bag_num_random_int = random.randint(50, 60)
        bag_list = []
        while len(bag_list) < bag_num_random_int:

            random_int = random.randint(1, 100)
            key = 'bag ' + str(random_int)
            while key in bag_list:
                random_int = random.randint(1, 100)
                key = 'bag ' + str(random_int)

            bag_list.append(key)

        p_data_dict['p' + str(i + 1)] = bag_list
        i += 1

    return p_data_dict


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

    choice_times = 0
    while choice_times < p_father_num:
        random_int = random.sample(range(1, p_times + 1), p_father_num)
        # print(random_int)
        p_father_dict = {}
        p_father_list = []

        for each_random_int in random_int:
            # print(each_random_int)
            p_father_dict['p' + str(each_random_int)] = p_fit_data['p' + str(each_random_int)]
            p_father_list.append(p_fit_data['p' + str(each_random_int)])

        # print(p_father_dict)
        # print(p_father_list)

        # 将随机选取的2个p按照大小顺序排序
        p_father_sum_value_dict = {}
        for each_father_p in p_father_dict:
            each_p_father_list = p_father_dict[each_father_p]
            each_p_father_capacity_sum, each_p_father_value_sum = get_bag_params(each_p_father_list)
            p_father_sum_value_dict[each_father_p] = each_p_father_value_sum

        p_father_sum_value_dict_sort = sorted(p_father_sum_value_dict.items(), key=lambda x: x[1])
        # print(p_father_sum_value_dict_sort)

        # 选取较大值存放总father表
        final_p_father_dict[p_father_sum_value_dict_sort[1][0]] = p_data[p_father_sum_value_dict_sort[1][0]]
        # print(final_p_father_dict)
        final_p_father_list.append(p_data[p_father_sum_value_dict_sort[1][0]])

        choice_times += 1

    return final_p_father_dict, final_p_father_list


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


p_times = 10
van_capacity = 300
bag_num_score = [50, 100]
p_fit_data = set_p_num(sum_list, p_times, van_capacity)
# print(p_fit_data)

p_data = set_p_bag_num(sum_list, p_times, bag_num_score)
# print(p_data)


# 计算p_data的value值
p_sum_value_dict = {}

for each_p_list in p_fit_data:
    # print(each_p_list)
    each_p_bag_list = p_fit_data[each_p_list]
    # print(each_p_bag_list)
    each_p_capacity_sum, each_p_value_sum = get_bag_params(each_p_bag_list)
    p_sum_value_dict[each_p_list] = each_p_value_sum

# print(p_sum_value_dict)
p_sum_value_dict_sort = sorted(p_sum_value_dict.items(), key=lambda x: x[1])
print(p_sum_value_dict_sort)

'''
终止标准，循环体
'''

termination_times = 10000
cross_num = 30
mutation_num = 1

final_p_sum_value_dict_sort = []


cycles_times = 0

while cycles_times < termination_times:
    print('循环第 ' + str(cycles_times))

    # 随机抽取两个父母 a 和 b
    p_father_num = 2

    p_father_dict_res, p_father_list = get_p_father(p_father_num)
    # print(p_father_dict_res)
    # print(p_father_list)
    # 运行交叉

    a_list = p_father_list[0]
    # print(a_list)
    # print(len(a_list))
    b_list = p_father_list[1]
    # print(b_list)
    # print(len(b_list))

    # 获取cross over 的部分
    # a_choice_part_int = cross_num
    # print(a_choice_part)
    # [1, 2, 3, 4,5 ]
    cross_num = random.randint(0, len(a_list)-10)
    a_list_left = a_list[0:cross_num]
    a_list_right = a_list[cross_num:len(a_list)-1]

    # b
    b_list_left = b_list[0:cross_num]
    b_list_right = b_list[cross_num:len(a_list)-1]

    # b_choice_part = sample(b_list, cross_num)
    # print(b_choice_part)
    #
    # # crossover c and d: remove
    # for i in a_choice_part:
    #     # print(i)
    #     a_list.remove(i)
    #
    # for m in b_choice_part:
    #     a_list.append(m)
    # # print(a_list)
    c_list = a_list_left + b_list_right
    # print(len(c_list))
    #
    # for h in b_choice_part:
    #     b_list.remove(h)
    #
    # for n in a_choice_part:
    #     b_list.append(n)
    # # print(b_list)
    d_list = b_list_left + a_list_right
    # print(len(d_list))

    # c and d 运行变异生成e
    random_mutation_int_list = []
    while len(random_mutation_int_list) < mutation_num:
        random_mutation_int = random.randint(1, 100)
        key = 'bag ' + str(random_mutation_int)
        while key in c_list:
            random_mutation_int = random.randint(1, 100)
            key = 'bag ' + str(random_mutation_int)
        random_mutation_int_list.append(random_mutation_int)
    # print(random_mutation_int_list)

    e_remove_list = sample(c_list, cross_num)
    for b in e_remove_list:
        c_list.remove(b)
    for v in random_mutation_int_list:
        key = 'bag ' + str(v)
        c_list.append(key)

    # print(len(c_list))

    e_list = c_list
    # a_list.copy()
    # print(e_list)
    # print(len(e_list))

    e_set_list = list(set(e_list))
    # print(len(e_set_list))
    # 评估e
    e_capacity_sum, e_value_sum = get_bag_params(e_set_list)
    print(e_capacity_sum)
    print(e_value_sum)

    if e_capacity_sum < 285:
        if e_value_sum > p_sum_value_dict_sort[0][1]:
            p_fit_data[str(p_sum_value_dict_sort[0][0])] = e_set_list

        else:
            # print(1)
            pass
    else:
        # print(2)
        pass

    #  and d 运行变异生成f
    random_mutation_int_list = []
    while len(random_mutation_int_list) < mutation_num:
        random_mutation_int = random.randint(1, 100)
        key = 'bag ' + str(random_mutation_int)
        while key in d_list:
            random_mutation_int = random.randint(1, 100)
            key = 'bag ' + str(random_mutation_int)
        random_mutation_int_list.append(random_mutation_int)
    # print(random_mutation_int_list)

    f_remove_list = sample(d_list, cross_num)
    for h in f_remove_list:
        d_list.remove(h)
    for j in random_mutation_int_list:
        key = 'bag ' + str(j)
        d_list.append(key)


    f_list = d_list

    f_set_list = list(set(f_list))
    # print(len(e_set_list))
    # 评估e
    f_capacity_sum, f_value_sum = get_bag_params(f_set_list)
    print(f_capacity_sum)
    print(f_value_sum)

    if f_capacity_sum < 285:
        if f_value_sum > p_sum_value_dict_sort[0][1]:
            p_fit_data[str(p_sum_value_dict_sort[0][0])] = f_set_list

        else:
            # print(1)
            pass
    else:
        # print(2)
        pass


    # 计算p_data的value值
    p_sum_value_dict = {}
    for each_p_list in p_fit_data:
        # print(each_p_list)
        each_p_bag_list = p_fit_data[each_p_list]
        # print(each_p_bag_list)
        each_p_capacity_sum, each_p_value_sum = get_bag_params(each_p_bag_list)
        p_sum_value_dict[each_p_list] = each_p_value_sum

    # print(p_sum_value_dict)
    p_sum_value_dict_sort = sorted(p_sum_value_dict.items(), key=lambda x: x[1])
    print(p_sum_value_dict_sort)

    final_list = p_fit_data[p_sum_value_dict_sort[1][0]]
    final_capacity, final_value = get_bag_params(final_list)

    # print(final_capacity)
    # print(final_value)

    cycles_times += 1


print(p_sum_value_dict_sort)



