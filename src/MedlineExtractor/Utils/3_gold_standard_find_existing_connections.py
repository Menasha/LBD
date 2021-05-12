import json
from tqdm import tqdm

year = 1985 #this is before the cut-off (e.g., 1960-1985)
start = "" #mention the start concept

#input_files
input_file = "Medline_global_repository/mesh/mesh_"+str(year)+".txt"

#output_files
output_file = "dataset/mesh/existing_connections.txt"

#get data
documents = json.load(open(input_file))

print(len(documents))

existing_connections = []

for document in tqdm(documents):

    #start    
    if start in document:
        
        existing_connections.append(document)
    
print(len(existing_connections))

if len(existing_connections) > 0:
    with open(output_file, "a") as fw:
        fw.write(json.dumps(existing_connections))
        fw.write("\n")
