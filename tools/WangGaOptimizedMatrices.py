#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.Abilities import Abilities
from tools.Matrix import Matrix

#here we present the matrix Goal that we want to have comparing with the Wang's experiments
class WangGaOptimizedMatrices:
    @staticmethod
    def dipm() -> Matrix:
        mat = [  # in x we store the y
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING]
        ]
        matrix = Matrix()
        matrix.init_matrix(mat)
        return matrix

    @staticmethod
    def pprint_dipm():
        WangGaOptimizedMatrices.dipm().pprint()

    @staticmethod
    def scpm() -> Matrix:
        mat = [  # in x we store the y
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING]
        ]
        matrix = Matrix()
        matrix.init_matrix(mat)
        return matrix

    @staticmethod
    def pprint_scpm():
        WangGaOptimizedMatrices.scpm().pprint()
