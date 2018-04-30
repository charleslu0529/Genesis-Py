import matplotlib.pyplot as plt
from tkinter import Tk
import tkinter
from tkinter.filedialog import askopenfilename
import numpy as np
import inquirer

Tk().withdraw()

N = 1000
xTrue = np.linspace(0,1000,N)


entries = []
print("Select evec file\n")

filename = askopenfilename()

pca_file = open(filename, "r+")

for line in pca_file:
    data = line.split()
    entries.append(data)
    # print(data)
    # print("\n")

number_of_pca = len(entries[1])

questions_pca = [inquirer.List('number', message="Which PCA do you need?", choices=list(range(1,number_of_pca))),]

data_set_1 = inquirer.prompt(questions_pca)
# data_set_2 = inquirer.prompt(questions_pca)

# print(data_set_1["number"])
# print(data_set_2["number"])


pca_file.close()



# plt.scatter(,)