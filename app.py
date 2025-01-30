import json
from flask import Flask, request
from flask import jsonify
import numpy as np
import pandas as pd
from sklearn.metrics import euclidean_distances


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'Hello, World!':'Hello, World!'})

# @app.route('/api/get_recomendation' , methods=['POST'])
# def Get_recomendations():
#     data=request.form
#     speciality=data['speciality']
#     moyenne=calculate_moyenne(speciality,data)
#     if speciality=='' or speciality==None or speciality=='N00':
#         return jsonify({'error':'Please enter a speciality'})
#     cluster=Find_cluster(speciality,data)
#     Recomendations=Recomendations(speciality,moyenne,cluster)
#     return jsonify({'Recomendations':Recomendations})
        
        

# def calculate_moyenne(speciality,data):
#     coeficients=[]
#     if speciality=='N00':
#         return -1
#     elif speciality=='N01':
#         coeficients=[6,3,3,4,2,2,6]
#     elif speciality=='N02':
#         coeficients=[5,5,5,3,2,4,2,2]
#     elif speciality=='N03':
#         coeficients=[3,2,2,2,2,5,6,5,2]
#     elif speciality=='N04':
#         coeficients=[3,2,2,2,2,7,2,6,2]
#     elif speciality=='N05':
#         coeficients=[2,2,2,2,2,6,7,2]
#     elif speciality=='N06':
#         coeficients=[3,2,2,4,2,5,2,5,6,2]
#     if 'sport_mark' in data.keys():
#         coeficients.append(1)
    
        
#     moyenne=0
#     i=0
#     for subject in data.keys():
#         if subject=='amazigh_mark':
#             continue 
#         if i>len(coeficients)-1:
#             break
#         if subject=='speciality':
#             continue
        
#         if data[subject]==None:
#             return -1
#         moyenne+=data['subject']*coeficients[i]
#         i+=1
#     sum_of_coeficients=sum(coeficients)
#     if sum_of_coeficients==0:
#         return -1
#     moyenne=moyenne/sum_of_coeficients
#     return moyenne



# def Find_cluster(speciality,data):
    
#     if speciality=="N04":
#         try:
#             with open("orientation_mapping_maths.json", "r") as json_file:
#                 json_data = json.load(json_file)
#             cluster_centroids = np.array(json_data["centroids"])
#         except (FileNotFoundError, json.JSONDecodeError, KeyError):
#             print("Error: Unable to load centroids from orientation_mapping_maths.json")
#             cluster_centroids = np.array([])
#         weights = {
#     'ANGLAIS': 4,
#     'FRANÇAIS': 4,
#     'LITTERATURE_ARABE': 9,
#     'MATHEMATIQUE': 49,
#     'PHYSIQUE': 36,
#     'SNV': 4,
#     'HISTOIRE_GEOGRAPHIE': 4,
#     'SCIENCE ISLAMIQUE': 4,
#     'PHILOSOPHIE': 4,
#     'E.P.S': 0.0001,
#     'LANGUE_AMAZIGH': 0.0001
# }
    
#     new_record = {
#     'ANGLAIS': data['Anglais'],
#     'FRANÇAIS': data['Français'],
#     'LITTERATURE_ARABE': data['Arabe'],
#     'MATHEMATIQUE': data['Mathématiques'],
#     'PHYSIQUE': data['Physique'],
#     'SNV': data['Science'],
#     'HISTOIRE_GEOGRAPHIE': data['Histoire Géographie'],
#     'SCIENCE_ISLAMIQUE': data['Education Islamique'],
#     'PHILOSOPHIE': data['Philosophie'],
#     'LANGUE_AMAZIGH': 0
# }
#     if 'spoort_mark' in data.keys():
#         new_record['E.P.S'] = data['sport_mark']

# # Apply the same weights to the new record
#     for subject, weight in weights.items():
#         if subject in new_record:
#             new_record[subject] = new_record[subject] * weight

#     # Convert new record to a DataFrame (same structure as original data)
#     new_record_df = pd.DataFrame([new_record])

#     if cluster_centroids.size > 0:
#         # Calculate distances from the new record to each centroid
#         distances = euclidean_distances(new_record_df, cluster_centroids)

#         # Find the closest cluster (the one with the minimum distance)
#         closest_cluster = np.argmin(distances)
#         print(f"The new record is assigned to cluster: {closest_cluster}")
#     else:
#         print("No centroids available to assign a cluster.")
    
    
    
    
# def Recomendations(speciality,moyenne,cluster):
#     Recomendations=[]
#     try:
#             with open("specialities__univ_map.json", "r") as json_file:
#                 json_data = json.load(json_file)
#             Etablissements=json_data[speciality]
#     except (FileNotFoundError, json.JSONDecodeError, KeyError):
#             print("Error: Unable to load Fillieres from specialities__univ_map.json")
#     try:
#             with open("orientation_mapping_maths.json", "r") as json_file:
#                 json_data = json.load(json_file)
#             cluster=json_data[cluster]
#     except (FileNotFoundError, json.JSONDecodeError, KeyError):             
#             print("Error: Unable to load centroids from orientation_mapping_maths.json")  
#     for Suggestion in cluster:
#         if len(Recomendations)>=5:
#             break
#         if Suggestion[0][1] in Etablissements.keys() and Suggestion[0][0] in Etablissements[Suggestion[0][1]] and moyenne>=Suggestion[3]:
#             Recomendations.append(Suggestion)
#     return Recomendations
















if __name__ == '__main__':
    app.run(debug=True)