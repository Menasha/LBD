import json

#input_files
input_file_shared_concepts = "dataset/mesh/concepts.txt"
input_file_common_documents = "dataset/mesh/existing_connections.txt"
#output_files
output_file = "dataset/mesh/filtered_concepts.txt"

#get data
shared_concepts = json.load(open(input_file_shared_concepts))

documents = []
with open(input_file_common_documents, "r") as f:
    for line in f:
        for item in json.loads(line):
            documents.extend(item)    
print(len(documents))
common_concepts = list(set(documents))
print(len(common_concepts))

selected_concepts = []
for item in shared_concepts:
    if item[0] in common_concepts:
        pass
    else:
        selected_concepts.append(item)
print(len(selected_concepts))

with open(output_file, "w") as fw:
    fw.write(json.dumps(selected_concepts))
