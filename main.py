import sys
import os

import_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(import_path)
sys.path.append(os.path.join(import_path, "../../"))
from data_loader.data_loader import DataLoader
from data_structures.big_time_series import BigCommonTimeSeries

if __name__ == '__main__':
    path = "/media/nikita/HDD/operations_1.csv"
    data_loader = DataLoader(path)
    b = BigCommonTimeSeries(data_loader)
