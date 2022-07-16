#applications with data sets

import numpy as np
import math
import csv

dataset = np.genfromtxt("covid_county.csv", delimiter = ",", skip_header = True)

print(dataset[:, [0,2,4]])