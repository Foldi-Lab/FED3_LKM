#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:01:57 2021

@author: lauramilton
"""

import pandas as pd
# from matplotlib import pyplot as plt
# from pylab import rcParams
# rcParams['figure.figsize'] = 7,7 
# import seaborn as sns
# import numpy as np
# sns.set(color_codes=True, font_scale=1.2)

# # from heatmap import heatmap, corrplot
# import openpyxl
# from openpyxl import Workbook

# #####-----

# def heatmap(x, y, **kwargs):
#     if 'color' in kwargs:
#         color = kwargs['color']
#     else:
#         color = [1]*len(x)

#     if 'palette' in kwargs:
#         palette = kwargs['palette']
#         # n_colors = len(palette)
#         n_colors = 256
#     else:
#         n_colors = 256 # Use 256 colors for the diverging color palette
#         palette = sns.color_palette("icefire", n_colors) 

#     if 'color_range' in kwargs:
#         color_min, color_max = kwargs['color_range']
#     else:
#         color_min, color_max = min(color), max(color) # Range of values that will be mapped to the palette, i.e. min and max possible correlation

#     def value_to_color(val):
#         if color_min == color_max:
#             return palette[-1]
#         else:
#             val_position = float((val - color_min)) / (color_max - color_min) # position of value in the input range, relative to the length of the input range
#             val_position = min(max(val_position, 0), 1) # bound the position betwen 0 and 1
#             ind = int(val_position * (n_colors - 1)) # target index in the color palette
#             return palette[ind]

#     if 'size' in kwargs:
#         size = kwargs['size']
#     else:
#         size = [1]*len(x)

#     if 'size_range' in kwargs:
#         size_min, size_max = kwargs['size_range'][0], kwargs['size_range'][1]
#     else:
#         size_min, size_max = min(size), max(size)

#     size_scale = kwargs.get('size_scale', 500)

#     def value_to_size(val):
#         if size_min == size_max:
#             return 1 * size_scale
#         else:
#             val_position = (val - size_min) * 0.99 / (size_max - size_min) + 0.01 # position of value in the input range, relative to the length of the input range
#             val_position = min(max(val_position, 0), 1) # bound the position betwen 0 and 1
#             return val_position * size_scale
#     if 'x_order' in kwargs: 
#         x_names = [t for t in kwargs['x_order']]
#     else:
#         x_names = [t for t in sorted(set([v for v in x]))]
#     x_to_num = {p[1]:p[0] for p in enumerate(x_names)}

#     if 'y_order' in kwargs: 
#         y_names = [t for t in kwargs['y_order']]
#     else:
#         y_names = [t for t in sorted(set([v for v in y]))]
#     y_to_num = {p[1]:p[0] for p in enumerate(y_names)}

#     plot_grid = plt.GridSpec(1, 15, hspace=0.2, wspace=0.1) # Setup a 1x10 grid
#     ax = plt.subplot(plot_grid[:,:-1]) # Use the left 14/15ths of the grid for the main plot

#     marker = kwargs.get('marker', 's')

#     kwargs_pass_on = {k:v for k,v in kwargs.items() if k not in [
#          'color', 'palette', 'color_range', 'size', 'size_range', 'size_scale', 'marker', 'x_order', 'y_order', 'xlabel', 'ylabel'
#     ]}

#     ax.scatter(
#         x=[x_to_num[v] for v in x],
#         y=[y_to_num[v] for v in y],
#         marker=marker,
#         s=[value_to_size(v) for v in size], 
#         c=[value_to_color(v) for v in color],
#         **kwargs_pass_on
#     )
#     ax.set_xticks([v for k,v in x_to_num.items()])
#     ax.set_xticklabels([k for k in x_to_num], rotation=45, horizontalalignment='right')
#     ax.set_yticks([v for k,v in y_to_num.items()])
#     ax.set_yticklabels([k for k in y_to_num])

#     ax.grid(False, 'major')
#     ax.grid(True, 'minor')
#     ax.set_xticks([t + 0.5 for t in ax.get_xticks()], minor=True)
#     ax.set_yticks([t + 0.5 for t in ax.get_yticks()], minor=True)

#     ax.set_xlim([-0.5, max([v for v in x_to_num.values()]) + 0.5])
#     ax.set_ylim([-0.5, max([v for v in y_to_num.values()]) + 0.5])
#     ax.set_facecolor('#F1F1F1')

#     ax.set_xlabel(kwargs.get('xlabel', ''))
#     ax.set_ylabel(kwargs.get('ylabel', ''))

#     # Add color legend on the right side of the plot
#     if color_min < color_max:
#         ax = plt.subplot(plot_grid[:,-1]) # Use the rightmost column of the plot

#         col_x = [0]*len(palette) # Fixed x coordinate for the bars
#         bar_y=np.linspace(color_min, color_max, n_colors) # y coordinates for each of the n_colors bars

#         bar_height = bar_y[1] - bar_y[0]
#         ax.barh(
#             y=bar_y,
#             width=[5]*len(palette), # Make bars 5 units wide
#             left=col_x, # Make bars start at 0
#             height=bar_height,
#             color=palette,
#             linewidth=0
#         )
#         ax.set_xlim(1, 2) # Bars are going from 0 to 5, so lets crop the plot somewhere in the middle
#         ax.grid(False) # Hide grid
#         ax.set_facecolor('white') # Make background white
#         ax.set_xticks([]) # Remove horizontal ticks
#         ax.set_yticks(np.linspace(min(bar_y), max(bar_y), 3)) # Show vertical ticks for min, middle and max
#         ax.yaxis.tick_right() # Show vertical ticks on the right 


# def corrplot(data, size_scale=500, marker='s'):
#     corr = pd.melt(data.reset_index(), id_vars='index').replace(np.nan, 0)
#     corr.columns = ['x', 'y', 'value']
#     heatmap(
#         corr['x'], corr['y'],
#         color=corr['value'], color_range=[-1, 1],
#         # palette=sns.diverging_palette(260, 30, n=256),
#         palette=sns.color_palette(palette="Spectral", n_colors=256),
#         size=corr['value'].abs(), size_range=[0,1],
#         marker=marker,
#         x_order=data.columns,
#         y_order=data.columns[::-1],
#         size_scale=size_scale
#     )

# #####-----#####

import_file = r'/Users/lauramilton/Desktop/RO 2021/Behavioural C1+2 correlations.xlsx'

# # create a dictionary of variables from column headings

column_data = pd.read_excel(import_file, sheet_name='Graph all')

variable = column_data.columns.tolist()

# column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# dictionary = dict(zip(column, variable))

# print(dictionary)

# data = pd.read_excel(import_file)

import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
# data = pd.read_excel(import_file, sheet_name='Graph all')

# corrMatrix = data.corr()

# corrMatrix.to_excel(import_file.strip('.xlsx') + ' matrix.xlsx')

corr_data = pd.read_excel(import_file.strip('.xlsx') + ' matrix.xlsx', header=0)

row_keep = []
column_keep = []


for i in range(0, len(variable)):
    if variable[i].startswith('ABA'):
        column_keep.append(variable[i])
    elif variable[i].startswith('EPM'):
        row_keep.append(variable[i])

row_drop = []
column_drop = []

for i in range(0, len(variable)):
    if variable[i] not in row_keep:
        row_drop.append(variable[i])
    elif variable[i] not in column_keep:
        column_drop.append(variable[i])
        
print(row_drop)
print(column_drop)

corr_data.drop(labels=column_drop, axis=1)

print(corr_data)

epm_rears_column = 'EPM rears'
epm_ce_bout_column = 'EPM centre bouts'
epm_o_bout_column = 'EPM open bouts'
epm_cl_bout_column = 'EPM closed bouts'
epm_oo_bout_column = 'EPM outer open bouts'
epm_ce_t_column = 'EPM centre time'
epm_o_t_column = 'EPM open time'
epm_cl_t_column = 'EPM closed time'
epm_oo_t_column = 'EPM outer open time'
epm_hd_column = 'EPM headdips'
of_rear_column = 'OF rears'
of_c_bout_column = 'OF Centre bouts'
of_o_bout_column = 'OF Outside bouts'
of_c_t_column = 'OF Centre time'
of_o_t_column = 'OF Outside time'
of_dist_column = 'OF Total distance (m)'
mbt_start_column = 'MBT start'
mbt_marble_column = 'MBT marble'
mbt_dig_column = 'MBT digging'
aba_hab_rwa_column = 'ABA HAB mean daily RWA'
aba_aba_rwa_column = 'ABA ABA mean daily RWA'
aba_fi_column = 'ABA ABA mean 90 min FI'
aba_bw_low_column = 'ABA Lowest BW%'
aba_bw_change_column = 'ABA Mean daily BW% change'

epm_rears = corr_data[epm_rears_column].tolist()
epm_ce_bout = corr_data[epm_ce_bout_column].tolist()
epm_o_bout = corr_data[epm_o_bout_column].tolist()
epm_cl_bout = corr_data[epm_cl_bout_column].tolist()
epm_oo_bout = corr_data[epm_oo_bout_column].tolist()
epm_ce_t = corr_data[epm_ce_t_column].tolist()
epm_o_t = corr_data[epm_o_t_column].tolist()
epm_cl_t = corr_data[epm_cl_t_column].tolist()
epm_oo_t = corr_data[epm_oo_t_column].tolist()
epm_hd = corr_data[epm_hd_column].tolist()
of_rear = corr_data[of_rear_column].tolist()
of_c_bout = corr_data[of_c_bout_column].tolist()
of_o_bout = corr_data[of_o_bout_column].tolist()
of_c_t = corr_data[of_c_t_column].tolist()
of_o_t = corr_data[of_o_t_column].tolist()
of_dist = corr_data[of_dist_column].tolist()
mbt_start = corr_data[mbt_start_column].tolist()
mbt_marble = corr_data[mbt_marble_column].tolist()
mbt_dig = corr_data[mbt_dig_column].tolist()
aba_hab_rwa = corr_data[aba_hab_rwa_column].tolist()
aba_aba_rwa = corr_data[aba_aba_rwa_column].tolist()
aba_fi = corr_data[aba_fi_column].tolist()
aba_low_bw = corr_data[aba_bw_low_column].tolist()
aba_bw_change = corr_data[aba_bw_change_column].tolist()

# epm_rears2 = [float(x) for x in epm_rears]
# epm_ce_bout2 = [float(x) for x in epm_ce_bout]
# epm_o_bout2 = [float(x) for x in epm_o_bout]

# corr_data_epm = [epm_rears2[20:], epm_ce_bout2[20:], epm_o_bout2[20:]]
# ax = sns.heatmap(corr_data, linewidth=0.5)
# plt.show()


# x = []
# y = []

# # key_list = list(dictionary.keys())
# # val_list = list(dictionary.values())


# print(x, y)

# data_x = pd.read_excel(import_file, sheet_name='Graph all', usecols=x)
# data_y = pd.read_excel(import_file, sheet_name='Graph all', usecols=y)



# corr_x = []
# corr_y = []



# plt.figure(figsize=(11, 3))
# heatmap(
#     x=['horsepower-group'],
#     y=g['make'],
#     size=g['cnt'],
#     marker='h',
#     x_order=bin_labels
# )


# # get the sheetnames

# import xlrd
# xls = xlrd.open_workbook(import_file, on_demand=True)
# sheetnames = xls.sheet_names()

# # for each sheet (group/s) create the following graphs

# for sheet in sheetnames:

#     if 'Graph all' in sheet:
        
#         # Plot of JUST EPM data
        
#         epm_data = pd.read_excel(import_file, sheet_name=sheet)
        
#         cols = epm_data.columns.tolist()
        
#         epm_cols_to_graph = []
        
#         for i in cols:
#             if i.startswith('EPM'):
#                 epm_cols_to_graph.append(i)
#             elif i.startswith('ABA'):
#                 epm_cols_to_graph.append(i)
        
#         epm_graph_data = pd.read_excel(import_file, sheet_name=sheet, usecols=epm_cols_to_graph)
        
        
        
#         plt.figure(figsize=(6, 6))
#         corrplot(epm_graph_data.corr(), size_scale=300);
        
        
        

# data = pd.read_excel(import_file, sheet_name='ABA graph')

# plt.figure(figsize=(4, 4))
# corrplot(data.corr(), size_scale=300);

# data = pd.read_excel(import_file, sheet_name='Graph EPM ABA both')

# plt.figure(figsize=(8, 8))
# corrplot(data.corr(), size_scale=300);


# plt.savefig(r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 corr.png')