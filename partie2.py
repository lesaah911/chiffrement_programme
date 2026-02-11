import os
dossier="C:/Users/Azriel/Desktop/python projet"
contenue=os.listdir(dossier)
for element in contenue:
    if element.endswith("txt"):
        print("fichier trouvé")
        chemin_fichier=os.path.join(dossier,element)
        break
print(element)
with open (chemin_fichier,"r",encoding="utf-8") as f:
    lignes=f.read()
