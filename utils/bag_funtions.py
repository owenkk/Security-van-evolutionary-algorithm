# -*- coding: utf-8 -*-
import random


class BagDataDeal:
    """ 用于存储计算流程方法 """
    @staticmethod
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

    @staticmethod
    def get_p_father(p_father_num):
        # p_father_num = 2
        random_int = random.sample(range(1, p_times), p_father_num)
        # print(random_int)
        p_father_dict = {}
        p_father_list = []
        for i in random_int:
            # print(i)
            p_father_dict['p' + str(i)] = p_data['p' + str(i)]
            p_father_list.append(p_data['p' + str(i)])

        # print(p_father_dict)

        return p_father_dict, p_father_list

    @staticmethod
    def get_bag_params(bag_list):
        bag_capacity_sum = 0
        bag_value_sum = 0
        for each_bag in bag_list:
            each_bag_split = each_bag.split(' ')
            each_bag_num = each_bag_split[1]
            bag_params = sum_list[int(each_bag_num) - 1]
            # 这个遇到一个bug，，会有bag 0 的出现
            # 这个遇到一个bug，，会有bag 0 的出现
            # 这个遇到一个bug，，会有bag 0 的出现
            each_bag_capacity = bag_params[each_bag]['weight']
            # 这个遇到一个bug，，会有bag 0 的出现
            # 这个遇到一个bug，，会有bag 0 的出现
            # 这个遇到一个bug，，会有bag 0 的出现
            bag_capacity_sum = float(bag_capacity_sum) + float(each_bag_capacity)
            bag_value = bag_params[each_bag]['value']
            bag_value_sum = bag_value_sum + float(bag_value)
        # print(bag_capacity_sum)
        # print(bag_value_sum)

        return bag_capacity_sum, bag_value_sum
