#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 14:30:08 2021

@author: lauramilton
"""

#-----------------------------------------------------------------------------

# GUI TUTORIAL

# Type 'pip install PySimpleGUI' into the console.
# If you have done this once, you do not need to do it again.
# Copy, paste and edit each block of code to add a new line to the GUI.

# For each block you should put in the type of input in inp[key_word] = ...
# It should light up in a different colour.
# If it is text, type str
# If it is a number, type float
# If it is a True or False, type bool
# Make sure the key_word variables are unique for each block as well.

#-----------------------------------------------------------------------------

# Import the PySimpleGUI package and choose a theme.
# To view more themes, type sg.theme_previewer() into the console.
# Change the height and width of the window in size_GUI, so it will include the submit button.

import PySimpleGUI as sg
sg.theme("DarkPurple5")
size_GUI = (650,500)
name_window = "GUI"
layout = []
inp = {}

# sg.theme_previewer() # uncomment to preview themes and select a new one to insert above if desired

# (Block 1) Create a buton to choose an import folder.
# Note that there should be no slash at the end of the default import path.

line          = []
display_text  = "Choose the import location PARENT folder"
default_value = "/Volumes/shared/MNHS-SOBS-Physiology/Foldi-Group/FED3 Reversal/FED210721/DatafilesPython/TEST"
key_word      = "Import"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
line += [sg.FolderBrowse()]
layout += [[sg.T("")]]
layout += [line]

# (Block 2) Create a button to choose an export folder.
# Note that there should be no slash at the end of the default export path.

line          = []
display_text  = "Choose the export location PARENT folder"
default_value = "/Volumes/shared/MNHS-SOBS-Physiology/Foldi-Group/FED3 Reversal/FED210721/DatafilesPython/TEST"
key_word      = "Export"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
line += [sg.FolderBrowse()]
layout += [[sg.T("")]]
layout += [line]

# (Block 3) Create a button to choose a cohort overview export folder.
# Note that there should be no slash at the end of the default export path.

line          = []
display_text  = "Choose the cohort joined export location folder"
default_value = "/Volumes/shared/MNHS-SOBS-Physiology/Foldi-Group/FED3 Reversal/FED210721/DatafilesPython/TESTOverview"
key_word      = "Cohort_export"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
line += [sg.FolderBrowse()]
layout += [[sg.T("")]]
layout += [line]


# (Block 4) Create a dropdown menu.

line          = []
display_text  = "Which schedule was used?"
dropdown_list = ['FR1/3/5 or FR1/3/5_reversed', 'FR1_both', 'New_Reversal']
default_value = ''
key_word      = "Schedule"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Combo(dropdown_list,default_value=default_value,key=key_word,enable_events=True)]
layout += [[sg.T("")]]
layout += [line]

# (Block 5) Create a number entry.

line          = []
display_text  = "What was the session duration (in minutes)"
default_value = 0
key_word      = "Session_length"
inp[key_word] = float

line += [sg.Text(display_text)]
line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
layout += [[sg.T("")]]
layout += [line]

# (Block 7) Create a checkbox.

line          = []
display_text  = "Were time bins used?"
default_value = False
key_word      = "Time_bins"
inp[key_word] = bool

line += [sg.Text(display_text)]
line += [sg.Checkbox('',default=default_value,key=key_word,enable_events=True)]
layout += [[sg.T("")]]
layout += [line]

# (Block 5) Create a number entry.

line          = []
display_text  = "If yes, what length (in minutes) were the first time bins? If no, leave blank"
default_value = ''
key_word      = "Bin_length1"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
layout += [[sg.T("")]]
layout += [line]

# (Block 5) Create a number entry.

line          = []
display_text  = "OPTIONAL, what length (in minutes) were the second time bins? If not used leave blank"
default_value = ''
key_word      = "Bin_length2"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
layout += [[sg.T("")]]
layout += [line]

# (Block 5) Create a number entry.

line          = []
display_text  = "Enter the dates of the sessions you want to join seperated by commas"
default_value = ''
key_word      = "Dates_to_join"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
layout += [[sg.T("")]]
layout += [line]

# (Block 5) Create a number entry.

# line          = []
# display_text  = "Length of reversal blocks (if schedule is New_Reversal)"
# default_value = 0
# key_word      = "Block_length"
# inp[key_word] = float

# line += [sg.Text(display_text)]
# line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
# layout += [[sg.T("")]]
# layout += [line]

# Create the GUI.

layout += [[sg.T("")],[sg.Button("Submit")]]
window = sg.Window(name_window, layout, size=size_GUI)
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        window.close()
        exit()
    elif event == "Submit":
        window.close()
        break
        
inputs = {}
for key in list(inp.keys()):
    inputs[key] = inp[key](values[key])
                           
# Assign each of the inputs to variable names.
# Replace the key_word variables in the square brackets.
# Note that the slash is added back to the end of the import and export locations.

import_location = inputs["Import"] + '/'
export_location = inputs["Export"] + '/'
cohort_export_location = inputs["Cohort_export"] + '/'
schedule = inputs["Schedule"]
session_length = inputs['Session_length']
# reversal_block_length = inputs["Block_length"]
binned = inputs["Time_bins"]
time_bin_length1 = inputs["Bin_length1"] 
time_bin_length2 = inputs["Bin_length2"] 
# FED_num = 'FED' + FED_number
dates_to_join = inputs["Dates_to_join"]

dates_to_join_list = dates_to_join.split(',')

print(dates_to_join_list[0])
# Verify the inputs by printing them in the console.

print('Import location is', import_location)
print('Export location is', export_location)
print('Cohort export location is', cohort_export_location)
print('Schedule is', schedule)
print('Session length is', str(session_length) + ' minutes')
# print('Reversal block length is', reversal_block_length)
print('Time bins are being used?', binned)
print('Length of time bins are', str(time_bin_length1) + ' minutes and', str(time_bin_length2) + ' minutes')
print('Dates to join are:', dates_to_join)
# Paste the rest of the code here

##########----------########## FR1/3/5 and reversed

if schedule == 'FR1/3/5 or FR1/3/5_reversed':
    
