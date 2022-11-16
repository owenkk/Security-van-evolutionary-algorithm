import numpy as np
import random
import matplotlib.pyplot as plt

with open('../docs/BankProblem.txt', 'r') as file:
    data = file.readlines()  # Read all lines
    # print(data)

    # bef1 and bef2 are used for initial processing of the read data
    bef1 = []
    bef2 = []

    bag = []
    value = []
    weight = []
    for x in data:  # Since readlines() returns a list, you can do this with each row of line data
        x = x.split()  # Use split to remove symbols such as Spaces, line breaks
        bef1.append(x)
    # print(bef1)

    for a in range(len(bef1)):
        number = bef1[a]
        number1 = ''.join(number)
        # for a1 in number1:
        # if a1.isdigit() or '.' in a1: number2 = ''.join(a1)
        number2 = ''.join(a1 for a1 in number1 if a1.isdigit() or '.' in a1)  # Isolate the numbers

        # Necessary operations, because empty lists cannot directly specify the subscript
        # , which will cause the subscale to cross the line
        bef2.append(1)
        bef2[a] = number2
    # print(number1)
    # print(bef2)

    # Loading various types of data
    max_weight = float(bef2[0])  # The first number is backpack capacity

    for i in range(1, len(bef2), 3):  # The next number is the backpack number
        # And every third number is a backpack number
        bag.append(bef2[i])
    # print(bag)

    for i in range(2, len(bef2), 3):  # Same thing as above
        weight.append(bef2[i])
    # print(weight)

    for i in range(3, len(bef2), 3):  # Same thing as above
        value.append(bef2[i])
    # print(value)


# Initialize the population, popsize is the population size, n chromosome length
def init(pop_size, n):
    init_population = []  # A list of populations to return
    for i in range(pop_size):
        person = []  # Create individuals, each of which stores information in a list
        for j in range(n):
            g = np.random.randint(0, 2)  # Random 0 or 1
            person.append(g)
        init_population.append(person)
    return init_population


# An evaluation function that calculates the value and weight of an individual
def fitness(person, weight, value):
    wei = 0
    val = 0
    for i in range(len(person)):
        if person[i] == 1:  # When the chromosome number in the list is 1, the backpack is selected
            wei = wei + float(weight[i])
            val = val + int(value[i])
    return val, wei


# Binary Tournament Selection.Returns the selected individual.Choose one at a time
def tournament_select(population, value_list):
    father = random.randint(0, pop_size - 1)
    mother = random.randint(0, pop_size - 1)
    # while mother == father:  # Prevent duplicate individuals from appearing
    # mother = random.randint(0, pop_size - 1)

    # Compare the value of two random individuals and choose the larger one
    if value_list[father] >= value_list[mother]:
        return population[father]
    else:
        return population[mother]


# Single-Point Crossover.Passing in both parents
def cross(father, mother):
    point = np.random.randint(0, len(mother))  # Pick a random point
    child1 = []
    child2 = []
    for i in range(len(mother)):
        if i <= point:  # Take the first half of the mother's and father's chromosomes before this point
            child1.append(mother[i])
            child2.append(father[i])
        else:  # After this point the second half of the father's and mother's chromosomes are taken
            child1.append(father[i])
            child2.append(mother[i])
    return child1, child2


# Mutation.child represents the incoming individual. m is for how many times mutations will occur in this individual
def mutation(child, m):
    mut_time = 1  # The number of variations currently occurring
    new_child = child  # When the new_child changes, the child changes
    while mut_time <= m:
        # A random point.It represents a mutation at this place in the chromosome
        point = np.random.randint(0, len(child))
        if new_child[point] == 0:
            new_child[point] = 1
        else:
            new_child[point] = 0
        mut_time += 1
    return new_child


# Weakest Replacement.
# Because I need to compare the value of not being imported and the child individual,import the total_val
def replacement(pop_list, child, total_val):
    fitness_child, weight_child = fitness(child, weight, value)

    # Verify that the individual is not overweight and is worth more than the minimum value in the current list
    if fitness_child > min(total_val) and weight_child <= max_weight:
        replacement_index = total_val.index(min(total_val))  # Return the subscript
        #   a = min(total_val)    # test code
        #   print(a)
        for i in range(len(child)):  # Replace.
            # The new individual will directly take the place of the weakest individual in the imported population
            pop_list[replacement_index][i] = child[i]
    #   b, e = fitness(pop_list[replacement_index], weight, value)
    #   print(b, e)


# Graph drawing function
def plot():
    # x = range(max_m+1)  # The x coordinate is max_m
    x = range(100, max_size + 1, 100)  # The x coordinate is start to max_size+1 and step 10
    # x = range(iters+1)  # The x coordinate is iters
    plt.plot(x, y)  # Add x and y
    # plt.title('The effect of increasing m on producing the optimal solution')
    plt.title('The effect of population size on the optimal solution produced')
    for i in range(len(x)):
        plt.text(x[i], y[i], (x[i], y[i]), c='green')
    plt.show()  # Show the graph


if __name__ == '__main__':
    pop_size = 10
    n = len(bag)
    m = 1
    max_m = 10
    max_size = 1000
    y = []
    # init_population = init(pop_size, n)  # Initialize and return the population
    iters = 10000  # Total number of iterations
    # while m <= max_m:
    while pop_size <= max_size:
        iter = 1
        init_population = []
        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        init_population = init(pop_size, n)  # Initialize and return the population
        print(init_population)
        while iter <= iters:  # From the first generation to the 10,000th

            total_value = []
            total_weight = []
            for person in init_population:  # Update the value list and weight list
                val, wei = fitness(person, weight, value)
                total_value.append(val)
                total_weight.append(wei)

            # Choose mother and father
            a = tournament_select(init_population, total_value)
            b = tournament_select(init_population, total_value)
            #  while a == b:  # Prevent father and mother from being alike
            #   b = tournament_select(init_population, total_value)

            c, d = cross(a, b)  # a and b cross to produce c and d
            #  c_value, c_weight = fitness(c, weight, value)
            #  d_value, d_weight = fitness(d, weight, value)

            e = mutation(c, m)  # c mutates to produce e
            f = mutation(d, m)  # d mutates to produce f
            #  test_pop = []
            #  test_pop = init_population.copy()

            replacement(init_population, e, total_value)  # Do the weakest replacement for e
            replacement(init_population, f, total_value)  # Do the weakest replacement for f
            # if test_pop == init_population:
            # xd = True
            # else:
            # xd = False
            #  print(xd)

            # Generate a new list of values and weights that represent the values and weights of the final population individuals of this generation
            new_value = []
            new_weight = []
            for item in init_population:
                new_v, new_w = fitness(item, weight, value)
                new_value.append(new_v)
                new_weight.append(new_w)

            # Search for the subscript of the most valuable individual of this generation
            best_index = new_value.index(max(new_value))
            print("第" + str(iter) + "次迭代最大价值为:" + str(max(new_value)))
            # y.append(max(new_value))  # Add a target for the y coordinate
            # qqq = len(y)
            iter += 1
        y.append(max(new_value))  # Add a target for the y coordinate
        # m += 1
        pop_size += 100
    plot()
