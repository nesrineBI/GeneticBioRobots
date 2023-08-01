#!/usr/bin/python3
# -*-coding: utf-8 -*


from DIPM import DIPM
import matplotlib.pyplot as plt
import pickle

simulator = None 



def load(file_name: str) -> dict:
    # Using pickle's deserialization to keep int keys as int
    with open(file_name, 'rb') as data_file:
        results = pickle.load(data_file)
    data_file.close()
    return results

config = None
results_file = 'result/exp3/results_dipm_exp3.p'
export_img = 'img/ga/dipm_exp3'

confiuration = {}

#init parameters of simulation
name = 'dipm1'
model_conf = {
	0: None,
	1: None,
	2: None
}
nb_sim = 5
time_interval = 1.0
channels = 3
time = 0.001
salience = {
        0: [0.0, 0.4, 0.4, 0.6, 0.4],
        1: [0.0, 0.0, 0.6, 0.6, 0.6],
        2: [0.0 for _ in range(0, nb_sim)]
}
thresholds = {}
gpi_outputs = {}
old_stn = []
dipms_list = {int: DIPM()}
selection_threshold = 0.05

for i in range(0, channels):
 dipm = DIPM();
    
 if model_conf[i] is not None:
   
   dipm.load_conf(model_conf[i])
            
 dipm.set_dt(time)
 dipms_list.update({i: dipm})
old_stn = [0.0 for _ in range(0, channels)]

for channel in range(0, channels):
	thresholds.update({channel: dipms_list[channel].get_theta_gpi()})
#pour chaque simulation
for s in range(0, nb_sim):
	#pour chaque pas de temps et chaque entrée
	for dt in range(0, int(1/time)):
		current_stn =[]
		for c in range(channels):
			values = dipms_list[c].compute_d1_to_gpi(salience[c][s], old_stn)
			current_stn.append(values['y_stn'])
			res = values['y_gpi']

			output = gpi_outputs.get(c, {})
			output.update({dt + s * int(1/time): res})
			gpi_outputs.update({c: output})
		old_stn = current_stn

simulation = {
	'salience': salience,
    'threshold': thresholds,
    'gpi_outputs': gpi_outputs
}


#save results 
with open(results_file, 'wb') as file:
        pickle.dump(simulation, file)
file.close()

#load data

data = load(results_file)

#plot the results 
outputs = sorted(data['gpi_outputs'].keys())

ordonnees = [[] for _ in range(3)]
# init the fig
fig = plt.figure(figsize=(9, 3), dpi=300)
for o in outputs:
    if o in [0, 1, 2]:
        
        sample_size = max(data['gpi_outputs'][o].keys())
        scale = int(sample_size / 1000)
           
        abscisses = [i for i in range(0, sample_size + 1, scale)]
        salience = []
        for i in abscisses:
            ordonnees[o].append(data['gpi_outputs'][o][i])
            salience.append(data['salience'][o][int(i / 1000)])

        # rows, column, plot number as 13X (1 row, 3 columns, channel X)
        fig_id = 100 + 3 * 10 + o + 1
        plt.subplot(fig_id)
        normalized_abcsisses = [a/1000.0 for a in abscisses]
        ax = plt.gca()
        ax.set_title('dipm' + ": channel " + str(o + 1))
        ax.set_xlim([0, 5])
        ax.set_ylim([0, 1])
        plt.plot(normalized_abcsisses, ordonnees[o])
        lines = plt.plot(normalized_abcsisses, salience)
        plt.setp(lines, color='blue')
        lines = plt.plot([0.0, 5.0], [selection_threshold, selection_threshold])
        plt.setp(lines, color='red')
        

#save results as img
if export_img is not (None or ''):
    plt.savefig(export_img)
    plt.show()
else:
    plt.show()
    
    plt.close(fig)



