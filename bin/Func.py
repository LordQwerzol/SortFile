import os
import shutil
from collections import OrderedDict
from Dialog import *


def get_files(path:str) -> list :
    """
    Функция из указанной директории возращяет список файлов
    """
    try:
        files_dir = os.listdir(path)
        only_files = []
        for i in files_dir:
            if os.path.isfile(path+i):
                only_files.append(i)
        return only_files
    except NotADirectoryError:
        CustomMessageBox().show_warning_box("Ошибка!", "Указанная дириктория не верная!")
        return []
    except FileNotFoundError:
        CustomMessageBox().show_warning_box("Ошибка!", "Указанной дириктории не существует!")
        return []
def move_files(start:str,end:str,files:list) -> None:
    """
    Процедура перемещяет из дириктории start в дирикторию end файлы из списка
    """
    try:
        end = end + '/' if end[-1]!='/' else end
        for file in files: 
            shutil.move(start+file, end+file)
    except SyntaxWarning:
        CustomMessageBox().show_warning_box('Внимание!', f'Ошибка в указании пути папки {end}') 
    except FileNotFoundError:
        CustomMessageBox().show_warning_box('Внимание!', f'Ошибка в указании пути папки {end}') 
def Get_mas_key(flag:bool) -> list: 
    """
    Возращает список ключей и дирикторий 
    """
    path = "/home/lexa/SortFile/file/Configuration Key.txt" if flag else "/home/lexa/SortFile/file/Configuration Extension.txt"
    mas = []
    with open(path, encoding="UTF-8") as data:
        for line in data:
            if ' - ' in line:
                mas.append(line.replace('\n','',1).split(' - '))
            else: return []
    return mas

def Sorted_files(download_path:str, flag:bool) -> None:
    """
    Сортирует файлы из заданной дириктории в зависимости от выбранного режима
    flag = 0 -> по расширению файла 
    flag = 1 -> по ключу
    """
    download_path = download_path + '/' if download_path[-1]!='/' else download_path
    files = get_files(download_path)
    keys = Get_mas_key(flag)
    if keys == []:
        message = "по ключу" if flag else "расширений файлов"
        CustomMessageBox().show_warning_box('Внимание!', f'Настройте конфигурацию {message}')
        return
    else: 
        dict_files = dict()
        for key, path in keys: dict_files[key] = []

        for file in files: 
            for key in dict_files.keys():
                if key in file: dict_files[key].append(file)
        
        for key, path in keys: move_files(download_path, path, dict_files[key])
        CustomMessageBox().show_information_box('Ура!', 'Все успешно!')

def MyRename(key:str, files:list) -> None:
    """
    Переменнует группу файлов, добавляет в конец имени ключ
    """
    for file in files:
        new_file = file[:file.find('.')] + f"-{key}" + file[file.find('.'):]
        os.rename(file, new_file)
    CustomMessageBox().show_information_box('Ура!', 'Все успешно!')

def MySynchronizationFloders(dir1:str, dir2:str) -> None:
    """
    Синхронизирует папки
    """
    files1 = get_files(dir1)
    files2 = get_files(dir2)
    rezult = list(OrderedDict.fromkeys(files1 + files2))
    for file in rezult:
        try:
            if not file in files1: shutil.copy(dir2+file, dir1+file)
            if not file in files2: shutil.copy(dir1+file, dir2+file)
        except OSError:
            pass
    CustomMessageBox().show_information_box('Ура!', 'Все успешно!')

if __name__ == "__main__":
    dir1 = "c:/Users/Alex/Desktop/1/"
    dir2 = "c:/Users/Alex/Desktop/2/"
    MySynchronizationFloders(dir1, dir2)
