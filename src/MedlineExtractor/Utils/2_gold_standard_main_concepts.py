import json
from operator import itemgetter
import pandas as pd
from tqdm import tqdm
#mention the start concept
start = ""

start_year = 1986 #should start after the cut-off date
end_year = 2019

#input_files
input_path = "dataset/mesh/"
#output_files
output_file = "dataset/mesh/concepts.txt"

#load data
mystartmesh = []

while start_year <= end_year:
    print(start_year)
    mystartmesh.extend(json.load(open(input_path+"start_mesh_"+str(start_year)+".txt")))
    
    start_year = start_year + 1

start_mesh = []

for mesh in mystartmesh:
    if start in mesh:
        start_mesh.extend(mesh)

print("Start terms processing: ")
start_terms_dictionary_sums = dict((x,start_mesh.count(x)) for x in set(start_mesh))
print(len(start_terms_dictionary_sums))
del start_terms_dictionary_sums[start]

print(len(start_terms_dictionary_sums))

print("Sorting the final results: ")

sorted_by_value = sorted(start_terms_dictionary_sums.items(), key=lambda kv: kv[1], reverse=True)

print(len(sorted_by_value))

#write files
with open(output_file, "w") as fw:
    fw.write(json.dumps(sorted_by_value))
