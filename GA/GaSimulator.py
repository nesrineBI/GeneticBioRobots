#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.MatrixGa import Matrix
from tools.Abilities import Abilities
from tools import tools

from SCPM import SCPM
from DIPM import DIPM


# inputs for the two channels
salience =  [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]



class GaSimulator:

    @staticmethod
    def run_sims(model: str, conf: {}) -> {}:
        sim = None
        results = {}

       
        salience =  [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        for sc1 in salience:
            sal1 = [0.0] + [sc1 for _ in range(5)]
            
            for sc2 in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
                print("sc1  " +str(sc1)+" sc2 "+str(sc2))
                sal2 = [0.0, 0.0] + [sc2 for _ in range(4)]

                # input pair
                sal = {
                    0: sal1,
                    1: sal2
                }
                conf.update({'salience': sal})

                if model == 'dipm':
                    dipms = {}
                    config = None
                    gpi_output = {float: {float: float}}
                    dt = 0.001
                    old_stn_list = []
                    result_file = ''
                    
                #config
                    config = conf
                    channels = config['channels']
                    dipms_conf = config['model_conf']
                    dt = config['dt']
                    for i in range(0, channels):
                        dipm = DIPM()
                        # if conf of weights and all, load and add
                        if dipms_conf[i] is not None:
                            dipm.load_conf(dipms_conf[i])
                        dipm.set_dt(dt)
                        # add the DIPM
                        dipms.update({i: dipm})
                    old_stn_list = [0.0 for _ in range(0, channels)]
                        
                    #run sim
                    channels = config['channels']
                    salience = config['salience']
                    thresholds = {}
                    gpi_outputs = {}
                                    
                    for channel in range(channels):
                        thresholds.update({channel: dipms[channel].get_theta_gpi()})
                                            
                    # main loop of the simulation
                    for r in range(0, config['nb_of_runs']):
                        # for each time step and each channel, computes its output
                        for t in range(0, int(1/dt)):
                            stn_list = []
                            for channel in range(channels):
                                values = dipms[channel].compute_d1_to_gpi(salience[channel][r], old_stn_list)
                                stn_list.append(values['y_stn'])
                                res = values['y_gpi']

                                # we store it
                                new = gpi_outputs.get(channel, {})
                                new.update({t + r * int(1/dt): res})
                                gpi_outputs.update({channel: new})
                                # update the old list of stn values
                                old_stn_list = stn_list
                                                                    
                    # once the sim finished, store the results
                    simulation = {
                        'salience': salience,
                        'threshold': thresholds,
                        'gpi_outputs': gpi_outputs
                                }
                    if result_file != '':
                       tools.store_data(simulation, result_file)
                    results.update({(sc1, sc2): simulation})
                
                elif model == 'scpm':
                    scpms = {int: SCPM()}
                    config = None
                    gpi_output = {float: {float: float}}
                    dt = 0.001
                    old_stn_list = []
                
                    #config
                    config = conf
                    channels = config['channels']
                    scpms_conf = config['model_conf']
                    dt = config['dt']
                    for i in range(0, channels):
                        scpm = SCPM()
                        # if conf of weights and all, load and add
                        if scpms_conf[i] is not None:
                            scpm.load_conf(scpms_conf[i])
                        scpm.set_dt(dt)
                        # add the SCPM
                        scpms.update({i: scpm})
                    old_stn_list = [0.0 for _ in range(0, channels)]
                    
                                    #channels = config['channels']
                    salience = config['salience']
                    thresholds = {}
                    gpi_outputs = {}
                    result_file = ''
                                    
                    for channel in range(0, channels):
                        thresholds.update({channel: scpms[channel].get_theta_gpi()})
                                    
                    # main loop of the simulation
                    for r in range(0, config['nb_of_runs']):
                        # for each time step and each channel, computes its output
                        for t in range(0, int(1/dt)):
                            stn_list = []
                            for channel in range(0, channels):
                                values = scpms[channel].compute_d1_to_gpi(salience[channel][r], old_stn_list)
                                stn_list.append(values['y_stn'])
                                res = values['y_gpi']
                                    
                                # we store it
                                new = gpi_outputs.get(channel, {})
                                new.update({t + r * int(1/dt): res})
                                gpi_outputs.update({channel: new})
                            # update the old list of stn values
                            old_stn_list = stn_list
                                    
                    # once the sim finished, store the results
                    simulation = {
                        'salience': salience,
                        'threshold': thresholds,
                        'gpi_outputs': gpi_outputs
                            }
                    if result_file != '':
                        tools.store_data(simulation, result_file)
                
                    results.update({(sc1, sc2): simulation})
                    
                     

        return results

    # generates the matrix of outputs
    @staticmethod
    def analyze_results(results: [{}], conf: {}, threshold) -> Matrix:
        dt = conf['dt']
        salience =  [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        
        
        matrix = Matrix()
        tmp_matrix = [[Abilities.NO_SELECTION] * len(salience) for _ in range(len(salience))]
       
        i = 0
        for sc1 in salience:
            j = 0
            for sc2 in salience:
                
                
                outputs = results[(sc1, sc2)]
               
                gpi_outputs = outputs['gpi_outputs']
                
                ability = tools.determine_ability(gpi_outputs, dt, threshold)
                
                tmp_matrix[i][j] = ability
                j += 1
            i += 1

        matrix.init_matrix(tmp_matrix)
        return matrix
