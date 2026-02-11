import os


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

tab_crypt=[]
print(len(base_alphabet))

def algo_crypter(texte,key):

    k=0
    j=0
    crypter=""
    for element in texte:
        if element in base_alphabet:
            for i in range(len(base_alphabet)):
                if base_alphabet[i]==element:
                    k=i
                    element=base_caracter[(key+k)%26]
                    crypter=crypter+element
                    tab_crypt.append(element)

    return crypter

tab_decrypt=[]
def algo_decrypter(texte,key):
    k=0
    j=0
    decrypter=""
    for element in texte:
        if element in base_alphabet:
            for i in range(len(base_alphabet)):
                if base_alphabet[i]==element:
                    k=i
                    element=base_caracter[(key-k)%26]
                    decrypter=decrypter+element
                    tab_decrypt.append(element)

    return decrypter

choix=input("Voulez vous 'chiffrer' ou 'déchiffer' ")

if choix.lower()=="chiffrer":
    key=int(input("entrer la clé:"))
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
    final= algo_crypter(lignes,key)
    with open(chemin_fichier,"w",encoding="utf-8") as f:
     f.write(final)
elif choix.lower()=="dechiffrer":
    key=int(input("entrer la clé:"))
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
    final= algo_decrypter(lignes,key)
    with open(chemin_fichier,"w",encoding="utf-8") as f:
     f.write(final)

print(final)



#parcourir les dossiers
