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
base_caracter_only=["!", "\"", "#", "$", "%", "&", "'",
    "(", ")", "*", "+", ",", "-", ".",
    "/", ":", ";", "<", "=", ">", "?",
    "@", "[", "\\", "]", "^", "_", "`",
    "{", "|", "}", "~"]
tab_crypt=[]
print(len(base_alphabet))
def algo_crypter(texte,key):


    increment=0
    k=0
    j=0
    crypter=""
    for element in texte:
        if element.isalpha():
            for i in range(len(base_alphabet)):
                if base_alphabet[i]==element:
                    k=i
                    break

            element=base_caracter[(key+k)%52]
            crypter=crypter+element
            tab_crypt.append(element)
        elif element.isdigit():
            element=(key+int(element))%10
            crypter=crypter+str(element)
            tab_crypt.append(element)
        elif element in base_caracter_only:
            for i in range(len(base_caracter)):
                if base_caracter[i]==element:
                    j=i
                break
            element=base_alphabet[(key+j)%52]
            crypter=crypter+element
            tab_crypt.append(element)
        
    return crypter

def algo_decrypter(tab_crypt,key):
 
 j=0
 decrypter=""
 for element in tab_crypt:
        if element in base_caracter:
            for i in range(len(base_caracter)):
                if base_caracter[i]==element:
                    k=i

            element=base_alphabet[(k-key)%52]
            decrypter=decrypter+element
        elif element.isdigit():
            compt=0
            while (element-key)<=0:
                new_element=10*compt+(element-key)
                compt+=1
            decrypter=decrypter+str(new_element)
        elif element in base_alphabet:
            for i in range(len(base_alphabet)):
                if base_alphabet[i]==element:
                 j=i
            element=base_caracter_only[(key+j)%52]
            decrypter=decrypter+element
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
print(tab_crypt)


#parcourir les dossiers
