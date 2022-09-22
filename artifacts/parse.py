import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

prefix_dict = {"#*":"title",
               "#@":"author",
               "#t":"year",
               "#c":"venue",
               "#index":"id",
               "#%":"reference_id", 
               "#!":"abstract"}

%%timeit
file = open("citation-network1/outputacm.txt", mode = 'r', encoding="utf8")
N_PUBLICATIONS = int(file.readline())
publications = []

for _ in range(N_PUBLICATIONS):
    publication = {}
    line = file.readline()
    while line != '\n':
        for key in prefix_dict.keys():
            if line.startswith(key):
                if prefix_dict[key] in publication:
                   publication[prefix_dict[key]].append(line.replace(key,""))
                publication[prefix_dict[key]] = [line.replace(key,"")]
                break
        line = file.readline()
    publications.append(publication)
    
df = pd.DataFrame(publications)