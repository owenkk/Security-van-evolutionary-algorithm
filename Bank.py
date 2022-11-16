import pandas as pd
import random
import matplotlib.pyplot as plt

# Read BankProblem.txt
data = pd.read_table('./docs/BankProblem.txt',
                     sep=':', header=None)

'''combination of parameters'''
termination_criterion = 10
tournament_size = 10
population_size = 60
mutation_rate = 0
'''combination of parameters'''

'''fitness algorithm'''


def fitness(list):
    sum_fit, sum_weight, sum_value = 0, 0, 0
    for p in list:
        each_child_bag = p
        each_child_bag_num_split = each_child_bag.split(' ')
        each_child_bag_num = each_child_bag_num_split[1]
        each_child_bag_params = sum_list[int(each_child_bag_num) - 1]
        each_child_value = each_child_bag_params[each_child_bag]['value']
        sum_value += float(each_child_value)
    return sum_value


'''Sorting algorithm'''


def dict_sorted(sort_dict):
    sorted_dict = dict(sorted(sort_dict.items(), key=lambda kv: (kv[1], kv[0])))
    return sorted_dict


'''Create a general table and save it in sum_ list'''
key = []
for a in data[0]:
    key.append(a.strip())
value = []
for b in data[1]:
    value.append(str(b))
sum_list = []
i = 1
while i < 301:
    bag_dict = {}
    value_dict = {key[i + 1]: value[i + 1], key[i + 2]: value[i + 2]}
    bag_dict[key[i]] = value_dict
    sum_list.append(bag_dict)
    i = i + 3
# print(sum_list)

'''Create a total bag list and save it to sum_ bag_ list'''
sum_bag_list_num = [n for n in range(1, 101)]
# print(sum_bag_list_num)
sum_bag_list = []
for i in sum_bag_list_num:
    a = 'bag ' + str(i)
    sum_bag_list.append(a)
# print('sum_bag_list', sum_bag_list)


'''create initial population of p randomly generated solutions'''
t = 0
p_data = {}
weight_list = []
final_max_value = []
while t < tournament_size:
    p = 0
    sum_cap = 0
    bag_list = []
    random_bag_list = []
    while p < population_size:
        random_bag = random.randint(0, 99)
        # Remove the same bag, and if the same bag is obtained again
        while True:
            if random_bag in random_bag_list:
                random_bag = random.randint(0, 99)
            else:
                random_bag_list.append(random_bag)
                break
        bag_sum_list = sum_list[random_bag]
        k = 'bag ' + str(random_bag + 1)
        weight = bag_sum_list[k]["weight"]
        sum_cap = sum_cap + float(weight)
        bag_list.append(k)
        p += 1
    # print(len(bag_list))
    p_data['p' + str(t + 1)] = bag_list
    t += 1
# print('p_data: ', p_data)

'''Cyclic evolutionary algorithm'''
h = 0
round_num = 0
while round_num < termination_criterion:
    p_data_p_list = []
    p_data_num_list = []
    p_data_p_list = list(p_data.keys())
    for y in p_data_p_list:
        p_data_p_num_str = y
        p_data_p_num = int(p_data_p_num_str.strip('p'))
        p_data_num_list.append(str(p_data_p_num))

    # Randomly choose a chromosome from the population
    def random_parent():
        random_bag = random.choice(p_data_num_list)
        parent_list = [p_data['p' + str(random_bag)]]
        parent_list = parent_list[0]
        sum_fit, sum_weight, sum_value = 0, 0, 0
        for m in parent_list:
            each_parent_split = m
            each_bag_split_num = each_parent_split.split(' ')
            each_bag_num = each_bag_split_num[1]
            each_bag_params = sum_list[int(each_bag_num) - 1]
            each_bag_weight = each_bag_params[each_parent_split]['weight']
            each_bag_value = each_bag_params[each_parent_split]['value']
            sum_weight += float(each_bag_weight)
            sum_value += float(each_bag_value)
        return random_bag, sum_value

    # Binary Tourism Selection
    def binary_tournament():
        random_bag_1, sum_value_1 = random_parent()
        random_bag_2, sum_value_2 = random_parent()
        while random_bag_2 == random_bag_1:
            random_bag_2, sum_value_2 = random_parent()
        if sum_value_2 >= sum_value_1:
            parent = random_bag_2
        else:
            parent = random_bag_1
        return parent

    '''Use the binary tournament selection select two parents a and b'''
    parent_a = binary_tournament()
    parent_b = binary_tournament()
    # '''Remove duplication and prevent parent_a == parent_b'''
    while parent_b == parent_a:
        parent_b = binary_tournament()
    parent_a_list = p_data['p' + str(parent_a)]
    parent_b_list = p_data['p' + str(parent_b)]
    print(len(parent_a_list))


    '''Run crossover on these parents to give 2 children, c and d.'''
    child_c = []
    child_d = []
    # Randomly select the crossover length
    if len(parent_a_list) <= len(parent_b_list):
        part_length = random.sample(range(1, len(parent_a_list)), 1)
    else:
        part_length = random.sample(range(1, len(parent_b_list)), 1)
    if len(parent_a_list) <= len(parent_b_list):
        part_start = random.sample(range(0, len(parent_a_list) - int(part_length[0])), 1)
    else:
        part_start = random.sample(range(0, len(parent_b_list) - int(part_length[0])), 1)
    # crossover
    part_a = parent_a_list[int(part_start[0]):int(part_start[0]) + int(part_length[0])]
    part_b = parent_b_list[int(part_start[0]):int(part_start[0]) + int(part_length[0])]
    del parent_a_list[int(part_start[0]):int(part_start[0]) + int(part_length[0])]
    del parent_b_list[int(part_start[0]):int(part_start[0]) + int(part_length[0])]
    for a in part_a:
        parent_b_list.insert(int(part_start[0]), a)
    for b in part_b:
        parent_a_list.insert(int(part_start[0]), b)
    # child_c and child_d
    child_c_list = parent_a_list
    print(len(child_c_list))
    child_d_list = parent_b_list
    # print(len(child_c_list),child_c_list)
    # print(len(child_d_list),child_d_list)

    '''mutation'''
    # Determine the maximum number of mutant genes
    if len(child_c_list) <= len(child_d_list):
        mutation_max_num = len(child_c_list)
    else:
        mutation_max_num = len(child_d_list)

    # Number of mutant genes
    mutation_num = mutation_rate * float(mutation_max_num)

    # do mutation
    # c is mutated to obtain e
    if mutation_num != 0:
        mutation_bag_list_a = random.sample(sum_bag_list, int(mutation_num))
        mutation_bag_list_b = random.sample(sum_bag_list, int(mutation_num))
        del_child_c_list = random.sample(child_c_list, int(mutation_num))
        for c in del_child_c_list:
            child_c_list.remove(c)
            child_e_list = child_c_list
        for e in mutation_bag_list_a:
            child_e_list.append(e)
    else:
        child_e_list = child_c_list
    # d is mutated to obtain f
    if mutation_num != 0:
        del_child_d_list = random.sample(child_d_list, int(mutation_num))
        for d in del_child_d_list:
            child_d_list.remove(d)
            child_f_list = child_d_list
        for e in mutation_bag_list_b:
            child_f_list.append(e)
    else:
        child_f_list = child_d_list

    # Removal of duplicate gene fragments in c and e
    child_e_list = list(set(child_e_list))
    child_f_list = list(set(child_f_list))
    print(len(child_e_list))

    # Calculate the fitness of e and f
    child_e_value = fitness(child_e_list)
    child_f_value = fitness(child_f_list)
    # print(child_e_value,child_f_value)

    '''evaluate the fitness in the population'''
    p_sum_value_list = []
    for q in p_data:
        each_p_sum_value = 0
        each_p_data_list = p_data[q]
        for p in each_p_data_list:
            each_p_data_split = p
            each_p_data_split_num = each_p_data_split.split(' ')
            each_p_data_num = each_p_data_split_num[1]
            each_p_data_params = sum_list[int(each_p_data_num) - 1]
            each_p_data_value = each_p_data_params[each_p_data_split]['value']
            each_p_sum_value += float(each_p_data_value)
        p_sum_value_list.append(each_p_sum_value)
    p_value = dict(zip(p_data_p_list, p_sum_value_list))
    # print('p_value',p_value)

    # Get the least fitness solution
    p_value_sorted = dict_sorted(p_value)
    for key, value in p_value_sorted.items():
        p_min_value_sorted = value
        p_min_key_sorted = key
        break

    '''Run weakest replacement, first using e, then f'''
    if float(child_e_value) >= float(p_min_value_sorted):
        h += 1
        del p_value_sorted[p_min_key_sorted]
        p_value_sorted['p' + str(t + h)] = child_e_value
        p_value_e = p_value_sorted
        del p_data[p_min_key_sorted]
        p_data['p' + str(t + h)] = child_e_list
        p_value_e_sorted = dict_sorted(p_value_e)
        final_value = p_value_e_sorted
        for key, value in p_value_e_sorted.items():
            p_min_value_e_sorted = value
            p_min_key_e_sorted = key
            break
        if float(child_f_value) >= float(p_min_value_e_sorted):
            h += 1
            del p_value_e_sorted[p_min_key_e_sorted]
            p_value_e_sorted['p' + str(t + h)] = child_f_value
            p_value_e_f = p_value_e_sorted
            del p_data[p_min_key_e_sorted]
            p_data['p' + str(t + h)] = child_f_list
            p_value_e_f_sorted = dict_sorted(p_value_e_f)
            final_value = p_value_e_f_sorted
    elif float(child_f_value) >= float(p_min_value_sorted):
        h += 1
        del p_value_sorted[p_min_key_sorted]
        p_value_sorted['p' + str(t + h)] = child_f_value
        p_value_f = p_value_sorted
        del p_data[p_min_key_sorted]
        p_data['p' + str(t + h)] = child_f_list
        p_value_f_sorted = dict_sorted(p_value_f)
        final_value = p_value_f_sorted
    elif float(child_e_value) < float(p_min_value_sorted) and float(child_f_value) < float(p_min_value_sorted):
        final_value = p_value_sorted

    '''Organize data'''
    final_value_list = list(final_value.keys())
    final_weight_list = []
    for each_final_p in final_value_list:
        each_p_sum_weight = 0
        each_final_p_bag_list = p_data[each_final_p]
        for each_final_p_bag in each_final_p_bag_list:
            each_final_p_bag_split = each_final_p_bag.split(' ')
            each_final_p_bag_num = each_final_p_bag_split[1]
            each_final_p_bag_params = sum_list[int(each_final_p_bag_num) - 1]
            each_final_p_bag_weight = each_final_p_bag_params[each_final_p_bag]['weight']
            each_p_sum_weight += float(each_final_p_bag_weight)
        final_weight_list.append('%.1f' % each_p_sum_weight)
    round_num += 1
    print('round_num = ' + str(round_num))

    final_weight_dict = []
    final_value_dict = []
    for c in final_weight_list:
        each_final_weight_list = ['weight: ' + c]
        final_weight_dict.append(each_final_weight_list)
    print(final_weight_dict)
    final_value_list = list(final_value.values())
    final_max_value.append(final_value_list[-1])
    for c in final_value_list:
        each_final_value_list = ['value: ' + str(c)]
        final_value_dict.append(each_final_value_list)
    print(final_value_dict)
    final_value_p_list = list(final_value.keys())

# '''Draw Line Chart'''
# plt.figure(figsize=(10, 6), dpi=100)
# plt.plot(range(0, 10000), final_max_value)
# plt.show()
