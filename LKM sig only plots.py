#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:36:22 2021

@author: lauramilton
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np




import_file = r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 w cyto pvalue matrix cleaned2.xlsx'
import_file2 = r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 w cyto correlation matrix cleaned.xlsx'
fig_export = r'/Users/lauramilton/Desktop/RO 2021/Beh C1+2 '

sig = '#d9ef8b'
trend = '#66bd63'
ns = '#F1F1F1'
palette_sig = [sig, trend, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns, ns]
palette_sig2 = [sig, trend]

#####-----#####

val_min = 0
val_max = 0.1

group = 'All cyto 6'

sheet1 = group + ' pvalues'
sheet2 = group

data = pd.read_excel(import_file, sheet_name=sheet1, header=0)
data = data.astype(float)

variable = data.columns.tolist()

cols_to_keep = []
for i in range(0, len(variable)):
    if variable[i].startswith('RANTES'):
        cols_to_keep.append(variable[i])
    elif variable[i].startswith('IL-'):
        cols_to_keep.append(variable[i])

# cols_to_keep.remove('ABA mean daily FI')
print(cols_to_keep)

data = pd.read_excel(import_file, sheet_name=sheet1, usecols=cols_to_keep, header=0)

fig, ax = plt.subplots(figsize=(10, 8))
plt.title(group + ' sig pvalues')

# matrix = np.triu(data, k=1)
cut_off = 0.1
mask = np.zeros_like(data, dtype=np.bool)
# mask[np.triu_indices_from(mask)] = True
mask |= np.abs(data) > cut_off
data = data[~mask]  # fill in NaN in the non-desired cells

remove_empty_rows_and_cols = True
if remove_empty_rows_and_cols:
    wanted_cols = np.flatnonzero(np.count_nonzero(~mask, axis=1))
    wanted_rows = np.flatnonzero(np.count_nonzero(~mask, axis=0))
    data = data.iloc[wanted_cols, wanted_rows]

labels_y = [item for i, item in enumerate(variable) if i in wanted_cols]


g = sns.heatmap(data=data, vmin=0, vmax=0.1, center=0.05, linewidths=1, linecolor='#d9d9d9', cmap=sns.color_palette(palette_sig2, 2), cbar=True, square=False, yticklabels=labels_y, xticklabels=True, annot=True, fmt='.4g', annot_kws={"fontsize":8})
g.set_xticklabels(g.get_xticklabels(), rotation=45, horizontalalignment='right')

plt.savefig(fig_export + group + ' sig pvalues', bbox_inches='tight')
plt.show()



data2 = pd.read_excel(import_file2, sheet_name=sheet2, usecols=cols_to_keep, header=0)

data = pd.read_excel(import_file, sheet_name=sheet1, usecols=cols_to_keep, header=0)
data = data.astype(float)

mask = np.zeros_like(data, dtype=np.bool)
# mask[np.triu_indices_from(mask)] = True
mask |= np.abs(data) > cut_off
data2 = data2[~mask]  # fill in NaN in the non-desired cells

data2 = data2.iloc[wanted_cols, wanted_rows]


fig, ax = plt.subplots(figsize=(10, 8))
plt.title(group + ' sig correlations')

g2 = sns.heatmap(data=data2, vmin=-1, vmax=1, center=0, linewidths=1, linecolor='#d9d9d9', cmap='coolwarm', cbar=True, square=False, yticklabels=labels_y, xticklabels=True, annot=True, fmt='.4g', annot_kws={"fontsize":8})
g2.set_xticklabels(g2.get_xticklabels(), rotation=45, horizontalalignment='right')

plt.savefig(fig_export + group + ' sig correlations', bbox_inches='tight')
plt.show()
