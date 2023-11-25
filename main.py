#Created by Nestorkoo
#Github: https://github.com/Nestorkoo

import shutil
import os
from datetime import datetime
import time
import art
from colorama import *

init()

Art = art.text2art('Nestorkoo')
print(Fore.CYAN + Art)
get_path = input('Path to folder: ')
interval = input('Interval beetwen saves for example 1d - 1 days, 1h - 1 hours, 1m - 1 minute')
print(Fore.RED + 'If you need to change a folder that we will saved, just press ctrl+c and run app again')
last_component = os.path.basename(get_path)

def get_interval():
    if interval[1] == 'd':
        get_day = interval[0]
        count_day = 24 * int(get_day) * 60 * 60
        time.sleep(count_day)
    elif interval[1] == 'h':
        get_hour = interval[0]
        count_hours = int(get_hour) * 60 * 60
        time.sleep(count_hours)
    elif interval[1] == 'm':
        get_minute = interval[0]
        count_minute = int(get_minute) * 60
        time.sleep(count_minute)
def if_file_saves():
    try:
        while True:
            try:
                os.mkdir(f'Backups {last_component}')
                os.chdir(f'Backups {last_component}')
                current_time = datetime.now().strftime("%H-%M-%S")
                os.mkdir(f'Backups {last_component} time - {current_time}')
                os.chdir(f'Backups {last_component} time - {current_time}')
                shutil.copyfile(get_path, f'Backups {last_component} time - {current_time}')
                os.chdir(get_path[2])
            except FileExistsError:
                os.chdir(f'Backups {last_component}')
                current_time = datetime.now().strftime("%H-%M-%S")
                os.mkdir(f'Backups {last_component} time - {current_time}')
                os.chdir(f'Backups {last_component} time - {current_time}')
                shutil.copyfile(get_path, f'Backups {last_component} time - {current_time}')
                os.chdir(get_path[2])
            print(Fore.GREEN + f'Save {last_component} | time: {current_time}')
            get_interval()
    except KeyboardInterrupt:
        print('Script is stopped')

def if_dir_saves():
    try:
        while True:
            try:
                os.mkdir(f'Backups {last_component}')
                os.chdir(f'Backups {last_component}')
                current_time = datetime.now().strftime("%H-%M-%S")
                os.mkdir(f'Backups {last_component} time - {current_time}')
                os.chdir(f'Backups {last_component} time - {current_time}')
                shutil.copytree(get_path, f'Backups {last_component} time - {current_time}')
                os.chdir(get_path[2])
                
            except FileExistsError:
                os.chdir(f'Backups {last_component}')
                current_time = datetime.now().strftime("%H-%M-%S")
                os.mkdir(f'Backups {last_component} time - {current_time}')
                os.chdir(f'Backups {last_component} time - {current_time}')
                shutil.copytree(get_path, f'Backups {last_component} time - {current_time}')
                os.chdir(get_path[2])
            print(Fore.GREEN + f'Save {last_component} | time: {current_time}')
            get_interval()
    except KeyboardInterrupt:
        print('Script is stopped')

if os.path.isfile(get_path):
    os.chdir(get_path[2])
    if_file_saves()
    
elif os.path.isdir(get_path):
    os.chdir(get_path[2])
    if_dir_saves()