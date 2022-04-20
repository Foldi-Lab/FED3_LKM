#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 15:15:20 2021

@author: lauramilton
"""

import PySimpleGUI as sg
sg.theme("DarkPurple5")
size_GUI = (750,475)
name_window = "Joining files"
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
display_text  = "Enter the session duration (in minutes)"
default_value = ''
key_word      = "Session_length"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
layout += [[sg.T("")]]
layout += [line]

# (Block 5) Create a number entry.

line          = []
display_text  = "Enter the duration of first time bins (in minutes)"
default_value = ''
key_word      = "Bin_length1"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
layout += [[sg.T("")]]
layout += [line]

# (Block 5) Create a number entry.

line          = []
display_text  = "OPTIONAL: Enter the duration of the second time bins (in minutes). If not used leave blank"
default_value = ''
key_word      = "Bin_length2"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
layout += [[sg.T("")]]
layout += [line]

# (Block 7) Create radio buttons.

line          = []
display_text  = "What do you want to do with your data?"
dropdown_list = ['1) Join ALL sessions in each FED subfolder', '2) Join ONLY sessions with specific dates that are consistent across all FEDs', '3) Join ONLY sessions that have a specific word in the filename', '4) Combination of 2 and 3, specific dates and specific word']
default_value = ''
key_word      = "What_to_do"
inp[key_word] = str

line += [sg.Text(display_text)]
line += [sg.Combo(dropdown_list,default_value=default_value,key=key_word,enable_events=True)]
layout += [[sg.T("")]]
layout += [line]

# End text

line          = []
display_text  = "If you chose to join all session pressing SUBMIT will run the code and generate a new file for each FED of all sessions joined in chronological order"
line += [sg.Text(display_text)]
layout += [line]

line          = []
display_text  = "If you chose any other option pressing SUBMIT will generate another popup window for additonal information"
line += [sg.Text(display_text)]
layout += [line]

###### Create the GUI.

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
    
#####

what_to_do = inputs["What_to_do"]

if what_to_do == '2) Join ONLY sessions with specific dates that are consistent across all FEDs':
    
    sg.theme("DarkRed")
    size_GUI = (750,150)
    name_window = "Joining only specific dates"
    layout = []
    inp = {}
    
    # Block X
    
    line          = []
    display_text  = "Enter all dates of sessions to be joined as dd/mm/yyyy seperated by comma space"
    default_value = ''
    key_word      = "Same_dates_to_join"
    inp[key_word] = str
    
    line += [sg.Text(display_text)]
    line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
    layout += [[sg.T("")]]
    layout += [line]
    
    # End text

    line          = []
    display_text  = "Pressing SUBMIT will create a new file for each FED of joined sessions of ONLY the above dates in chronological order"  
    line += [sg.Text(display_text)]    
    layout += [line]

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
        
    print('specific dates only')

elif what_to_do == '3) Join ONLY sessions that have a specific word in the filename':
    
    sg.theme("DarkTeal7")
    size_GUI = (750,150)
    name_window = "Joining only specific filenames"
    layout = []
    inp = {}
    
    # Block X
    
    line          = []
    display_text  = "Enter the word in the filename that denotes which sessions are to be joined"
    default_value = ''
    key_word      = "Filenames_to_join"
    inp[key_word] = str
    
    line += [sg.Text(display_text)]
    line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
    layout += [[sg.T("")]]
    layout += [line]
    
    # End text

    line          = []
    display_text  = "Pressing SUBMIT will create a new file for each FED of joined sessions of ONLY those sessions whose filenames contain the entered word in chronological order"  
    line += [sg.Text(display_text)]    
    layout += [line]

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
        
    print('specific filenames only')
    
elif what_to_do == '4) Combination of 2 and 3, specific dates and specific word':
    
    sg.theme("DarkGreen")
    size_GUI = (750,200)
    name_window = "Joining specific filenames and dates"
    layout = []
    inp = {}
    
    # Block X
    
    line          = []
    display_text  = "Enter the word in the filename that denotes which sessions are to be joined"
    default_value = ''
    key_word      = "Filenames_to_join"
    inp[key_word] = str
    
    line += [sg.Text(display_text)]
    line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
    layout += [[sg.T("")]]
    layout += [line]

    # Block X
    
    line          = []
    display_text  = "Enter all dates of sessions to be joined as dd/mm/yyyy seperated by comma space"
    default_value = ''
    key_word      = "Same_dates_to_join"
    inp[key_word] = str
    
    line += [sg.Text(display_text)]
    line += [sg.Input(default_text=default_value,key=key_word,enable_events=True)]
    layout += [[sg.T("")]]
    layout += [line]
    
    # End text

    line          = []
    display_text  = "Pressing SUBMIT will create a new file for each FED of joined sessions whose filename contains or was on a date entered above in chronological order"  
    line += [sg.Text(display_text)]    
    layout += [line]

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
        
    print('filenames and dates')

#####
    
print('run join code')

#####
    
# join_all_yes = values["Yes"]
# join_all_no = values["No"]

# print(join_all_yes, join_all_no)