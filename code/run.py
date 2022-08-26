import pandas as pd
import numpy as np
import time
import copy
import ga
start_time = time.time()

''' ================= initialization setting ======================'''

# Enter input
population_size = int(input('Please input the size of population: ') or 20)  # default value is 20
crossover_rate = float(input('Please input the size of Crossover Rate: ') or 0.8)  # default value is 0.8
mutation_rate = float(input('Please input the size of Mutation Rate: ') or 0.3)  # default value is 0.3
mutation_selection_rate = float(input('Please input the mutation selection rate: ') or 0.4)
num_iteration = int(input('Please input number of iteration: ') or 1000)  # default value is 1000



'''==================== main code ==============================='''
'''----- generate initial population -----'''
best_list, best_obj = [], []
population_list = []
for n in range(num_iteration):
    #TODO: Define parent_list and offspring_list
    parent_list = copy.deepcopy(population_list)
    offspring_list = []
    chroms_obj_record = {}  # record each chromosome objective values as chromosome_obj_record={chromosome:[HC_time,HC_record]}
    total_chromosome = copy.deepcopy(parent_list) + copy.deepcopy(
        offspring_list)  # combine parent and offspring chromosomes
    '''-------non-dominated sorting-------'''
    front = ga.non_dominated_sorting(population_size, chroms_obj_record)

    '''----------selection----------'''
    population_list, new_pop = ga.selection(population_size, front, chroms_obj_record, total_chromosome)
    new_pop_obj = [chroms_obj_record[k] for k in new_pop]

    '''----------comparison----------'''
    if n == 0:
        best_list = copy.deepcopy(population_list)
        best_obj = copy.deepcopy(new_pop_obj)
    else:
        total_list = copy.deepcopy(population_list) + copy.deepcopy(best_list)
        total_obj = copy.deepcopy(new_pop_obj) + copy.deepcopy(best_obj)

        now_best_front = ga.non_dominated_sorting(population_size, total_obj)
        best_list, best_pop = ga.selection(population_size, now_best_front, total_obj, total_list)
        best_obj = [total_obj[k] for k in best_pop]
'''----------result----------'''
print('best list', best_list)
print('best obj', best_obj)
print('the elapsed time:%s' % (time.time() - start_time))


