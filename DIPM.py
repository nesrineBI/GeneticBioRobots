#!/usr/bin/python3
# -*-coding: utf-8 -*





class DIPM:
    def __init__(self):
        # weights
        self.wcs1 = 0.7965933524729384 #1.0
        self.wcs2 = 0.9933189996262195 #1.0
        self.wsd2_gpe = 0.7498378125116993 #1.0
        self.wgpe_stn = 0.7562354658044542 #1.0
        self.wsd1_gpi = 0.7841440060395849 #1.0
        self.wstn_gpi = 0.765171786187149 #0.8

        # thresholds
        self.theta_d1 = 0.2022375727033796 #0.2
        self.theta_d2 = 0.32917845471779494 #0.2
        self.theta_gpe = -0.5328443795460719 #-0.2
        self.theta_stn = -0.4129138058219399 #-0.25
        self.theta_gpi = -0.1467758116462642 #-0.2

        # slope parameter
        self.m = 1.0
        # activation rate
        self.k = 25
        # time increment
        self.dt = 0.001

        # activation
        self.a_d1 = 0.0
        self.a_d2 = 0.0
        self.a_gpe = 0.0
        self.a_stn = 0.0
        self.a_gpi = 0.0

        # dopamine levels
        self.dopamine_level_d1 = 0.2
        self.dopamine_level_d2 = 0.2

        # storage of u_xxx values
        self.u_d1 = 0.0
        self.u_d2 = 0.0
        self.u_gpe = 0.0
        self.u_stn = 0.0
        self.u_gpi = 0.0

        # storage of y_xxx values
        self.y_d1 = 0.0
        self.y_d2 = 0.0
        self.y_gpe = 0.0
        self.y_stn = 0.0
        self.y_gpi = 0.0

        # old activation
        self.old_a_d1 = 0.0
        self.old_a_d2 = 0.0
        self.old_a_gpe = 0.0
        self.old_a_stn = 0.0
        self.old_a_gpi = 0.0

        # storage of old u_xxx values
        self.old_u_d1 = 0.0
        self.old_u_d2 = 0.0
        self.old_u_gpe = 0.0
        self.old_u_stn = 0.0
        self.old_u_gpi = 0.0

        # storage of old y_xxx values
        self.old_y_d1 = 0.0
        self.old_y_d2 = 0.0
        self.old_y_gpe = 0.0
        self.old_y_stn = 0.0
        self.old_y_gpi = 0.0
    #HeavisideFunction
    def calculate_H_function(self,number):
        return 0 if number < 0 else 1
    
    def get_theta_gpi(self) -> float:
        return self.theta_gpi
        
    def set_dt(self, dt: float):
        self.dt = dt
    #generic function to calculate the output of neuronne
    def output(self, a: float, theta: float) -> float:
        return self.m * (a - theta) * self.calculate_H_function(a - theta)
    #calculate the activation of neuronne
    def a_plus_delta_a(self, a: float, u: float) -> float:
        return a - self.k * (a - u) * self.dt

    # StratiumD1
    def u_i_d1(self, y_c: float) -> float:
        return self.wcs1 * y_c

    # StratiumD2
    def u_i_d2(self, y_c: float) -> float:
        return self.wcs2 * y_c

    # GPe
    def u_i_gpe(self, y_d2: float) -> float:
        return (-self.wsd2_gpe) * y_d2

    # STN
    def u_i_stn(self, y_gpe: float) -> float:
        return -self.wgpe_stn * y_gpe

    # GPi
    def u_i_gpi(self, y_d1: float, stn_list: list) -> float:
        return (-self.wsd1_gpi * y_d1) + (self.wstn_gpi * sum(stn_list))

    #call the differents function to calculate the get the input and calculate the output of d1
    def compute_d1(self, salience: float) -> float:
        self.u_d1 = self.u_i_d1(salience * (1 + self.dopamine_level_d1))
        self.a_d1 = self.a_plus_delta_a(self.old_a_d1, self.old_u_d1)
        self.y_d1 = self.output(self.old_a_d1, self.theta_d1)
        return self.y_d1
    #call the differents function to calculate the get the input and calculate the output of d2
    def compute_d2(self, salience: float) -> float:
        self.u_d2 = self.u_i_d2(salience * (1 - self.dopamine_level_d2))
        self.a_d2 = self.a_plus_delta_a(self.old_a_d2, self.old_u_d2)
        self.y_d2 = self.output(self.old_a_d2, self.theta_d2)
        return self.y_d2

    # requires previous values of stn outputs (at t-1)
    #call the differents function to calculate the get the input and calculate the output of gpe
    def compute_gpe(self, y_d2: float) -> float:
        self.u_gpe = self.u_i_gpe(y_d2)
        self.a_gpe = self.a_plus_delta_a(self.old_a_gpe, self.old_u_gpe)
        self.y_gpe = self.output(self.old_a_gpe, self.theta_gpe)
        return self.y_gpe

    #call the differents function to calculate the get the input and calculate the output of stn
    def compute_stn(self, y_gpe: float) -> float:
        self.u_stn = self.u_i_stn(y_gpe)
        self.a_stn = self.a_plus_delta_a(self.old_a_stn, self.old_u_stn)
        self.y_stn = self.output(self.old_a_stn, self.theta_stn)
        return self.y_stn

    #call the differents function to calculate the get the input and calculate the output of gpi
    def compute_gpi(self, y_d1: float, stn_list: [float]) -> float:
        self.u_gpi = self.u_i_gpi(y_d1, stn_list)
        self.a_gpi = self.a_plus_delta_a(self.old_a_gpi, self.old_u_gpi)
        self.y_gpi = self.output(self.old_a_gpi, self.theta_gpi)
        return self.y_gpi

    #function which represent all the process of DIPM
    def compute_d1_to_gpi(self, salience: float, stn_list: [float]) -> {str: float}:
        self.compute_d1(salience)
        self.compute_d2(salience)
        self.compute_gpe(self.old_y_d2)
        self.compute_stn(self.old_y_gpe)
        self.compute_gpi(self.old_y_d1, stn_list)
        self.store_old_values()
        return {'y_d1': self.y_d1, 'y_d2': self.y_d2, 'y_gpe': self.y_gpe, 'y_stn': self.y_stn, 'y_gpi': self.y_gpi}

#some additional function to store and load params
    def store_old_values(self):
        self.old_a_d1 = self.a_d1
        self.old_a_d2 = self.a_d2
        self.old_a_gpe = self.a_gpe
        self.old_a_stn = self.a_stn
        self.old_a_gpi = self.a_gpi
        self.old_u_d1 = self.u_d1
        self.old_u_d2 = self.u_d2
        self.old_u_gpe = self.u_gpe
        self.old_u_stn = self.u_stn
        self.old_u_gpi = self.u_gpi
        self.old_y_d1 = self.y_d1
        self.old_y_d2 = self.y_d2
        self.old_y_gpe = self.y_gpe
        self.old_y_stn = self.y_stn
        self.old_y_gpi = self.y_gpi

    def load_conf(self, conf):
        self.wcs1 = conf['wcs1']
        self.wcs2 = conf['wcs2']
        self.wsd2_gpe = conf['wsd2_gpe']
        self.wgpe_stn = conf['wgpe_stn']
        self.wsd1_gpi = conf['wsd1_gpi']
        self.wstn_gpi = conf['wstn_gpi']
        self.theta_d1 = conf['theta_d1']
        self.theta_d2 = conf['theta_d2']
        self.theta_gpe = conf['theta_gpe']
        self.theta_stn = conf['theta_stn']
        self.theta_gpi = conf['theta_gpi']
        self.m = conf['m']
        self.k = conf['k']
        self.dt = conf['dt']
        self.a_d1 = conf['a_d1']
        self.a_d2 = conf['a_d2']
        self.a_gpe = conf['a_gpe']
        self.a_stn = conf['a_stn']
        self.a_gpi = conf['a_gpi']

    
