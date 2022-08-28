import pandas as pd
import numpy as np
import time
import copy
import ga

start_time = time.time()

''' ================= initialization setting ======================'''

# Enter input
population_size = int(input('Please input the size of population: ') or 20)
num_crossover = int(input('Please input the size of Crossover: ') or population_size / 2)
mutation_rate = float(input('Please input the size of Mutation Rate: ') or 0.3)
num_iteration = int(input('Please input number of iteration: ') or 1)

'''==================== main code ==============================='''
'''----- generate initial population -----'''
best_list, best_obj = [], []
population_list = ga.createPop(population_size)
for n in range(num_iteration):
    parent_list = ga.select_mating_pool(population_list, num_crossover)
    offspring_crossover_list = ga.crossover(parent_list)
    offspring_mutation_list = ga.mutation(population_list, mutation_rate)
    chroms_obj_record = {}  # record each chromosome objective values as chromosome_obj_record={chromosome:[HC_time,HC_record]}

    total_chromosome = np.concatenate((copy.deepcopy(parent_list), copy.deepcopy(
        offspring_crossover_list), copy.deepcopy(population_list), copy.deepcopy(
        offspring_mutation_list)))  # combine parent and offspring chromosomes
    for m in range(population_size * 2):
        HC_time, HC_resource = ga.fitness_value(total_chromosome[m])
        chroms_obj_record[m] = [HC_time, HC_resource]
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
        total_list = np.concatenate((copy.deepcopy(population_list), copy.deepcopy(best_list)))
        total_obj = np.concatenate((copy.deepcopy(new_pop_obj), copy.deepcopy(best_obj)))

        now_best_front = ga.non_dominated_sorting(population_size, total_obj)
        best_list, best_pop = ga.selection(population_size, now_best_front, total_obj, total_list)
        best_obj = [total_obj[k] for k in best_pop]
'''----------result----------'''
print('best list', best_list)
print('best obj', best_obj)
print('the elapsed time:%s' % (time.time() - start_time))
