import os
import datetime
crypter=[]
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

# Debut du code
choix=input("Voulez vous 'chiffrer' ou 'déchiffer' ")

if choix.lower()=="chiffrer":
    key=int(input("entrer la clé; (entier naturel):"))
    dossier="C:/Users/Azriel/Desktop/python projet"
    contenue=os.listdir(dossier)
    for element in contenue:
        if element.endswith("txt"):
            print("fichier trouvé")
            chemin_fichier=os.path.join(dossier,element)
            print(element)
            with open (chemin_fichier,"r",encoding="utf-8") as f:
                lignes=f.read()
            final= algo_crypter(lignes,key)
            print("texte chiffré: ",final)
elif choix.lower()=="dechiffrer":
    key=int(input("entrer la clé; (entier naturel):"))
    dossier="C:/Users/Azriel/Desktop/python projet"
    contenue=os.listdir(dossier)
    for element in contenue:
        if element.endswith("txt"):
            print("fichier trouvé")
            chemin_fichier=os.path.join(dossier,element)
            print(element)
            with open (chemin_fichier,"r",encoding="utf-8") as f:
                lignes=f.read()
            final= algo_decrypter(lignes,key)
            print("texte décrypter: ",final)
else:
    print("Entrer Invalide")

# Affichage

