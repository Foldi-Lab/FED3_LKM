#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 12:20:42 2021

@author: lauramilton
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

import_file = r'/Users/lauramilton/Desktop/RO 2021/Behavioural C1+2 correlations.xlsx'
export_file = r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 w cyto correlation matrix.xlsx'

# ### Generate correlation matrix file

# # first create a new excel document with a copy of the raw data

# import xlrd
# xls = xlrd.open_workbook(import_file, on_demand=True)
# sheetnames = xls.sheet_names()

# data = pd.read_excel(import_file, sheet_name='All data')

# with pd.ExcelWriter(export_file, engine='xlsxwriter') as writer:
#     data.to_excel(writer, sheet_name='All data', index=False, header=True)

# # open the document you just created so you can save new sheets into it

# from openpyxl import load_workbook

# book = load_workbook(export_file)
# writer = pd.ExcelWriter(export_file, engine = 'openpyxl')
# writer.book = book

# # create a correlation matrix of all data for each of the groups (each group has it's own sheet in the original file)

# for sheet in sheetnames:
#     if 'corr' in sheet:

#         data = pd.read_excel(import_file, sheet_name=sheet)
        
#         corrMatrix = data.corr()
                
#         corrMatrix.to_excel(writer, sheet_name=sheet, engine='openpyxl', index=False, header=True)
        
#         writer.save()

# writer.close()

# #####-----#####

# column_labels = pd.read_excel(export_file, sheet_name='All data') # get the column labels

# variable = column_labels.columns.tolist()

# del variable[:2] # remove RAT# and EXP ID column labels as they're not in the correlation data sheets

# # xls = xlrd.open_workbook(export_file, on_demand=True)
# # sheetnames = xls.sheet_names()

# ###--- Generate figures ---###

# # Big figure into which each subplot will be placed

# f,(ax1,ax2, axcb) = plt.subplots(1,3, 
#             gridspec_kw={'width_ratios':[1,1,0.1]},
#             figsize=(8, 8))

# # first subplot

# corr_data = pd.read_excel(export_file, sheet_name='ABA_S corr')
        
# col_to_drop = []

# for i in range(0, len(variable)):
#     if variable[i].startswith('ABA'):
#         continue

#     else:
#         col_to_drop.append(variable[i])

# corr_data.drop(columns=col_to_drop, inplace=True)
# corr_data.drop(index=[19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], inplace=True)

# del variable[19:]

# sns.heatmap(data=corr_data, vmin=-1, vmax=1, center=0, linewidths=1, cmap='coolwarm', cbar=False, square=False, ax=ax1, yticklabels=variable, xticklabels=True, annot=True, fmt='.2f', annot_kws={"fontsize":8})

# # second subplot

# variable = column_labels.columns.tolist()

# del variable[:2] # remove RAT# and EXP ID column labels as they're not in the correlation data sheets

# corr_data = pd.read_excel(export_file, sheet_name='ABA_R corr')
        
# col_to_drop = []

# for i in range(0, len(variable)):
#     if variable[i].startswith('ABA'):
#         continue

#     else:
#         col_to_drop.append(variable[i])

# corr_data.drop(columns=col_to_drop, inplace=True)
# corr_data.drop(index=[19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], inplace=True)

# del variable[19:]

# sns.heatmap(data=corr_data, vmin=-1, vmax=1, center=0, linewidths=1, cmap='coolwarm', cbar=True, cbar_ax=axcb, square=False, ax=ax2, yticklabels=False, xticklabels=True, annot=True, fmt='.2f', annot_kws={"fontsize":8})

# plt.savefig(r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 ABA S + R.png', bbox_inches = 'tight')
# plt.show()

#####----- difference heatmap

# fig, ax = plt.subplots(figsize=(5, 8))

# corr_data = pd.read_excel(export_file, sheet_name='ABA diff')
        
# col_to_drop = []

# for i in range(0, len(variable)):
#     if variable[i].startswith('ABA'):
#         continue

#     else:
#         col_to_drop.append(variable[i])

# corr_data.drop(columns=col_to_drop, inplace=True)
# corr_data.drop(index=[19, 20, 21, 22, 23], inplace=True)

# del variable[19:]

# palette = ['#543005','#8c510a','#bf812d','#dfc27d','#f6e8c3','#c7eae5','#80cdc1','#35978f','#01665e','#003c30']

# sns.heatmap(data=corr_data, vmin=-2, vmax=2, center=0, linewidths=1, cmap=sns.color_palette(palette, 10), cbar=True, square=False, yticklabels=variable, xticklabels=True, annot=True, fmt='.2f', annot_kws={"fontsize":8})

# plt.savefig(r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 ABA difference.png', bbox_inches = 'tight')
# plt.show()

#####-----

# cytokine correlation PRE measures with behavioural test data for ALL rats

f,(ax1, ax2, ax3, ax4) = plt.subplots(1, 4, 
            gridspec_kw={'width_ratios':[1, 0.1, 1, 0.1]},
            figsize=(8, 8))

column_labels = pd.read_excel(export_file, sheet_name='All data') # get the column labels

variable = column_labels.columns.tolist()

del variable[:2] # remove RAT# and EXP ID column labels as they're not in the correlation data sheets

corr_data = pd.read_excel(export_file, sheet_name='All corr')
        
col_to_drop = []

for i in range(0, len(variable)):
    if variable[i].startswith('RANTES'):
        continue
    elif variable[i].startswith('IL'):
        continue

    else:
        col_to_drop.append(variable[i])

for i in range(0, len(variable)):
    if 'pre' in variable[i]:
        continue
    else:
        col_to_drop.append(variable[i])
        
del variable[19:]

corr_data.drop(columns=col_to_drop, inplace=True)
corr_data.drop(index=[19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], inplace=True)

sns.heatmap(data=corr_data, vmin=-1, vmax=1, center=0, linewidths=1, cmap='coolwarm', ax=ax1, cbar=True, cbar_ax=ax2, square=False, yticklabels=variable, xticklabels=True, annot=True, fmt='.2f', annot_kws={"fontsize":8})

plt.show()






















#####-----##### using for loop

# for sheet in sheetnames:
    
#     if 'ABA' in sheet:
        
#         corr_data = pd.read_excel(export_file, sheet_name=sheet)
        
#         col_to_drop = []
        
#         for i in range(0, len(variable)):
#             if variable[i].startswith('ABA'):
#                 continue

#             else:
#                 col_to_drop.append(variable[i])
        
#         corr_data.drop(columns=col_to_drop, inplace=True)
#         corr_data.drop(index=[19, 20, 21, 22, 23], inplace=True)
        
#         del variable[19:]
        
#         # print(corr_data)
#         plt.subplot(1, groups, c)
#         plt.title(sheet)
        
#         x_tick_labels = []
        
#         for i in range(0, len(x_labels)):
#             x_tick_labels.append(x_labels[i] + ' ' + sheet.strip('corr'))
        
#         if c == 1:
#             sns.heatmap(data=corr_data, vmin=-1, vmax=1, center=0, linewidths=1, cmap='coolwarm', cbar=False, square=False, yticklabels=variable, xticklabels=x_tick_labels, annot=True, fmt='.2f', annot_kws={"fontsize":8})
        
#         elif c < groups:
#             sns.heatmap(data=corr_data, vmin=-1, vmax=1, center=0, linewidths=1, cmap='coolwarm', cbar=False, square=False, yticklabels=False, xticklabels=x_tick_labels, annot=True, fmt='.2f', annot_kws={"fontsize":8})
        
#         elif c == groups:
#             sns.heatmap(data=corr_data, vmin=-1, vmax=1, center=0, linewidths=1, cmap='coolwarm', cbar=True, cbar_ax=axcb, square=False, yticklabels=False, xticklabels=x_tick_labels, annot=True, fmt='.2f', annot_kws={"fontsize":8})
        
#         c +=1
        
#         # plt.savefig(r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 ' + sheet + ' all vs ABA tall.png', bbox_inches = 'tight')
        
#         # plt. clf()
        
#         # corr_data_t = corr_data.transpose()
        
#         # print(corr_data_t)
        
#         # plt.figure()
#         # sns.heatmap(data=corr_data_t, vmin=-1, vmax=1, center=0, linewidths=1, cmap='coolwarm', cbar=True, square=True, xticklabels=variable)
        
#         # plt.savefig(r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 ' + sheet + ' all vs ABA wide.png', bbox_inches = 'tight')
        
#         # plt. clf()

# plt.show()

