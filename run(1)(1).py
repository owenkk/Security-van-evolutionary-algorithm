#!/usr/bin/python3
# coding: utf8

import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_data(info_text_path):
    """
    read bank bags information
    :param info_text_path: txt path to read
    :return:
    """
    df = pd.read_table(info_text_path, sep=':', header=None)
    # 1.read basic info
    key_list = []
    value_list = []
    for (a, b) in zip(df[0], df[1]):
        key_list.append(a.strip())
        value_list.append(str(b))

    security_van_capacity = float(value_list[0])
    bags_info = {}
    bags_cnt = 0  # record the number of bags, start from 0
    list_cnt = 1  # record the info index of key/value list
    while True:
        # search the line index
        weight_line_idx, value_line_idx = list_cnt + 1, list_cnt + 2
        if value_line_idx >= len(value_list):
            break
        list_cnt += 3

        # write bags info
        if key_list[weight_line_idx] != 'weight' or key_list[value_line_idx] != 'value':
            print('key error! line index is {}'.format(list_cnt))
            break
        bags_info[bags_cnt] = {'weight': float(value_list[weight_line_idx]), 'value': float(value_list[value_line_idx])}
        bags_cnt += 1

    return security_van_capacity, bags_info


def sort_list_by_dict_key(list_in: list, dict_key: str = 'bags_value_sum', big2small=True):
    """
     输入列表，列表内容为字典，按照字典中的值进行排序
    :param list_in: 输入的李彪
    :param dict_key: 用于判定的键值
    :param big2small: 是否从大到小排序
    :return:
    """
    list_keys = np.array([list_dict[dict_key] for list_dict in list_in])  # 从列表中提取值
    new_list_idx = np.argsort(list_keys)
    if big2small:
        new_list_idx = new_list_idx[::-1]  # 逆序，从大到小排序

    list_in_sorted = [list_in[i] for i in new_list_idx]
    return list_in_sorted, new_list_idx


class EvolutionTool:
    def __init__(self, security_van_capacity, bags_info, popution_size=10):
        self.security_van_capacity = security_van_capacity
        self.bags_info = bags_info
        self.bags_number = len(bags_info)
        self.p_father_num = 2  # 每次迭代抽取的父辈数量
        self.popution_size = popution_size

        # 总的选择池
        self.populations = self.set_p_initial_population()

    def set_p_initial_population(self):
        """ Generate an initial population of p randomly generated solutions """
        initial_popution = []
        for p in range(self.popution_size):
            # generate the p th initial
            # setp1: set empty array
            bags_selection = np.zeros(self.bags_number)
            bags_weight_sum = 0.0
            bags_value_sum = 0.0

            # step2: get rand list
            search_index = list(np.arange(100))  # get number from 0 to 99
            random.shuffle(search_index)  # shuffle the list

            # try to load the bag, until overload
            for bag_id in search_index:
                bag_weight, bag_value = self.bags_info[bag_id]['weight'], self.bags_info[bag_id]['value']
                # try to load the bag
                if (bags_weight_sum + bag_weight) < self.security_van_capacity:
                    bags_selection[bag_id] = 1
                    bags_weight_sum += bag_weight
                    bags_value_sum += bag_value
                else:
                    break

            initial_popution.append({'bags_selection': bags_selection, 'bags_weight_sum': bags_weight_sum,
                                     'bags_value_sum': bags_value_sum})

        # 按照value值对popution进行排序
        initial_popution, _ = sort_list_by_dict_key(initial_popution, 'bags_value_sum')

        return initial_popution

    def get_two_fathers(self):
        """ 从整个 popution 中选择2个father
        Use the binary tournament selection twice (with replacement) to select two parents a and b
        """
        select_fathers = []
        select_fathers_idx = []
        for i in range(self.p_father_num):
            # 1.随机选择两个父辈
            total_popution_idx = list(np.arange(self.popution_size))
            select_idxs = random.sample(total_popution_idx, 2)
            # print('select_idxs ', select_idxs)
            tmp_select_fathers = [self.populations[select_idxs[0]], self.populations[select_idxs[1]]]
            tmp_select_fathers_idx = [select_idxs[0], select_idxs[1]]

            # 2.对两个父辈进行排序, 并选择优秀的父辈，并记录下选择的id
            tmp_select_fathers_sorted, tmp_idx = sort_list_by_dict_key(tmp_select_fathers)
            select_fathers.append(tmp_select_fathers_sorted[0])
            select_fathers_idx.append(tmp_select_fathers_idx[tmp_idx[0]])

        return select_fathers, select_fathers_idx

    def run_crossover(self, fathers_to_crossover, cross_num=30):
        """ 运行交叉
        :param cross_num: 运行交叉的长度
        """
        a_list = list(fathers_to_crossover[0]['bags_selection'])
        b_list = list(fathers_to_crossover[1]['bags_selection'])

        # 获取cross over 的部分
        a_list_left = a_list[0:cross_num]
        a_list_right = a_list[cross_num:]
        b_list_left = b_list[0:cross_num]
        b_list_right = b_list[cross_num:]

        # 进行拼接
        c_list = a_list_left + b_list_right
        d_list = b_list_left + a_list_right
        # 确保长度还是和交叉前一致
        if len(c_list) != self.bags_number or len(d_list) != self.bags_number:
            raise ValueError

        return c_list, d_list

    def run_mutation(self, list_in, mutation_num=3, ):
        """
        运行突变
        :param list_in: 当前选择包的列表
        :param mutation_num: 突变数量
        :return:
        """
        if len(list_in) != self.bags_number:
            raise ValueError
        # 随机选择突变点位
        mutation_idxs = random.sample(list(np.arange(self.bags_number)), mutation_num)
        for idx in mutation_idxs:
            list_in[idx] = 1 - list_in[idx]  # list_in中的值为0或1
        return list_in

    def evaluate_bags_list(self, list_in: list):
        """
        根据当前选择bags的情况，计算weight和value信息
        :param list_in:
        :return:
        """
        if len(list_in) != self.bags_number:
            raise ValueError
        bags_weight_sum = 0.0
        bags_value_sum = 0.0
        for bag_id, load_bag in enumerate(list_in):
            if load_bag == 1:
                bag_weight, bag_value = self.bags_info[bag_id]['weight'], self.bags_info[bag_id]['value']
                bags_weight_sum += bag_weight
                bags_value_sum += bag_value

        return {'bags_selection': np.array(list_in), 'bags_weight_sum': bags_weight_sum,
                'bags_value_sum': bags_value_sum}

    def evolution_run(self, termination_times=10000, mutation_num=5):
        best_value_record = []

        for cycle_iter in (range(termination_times)):
            # print('循环第{}次'.format(cycle_iter))

            # #### 进行进化
            # step1.随机抽取两个父母 a 和 b
            select_fathers, select_fathers_idx = self.get_two_fathers()
            # step2.进行交叉
            # Randomly select a ‘crossover point’ which should be smaller than the total length of the chromosome.
            cross_num = random.randint(1, self.bags_number - 2)  # 取值1-98，因为总长度下标为0-99
            # print('cross_num ', cross_num)
            c_list, d_list = self.run_crossover(select_fathers, cross_num)
            # step3.进行变异
            e_list = self.run_mutation(c_list, mutation_num=mutation_num)
            f_list = self.run_mutation(d_list, mutation_num=mutation_num)

            # 评估进化结果
            e_evo_res = self.evaluate_bags_list(e_list)
            f_evo_res = self.evaluate_bags_list(f_list)

            # 如果重量满足要求就加入总的记录
            if e_evo_res['bags_weight_sum'] < self.security_van_capacity:
                self.populations.append(e_evo_res)
            if f_evo_res['bags_weight_sum'] < self.security_van_capacity:
                self.populations.append(f_evo_res)

            # 排序，筛去最差的结果，保持popution数量
            populations_sorted, _ = sort_list_by_dict_key(self.populations)
            self.populations = populations_sorted[:self.popution_size]

            # 记录最优值
            best_value_record.append(self.populations[0]['bags_value_sum'])

        # print('run evolution done')
        return best_value_record


def print_result(populations, popution_size):
    print('bags info={}'.format(populations[0]['bags_selection']))
    print('value = {}'.format([populations[i]['bags_value_sum'] for i in range(popution_size)]))
    print('max value = {:.2f}'.format(populations[0]['bags_value_sum']))
    print('max value weight = {:.2f}'.format(populations[0]['bags_weight_sum']))


def draw_iteraiont_result(record_list: list):
    iterations = list(np.arange(len(record_list)))
    plt.figure()
    plt.plot(iterations, record_list, 'b-')
    # 设置图片相关
    plt.title('best values record')
    plt.xlabel('iterations')
    plt.ylabel('best value')
    plt.show()


def run(text_path='', popution_size=10):
    # step1 get_data
    security_van_capacity, bags_info = read_data(text_path)

    # step2 get initial
    evo_tool = EvolutionTool(security_van_capacity, bags_info, popution_size=popution_size)
    # print('evo_tool.populations ', evo_tool.populations)
    # print('popution_size ', popution_size)
    # print('initial')
    # print_result(evo_tool.populations, popution_size)

    # step3 run evolution
    best_value_record = evo_tool.evolution_run(termination_times=10000)
    print('final')
    print_result(evo_tool.populations, popution_size)
    # 画图
    draw_iteraiont_result(best_value_record)


print('-' * 20, '\n')


def main():
    # set data path
    text_path = '../bankproblem.txt'

    # run evolution
    """ Your experiments should assess the performance of the algorithm over a number of randomly seeded 
        trials for each setting of t, p, m, to provide robust results """
    tournament_size = 1  # 实验次数
    popution_size = 10
    for i in range(tournament_size):
        run(text_path, popution_size)


if __name__ == "__main__":
    main()
