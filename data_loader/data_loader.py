
from datetime import datetime
import sys
import os

import_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(import_path)
sys.path.append(os.path.join(import_path, "../../"))
from tqdm import tqdm
# format output is list of files and list of anomalies with type and descriptions

class DataLoader:
    def __init__(self, filename):
        self.file_name = filename
        self.read_data_from_csv_file(self.file_name)

    def read_data_from_csv_file(self, filename: str) -> None:
        """
        Main data_loader

        Data in file has to be in following format:
        'Дата операции'
        'Дата платежа'
        'Номер карты'
        'Статус'
        'Сумма операции'
        'Валюта операции'
        'Сумма платежа'
        'Валюта платежа'
        'Кэшбэк'
        'Категория'
        'MCC'
        'Описание'
        'Бонусы (включая кэшбэк)'
        'Округление на инвесткопилку'
        'Сумма операции с округлением']
        With ";" delimeter. 
        Args:
            filename (str): path to csv file

        """
        with open(filename, 'r') as file:
            lines = file.readlines()
        # Get lables
        self.lables = lines[0].strip().split(";")
        self.horizontal_data_list = []
        self.vertical_data_list = [[]] * len(self.lables)
        for i in tqdm(range(len(lines)-1, 1, -1)): #len(lines)-2
            temp_line = lines[i].strip().split(";")
            temp_line[0] = datetime. strptime(temp_line[0], '%d.%m.%Y %H:%M:%S')
            if temp_line[1] != "": temp_line[1] = datetime. strptime(temp_line[1], '%d.%m.%Y')
            else: temp_line[1] = datetime(1970, 1, 1)
            temp_line[4] = float(temp_line[4])
            temp_line[6] = float(temp_line[6])
            if temp_line[8] == "": temp_line[8] = 0
            else: temp_line[8] = int(temp_line[8] )
            temp_line[12] = float(temp_line[12])
            temp_line[13] = float(temp_line[13])
            temp_line[14] = float(temp_line[14])
            self.horizontal_data_list.append(temp_line)
            for j in range(len(self.vertical_data_list)):
                self.vertical_data_list[j].append(temp_line[j])


if __name__ == '__main__':
    path = "/media/nikita/HDD/operations_1.csv"

    data_loader = DataLoader(path)
    print(data_loader.vertical_data_list)
    print(data_loader.horizontal_data_list)
    print(data_loader.lables)
