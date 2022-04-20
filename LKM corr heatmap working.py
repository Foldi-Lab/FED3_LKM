#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:02:28 2021

@author: lauramilton
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

import_file = r'/Users/lauramilton/Desktop/RO 2021/Behavioural C1+2 correlations.xlsx'
export_file = r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 correlation matrix short.xlsx'


def heatmap(x, y, size, color):
    fig, ax = plt.subplots()

    # Mapping from column names to integer coordinates
    x_labels = [v for v in sorted(x.unique())]
    y_labels = [v for v in sorted(y.unique())]
    x_to_num = {p[1]:p[0] for p in enumerate(x_labels)} 
    y_to_num = {p[1]:p[0] for p in enumerate(y_labels)} 
    
    size_scale = 250
    # ax.scatter(
    #     x=x.map(x_to_num), # Use mapping for x
    #     y=y.map(y_to_num), # Use mapping for y
    #     s=size * size_scale, # Vector of square sizes, proportional to size parameter
    #     marker='s' # Use square as scatterplot marker
    # )
    
    x_labels2 = ['EPM rears', 'EPM centre bouts', 'EPM open bouts', 'EPM closed bouts', 'EPM outer open bouts', 'EPM centre time', 'EPM open time', 'EPM closed time', 'EPM outer open time', 'EPM headdips', 'OF rears', 'OF Centre bouts', 'OF Outside bouts', 'OF Centre time', 'OF Outside time', 'OF Total distance (m)', 'MBT start', 'MBT marble', 'MBT digging']
    
    plot_grid = plt.GridSpec(15, 1, hspace=0.2, wspace=0.1) # Setup a 1x10 grid
    ax = plt.subplot(plot_grid[1:10, :]) # Use the left 14/15ths of the grid for the main plot
    
    # Show column labels on the axes
    ax.set_xticks([x_to_num[v] for v in x_labels])
    ax.set_xticklabels(x_labels2, rotation=90, horizontalalignment='center')
    ax.set_yticks([y_to_num[v] for v in y_labels])
    ax.set_yticklabels(y_labels)
    
    ax.grid(False, 'major')
    ax.grid(True, 'minor', color='white')
    ax.set_xticks([t + 0.5 for t in ax.get_xticks()], minor=True)
    ax.set_yticks([t + 0.5 for t in ax.get_yticks()], minor=True)
    ax.tick_params(axis=u'both', which=u'both',length=0)
    
    ax.set_xlim([-0.5, max([v for v in x_to_num.values()]) + 0.5]) 
    ax.set_ylim([-0.5, max([v for v in y_to_num.values()]) + 0.5])
    ax.set_facecolor('#F1F1F1')
    # ax.set_facecolor('#000000')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    n_colors = 256 # Use 256 colors for the diverging color palette
    palette = sns.color_palette("coolwarm", n_colors) 
    # palette = sns.diverging_palette(20, 220, n=n_colors) # Create the palette
    color_min, color_max = [-1, 1] # Range of values that will be mapped to the palette, i.e. min and max possible correlation
    # color_min, color_max = min(color), max(color) # Range of values that will be mapped to the palette, i.e. min and max possible correlation

    def value_to_color(val):
        val_position = float((val - color_min)) / (color_max - color_min) # position of value in the input range, relative to the length of the input range
        val_position = min(max(val_position, 0), 1) # bound the position betwen 0 and 1
        ind = int(val_position * (n_colors - 1)) # target index in the color palette
        return palette[ind]
    
    ax.scatter(
        x=x.map(x_to_num),
        y=y.map(y_to_num),
        s=size * size_scale,
        c=[value_to_color(v) for v in color], # Vector of square color values, mapped to color palette
        marker='s'
    )
    
    plt.gca().set_aspect("equal")
    
    # Add color legend on the right side of the plot
    if color_min < color_max:
        ax = plt.subplot(plot_grid[0,:]) # Use the rightmost column of the plot

        col_y = [0]*len(palette) # Fixed x coordinate for the bars
        bar_x=np.linspace(color_min, color_max, n_colors) # y coordinates for each of the n_colors bars

        bar_height = bar_x[1] - bar_x[0]
        ax.bar(
            x=bar_x,
            height=[5]*len(palette), # Make bars 5 units wide
            bottom=col_y, # Make bars start at 0
            width=bar_height,
            color=palette,
            linewidth=0
        )
        
        ax.set_ylim(1, 2) # Bars are going from 0 to 5, so lets crop the plot somewhere in the middle
        ax.grid(False) # Hide grid
        ax.set_facecolor('white') # Make background white
        ax.set_yticks([]) # Remove horizontal ticks
        ax.set_xticks(np.linspace(min(bar_x), max(bar_x), 9)) # Show vertical ticks for min, middle and max
        ax.xaxis.tick_top() # Show vertical ticks on the right
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        
#####-----#####        
    
import xlrd
xls = xlrd.open_workbook(export_file, on_demand=True)
sheetnames = xls.sheet_names()

for sheet in sheetnames:
    if 'ABA' in sheet:

        data = pd.read_excel(export_file, sheet_name=sheet)
        columns = ['ABA HAB mean daily RWA', 'ABA ABA mean daily RWA', 'ABA ABA mean 90 min FI', 'ABA Lowest BW%', 'ABA Mean daily BW% change']
        
        corr = data[columns]
        data_to_graph = pd.melt(corr.reset_index(), id_vars='index') # Unpivot the dataframe, so we can get pair of arrays for x and y
        data_to_graph.columns = ['x', 'y', 'value']
        heatmap(
            x=data_to_graph['x'],
            y=data_to_graph['y'],
            color=data_to_graph['value'],
            size=data_to_graph['value'].abs()
        )

