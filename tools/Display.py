#!/usr/bin/python3
# -*-coding: utf-8 -*

import matplotlib.pyplot as plt
from tools.Abilities import Abilities

from tools.Matrix import Matrix
import matplotlib.patches as mpatches

"""
def display_and_save(gpi_outputs: {int: {int: float}}, title: str, export_name: str, channels_to_display: [int]):
    channels = sorted(gpi_outputs.keys())
    # one empty list per channel
    ordonnees = [[] for _ in range(len(channels_to_display))]
    # init the fig
    fig = plt.figure(figsize=(3*len(channels_to_display), 3), dpi=300)
    for channel in channels:
        if channel in channels_to_display:
            # max should be len, but we get an error because we do not have all of our points...
            sample_size = max(gpi_outputs[channel].keys())
            scale = int(sample_size / 1000)
            # 1000 per plot max, so we pick only one value out of size/1000

            abscisses = [i for i in range(0, sample_size + 1, scale)]
            for i in abscisses:
                ordonnees[channel].append(gpi_outputs[channel][i])

            # rows, column, plot number as 13X (1 row, 3 columns, channel X)
            fig_id = 100 + len(channels_to_display) * 10 + channel + 1
            plt.subplot(fig_id)
            normalized_abcsisses = [a/1000.0 for a in abscisses]
            ax = plt.gca()
            ax.set_title(title + ": channel " + str(channel + 1))
            ax.set_xlim([0, 5])
            ax.set_ylim([0, 1])
            plt.plot(normalized_abcsisses, ordonnees[channel])

    if export_name is not (None or ''):
        plt.savefig(export_name)
    else:
        plt.show()

    plt.close(fig)


def save_simple(gpi_outputs: {int: {float: float}},
                title: str,
                export_name: str):
    channels = sorted(gpi_outputs.keys())
    # one empty list per channel
    ordinates = [[] for _ in range(len(channels))]
    # init the fig
    fig = plt.figure(figsize=(3*len(channels), 3), dpi=300)
    for channel in channels:
        abscissae = sorted(gpi_outputs[channel].keys())
        for a in abscissae:
            ordinates[channel].append(gpi_outputs[channel][a])

        # rows, column, plot number as 13X (1 row, 3 columns, channel X)
        fig_id = 100 + len(channels) * 10 + channel + 1
        plt.subplot(fig_id)
        ax = plt.gca()
        ax.set_title(title + ": channel " + str(channel + 1))
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        plt.plot(abscissae, ordinates[channel])
        lines = plt.plot(abscissae, abscissae)
        plt.setp(lines, color='red')

    if export_name is not (None or ''):
        plt.savefig(export_name)
    else:
        plt.show()

    plt.close(fig)


def display_all_and_save(gpi_outputs: {int: {int or float: float}}, title: str, export_name: str,
                         channels_to_display: [int], saliences: {int: [float]}, selection_threshold: float):
    channels = sorted(gpi_outputs.keys())
    # one empty list per channel
    ordonnees = [[] for _ in range(len(channels_to_display))]
    # init the fig
    fig = plt.figure(figsize=(3*len(channels_to_display), 3), dpi=300)
    for channel in channels:
        if channel in channels_to_display:
            # max should be len, but we get an error because we do not have all of our points...
            sample_size = max(gpi_outputs[channel].keys())
            scale = int(sample_size / 1000)
            # 1000 per plot max, so we pick only one value out of size/1000

            abscisses = [i for i in range(0, sample_size + 1, scale)]
            salience = []
            for i in abscisses:
                ordonnees[channel].append(gpi_outputs[channel][i])
                salience.append(saliences[channel][int(i / 1000)])

            # rows, column, plot number as 13X (1 row, 3 columns, channel X)
            fig_id = 100 + len(channels_to_display) * 10 + channel + 1
            plt.subplot(fig_id)
            normalized_abcsisses = [a/1000.0 for a in abscisses]
            ax = plt.gca()
            ax.set_title(title + ": channel " + str(channel + 1))
            ax.set_xlim([0, 5])
            ax.set_ylim([0, 1])
            plt.plot(normalized_abcsisses, ordonnees[channel])
            lines = plt.plot(normalized_abcsisses, salience)
            plt.setp(lines, color='red')
            lines = plt.plot([0.0, 5.0], [selection_threshold, selection_threshold])
            plt.setp(lines, color='green')

    if export_name is not (None or ''):
        plt.savefig(export_name)
        plt.show()
    else:
        plt.show()

    plt.close(fig)


def flexible_display_or_save(gpi_outputs: {int: {int or float: float}},
                             title: str,
                             export_name: str,
                             channels_to_display: [int],
                             saliences: {int: [float]},
                             selection_threshold: float):
    channels = sorted(gpi_outputs.keys())
    # one empty list per channel
    ordonnees = [[] for _ in range(len(channels_to_display))]
    # init the fig
    fig = plt.figure(figsize=(3*len(channels_to_display), 3), dpi=300)
    for channel in channels:
        if channel in channels_to_display:
            x_lim = len(saliences[0])
            # max should be len, but we get an error because we do not have all of our points...
            sample_size = max(gpi_outputs[channel].keys())
            scale = int(sample_size / 1000)
            # 1000 per plot max, so we pick only one value out of size/1000

            abscisses = [i for i in range(0, sample_size + 1, scale)]
            salience = []
            for i in abscisses:
                ordonnees[channel].append(gpi_outputs[channel][i])
                salience.append(saliences[channel][int(i / 1000)])

            # rows, column, plot number as 13X (1 row, 3 columns, channel X)
            fig_id = 100 + len(channels_to_display) * 10 + channel + 1
            plt.subplot(fig_id)
            normalized_abcsisses = [a/1000.0 for a in abscisses]
            ax = plt.gca()
            ax.set_title(title + ": channel " + str(channel + 1))
            ax.set_xlim([0, x_lim])
            ax.set_ylim([0, 1])
            plt.plot(normalized_abcsisses, ordonnees[channel])
            lines = plt.plot(normalized_abcsisses, salience)
            plt.setp(lines, color='red')
            lines = plt.plot([0.0, x_lim], [selection_threshold, selection_threshold])
            plt.setp(lines, color='green')

    if export_name is not (None or ''):
        plt.savefig(export_name)
    else:
        plt.show()

    plt.close(fig)
"""
def display_save_figure1(model: str, matrix: Matrix, title: str, export_name: str):
    x_no_selection = []
    x_selection = []
    x_no_switching = []
    x_switching = []
    y_no_selection = []
    y_selection = []
    y_no_switching = []
    y_switching = []
    
    x_keys = matrix.get_x_keys()
    y_keys = matrix.get_y_keys()
    if model is 'dipm':
        mat = [
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING]
               ]
        matrix = Matrix()
        matrix.init_matrix(mat)
    if model is 'scpm':
        mat = [  # in x we store the y
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING]
               ]
        matrix = Matrix()
        matrix.init_matrix(mat)
    fig = plt.figure()
    for x in x_keys:
        for y in y_keys:
            value = matrix.get_item(x, y)
            if value is Abilities.NO_SELECTION:
                x_no_selection.append(x)
                y_no_selection.append(y)
            elif value is Abilities.SELECTION:
                x_selection.append(x)
                y_selection.append(y)
            elif value is Abilities.NO_SWITCHING:
                x_no_switching.append(x)
                y_no_switching.append(y)
            elif value is Abilities.SWITCHING:
                x_switching.append(x)
                y_switching.append(y)


    plt.scatter(x_no_selection, y_no_selection, marker='*')
    plt.scatter(x_selection, y_selection, marker='o')
    plt.scatter(x_no_switching, y_no_switching, marker='s')
    plt.scatter(x_switching, y_switching, marker='p')

    if export_name is '':
        plt.show()
    else:
        plt.show()
        plt.savefig(export_name)

    plt.close(fig)



def save_simple_abilities_matrix(matrix: Matrix, title: str, export_name: str, coordinates: [[], []]):
    x_no_selection = []
    x_selection = []
    x_no_switching = []
    x_switching = []
    y_no_selection = []
    y_selection = []
    y_no_switching = []
    y_switching = []

    x_len = matrix.get_x_len()
    y_len = matrix.get_y_len()

    no_labels = True if coordinates == [] else False
    
    fig = plt.figure()
    for x in range(x_len):
        for y in range(y_len):
            value = matrix.get_item(x, y)
            if value is Abilities.NO_SELECTION:
                if no_labels:
                    x_no_selection.append(x)
                    y_no_selection.append(y)
                else:
                    x_no_selection.append(coordinates[0][x])
                    y_no_selection.append(coordinates[1][y])
            elif value is Abilities.SELECTION:
                if no_labels:
                    x_selection.append(x)
                    y_selection.append(y)
                else:
                    x_selection.append(coordinates[0][x])
                    y_selection.append(coordinates[1][y])
            elif value is Abilities.NO_SWITCHING:
                if no_labels:
                    x_no_switching.append(x)
                    y_no_switching.append(y)
                else:
                    x_no_switching.append(coordinates[0][x])
                    y_no_switching.append(coordinates[1][y])
            elif value is Abilities.SWITCHING:
                if no_labels:
                    x_switching.append(x)
                    y_switching.append(y)
                else:
                    x_switching.append(coordinates[0][x])
                    y_switching.append(coordinates[1][y])

    plt.scatter(x_no_selection, y_no_selection, marker='*')
    plt.scatter(x_selection, y_selection, marker='o')
    plt.scatter(x_no_switching, y_no_switching, marker='s')
    plt.scatter(x_switching, y_switching, marker='p')
    no_sel = mpatches.Patch(color='#FF5733', label='selection')
    with_sel = mpatches.Patch(color='#3393FF', label='no_selection')
    No_swit = mpatches.Patch(color='#FF3333', label='switching')
    with_swit = mpatches.Patch(color='#32F260', label='no_switching')
    
    plt.legend(handles=[no_sel,with_sel,No_swit,with_swit],loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, ncol=5)

    if title != '':
        plt.title(title)

    if export_name is '':
        plt.show()
    else:
        plt.savefig(export_name)
        plt.show()

    plt.close(fig)

def display_save_figure(model:str, matrix: Matrix, title: str, export_name: str, coordinates: [[], []]):
    x_no_selection = []
    x_selection = []
    x_no_switching = []
    x_switching = []
    y_no_selection = []
    y_selection = []
    y_no_switching = []
    y_switching = []
    
    
    
    no_labels = True if coordinates == [] else False
    if model is 'dipm':
        mat = [
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING]
               ]
        matrix = Matrix()
        matrix.init_matrix(mat)
    if model is 'scpm':
        mat = [  # in x we store the y
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
               [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING]
               ]
        matrix = Matrix()
        matrix.init_matrix(mat)
    x_len = matrix.get_x_len()
    y_len = matrix.get_y_len()
    fig = plt.figure()
    for x in range(x_len):
        for y in range(y_len):
            value = matrix.get_item(x, y)
            if value is Abilities.NO_SELECTION:
                if no_labels:
                    x_no_selection.append(x)
                    y_no_selection.append(y)
                else:
                    x_no_selection.append(coordinates[0][x])
                    y_no_selection.append(coordinates[1][y])
            elif value is Abilities.SELECTION:
                if no_labels:
                    x_selection.append(x)
                    y_selection.append(y)
                else:
                    x_selection.append(coordinates[0][x])
                    y_selection.append(coordinates[1][y])
            elif value is Abilities.NO_SWITCHING:
                if no_labels:
                    x_no_switching.append(x)
                    y_no_switching.append(y)
                else:
                    x_no_switching.append(coordinates[0][x])
                    y_no_switching.append(coordinates[1][y])
            elif value is Abilities.SWITCHING:
                if no_labels:
                    x_switching.append(x)
                    y_switching.append(y)
                else:
                    x_switching.append(coordinates[0][x])
                    y_switching.append(coordinates[1][y])

    plt.scatter(x_no_selection, y_no_selection, marker='*')
    plt.scatter(x_selection, y_selection, marker='o')
    plt.scatter(x_no_switching, y_no_switching, marker='s')
    plt.scatter(x_switching, y_switching, marker='p')
    no_sel = mpatches.Patch(color='#FF5733', label='selection')
    with_sel = mpatches.Patch(color='#3393FF', label='no_selection')
    No_swit = mpatches.Patch(color='#FF3333', label='switching')
    with_swit = mpatches.Patch(color='#32F260', label='no_switching')

    plt.legend(handles=[no_sel,with_sel,No_swit,with_swit],loc='upper center', bbox_to_anchor=(0.5, -0.05),fancybox=True, ncol=5)

    if title != '':
        plt.title(title)
    
    if export_name is '':
        plt.show()
    else:
        plt.savefig(export_name)
        plt.show()
    
    plt.close(fig)
