import os
import sys
from colorama import Fore, init

init(autoreset=True)

def list_directory_structure(path):
    try:
        if not os.path.isdir(path):
            print(f"{Fore.RED}Шлях {path} не є директорією або не існує.")
            return

        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                print(f"{Fore.BLUE}{dir_name}")
            for file_name in files:
                print(f"{Fore.GREEN}{file_name}")

    except Exception as e:
        print(f"{Fore.RED}Помилка: {e}")

if len(sys.argv) != 2:
    print(f"{Fore.RED}Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.")
else:
    path = sys.argv[1]
    list_directory_structure(path)