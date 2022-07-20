
from datetime import datetime
import sys
import os

sys.path.append('../utils')
import_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(import_path)
sys.path.append(os.path.join(import_path, "../../"))
from tqdm import tqdm
# format output is list of files and list of anomalies with type and descriptions


def read_data_from_csv_file(filename: str) -> list:
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Get lables
    lables = lines[0].strip().split(";")
    temp_horizontal_list = []
    temp_vertical_list = [[]] * len(lables)
    for i in tqdm(range(1, len(lines), 1)): #len(lines)-2
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
        temp_horizontal_list.append(temp_line)
        for j in range(len(temp_vertical_list)):
            temp_vertical_list[j].append(temp_line[j])
    return temp_horizontal_list, temp_vertical_list, lables


if __name__ == '__main__':
    path = "/media/nikita/HDD/operations_1.csv"

    test_1, test_2, lables= read_data_from_csv_file(path)
    print(test_1)
    print(test_2)
    print(lables)
