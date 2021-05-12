import pandas as pd
import json
import string
from tqdm import tqdm
import ast

year = 1986 #do for every year (e.g., 1960-2019)
start = "" #mention the start concept (e.g., raynaud disease)

#input_files
input_path = "Medline_global_repository/mesh/"
input_file = str(year)+".tsv"

#output_files
output_path = "dataset/mesh/"
start_document_ids = "start_document_ids_"+str(year)+".txt"
start_file = "start_mesh_"+str(year)+".txt"

#Load mesh
input_data = pd.read_csv(input_path+input_file, header=0, delimiter="\t", quoting=3)
input_data.fillna("#########", inplace=True)

L = (input_data[["ID", "MESH"]])
print(L.shape)

#remove duplicates
L_new = L.groupby(["ID", "MESH"]).head(1)
print(L_new.shape)

#convert to a list of tuples
L_list = [tuple(x) for x in L_new.values]
print(len(L_list))

def preprocess_mesh(mesh_list):
    mytemp = []
    
    for item in mesh_list:
        
        if isinstance(item, str):
            pass
        
        else:
            mesh = item.decode("utf-8").lower()
            
            for item in string.punctuation:
                if item in mesh:
                    
                    mesh = mesh.replace(item, " ")
                    
            words = mesh.split()
            mesh = ' '.join(words)
            
            mytemp.append(mesh)
            
    #list
    return(mytemp)

#mesh list
mymesh = []

for item in tqdm(L_list):
     
    if item[1] != "#########": 
        mesh = ast.literal_eval(item[1])
        
        if type(mesh) is list:
            
            mesh_preprocessed = preprocess_mesh(mesh)
            
            if len(mesh_preprocessed) > 0:
                mymesh.append(tuple((item[0], mesh_preprocessed)))

print(len(mymesh))

start_ids = []
start_mesh = []
#start
for item in mymesh:
    if start in item[1]:
        start_ids.append(item[0])
        start_mesh.append(item[1])
print("Length of start ids:")
print(len(start_ids))

#write files
with open(output_path+start_document_ids, "w") as fw_1:
    fw_1.write(json.dumps(start_ids))

with open(output_path+start_file, "w") as fw1:
    fw1.write(json.dumps(start_mesh))
