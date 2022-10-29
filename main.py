#!/usr/bin/python3
# coding: utf8

# import pandas as pd
#
# df=pd.read_table('BankProblem.txt', sep=':', header= None)
# df = df.drop(0)
# df.to_dict(orient="index")
# # print(df)
# music_dict_list = df.to_dict(orient="index")
# print(df)


# f = open("BankProblem.txt")
# line = f.readline()[1]
# while line:
#     print(line)
#     line = f.readline()
#
# f.close()

# import numpy as np
# import pandas as pd
# music_info = pd.read_table('BankProblem.txt', header=None,sep='  ')
# print('数据预览：', music_info.head())
# print('样本个数：', len(music_info))


# music_dict_list = music_info.to_dict(orient="index")
# print(music_dict_list)


# # 写入文件代码 通过keys的顺序写入
# fw = open('wdic.txt', 'w')
# for k in keys:
#     fw.write(k + ':' + dic[k] + '\n')
#
# fw.close()
# dict_temp ={}
# file = open("BankProblem.txt")
# for line in file.readlines():
#     line = line.strip()
#     k = line.split(" ")[0]
#     v = line.split(" ")[1]
#     dict_temp[k] = v
#     # print(dict_temp)
#
# print(dict_temp)
#
# file.close()

with open('BankProblem.txt','r',encoding='utf-8') as f:
    dic=[]
    for line in f.readlines():
        line=line.strip('\n') #去掉换行符\n
        b=line.split(' ') #将每一行以空格为分隔符转换成列表
        dic.append(b)
dic=dict(dic)
print(dic)