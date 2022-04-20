#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:25:25 2021

@author: lauramilton
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

from scipy.stats import pearsonr

def calculate_pvalues(df):
    df = df.dropna()._get_numeric_data()
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            pvalues[r][c] = round(pearsonr(df[r], df[c])[1], 4)
    return pvalues



import_file = r'/Users/lauramilton/Desktop/RO 2021/Behavioural C1+2 correlations.xlsx'
export_file = r'/Users/lauramilton/Desktop/RO 2021/Behavioural C1+2 correlations pvalues.xlsx'

column_labels = pd.read_excel(import_file, sheet_name='All data')

variable = column_labels.columns.tolist()

del variable[:2]


# import xlrd
# xls = xlrd.open_workbook(import_file, on_demand=True)
# sheetnames = xls.sheet_names()

# from openpyxl import load_workbook

# book = load_workbook(export_file)
# writer = pd.ExcelWriter(export_file, engine = 'openpyxl')
# writer.book = book

# for sheet in sheetnames:
#     if 'ABA_' in sheet:

#         data = pd.read_excel(import_file, sheet_name=sheet)
        
#         pvalues = calculate_pvalues(data)
        
#         sheetname_new = sheet.strip('corr') + 'pvalues'
        
#         pvalues.to_excel(writer, sheet_name=sheetname_new, engine='openpyxl', index=False, header=True)
        
#         writer.save()

# writer.close()

sig = '#000000'
ns1 = '#9e0142'
ns2 = '#d53e4f'
ns3 = '#f46d43'
ns4 = '#fdae61'
ns5 = '#fee08b'
ns6 = '#e6f598'
ns7 = '#abdda4'
ns8 = '#66c2a5'
ns9 = '#3288bd'
ns10 = '#5e4fa2'

palette_rainbow = [sig, ns1, ns2, ns2, ns3, ns3, ns4, ns4, ns5, ns5, ns6, ns6, ns7, ns7, ns8, ns8, ns9, ns9, ns10, ns10]
sns.set_palette(palette_rainbow)


sig = '#d9ef8b'
trend = '#66bd63'
ns = '#F1F1F1'
palette_sig = [sig, trend, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns]

import xlrd
xls = xlrd.open_workbook(export_file, on_demand=True)
sheetnames = xls.sheet_names()

f,(ax1,ax2, axcb) = plt.subplots(1,3, 
            gridspec_kw={'width_ratios':[1,1,0.1]},
            figsize=(8, 8))

p_data = pd.read_excel(export_file, sheet_name='ABA_S pvalues')

col_to_drop = []

for i in range(0, len(variable)):
    if variable[i].startswith('ABA'):
        continue

    else:
        col_to_drop.append(variable[i])

p_data.drop(columns=col_to_drop, inplace=True)
p_data.drop(index=[19, 20, 21, 22, 23], inplace=True)

del variable[19:]

sns.heatmap(data=p_data, vmin=0, vmax=1, center=0.5, linewidths=1, cmap=sns.color_palette(palette_sig, 20), cbar=False, ax=ax1, square=False, yticklabels=variable, xticklabels=True, annot=True, fmt='.4f', annot_kws={"fontsize":8})

p_data = pd.read_excel(export_file, sheet_name='ABA_R pvalues')

col_to_drop = []

for i in range(0, len(variable)):
    if variable[i].startswith('ABA'):
        continue

    else:
        col_to_drop.append(variable[i])

p_data.drop(columns=col_to_drop, inplace=True)
p_data.drop(index=[19, 20, 21, 22, 23], inplace=True)

del variable[19:]

sns.heatmap(data=p_data, vmin=0, vmax=1, center=0.5, linewidths=1, cmap=sns.color_palette(palette_sig, 20), cbar=True, ax=ax2, cbar_ax=axcb, square=False, yticklabels=False, xticklabels=True, annot=True, fmt='.4f', annot_kws={"fontsize":8})

plt.show()

plt.show()
        
        



# for sheet in sheetnames:
        
#     p_data = pd.read_excel(export_file, sheet_name=sheet)
    
#     col_to_drop = []

#     for i in range(0, len(variable)):
#         if variable[i].startswith('ABA'):
#             continue
    
#         else:
#             col_to_drop.append(variable[i])
    
#     p_data.drop(columns=col_to_drop, inplace=True)
#     p_data.drop(index=[19, 20, 21, 22, 23], inplace=True)
    
#     del variable[19:]
    
#     sns.heatmap(data=p_data, vmin=0, vmax=1, center=0.5, linewidths=1, cmap='icefire', cbar=True, square=False, yticklabels=variable, xticklabels=True, annot=True, fmt='.2f', annot_kws={"fontsize":8})
    
#     plt.show()
        
        

