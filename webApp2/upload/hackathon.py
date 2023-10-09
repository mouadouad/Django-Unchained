#model predict for one image
import os
from PIL import Image
from tensorflow import keras
import numpy as np
from numpy import asarray
import json



def initialiserJSON():                                    # prépare le json a accueillir des données
    filename = "resultat.txt"                             # on créé un fichier texte
    f= open(filename, 'w')                                # on l'ouvre en écriture seule pour l'écraser
    f.write("{\n\t\"tab\": [\n")                          
    f.write("\n\t]\n}")
    f.close()
    os.rename(filename, "resultat.json")
    
    

def fermerJSON(f):
    f.close()

def writeJSON(new_data,fDATA,f):
    print("coucou")
    fDATA["tab"].append(new_data)
    json.dump(fDATA, f)
    f.seek(0)



def demarrer():
    path = "media/"                            # dossier d'image à traiter
    nom = os.listdir(path)                                    # recup de la liste des noms des images

    initialiserJSON()                                         # prépare le json a accueillir des données
    f = open("resultat.json", 'r+')                           # ouvre le json
    fDATA = json.load(f)


    for i in range(len(nom)) :
        
        image = Image.open(path+nom[i])
        model = keras.models.load_model('model3')

        image = image.resize((224,224)) 
        data = asarray(image)
        data = data.reshape((1,) + data.shape)
        result = model.predict(data)
        classes = ["Bouteille","Plastique","goblet plastique","goblet en papier","metal","carton","vide"]

        resultat = np.argmax(result)

        
        data = {
            "id":path+nom[i],
            "resultat":classes[resultat]
        }



        # .dumps() as a string
        writeJSON(data,fDATA,f)


        with open("resultat.json", "r+") as file:
            print(file)

    fermerJSON(f)