#!/usr/bin/python3
# -*-coding: utf-8 -*

import random
from pyeasyga import pyeasyga
from operator import attrgetter
from GA.GaSimulator import GaSimulator
from tools import tools
from tools import Values
from tools.WangGaOptimizedMatrices import WangGaOptimizedMatrices
from copy import deepcopy
threshold = 0.05
current_model = ''

gen_number = 0
best_fitness = 0




# generated at random
# each weight or threshold is a single gene within the genome and is a real number in range [0,1]
def create_individual(data: [str]) -> [float]:
    return [random.uniform(0, 1) for _ in range(len(data))]


# A single crossover point on both parents' chains is randomly selected.
# All data beyond that point in either chain is swapped between the two parent genomes.
def one_point_crossover(parent_1: [float], parent_2: [float]) -> ([float], [float]):
    crossover_index = random.randrange(1, len(parent_1))
    child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
    child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
    return child_1, child_2


def simple_mutation(individual: [float]) -> [float]:
    mutate_index = random.randrange(len(individual))
    individual[mutate_index] = random.uniform(0, 1)


# the selection probability is proportional to the fitness of the individual
def roulette_wheel_selector(population: [pyeasyga.Chromosome]) -> pyeasyga.Chromosome:
    sum_of_fitness = 0
    fitnesses = []
    # sort from worst to fittest individual
    tmp_pop = deepcopy(population)

    tmp_pop.sort(key=attrgetter('fitness'))

    for individual in tmp_pop:
        sum_of_fitness += individual.fitness
        fitnesses.append(sum_of_fitness)

    rand = random.random() * sum_of_fitness

    for i in range(len(tmp_pop)):
        if rand < fitnesses[i]:
            return tmp_pop[i]

    # when rounding errors occur, we return the fittest individual
    return tmp_pop[-1]


def fitness(individual: [float], data: [str]) -> float:
    global gen_number
    print('Generation number: ' + str(gen_number))
    gen_number += 1

    # the last 3 values of the individual  must be negatives
    for i in range(1, 4):
        individual[-i] = -individual[-i]

    conf = {}
    model_conf = {}
    if current_model is 'dipm':
        conf = tools.config_dipm_exp2()
        model_conf = tools.get_dipm_base_generator()
    elif current_model is 'scpm':
        conf = tools.config_scpm_exp2()
        model_conf = tools.get_scpm_base_generator()

    # we update the model's weights' configuration
    model_conf = tools.update_conf(model_conf, data, individual)
    # we update the sim's configuration
    conf.update({'model_conf': {0: model_conf, 1: model_conf}})

    results = GaSimulator.run_sims(current_model, conf)
    matrix = GaSimulator.analyze_results(results, conf, threshold)

   
    
    if current_model is 'dipm':
        goal = WangGaOptimizedMatrices.dipm()
    if current_model is 'scpm':
        goal = WangGaOptimizedMatrices.scpm()

    fitness_value = tools.value_for_fitness(matrix, goal)

    global best_fitness
    if fitness_value != 0 and fitness_value >= best_fitness:
        best_fitness = fitness_value
        filename = 'result/ga/ga_' + str(current_model) + '_gen_' + str(tools.normalized_number(4, gen_number))\
                   + '_fit_' + str(fitness_value) + '.txt'
        tools.store_text([current_model, threshold, data, (fitness_value, individual)], filename)

    return fitness_value


def run_ga(data: [str], population_size: int, generations: int, crossover_proba: float,
           mutation_proba: float, elitism: bool) -> [str]:
    ga = pyeasyga.GeneticAlgorithm(data, population_size, generations, crossover_proba, mutation_proba, elitism)

    ga.create_individual = create_individual
    ga.crossover_function = one_point_crossover
    ga.mutate_function = simple_mutation
    ga.selection_function = roulette_wheel_selector
    ga.fitness_function = fitness

    random.seed()
    ga.run()
    return ga.best_individual()
