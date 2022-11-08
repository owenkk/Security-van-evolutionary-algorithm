# -*- coding: utf-8 -*-
import pandas as pd

class DataDeal:
    """ 用于存储读取数据的方法"""

    def __init__(self, text_name_input=None):
        self.text_name_input = text_name_input

    @staticmethod
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



