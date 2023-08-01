from tools.Abilities import Abilities
from tools.MatrixGa import Matrix
import pickle
import pprint
import copy

#this class represent the diffents additional tools that we use in experiments



def store_data(data: dict, file_name: str):
    # Using pickle's serialization to keep int keys as int
    with open(file_name, 'wb') as results_file:
        pickle.dump(data, results_file)
    results_file.close()



def store_text(text: [str], file_name: str):
    with open(file_name, 'w') as results_file:
        for t in text:
            line = str(t) + '\n'
            results_file.write(line)
    results_file.close()

def strip_and_split(txt: str, chars: [str], splitter: str) -> [str]:
    tmp = copy.deepcopy(txt)
    for char in chars:
        tmp = tmp.replace(char, '')
    
    return tmp.split(splitter)

def get_dipm_base_generator():
    conf = {}
    
    # weights
    conf.update({'wcs1': 1.0})
    conf.update({'wcs2': 1.0})
    conf.update({'wsd2_gpe': 1.0})
    conf.update({'wgpe_stn': 1.0})
    conf.update({'wsd1_gpi': 1.0})
    conf.update({'wstn_gpi': 0.8})
    
    # threshold
    conf.update({'theta_d1': 0.2})
    conf.update({'theta_d2': 0.2})
    conf.update({'theta_gpe': -0.2})
    conf.update({'theta_stn': -0.25})
    conf.update({'theta_gpi': -0.2})
    
    # slope parameter
    conf.update({'m': 1.0})
    # activation rate
    conf.update({'k': 25.0})
    # time increment
    conf.update({'dt': 0.001})
    
    # activation
    conf.update({'a_d1': 0.0})
    conf.update({'a_d2': 0.0})
    conf.update({'a_gpe': 0.0})
    conf.update({'a_stn': 0.0})
    conf.update({'a_gpi': 0.0})
    
    return conf


def get_scpm_base_generator():
    conf = {}
    
    # weights
    conf.update({'wcs1': 1.0})
    conf.update({'wcs2': 1.0})
    conf.update({'wsd2_gpe': 1.0})
    conf.update({'wc_stn': 1.0})
    conf.update({'wgpe_stn': 1.0})
    conf.update({'wsd1_gpi': 1.0})
    conf.update({'wstn_gpe': 0.8})
    conf.update({'wstn_gpi': 0.8})
    conf.update({'wgpe_gpi': 0.4})
    
    # threshold
    conf.update({'theta_d1': 0.2})
    conf.update({'theta_d2': 0.2})
    conf.update({'theta_gpe': -0.2})
    conf.update({'theta_stn': -0.25})
    conf.update({'theta_gpi': -0.2})
    
    # slope parameter
    conf.update({'m': 1.0})
    # activation rate
    conf.update({'k': 25.0})
    # time increment
    conf.update({'dt': 0.001})
    
    # activation
    conf.update({'a_d1': 0.0})
    conf.update({'a_d2': 0.0})
    conf.update({'a_gpe': 0.0})
    conf.update({'a_stn': 0.0})
    conf.update({'a_gpi': 0.0})
    
    return conf


def config_dipm_exp2() -> {}:
    conf = {}
    name = 'dipm2'
    model_conf = {
        0: None,
        1: None,
    }
    channels = 2
    nb_of_runs = 6
    time_interval = 1
    dt = 0.001

    conf.update({'name': name})
    conf.update({'model_conf': model_conf})
    conf.update({'nb_of_runs': nb_of_runs})
    conf.update({'time_interval': time_interval})
    conf.update({'channels': channels})
    conf.update({'dt': dt})

    return conf


def config_scpm_exp2() -> {}:
    conf = {}
    name = 'scpm2'
    model_conf = {
        0: None,
        1: None,
    }
    channels = 2
    nb_of_runs = 6
    time_interval = 1
    dt = 0.001

    conf.update({'name': name})
    conf.update({'model_conf': model_conf})
    conf.update({'nb_of_runs': nb_of_runs})
    conf.update({'time_interval': time_interval})
    conf.update({'channels': channels})
    conf.update({'dt': dt})

    return conf



def update_conf(conf: {}, param: [str], value: [float]) -> {}:
    for i in range(len(param)):
        conf.update({param[i]: value[i]})
    return conf

def load_txt(file_name: str) -> [str]:
    with open(file_name) as f:
        content = f.readlines()
    content = [line.strip() for line in content]
    return content



def normalized_number(size: int, number: int) -> str:
    n = str(number)
    tmp = ''
    s = size - len(n)
    for i in range(0, s):
        tmp += '0'
    return tmp + n






# determines the outcome of the simulation: Selection, No Selection, Switching or No Switching
def determine_ability(outputs: {}, dt: float, threshold: float) -> Abilities:
    chan1 = outputs[0]
    chan2 = outputs[1]
    pas_par_seconde = (1 / dt)
    keys_chan1 = chan1.keys()

    # channel 1 ever selected?
    chan1_never_selected = True
    for t in keys_chan1:
        if chan1[t] <= threshold:
            chan1_never_selected = False
            break

    # channel 1 selected in I1?
    selected = 0
    for t in range(int(1 * pas_par_seconde), int(2 * pas_par_seconde + 1)):
        if chan1[t] <= threshold:
            selected += 1
    chan1_i1_selected = True if selected >= 0.8 * pas_par_seconde else False

    # channel 1 selected in I2? channel 2 selected in I2?
    selected_chan1 = 0
    selected_chan2 = 0
    for t in range(int(2 * pas_par_seconde + 1), int(len(chan2))):
        if chan1[t] <= threshold:
            selected_chan1 += 1
        if chan2[t] <= threshold:
            selected_chan2 += 1
    chan1_i2_selected = True if selected_chan1 >= 0.8 * (len(chan2) - (2 * pas_par_seconde + 1)) else False
    chan2_selected = True if selected_chan2 >= 0.8 * (len(chan2) - (2 * pas_par_seconde + 1)) else False

    # NO SELECTION: Neither active channel becomes selected
    ability = Abilities.NO_SELECTION

    # SELECTION: a single channel is selected
    # either channel 1 becomes selected in the 1st interval or channel 2 becomes selected in the 2nd interval
    if (chan1_i1_selected and not chan2_selected) or (chan1_never_selected and chan2_selected):
        ability = Abilities.SELECTION
    # NO SWITCHING: channel 1 is selected in I1 and concurrent channel selection occurs in I2
    elif chan1_i1_selected and chan1_i2_selected and chan2_selected:
        ability = Abilities.NO_SWITCHING
    # SWITCHING: channel 1 is selected in I1, then becomes de-selected as channel 2 becomes selected in I2
    elif chan1_i1_selected and not chan1_i2_selected and chan2_selected:
        ability = Abilities.SWITCHING

    return ability





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
    




def load_individual(filename: str):
    content = load_txt(filename)
    model = content[0]
    threshold = float(content[1])
    strip = ['[', ']', '(', ')', '\'']
    data = strip_and_split(content[2], strip, ', ')
    tmp = strip_and_split(content[3], strip, ', ')
    fitness_value = int(tmp.pop(0))
    individual = [float(s) for s in tmp]
    return model, threshold, fitness_value, data, individual
