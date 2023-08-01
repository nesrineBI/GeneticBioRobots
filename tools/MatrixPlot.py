#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.Abilities import Abilities
import pprint

#this class allows us to analyse the results of expérience 2 (121 simulations) and attribute thethe right abilities to prepare the data-plot
class Matrix:
    def __init__(self):
        self.x_keys = []
        self.y_keys = []
        self.x_len = 0
        self.y_len = 0
        self.x_keys_map = {}
        self.reversed_x_keys_map = {}
        self.y_keys_map = {}
        self.reversed_y_keys_map = {}
        self.matrix = [[]]
        self.threshold = 0.05

    def generate_matrix(self, channel1: {float: float}, channel2: {float: float}, threshold: float):
        self.threshold = threshold
        self.x_keys = sorted(channel1.keys())
        self.x_len = len(self.x_keys)
        self.y_keys = sorted(channel2.keys())
        self.y_len = len(self.y_keys)

        self.matrix = [[Abilities.NO_SELECTION] * self.y_len for i in range(self.x_len)]

        i = 0
        for k in self.x_keys:
            self.x_keys_map.update({k: i})
            self.reversed_x_keys_map.update({i: k})
            i += 1

        i = 0
        for k in self.y_keys:
            self.y_keys_map.update({k: i})
            self.reversed_y_keys_map.update({i: k})
            i += 1
        #give the abilities comparing to threshold
        for x in self.x_keys:
            i = self.x_keys_map[x]
            for y in self.y_keys:
                j = self.y_keys_map[y]
                if channel1[x] < threshold or channel2[y] < threshold:
                    value = Abilities.SELECTION
                    if channel2[y] < threshold <= channel1[x]:
                        if i != 0:
                            prev_x = self.reversed_x_keys_map[i-1]
                            if channel2[prev_x] < threshold:
                                value = Abilities.SWITCHING
                    elif channel1[x] < threshold and channel2[y] < threshold and i != 0 and j != 0:
                        value = Abilities.NO_SWITCHING

                    self.matrix[i][j] = value

    def get_x_keys(self):
        return self.x_keys

    def get_y_keys(self):
        return self.y_keys

    def get_value(self, x_key: float, y_key: float):
        return self.matrix[self.x_keys_map[x_key]][self.y_keys_map[y_key]]

    def normal_print(self):
        for x in self.matrix:
            print(x)

    def pretty_print(self):
        pp = pprint.PrettyPrinter(indent=0)
        pp.pprint(self.matrix)
