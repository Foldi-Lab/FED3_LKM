#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:07:07 2021

@author: lauramilton
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

import_file = r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 w cyto pvalue matrix cleaned.xlsx'
fig_export = r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 pvalues '

sig = '#d9ef8b'
trend = '#66bd63'
ns = '#F1F1F1'
palette_sig = [sig, trend, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns]

#####-----#####


import xlrd
xls = xlrd.open_workbook(import_file, on_demand=True)
sheetnames = xls.sheet_names()

for sheet in sheetnames:
    if 'All' in sheet:
        continue
    else:
        
        column_labels = pd.read_excel(import_file, sheet_name=sheet) # get the column labels
        
        variable = column_labels.columns.tolist()
        
        fig, ax = plt.subplots(figsize=(15,10))
        plt.title(sheet)
        
        data = pd.read_excel(import_file, sheet_name=sheet)
        
        # matrix = np.triu(data, k=1)
        
        mask = np.zeros_like(data, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
    
        # Want diagonal elements as well
        # mask[np.diag_indices_from(mask)] = False
        
        g = sns.heatmap(data=data, mask=mask, vmin=0, vmax=1, center=0.5, linewidths=1, cmap=sns.color_palette(palette_sig, 20), cbar=True, square=False, yticklabels=variable, xticklabels=True, annot=True, fmt='.3f', annot_kws={"fontsize":6})
        g.set_xticklabels(g.get_xticklabels(), rotation=45, horizontalalignment='right')
        
        plt.savefig(fig_export + sheet, bbox_inches='tight')
        plt.show()
        
#####-----#####

# f,(ax1,ax2, axcb) = plt.subplots(1,3, 
#             gridspec_kw={'width_ratios':[1,1,0.1]},
#             figsize=(8, 8))



# # first subplot

# corr_data = pd.read_excel(p_export_file, sheet_name='ABA_S pvalues')
        
# col_to_drop = []

# for i in range(0, len(variable)):
#     if variable[i].startswith('ABA'):
#         continue

#     else:
#         col_to_drop.append(variable[i])

# corr_data.drop(columns=col_to_drop, inplace=True)
# corr_data.drop(index=[19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], inplace=True)

# del variable[19:]

# g = sns.heatmap(data=corr_data, vmin=0, vmax=1, center=0.5, linewidths=1, cmap=sns.color_palette(palette_sig, 20), ax=ax1, cbar=False, square=False, yticklabels=variable, xticklabels=True, annot=True, fmt='.4f', annot_kws={"fontsize":8})
# # g = sns.heatmap(data=corr_data, vmin=-1, vmax=1, center=0, linewidths=1, cmap='coolwarm', cbar=False, square=False, ax=ax1, yticklabels=variable, xticklabels=True, annot=True, fmt='.2f', annot_kws={"fontsize":8})
# g.set_xticklabels(g.get_xticklabels(), rotation=45, horizontalalignment='right')