#!/usr/bin/python3
# coding: utf8
"""
Template file for ECMM409 Nature-Inspired-Computation CA1
Academic Year: 2022/23
Version: 1
Author: Kang kai
"""

import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np


def read_data(text_name_input, text_num_input):
    '''
    :param text_name_input: The file name of the read data
    :param text_num_input: The number of files to read
    :return: return read data
    '''
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


def initial_population(p_times, p_size):
    '''
    function to generate initial population
    :param p_times: Number of randomly generated solutions
    :param p_size:The size of the randomly generated solution
    :return: returns the randomly generated solution population as a list
    '''
    p_initial_population_list = []

    i = 0
    while i < p_times:

        # 生成含有100个0的列表
        bag_initial_list = []
        while len(bag_initial_list) < p_size:
            sign = random.randint(0, 1)
            bag_initial_list.append(sign)
        # print(len(bag_initial_list))
        p_initial_population_list.append(bag_initial_list)

        i += 1

    return p_initial_population_list


def get_bag_info(sum_list, p_initial_population_list):
    '''
    Functions to calculate the total weight and total value of a solution
    :param sum_list: The read data, in the form of a dictionary
    :param p_initial_population_list: population of randomly generated solutions
    :return: Returns the total weight and total value of randomly generated solutions
    '''
    weight = 0
    value = 0
    for i in range(len(p_initial_population_list)):
        if p_initial_population_list[i] == 1:
            bag_params = sum_list[int(i)]
            bag_weight = bag_params['bag ' + str(i + 1)]['weight']
            bag_value = bag_params['bag ' + str(i + 1)]['value']
            weight = weight + float(bag_weight)
            value = value + float(bag_value)

    return weight, value


def Binary_Tournament_Selection(population_size, sum_value_list):
    '''
    Binary Tournament Function
    :param population_size: The size of the randomly generated solution
    :param sum_value_list: The value of all randomly generated solutions
    :return: Scheme of Binary Tournament
    '''
    choose_first = random.randint(0, population_size - 1)
    choose_second = random.randint(0, population_size - 1)

    if sum_value_list[choose_first] >= sum_value_list[choose_second]:
        return p_initial_population_list[choose_first]
    else:
        return p_initial_population_list[choose_second]


def cross_over(cross_over_a, cross_over_b):
    '''
    cross function
    :param cross_over_a: The first data that needs to be intersected
    :param cross_over_b: The first data that needs to be intersected
    :return: Return the two new solutions obtained after crossing
    '''
    Single_Point = random.randint(0, len(cross_over_a))
    # Single_Point = 30

    a_list_left = cross_over_a[0:Single_Point]
    a_list_right = cross_over_a[Single_Point:len(cross_over_a) - 1]

    b_list_left = cross_over_b[0:Single_Point]
    b_list_right = cross_over_b[Single_Point:len(cross_over_b) - 1]

    cross_overed_c = a_list_left + b_list_right
    cross_overed_d = b_list_left + a_list_right

    return cross_overed_c, cross_overed_d


def Mutation(mutation_list, mutation_num):
    '''
    Variation function
    :param mutation_list: Store the positions that need to be mutated in the form of a list
    :param mutation_num: amount of variation
    :return: return the mutated list
    '''
    choose_mutation_list = random.sample(range(0, len(mutation_list)), mutation_num)

    for each_c_mutation in choose_mutation_list:
        if mutation_list[each_c_mutation] == 0:
            mutation_list[each_c_mutation] = 1
        else:
            mutation_list[each_c_mutation] = 0

    return mutation_list


def Weakest_Replacement(sum_list, p_initial_population_list, sum_value_list, Replacement_list):
    '''
    weakest substitution function
    :param sum_list: The read data, in the form of a dictionary
    :param p_initial_population_list: population of randomly generated solutions
    :param sum_value_list: Total Value List of Solutions
    :param Replacement_list: Run the list of weakest replacements
    :return:
    '''
    sum_weight, sum_value = get_bag_info(sum_list, Replacement_list)
    if sum_weight <= max_weight:
        if sum_value > min(sum_value_list):
            Replacement_index = sum_value_list.index(min(sum_value_list))
            p_initial_population_list[Replacement_index] = Replacement_list
        else:
            pass
    else:
        pass


def draw_picture(record_list):
    iterations = list(np.arange(len(record_list)))
    plt.figure()
    plt.plot(iterations, record_list, 'b-')
    # 设置图片相关
    plt.title('best values record')
    plt.xlabel('Cycles')
    plt.ylabel('best value')
    plt.show()


if __name__ == '__main__':

    # The name of the file to read
    text_name = 'docs/BankProblem.txt'

    # The number of lines in the file to read
    text_num = 301

    # Store the read file as a dictionary
    sum_list = read_data(text_name, text_num)
    # print(sum_list)
    # num_y = []

    # The number of randomly generated populations
    p_times = 10

    # randomly generated population size
    p_size = 100

    # Randomly generated population of solutions
    p_initial_population_list = initial_population(p_times, p_size)
    # print(p_initial_population_list)

    p_father_num = 2

    # The number of mutant individuals
    mutation_num = 2

    # Maximum number of cycles
    termination_times = 10000

    # Maximum load
    max_weight = 285
    cycles_times = 0
    sum_max_value = []
    while cycles_times < termination_times:

        print( str(cycles_times))

        sum_value_list = []
        sum_weight_list = []
        for each_p in p_initial_population_list:
            sum_weight, sum_value = get_bag_info(sum_list, each_p)
            sum_weight_list.append(sum_weight)
            sum_value_list.append(sum_value)

        # total_weight, total_value = get_bag_info(sum_list, p_initial_population_list)
        # print(total_value)

        # Generate a solution a via a binary tournament
        a = Binary_Tournament_Selection(p_times, sum_value_list)
        # Generate a solution b via a binary tournament
        b = Binary_Tournament_Selection(p_times, sum_value_list)

        # Solution a and b are crossed
        c, d = cross_over(a, b)

        # c generates e by mutation
        e = Mutation(c, mutation_num)
        # d generates f by mutation
        f = Mutation(d, mutation_num)
        # print(len(e))

        # First use e for the weakest replacement
        Weakest_Replacement(sum_list, p_initial_population_list, sum_value_list, e)
        # use f for the weakest replacement
        Weakest_Replacement(sum_list, p_initial_population_list, sum_value_list, f)

        new_sum_value = []
        new_sum_weight = []
        for each_new_p in p_initial_population_list:
            new_each_weight, new_each_value = get_bag_info(sum_list, each_new_p)
            new_sum_weight.append(new_each_weight)
            new_sum_value.append(new_each_value)
        # print(new_sum_value)
        print('max value is ：' + str(max(new_sum_value)))
        sum_max_value.append(str(max(new_sum_value)))
        cycles_times += 1

    draw_picture(sum_max_value)
