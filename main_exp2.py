#!/usr/bin/python3
# -*-coding: utf-8 -*

import tools.MatrixPlot as MatrixPlot
import pickle
import matplotlib.pyplot as plt
from tools import tools

import tools.Display as Display


#not need
def get_scpm_improved_generator():
    conf = tools.get_dipm_base_generator()
    conf.update({'wcs1': 1.15})
    conf.update({'wcs2': 1.15})
    return conf

#configuration of experience 2
def config_exp2() -> {}:
    conf = {}
    name = 'scpm2'
    basic_conf = tools.get_scpm_base_generator()
    model_conf = {
        0: basic_conf,
        1: basic_conf,
    }
    salience = {
        0: [0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.0],
        1: [0.0, 0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    }
    channels = len(salience)
    nb_of_runs = len(salience[0])
    time_interval = 0.1
    dt = 0.001
    
    conf.update({'name': name})
    conf.update({'model_conf': model_conf})
    conf.update({'nb_of_runs': nb_of_runs})
    conf.update({'time_interval': time_interval})
    conf.update({'channels': channels})
    conf.update({'salience': salience})
    conf.update({'dt': dt})
    
    #conf.update({'basic_conf': get_scpm_improved_generator()})
    
    return conf

#load a file
def load(file_name: str) -> dict:
    # Using pickle's deserialization to keep int keys as int
    with open(file_name, 'rb') as data_file:
        results = pickle.load(data_file)
    data_file.close()
    return results








#main script of expérience 2 to get results
def get_results():
   
   #init
    results = {}
    channels = config_exp2()['channels']
    salience = config_exp2()['salience']
    dt = config_exp2()['dt']
  

    models = ['dipm', 'scpm']

    
    model_res = {}
    #main loop
    for model in models:  # for each model
        for sim_number in range(0, 121):  # for each simulation
            filename = 'result/exp2-1/' + 'results_' + model + '_exp2_' + tools.normalized_number(3, sim_number) + '.p'
            data = load(filename)
            gpi_outputs = data['gpi_outputs']
            channel_res = {}
            for channel in range(0, channels):  # for each channel
                tmp = []
                salience_res = {}
                for s in range(0, len(salience[channel])):  # for each salience 0.0, 0.1, ..., 1.0 of channel channel
                    time_intervals = int(1/dt)
                    for i in range(0, time_intervals):  # for each dt of salience s
                        tmp.append(gpi_outputs[channel][i + s * time_intervals])  # append outputs of gpi to tmp
                    avg = sum(tmp) / len(tmp)   # we average the whole interval
                    val = salience_res.get(salience[channel][s], [])
                    val.append(avg)
                    salience_res.update({salience[channel][s]: val})
                channel_res.update({channel: salience_res})
            val = model_res.get(model, {})
            val.update({sim_number: channel_res})
            model_res.update({model: val})



    res_tmp = {}
    for model in models:
        chan_tmp = {}
        for exp in model_res[model]:
            for channel in model_res[model][exp]:
                sal_tmp = {}
                for sal in model_res[model][exp][channel]:
                    tmp = sal_tmp.get(sal, [])
                    for value in model_res[model][exp][channel][sal]:
                        tmp.append(value)
                    sal_tmp.update({sal: tmp})
                chan_tmp.update({channel: sal_tmp})
            res_tmp.update({model: chan_tmp})



    for model in models:
        chan = results.get(model, {})
        for channel in res_tmp[model]:
            sal = chan.get(channel, {})
            for s in res_tmp[model][channel]:
                res = sum(res_tmp[model][channel][s]) / len(res_tmp[model][channel][s])
                sal.update({s: res})
            chan.update({channel: sal})
        results.update({model: chan})

   

    return results


#not need
def display_curves(results):
    for model in results.keys():
        title = str(model) + ' exp2'
        export_name = str(model) + '_exp2'
        Display.save_simple(results[model], title, 'img/exp2/' + export_name)


def exp2(model: str, export_name: str):
    #get results
    results = get_results()
    #display_curves(results)
    
    #initialise plot
    matrix = MatrixPlot.Matrix()
    if model is 'dipm':
        
        #get matrix plot
        matrix.generate_matrix(results['dipm'][0], results['dipm'][1], 0.05)
    elif model is 'scpm':
        
        #get matrix plot
        matrix.generate_matrix(results['scpm'][0], results['dipm'][1], 0.14)
    #save plot
    coordinates_tenths = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    coordinates = [coordinates_tenths, coordinates_tenths]
    Display.display_save_figure(model,matrix, '', export_name, coordinates)





def main():
   
#run here
    exp2('dipm', export_name="img/exp2/dipm_abilities_matrix.png")
    #exp2('scpm', export_name="img/exp2/scpm_abilities_matrix.png")



main()
