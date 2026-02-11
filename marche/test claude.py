import os

base_alphabet = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]

base_caracter = [
    "!", "\"", "#", "$", "%", "&", "'",
    "(", ")", "*", "+", ",", "-", ".",
    "/", ":", ";", "<", "=", ">", "?",
    "@", "[", "\\", "]", "^", "_", "`",
    "{", "|", "}", "~","U1", "VV", "WW", "XX", "YY", "ZZ",
    "uA", "vB", "wC", "xD", "yE", "zF",
    "AG", "BH", "CI", "DJ","FK","FL","FM","FN"
]

def algo_crypter(texte, key):
    crypter = ""
    for element in texte:
        if element in base_alphabet:
            k = base_alphabet.index(element)
            crypter += base_caracter[(key + k) % len(base_caracter)]  # Utiliser len()
        elif element.isdigit():
            crypter += str((key + int(element)) % 10)
        else:
            crypter += element  # Garder espaces, ponctuation, etc.
    
    return crypter

def algo_decrypter(texte_crypte, key):
    decrypter = ""
    i = 0
    
    while i < len(texte_crypte):
        # Gérer les codes à 2 caractères
        if i + 1 < len(texte_crypte):
            deux_char = texte_crypte[i:i+2]
            if deux_char in base_caracter:
                k = base_caracter.index(deux_char)
                decrypter += base_alphabet[(k - key) % len(base_alphabet)]
                i += 2
                continue
        
        # Caractère simple
        element = texte_crypte[i]
        
        if element in base_caracter:
            k = base_caracter.index(element)
            decrypter += base_alphabet[(k - key) % len(base_alphabet)]
        elif element.isdigit():
            decrypter += str((int(element) - key) % 10)
        else:
            decrypter += element
        
        i += 1
    
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

