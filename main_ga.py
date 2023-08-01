#!/usr/bin/python3
# -*-coding: utf-8 -*

from GA import GA
from tools import tools



population_size = 100
generations = 3
crossover_proba = 0.8
mutation_proba = 0.02
elitism = True

# models = ['dipm', 'scpm']
models = ['scpm']
# models = ['scpm']

for model in models:
    # data : genes (weights and thresholds) of the genome
    data = [str]
    if model == 'dipm':
        data = ['wcs1', 'wcs2', 'wsd2_gpe', 'wgpe_stn', 'wsd1_gpi', 'wstn_gpi', 'theta_d1', 'theta_d2', 'theta_gpe',
                'theta_stn', 'theta_gpi']

    elif model == 'scpm':
        data = ['wcs1', 'wcs2', 'wsd2_gpe', 'wc_stn', 'wgpe_stn', 'wsd1_gpi', 'wstn_gpe', 'wstn_gpi', 'wgpe_gpi',
                'theta_d1', 'theta_d2', 'theta_gpe', 'theta_stn', 'theta_gpi']

    GA.threshold = 0.05
    GA.current_model = model
    GA.gen_number = 0
    result = GA.run_ga(data, population_size, generations, crossover_proba, mutation_proba, elitism)

    text = [
        model,
        GA.threshold,
        data,
        result
    ]

    binaries = {
        'model': model,
        'threshold': GA.threshold,
        'data': data,
        'result': result
    }

    filename = 'result/ga_' + model + '_results'
    tools.store_text(text, filename + '.txt')
    tools.store_data(binaries, filename + '.p')
