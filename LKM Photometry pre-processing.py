#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:55:57 2022

@author: lauramilton
"""

import_location = r'/Users/lauramilton/Desktop/RO 2021/Photometry/All files Alex mouse 1/'
export_location = r'/Users/lauramilton/Desktop/RO 2021/Photometry/All files Alex mouse 1/'

import pandas as pd
import numpy as np
import os
import openpyxl
import math

video_frame_column = 'Timestamp.FrameCounter'
video_timestamp_column = 'Timestamp.Timestamp'
video_channel_column = 'Timestamp.Flags'

right_frame_column = 'Timestamp.FrameCounter'
right_timestamp_column = 'Timestamp.Timestamp'
right_channel_column = 'Timestamp.Flags'

down_frame_column = 'Timestamp.FrameCounter'
down_timestamp_column = 'Timestamp.Timestamp'
down_channel_column = 'Timestamp.Flags'

left_frame_column = 'Timestamp.FrameCounter'
left_timestamp_column = 'Timestamp.Timestamp'
left_channel_column = 'Timestamp.Flags'

c_470_frame_column = 'FrameCounter'
c_470_timestamp_column = 'Timestamp'
c_470_0G_column = 'Region0G'
c_470_1R_column = 'Region1R'
c_470_2G_column = 'Region2G'
c_470_3R_column = 'Region3R'

c_415_frame_column = 'FrameCounter'
c_415_timestamp_column = 'Timestamp'
c_415_0G_column = 'Region0G'
c_415_1R_column = 'Region1R'
c_415_2G_column = 'Region2G'
c_415_3R_column = 'Region3R'

for filename in sorted(list(os.listdir(import_location))):
    if filename.endswith('.csv'):
        if 'video' in filename:
            print('Video ', filename)
            
            import_name = filename
            import_destination = import_location + import_name
            
            df = pd.read_csv(import_destination)
            
            video_frame = df[video_frame_column].tolist()
            video_timestamp = df[video_timestamp_column].tolist()
            video_channel_column = df[video_channel_column].tolist()
            
        elif 'Right' in filename:
            print('Right ', filename)
            
            import_name = filename
            import_destination = import_location + import_name
            
            df = pd.read_csv(import_destination)
            
            right_frame = df[right_frame_column].tolist()
            right_timestamp = df[right_timestamp_column].tolist()
            right_channel_column = df[right_channel_column].tolist()
            
        elif 'Pellet' in filename:
            print('Down ', filename)
            
            import_name = filename
            import_destination = import_location + import_name
            
            df = pd.read_csv(import_destination)
            
            down_frame = df[down_frame_column].tolist()
            down_timestamp = df[down_timestamp_column].tolist()
            down_channel_column = df[down_channel_column].tolist()

        elif 'Left' in filename:
            print('Left ', filename)
            
            import_name = filename
            import_destination = import_location + import_name
            
            df = pd.read_csv(import_destination)
            
            left_frame = df[left_frame_column].tolist()
            left_timestamp = df[left_timestamp_column].tolist()
            left_channel_column = df[left_channel_column].tolist()
            
        elif '415' in filename:
            print('415 ', filename)
            
            import_name = filename
            import_destination = import_location + import_name
            
            df = pd.read_csv(import_destination)
    
            c_415_frame = df[c_415_frame_column].tolist()
            c_415_timestamp  = df[c_415_timestamp_column].tolist()
            c_415_0G = df[c_415_0G_column].tolist()
            c_415_1R = df[c_415_1R_column].tolist()
            c_415_2G = df[c_415_2G_column].tolist()
            c_415_3R = df[c_415_3R_column].tolist()
    
        elif '470' in filename:
            print('470 ', filename)
            
            import_name = filename
            import_destination = import_location + import_name
            
            df = pd.read_csv(import_destination)
    
            c_470_frame = df[c_470_frame_column].tolist()
            c_470_timestamp  = df[c_470_timestamp_column].tolist()
            c_470_0G = df[c_470_0G_column].tolist()
            c_470_1R = df[c_470_1R_column].tolist()
            c_470_2G = df[c_470_2G_column].tolist()
            c_470_3R = df[c_470_3R_column].tolist()

c_415_test_timestamp = []
c_470_test_timestamp = []

for i in range(0, len(c_415_timestamp)):
    c_415_test_timestamp.append(np.nan)
    c_415_test_timestamp.append(np.nan)
    c_415_test_timestamp.append(c_415_timestamp[i])
    
for i in range(0, len(c_470_timestamp)):
    c_470_test_timestamp.append(c_470_timestamp[i])
    c_470_test_timestamp.append(np.nan)
    c_470_test_timestamp.append(np.nan)

video_timestamp_truncated = []
video_frame_truncated = []
skipped_frames = []
for i in range(0, (len(video_frame) - 1)):
    if video_frame[i] != video_frame[i + 1]:
        video_timestamp_truncated.append(video_timestamp[i])
        video_frame_truncated.append(video_frame[i])
video_timestamp_truncated.append(video_timestamp[-1])
video_frame_truncated.append(video_frame[-1])

for i in range(0, (int(video_frame_truncated[-1])) - 1):
    while int(video_frame_truncated[i] + 1) < int(video_frame_truncated[i + 1]):
        video_frame_truncated.insert((i + 1), int(video_frame_truncated[i]) + 1)
        video_timestamp_truncated.insert((i + 1), np.nan)
        # c_415_test_timestamp.insert((i + 1), np.nan)
        # c_470_test_timestamp.insert((i + 1), np.nan)
        skipped_frames.append(int(video_frame_truncated[i]) + 1)

right_arrow_column = []
left_arrow_column = []
down_arrow_column = []
c_415_0G_channel = []
c_415_1R_channel = []
c_415_2G_channel = []
c_415_3R_channel = []
c_470_0G_channel = []
c_470_1R_channel = []
c_470_2G_channel = []
c_470_3R_channel = []
# timestamp = []


# for i in range(0, len(video_timestamp_truncated)):
#     if math.isnan(video_timestamp_truncated[i]) == False:
#         timestamp.append(video_timestamp_truncated[i])
#     else:
#         if math.isnan(c_415_test_timestamp[i]) == False:
#             timestamp.append(c_415_test_timestamp[i])
#         elif math.isnan(c_470_test_timestamp[i]) == False:
#             timestamp.append(c_470_test_timestamp[i])

index_415 = 0
index_470 = 0

for i in range(0, len(video_frame_truncated)):
    if video_frame_truncated[i] in right_frame:
        right_arrow_column.append('Right')
    else:
        right_arrow_column.append(np.nan)
        
    if video_frame_truncated[i] in left_frame:
        left_arrow_column.append('Left')
    else:
        left_arrow_column.append(np.nan)
    
    if video_frame_truncated[i] in down_frame:
        down_arrow_column.append('Down')
    else:
        down_arrow_column.append(np.nan)
    
    if video_frame_truncated[i] in c_415_frame:
        c_415_0G_channel.append(c_415_0G[index_415])
        c_415_1R_channel.append(c_415_1R[index_415])
        c_415_2G_channel.append(c_415_2G[index_415])
        c_415_3R_channel.append(c_415_3R[index_415])
        index_415 += 1
    else:
        c_415_0G_channel.append(np.nan)
        c_415_1R_channel.append(np.nan)
        c_415_2G_channel.append(np.nan)
        c_415_3R_channel.append(np.nan)
        
    if video_frame_truncated[i] in c_470_frame:
        c_470_0G_channel.append(c_470_0G[index_470])
        c_470_1R_channel.append(c_470_1R[index_470])
        c_470_2G_channel.append(c_470_2G[index_470])
        c_470_3R_channel.append(c_470_3R[index_470])
        index_470 += 1
    else:
        c_470_0G_channel.append(np.nan)
        c_470_1R_channel.append(np.nan)
        c_470_2G_channel.append(np.nan)
        c_470_3R_channel.append(np.nan)

for i in range(0, len(video_timestamp_truncated)):
    if math.isnan(video_timestamp_truncated[i]) == True:
        if math.isnan(c_415_test_timestamp[i]) == False:
            video_timestamp_truncated[i] = c_415_test_timestamp[i]
        elif math.isnan(c_470_test_timestamp[i]) == False:
            video_timestamp_truncated[i] = c_470_test_timestamp[i]

results = {'Frame': video_frame_truncated, 'Timestamp': video_timestamp_truncated, 'Left Arrow': left_arrow_column, 'Right Arrow': right_arrow_column, 'Down Arrow': down_arrow_column,
            '415 Region 0G': c_415_0G_channel, '415 Region 1R': c_415_1R_channel, '415 Region 2G': c_415_2G_channel, '415 Region 3R': c_415_3R_channel,
            '470 Region 0G': c_470_0G_channel, '470 Region 1R': c_470_1R_channel, '470 Region 2G': c_470_2G_channel, '470 Region 3R': c_470_3R_channel}
export_file = pd.DataFrame(results, columns = ['Frame', 'Timestamp', 'Left Arrow', 'Right Arrow', 'Down Arrow', '415 Region 0G', '415 Region 1R', '415 Region 2G', '415 Region 3R', '470 Region 0G', '470 Region 1R', '470 Region 2G', '470 Region 3R'])

# results = {'Video': video_timestamp_truncated}
# export_file = pd.DataFrame(results, columns = ['Video'])

# Export to excel

from openpyxl import Workbook

wb = Workbook()

ws1 = wb.active
ws1.title = 'Photometry'

export_name = 'Photometry data test.xlsx'
export_destination = export_location + '/' + export_name

with pd.ExcelWriter(export_destination) as writer:
    export_file.to_excel(writer, sheet_name='Photometry', engine='openpyxl', index=False, header=True)

    
                
