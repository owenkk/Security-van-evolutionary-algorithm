#!/usr/bin/python3
# coding: utf8

import pandas as pd
import random
from random import sample

a = ['bag 19', 'bag 93', 'bag 80', 'bag 58', 'bag 54']
b = sample(a, 4)
# print(b)

a = ['bag 63', 'bag 8', 'bag 14', 'bag 99', 'bag 68', 'bag 67', 'bag 6', 'bag 27', 'bag 100', 'bag 69', 'bag 96', 'bag 74', 'bag 79', 'bag 85', 'bag 61', 'bag 81', 'bag 32', 'bag 65', 'bag 72', 'bag 40', 'bag 46', 'bag 29', 'bag 50', 'bag 71', 'bag 58', 'bag 23', 'bag 34', 'bag 78', 'bag 98', 'bag 91', 'bag 48', 'bag 73', 'bag 3', 'bag 22', 'bag 42', 'bag 69', 'bag 55', 'bag 9', 'bag 51', 'bag 4', 'bag 40', 'bag 24', 'bag 17', 'bag 94', 'bag 47', 'bag 86', 'bag 62', 'bag 87', 'bag 93', 'bag 60', 'bag 89', 'bag 10', 'bag 67', 'bag 5']

# for i in a:
#      a.remove(i)
#      if i in a:
#           print(i)
#           print(11111)

# a_list = ['bag 29', 'bag 54', 'bag 59', 'bag 2', 'bag 76']
# a_part = ['bag 29', 'bag 54']
# for i in a_part:
#     a_list.remove(i)
# print(a_list)

i = 0
random_int_list = []

while i < 5:
     # random int
     random_int = random.randint(0, 6)
     # print(random_int)

     # 需要去重
     if random_int in random_int_list:
          random_int = random.randint(0, 6)
     else:
          random_int_list.append(random_int)
     i += 1
print(random_int_list)


[54, 22, 61, 51, 81, 93, 29, 62, 9, 75, 92, 64, 26, 33, 70, 15, 60, 71, 10, 40, 1, 85, 80, 68, 4, 41, 38, 3, 25, 55, 56, 2, 16, 83, 35, 0, 98, 94, 18, 63, 6, 31]
