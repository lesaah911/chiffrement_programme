import os
import shutil

base_caracter=[
    "!", "\"", "#", "$", "%", "&", "'",
    "(", ")", "*", "+", ",", "-", ".",
    "/", ":", ";", "<", "=", ">", "?",
    "@", "[", "\\", "]", "^", "_", "`",
    "{", "|", "}", "~","U1", "VV", "WW", "XX", "YY", "ZZ",
 "uA", "vB", "wC", "xD", "yE", "zF",
 "AG", "BH", "CI", "DJ","FK","FL","FM","FN"
]
base_alphabet=[
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]

# Fonction de cryptage
def algo_crypter(texte,key):
    crypter=""
    for element in texte:
        if element in base_alphabet:
                k=base_alphabet.index(element)
                element=base_caracter[(key+k)%len(base_caracter)]
                crypter=crypter+element
            
        elif element.isdigit():
            element=(key+int(element))%10
            crypter=crypter+str(element)
        
        else:
            crypter+=element

    return crypter

# Fonction de Décryptage
def algo_decrypter(crypter,key):
 decrypter=""
 i=0
 while i<len(crypter):
        if i+1<len(crypter):
            deux_car=crypter[i:i+2]
            if deux_car in base_caracter:
             k=base_caracter.index(deux_car)
             element=base_alphabet[(k-key)%len(base_alphabet)]
             decrypter=decrypter+element
             i=i+2
             continue
        element=crypter[i]
        if element in base_caracter:
                k=base_caracter.index(element)
                element=base_alphabet[(k-key)%len(base_alphabet)]
                decrypter=decrypter+element
        elif element.isdigit():
                new_element=(int(element)-key)%10
                decrypter=decrypter+str(new_element)
                
        else:
                decrypter+=element
        i=i+1


 return decrypter

# Déclaration des variables
choix=input("Voulez vous 'chiffrer' ou 'dechiffrer' ")
tab_log=[]
tab_log2=[]
i=0


while choix!="chiffrer" and choix!="dechiffrer":
    print("mauvaise entrée réessayez")
    choix=input("Voulez vous 'chiffrer' ou 'dechiffrer' ")

# Option Chiffrement
if choix.lower()=="chiffrer":   
 # Initialisation
    key=int(input("entrer la clé; (entier naturel):"))
    print("cle: ",key)
    dossier="C:/Users/Azriel/Desktop/python projet"
    contenue=os.listdir(dossier)

    for element in contenue:
        if element.endswith("txt"):
            chemin_fichier=os.path.join(dossier,element)

             #Sauvegarde
            os.makedirs("C:/Users/Azriel/Desktop/python projet/Sauvegardes",exist_ok=True)
            shutil.copy(chemin_fichier,"C:/Users/Azriel/Desktop/python projet/Sauvegardes")

            #creation de la table de logs
            tab_log.append(f"fichiers trouvé: {element}") 

            with open (chemin_fichier,"r",encoding="utf-8") as f:
                lignes=f.read()
            final= algo_crypter(lignes,key)
            with open(chemin_fichier,"w",encoding="utf-8") as f:
                f.write(final)

            # logs cryptage
            tab_log2.append(f"fichiers crypté: {element}")

# Option Déchiffrement

elif choix.lower()=="dechiffrer":   

    # initialisation
    key=int(input("entrer la clé; (entier naturel):"))
    dossier="C:/Users/Azriel/Desktop/python projet"
    contenue=os.listdir(dossier)

    for element in contenue:
        if element.endswith("txt"):
            chemin_fichier=os.path.join(dossier,element)

            #creation de la table de logs
            tab_log.append(f"fichiers trouvé: {element}") 

            with open (chemin_fichier,"r",encoding="utf-8") as f:
                lignes=f.read()
            final= algo_decrypter(lignes,key)
            
            # Vérifier si la clé décryptage est correcte
            contenue_sauvegarde=os.listdir("C:/Users/Azriel/Desktop/python projet/Sauvegardes")
            chemin_sauvegarde=os.path.join("C:/Users/Azriel/Desktop/python projet/Sauvegardes",contenue_sauvegarde[i])
            i+=1
            with open(chemin_sauvegarde,"r",encoding="utf-8") as f:
              lignes_1er_sauvegarde=f.read()       
            if final==lignes_1er_sauvegarde:
             
             # Décryptage car clé correcte
             with open(chemin_fichier,"w",encoding="utf-8") as f:
               f.write(final)

             #logs decryptage
             tab_log2.append(f"fichiers décrypté: {element}")
            
            # Message d'erreur car clé incorect
            else:
               print("Mauvaise clé (pas la meme)")
                  

# Affichage des logs

for elm in tab_log:
     print(elm)
for elm in tab_log2:
     print(elm)