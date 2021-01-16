# moves files from downloads folder into categorized subfolders.

import shutil, os, time
from pathlib import Path

filechecker = {'00_Exe_Files': ['EXE'],
               '00_Python_Files': ['PY'],
               '01_3D_Files': ['BLEND', 'OBJ', 'BLEND1', 'FBX', 'MTL', 'DAE'],
               '02_Videos': ['MP4', 'MOV'],
               '03_Pictures': ['JPG', 'JPEG', 'PNG', 'BMP'],
               '04_Audio': ['MP3', 'WAV'],
               '05_Documents': ['PDF', 'DOCX', 'TXT',],
               '06_Zipped_Files': ['ZIP'],}

""" Path to Downloads Folder"""
##########################################
download_path = f'{str(os.path.join(Path.home()))}\Downloads'
##########################################

try:
    os.chdir(download_path)
except FileNotFoundError:
    print(f'Path to file "{download_path}" incorrect.')
    exit()

for filename in os.listdir():
    filename = filename.upper()
    ###---------------
    ###-- Find files and make folder if not there, move file to folder 
    for folder, extensions in filechecker.items():
        for ext in extensions:
            if filename.endswith(f'.{ext}'):
                if os.path.isdir(f'{os.getcwd()}\\{folder}'):
                    shutil.move(f'{os.getcwd()}\\{filename.title()}', f'{os.getcwd()}\\{folder}')
                else:
                    os.mkdir(folder)
                    shutil.move(f'{os.getcwd()}\\{filename.title()}', f'{os.getcwd()}\\{folder}')

print('Done')
