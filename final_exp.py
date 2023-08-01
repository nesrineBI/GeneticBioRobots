
from tools.MatrixGa import Matrix
from tools.Abilities import Abilities
from tools import Display
from tools import tools
from GA.GaSimulator import GaSimulator
from tools.WangGaOptimizedMatrices import WangGaOptimizedMatrices




# for the fitness function : gives +1 if the outcome is the same as the goal outcome
def get_reward(evaluated: Abilities, goal: Abilities) -> int:
    res = 0
    if evaluated is goal:
        res = 1
    return res


# compares the GA-optimized output matrix to the goal matrix
def value_for_fitness(test: Matrix, goal: Matrix) -> float:
    x_len = test.get_x_len()
    y_len = test.get_y_len()

    fitness_value = 0
    for x in range(x_len):
        for y in range(y_len):
            fitness_value += get_reward(test.get_item(x, y), goal.get_item(x, y))

    return fitness_value

def exp3(model, individual, data, threshold, export_file, title):
    #get initial configuration of dipm
    conf = {}
    model_conf = {}
    if model == 'dipm':
        conf = {}
        name = 'dipm2'
        model_conf = {
            0: None,
            1: None,
            }
        channels = 2
        nb_of_runs = 5
        time_interval = 1
        dt = 0.001

        conf.update({'name': name})
        conf.update({'model_conf': model_conf})
        conf.update({'nb_of_runs': nb_of_runs})
        conf.update({'time_interval': time_interval})
        conf.update({'channels': channels})
        conf.update({'dt': dt})
        
        model_conf = tools.get_dipm_base_generator()
    #get initial configuration of scpm
    elif model == 'scpm':
        conf = {}
        name = 'scpm2'
        model_conf = {
           0: None,
           1: None,
           }
        channels = 2
        nb_of_runs = 5
        time_interval = 1
        dt = 0.001

        conf.update({'name': name})
        conf.update({'model_conf': model_conf})
        conf.update({'nb_of_runs': nb_of_runs})
        conf.update({'time_interval': time_interval})
        conf.update({'channels': channels})
        conf.update({'dt': dt})
        model_conf = tools.get_scpm_base_generator()

    # we update the model's weights' configuration
    for i in range(len(data)):
        model_conf.update({data[i]: individual[i]})
    
    # we update the sim's configuration
    conf.update({'model_conf': {0: model_conf, 1: model_conf}})

    results = GaSimulator.run_sims(model, conf)
    matrix = GaSimulator.analyze_results(results, conf, threshold)
    goal = WangGaOptimizedMatrices.scpm()
    print('Fitness value: ' + str(value_for_fitness(matrix, goal)))

    
    coordinates_tenths = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    coordinates = [coordinates_tenths, coordinates_tenths]
    Display.save_simple_abilities_matrix(matrix, title, export_file, coordinates)



def main_exp3_config():
    
 
    #path = 'result/ga/scpm/'
    #filename = 'ga_scpm_gen_0226_fit_65.txt'
    path = 'result/ga_final/'
    filename = 'ga_dipm_results.txt'
    #path = 'result/ga_final/'
    #filename = 'ga_scpm_results.txt'
    
    #load data that we get with GA
    model, threshold, fitness_value, data, individual = tools.load_individual(path + filename)

    export_file = 'img/ga/'+model+'_ga.png'
    title = 'GA-' + model.upper() + ', fitness: ' + str(fitness_value)
    #main loop
    exp3(model, individual, data, threshold, export_file, title)


def main():
    
    main_exp3_config()

    pass


main()
